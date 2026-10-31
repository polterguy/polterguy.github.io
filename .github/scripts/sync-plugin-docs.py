#!/usr/bin/env python3
"""
Publishes each plugin's README.md from the Magic repository as pages on this site.

The README is the source of truth, and it is never touched. For every plugin this writes

* plugins/<plugin>/index.md - the hub: the introduction, the list of the plugin's slots, linking
  to their pages, the small sections, and a list of the topics;
* plugins/<plugin>/<topic>/index.md - one page for each larger section that is not the guide of
  a slot, split again when it is long;

and the guide of every slot, the "How to use [slot]" sections, is left for build-slot-reference.py,
which places it on the slot's own page. See docsplit.py for the rules, and .github/split/ for the
manifests that override them.

Each page is adapted for Jekyll: absolute https://docs.ainiro.io links become relative links, and
Liquid is escaped with {% raw %} around every code block and inline code span that contains "{{"
or "{%", since an unescaped "{{" breaks the page.

Usage: sync-plugin-docs.py <magic-checkout> [--slots slots.json] [--check]
With --check nothing is written and the exit status is 1 if any page would change.
"""

import argparse
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import docsplit  # noqa: E402

ROOT = docsplit.ROOT


def has_liquid(s):
    return '{{' in s or '{%' in s


def to_index(text):
    lines = text.replace('\r\n', '\n')
    lines = re.sub(r'https://docs\.ainiro\.io(/[^\s)\]]*)', r'\1', lines).split('\n')
    out, i = [], 0

    def wrap(m):
        return '{% raw %}' + m.group(0) + '{% endraw %}' if has_liquid(m.group(0)) else m.group(0)

    while i < len(lines):
        if lines[i].startswith('```'):
            j = i + 1
            while j < len(lines) and not lines[j].startswith('```'):
                j += 1
            block = lines[i:j + 1]
            if has_liquid('\n'.join(block)):
                out += ['{% raw %}'] + block + ['{% endraw %}']
            else:
                out += block
            i = j + 1
            continue
        out.append(re.sub(r'`[^`\n]+`', wrap, lines[i]))
        i += 1
    result = '\n'.join(out)
    return result if result.endswith('\n') else result + '\n'


def raw_front_matter(readme):
    m = re.match(r'---\n(.*?)\n---\n', readme.replace('\r\n', '\n'), re.S)
    return m.group(1) if m else ''


def build(readme, plugin, names):
    """The pages of one plugin, as {relative path: text}."""
    result = docsplit.plan(readme, plugin, names, docsplit.load_manifest(plugin))
    files = {}

    front = raw_front_matter(readme)
    if result['moved']:
        front += '\nmoved_anchors: ' + json.dumps(result['moved'], ensure_ascii=False, sort_keys=True)
    files['plugins/%s/index.md' % plugin] = '---\n%s\n---\n\n%s' % (front, to_index(docsplit.hub_markdown(result, names)))

    for index, page in enumerate(result['pages']):
        description = docsplit.describe(page)
        head = '---\ntitle: %s\ndescription: %s\ngenerated: true\n---\n\n' % (
            json.dumps(page['title'], ensure_ascii=False), json.dumps(description, ensure_ascii=False))
        files['plugins/%s/%s/index.md' % (plugin, page['slug'])] = head + to_index(docsplit.page_markdown(result, page, index, names))
    return files


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('magic')
    ap.add_argument('--slots')
    ap.add_argument('--check', action='store_true')
    args = ap.parse_args()

    names = docsplit.load_slot_names(args.slots)
    wanted = {}
    for readme in sorted(glob.glob(os.path.join(args.magic, 'plugins', '*', 'README.md'))):
        plugin = os.path.basename(os.path.dirname(readme))
        with open(readme, encoding='utf-8-sig') as f:
            wanted.update(build(f.read(), plugin, names))

    # A topic page must never replace a page that somebody wrote by hand.
    for rel in wanted:
        path = os.path.join(ROOT, rel)
        if rel.count('/') == 3 and os.path.exists(path):
            with open(path, encoding='utf-8') as f:
                if 'generated: true' not in f.read():
                    sys.exit('%s exists and was not generated, so it would be overwritten.' % rel)

    changed = []
    for rel, text in sorted(wanted.items()):
        path = os.path.join(ROOT, rel)
        old = None
        if os.path.exists(path):
            with open(path, encoding='utf-8-sig') as f:
                old = f.read().replace('\r\n', '\n')
        if old == text:
            continue
        changed.append(rel)
        if not args.check:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, 'w', encoding='utf-8', newline='\n') as f:
                f.write(text)

    # Topic pages whose section no longer exists are stale.
    stale = []
    for path in glob.glob(os.path.join(ROOT, 'plugins', '*', '*', 'index.md')):
        rel = os.path.relpath(path, ROOT)
        if rel in wanted:
            continue
        with open(path, encoding='utf-8') as f:
            if 'generated: true' in f.read():
                stale.append(rel)
                if not args.check:
                    os.remove(path)
                    if not os.listdir(os.path.dirname(path)):
                        os.rmdir(os.path.dirname(path))

    print('%s: %d pages, %d stale%s' % ('would change' if args.check else 'updated', len(changed), len(stale),
                                         (' (' + ', '.join(changed[:6]) + (' ...' if len(changed) > 6 else '') + ')') if changed else ''))
    if args.check and (changed or stale):
        sys.exit(1)


if __name__ == '__main__':
    main()

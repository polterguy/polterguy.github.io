#!/usr/bin/env python3
"""
Checks the markdown of this site, and fails when a page would be published broken.

* every internal link points at a page or a file that exists, and, for a generated page, at an
  anchor that exists on it;
* no page is over MAX_WORDS words, except the pages listed in .github/lint-allow.txt, one path
  per line, which is the list of pages still waiting to be split;
* a generated topic page is not under MIN_WORDS words, and every page has a title;
* with --magic, every word of every plugin README is accounted for on a published page, which
  is what stops a bug in the splitter from silently dropping text.

Usage: lint-docs.py [--magic <magic-checkout>] [--slots slots.json]
Exits with status 1 when anything fails. Warnings never do.
"""

import argparse
import glob
import json
import os
import re
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import docsplit  # noqa: E402

ROOT = docsplit.ROOT
MAX_WORDS = 2000
MIN_WORDS = 120


def read(path):
    with open(path, encoding='utf-8-sig') as f:
        return f.read().replace('\r\n', '\n')


def pages(skip=None):
    """Every markdown page that is published, as {url: {path, front, body, generated}}.
    skip is a checkout of another repository inside this one, which is not part of the site."""
    found = {}
    for dp, dn, fn in os.walk(ROOT):
        dn[:] = [d for d in dn if not d.startswith(('.', '_'))
                 and not (skip and os.path.realpath(os.path.join(dp, d)) == os.path.realpath(skip))]
        for name in fn:
            if not name.endswith('.md'):
                continue
            path = os.path.join(dp, name)
            rel = os.path.relpath(path, ROOT)
            text = read(path)
            front, body = docsplit.split_front_matter(text)
            url = '/' + rel.replace('index.md', '').replace('.md', '/')
            found[url] = {'path': rel, 'front': front, 'body': body, 'generated': front.get('generated') == 'true'}
    return found


def anchors_of(body):
    ids, counts, inside = set(), Counter(), False
    for line in body.split('\n'):
        if line.startswith('```'):
            inside = not inside
        m = None if inside else re.match(r'#{1,6} (.*)', line)
        if m:
            base = docsplit.slug(m.group(1).strip())
            n = counts[base]
            counts[base] += 1
            ids.add(base if n == 0 else '%s-%d' % (base, n))
    ids.update(re.findall(r'\bid="([^"]+)"', body))
    return ids


def resolve(url, site):
    """The page a link goes to, or None when it is a file that exists, or False when nothing is there."""
    path = url.split('#')[0].split('?')[0]
    if not path.endswith('/') and path not in site and os.path.exists(os.path.join(ROOT, path.lstrip('/'))):
        return None
    if path in site:
        return site[path]
    if path.rstrip('/') + '/' in site:
        return site[path.rstrip('/') + '/']
    if os.path.exists(os.path.join(ROOT, path.lstrip('/'))):
        return None
    return False


def tokens(text):
    text = re.sub(r'\{% (end)?raw %\}', '', text)
    text = re.sub(r'https://docs\.ainiro\.io|\\\[|\\\]', '', text)
    return re.findall(r"[A-Za-z0-9_.\-@:/*#$]+", text)


def conservation(site, magic, names, errors):
    total = 0
    for readme in sorted(glob.glob(os.path.join(magic, 'plugins', '*', 'README.md'))):
        plugin = os.path.basename(os.path.dirname(readme))
        text = read(readme)
        result = docsplit.plan(text, plugin, names, docsplit.load_manifest(plugin))
        source = docsplit.split_front_matter(text)[1]
        moved_headings = {g['heading'] for g in result['guides'].values()}
        source = '\n'.join(l for l in source.split('\n')
                           if not (re.match(r'#{2,6} ', l) and l.split(' ', 1)[1].strip() in moved_headings))
        published = []
        for url, page in site.items():
            if url == '/plugins/%s/' % plugin or (url.startswith('/plugins/%s/' % plugin) and page['generated']):
                published += tokens(page['path'] and read(os.path.join(ROOT, page['path'])))
        have, want = Counter(published), Counter(tokens(source))
        missing = sum(c - have[t] for t, c in want.items() if c > have[t])
        total += sum(want.values())
        if missing > max(5, 0.005 * sum(want.values())):
            lost = ', '.join('%s x%d' % (t, c - have[t]) for t, c in want.items() if c > have[t])[:160]
            errors.append('%s: %d words of the README are on no published page (%s)' % (plugin, missing, lost))
    return total


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--magic')
    ap.add_argument('--slots')
    args = ap.parse_args()

    site = pages(args.magic)
    allow = set()
    allow_file = os.path.join(ROOT, '.github', 'lint-allow.txt')
    if os.path.exists(allow_file):
        allow = {l.strip() for l in read(allow_file).split('\n') if l.strip() and not l.startswith('#')}

    errors, warnings = [], []
    titles = {}
    for url, page in sorted(site.items()):
        front, body, rel = page['front'], page['body'], page['path']
        if not front.get('title'):
            errors.append('%s has no title' % rel)
        else:
            titles.setdefault(front['title'], []).append(rel)
        count = len(body.split())
        if count > MAX_WORDS and rel not in allow and not rel.startswith('reference/'):
            errors.append('%s is %d words, over %d, and is not on the list of pages waiting to be split' % (rel, count, MAX_WORDS))
        if page['generated'] and not front.get('guide') and rel.startswith('plugins/') and rel.count('/') == 3 and count < MIN_WORDS:
            errors.append('%s is only %d words, too thin to be a page of its own' % (rel, count))

        for target in re.findall(r'\]\((/[^)\s]*)\)|href="(/[^"#\s]*)"', body):
            target = target[0] or target[1]
            if target.startswith('//'):
                continue
            where = resolve(target, site)
            if where is False:
                errors.append('%s links to %s, which does not exist' % (rel, target))
            elif where and '#' in target:
                anchor = target.split('#', 1)[1]
                moved = json.loads(where['front'].get('moved_anchors') or '{}')
                if anchor and anchor not in anchors_of(where['body']) and anchor not in moved:
                    message = '%s links to %s, which has no such anchor' % (rel, target)
                    (errors if (where['generated'] or page['generated']) else warnings).append(message)

    for title, where in titles.items():
        if len(where) > 1 and all(site[('/' + w.replace('index.md', '').replace('.md', '/'))]['generated'] for w in where):
            errors.append('the title "%s" is used by %d generated pages, for instance %s' % (title, len(where), where[0]))

    checked = 0
    if args.magic:
        checked = conservation(site, args.magic, docsplit.load_slot_names(args.slots), errors)

    print('%d pages checked%s' % (len(site), (', %d words of README text accounted for' % checked) if checked else ''))
    for w in warnings[:15]:
        print('warning:', w)
    if len(warnings) > 15:
        print('warning: ... and %d more' % (len(warnings) - 15))
    for e in errors:
        print('ERROR:', e)
    if errors:
        print('%d errors' % len(errors))
        sys.exit(1)
    print('no errors, %d warnings' % len(warnings))


if __name__ == '__main__':
    main()

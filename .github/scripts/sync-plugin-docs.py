#!/usr/bin/env python3
"""
Copies each plugin's README.md from the Magic repository into this site as
plugins/<plugin>/index.md, adapting it for Jekyll:

* absolute https://docs.ainiro.io links become relative links, and
* Liquid is escaped with {% raw %} around every code block and inline code span that
  contains "{{" or "{%", since an unescaped "{{" breaks the page.

The README is the source of truth. Plugins listed in SITE_STRUCTURED are skipped, since
this site documents them as a landing page plus sub-pages instead of one long page.

Usage: sync-plugin-docs.py <magic-checkout> [--check]
With --check nothing is written and the exit status is 1 if any page would change.
"""

import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SITE_STRUCTURED = {'magic.lambda'}


def has_liquid(s):
    return '{{' in s or '{%' in s


def to_index(readme):
    lines = readme.replace('\r\n', '\n')
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
    text = '\n'.join(out)
    return text if text.endswith('\n') else text + '\n'


def main():
    magic = sys.argv[1]
    check = '--check' in sys.argv
    changed = []
    for readme in sorted(glob.glob(os.path.join(magic, 'plugins', '*', 'README.md'))):
        plugin = os.path.basename(os.path.dirname(readme))
        if plugin in SITE_STRUCTURED:
            continue
        target = os.path.join(ROOT, 'plugins', plugin, 'index.md')
        with open(readme, encoding='utf-8-sig') as f:
            new = to_index(f.read())
        old = ''
        if os.path.exists(target):
            with open(target, encoding='utf-8-sig') as f:
                old = f.read().replace('\r\n', '\n')
        if new.strip() == old.strip():
            continue
        changed.append(plugin)
        if not check:
            os.makedirs(os.path.dirname(target), exist_ok=True)
            with open(target, 'w', encoding='utf-8') as f:
                f.write(new)
    print('%s: %s' % ('would change' if check else 'updated', ', '.join(changed) or 'nothing'))
    if check and changed:
        sys.exit(1)


if __name__ == '__main__':
    main()

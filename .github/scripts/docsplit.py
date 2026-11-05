#!/usr/bin/env python3
"""
Splits a long plugin README into pages small enough to be good retrieval chunks, without
touching the README. The README stays the single source, complete for readers on GitHub,
and this decides what the published site makes of it.

* A section headed "How to use [slot]" is the guide of that slot. It moves to the slot's own
  reference page, next to the slot's contract, where it makes a page of a useful size.
* Every other section of two or more paragraphs becomes a page of its own, a concept page,
  and one that is long is split again by its subsections. Small sections stay on the hub.
* What is left, the introduction and the small sections, is the hub: the plugin's own page,
  with the list of its slots, now linking to their pages, and a list of its topics.

A manifest, .github/split/<plugin>.json, can override the automatic rules:

    {"pages": [{"slug": "rsa", "title": "RSA", "sections": ["Heading", "Another heading"]}],
     "hub": ["A heading that must stay on the hub"]}

Usage: docsplit.py --report <magic-checkout> [--slots slots.json]
prints what each README would be split into, and writes nothing.
"""

import argparse
import glob
import json
import os
import re
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SLOTS_URL = 'https://hyperlambda.dev/magic/modules/docs/slots'
USER_AGENT = 'magic-docs-sync/1.0 (+https://docs.ainiro.io/reference/slots/)'

MIN_CONCEPT_WORDS = 250   # a section shorter than this stays on the hub, as a page of its own it would be too thin
SPLIT_ABOVE = 1500        # a section longer than this is split by its subsections
MERGE_BELOW = 300         # sibling subsections shorter than this are joined to a neighbour


# ------------------------------------------------------------------------------------
# Small helpers.
# ------------------------------------------------------------------------------------

def slug(text):
    """The id kramdown gives a heading, which is what a link to it has to use."""
    s = re.sub(r'^[^a-zA-Z]+', '', text)
    s = re.sub(r'[^a-zA-Z0-9 -]', '', s).strip().replace(' ', '-').lower()
    return s or 'section'


def page_slug(text):
    """The address of a page: readable, with the dots and brackets of slot names turned into hyphens."""
    s = re.sub(r'[^a-zA-Z0-9]+', '-', text).strip('-').lower()
    return s or 'page'


def words(lines):
    return len(re.sub(r'```.*?```', lambda m: m.group(0), '\n'.join(lines), flags=re.S).split())


def ns_of(name):
    return name.split('.')[0] if '.' in name else 'core'


def slot_url(name):
    return '/reference/slots/%s/%s/' % (ns_of(name), name)


def load_slot_names(path=None):
    if path:
        with open(path, encoding='utf-8') as f:
            data = json.load(f)
    else:
        request = urllib.request.Request(SLOTS_URL, headers={'User-Agent': USER_AGENT})
        with urllib.request.urlopen(request, timeout=120) as response:
            data = json.load(response)
    return {d['name'] for d in data}


def split_front_matter(text):
    m = re.match(r'---\n(.*?)\n---\n', text, re.S)
    if not m:
        return {}, text
    fields = {}
    for line in m.group(1).split('\n'):
        k, sep, v = line.partition(':')
        if sep:
            fields[k.strip()] = v.strip().strip('"')
    return fields, text[m.end():]


def headings_of(lines):
    """(index, level, text) of every heading outside a code fence."""
    out, inside = [], False
    for i, line in enumerate(lines):
        if line.startswith('```'):
            inside = not inside
        elif not inside:
            m = re.match(r'(#{2,6}) (.*)', line)
            if m:
                out.append((i, len(m.group(1)), m.group(2).strip()))
    return out


def shift_headings(lines, by):
    """Moves every heading outside a code fence `by` levels, never above level two."""
    out, inside = [], False
    for line in lines:
        if line.startswith('```'):
            inside = not inside
        m = None if inside else re.match(r'(#{2,6})( .*)', line)
        out.append('#' * max(2, len(m.group(1)) + by) + m.group(2) if m else line)
    return out


def trim(lines):
    while lines and not lines[0].strip():
        lines = lines[1:]
    while lines and not lines[-1].strip():
        lines = lines[:-1]
    return lines


def first_sentence(lines, limit=200):
    skip = re.compile(r'(#|```|\||<|>|[*-]\s)')
    fence, kept = False, []
    for l in lines:
        if l.startswith('```'):
            fence = not fence
        elif l.strip() and not fence and not skip.match(l):
            kept.append(l)
    text = ' '.join(kept)
    text = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', text)
    text = re.sub(r'[*_`]', '', text).strip()
    m = re.match(r'(.{20,%d}?[.!?])(\s|$)' % limit, text)
    return (m.group(1) if m else text[:limit]).strip()


# ------------------------------------------------------------------------------------
# The split.
# ------------------------------------------------------------------------------------

def plan(readme, plugin, names, manifest=None):
    """
    Returns a dict with hub (markdown), pages (slug, title, markdown, words), guides (slot ->
    markdown) and moved (old anchor -> new address), for one README.
    """
    manifest = manifest or {}
    front, body = split_front_matter(readme.replace('\r\n', '\n'))
    lines = body.split('\n')
    heads = headings_of(lines)
    n = len(lines)

    def end_of(k):
        lvl = heads[k][1]
        return next((heads[j][0] for j in range(k + 1, len(heads)) if heads[j][1] <= lvl), n)

    # 1. Guides: "How to use [slot]" sections naming at least one slot that exists.
    owner = [None] * n
    guides = []
    for k, (i, lvl, text) in enumerate(heads):
        if not re.match(r'(How to use\s+)?\[', text):
            continue
        real = [b for b in re.findall(r'\[([^\]]+)\]', text) if b in names]
        if real:
            guides.append({'k': k, 'start': i, 'end': end_of(k), 'level': lvl, 'heading': text, 'slots': real})
    for gid, g in sorted(enumerate(guides), key=lambda x: x[1]['start'] - x[1]['end']):
        for i in range(g['start'], g['end']):
            owner[i] = gid           # inner guides come later in the sort, so they win

    # 2. Everything else is grouped under the level-two heading it sits below.
    units, current = [], {'heading': None, 'lines': [], 'level': 2}
    h2_at = {i for (i, lvl, _) in heads if lvl == 2}
    for i, line in enumerate(lines):
        if owner[i] is not None:
            continue
        if i in h2_at:
            units.append(current)
            current = {'heading': next(t for (j, l, t) in heads if j == i), 'lines': [], 'level': 2}
        current['lines'].append(line)
    units.append(current)
    intro = units[0]['lines']
    units = units[1:]

    # 3. Which sections stay on the hub and which become pages.
    forced_hub = set(manifest.get('hub', []))
    manifest_pages = manifest.get('pages', [])
    in_manifest = {s for p in manifest_pages for s in p['sections']}
    pages, hub_sections = [], []

    def subsections(unit):
        """Non-guide subsections of a unit: (level, heading, lines) for each, plus its own lines."""
        sub_heads = headings_of(unit['lines'])
        sub_heads = [h for h in sub_heads if h[1] == 3]
        if not sub_heads:
            return unit['lines'], []
        own = unit['lines'][:sub_heads[0][0]]
        subs = []
        for k, (i, lvl, text) in enumerate(sub_heads):
            e = sub_heads[k + 1][0] if k + 1 < len(sub_heads) else len(unit['lines'])
            subs.append((lvl, text, unit['lines'][i:e]))
        return own, subs

    def make_page(slug_, title, chunks, keep_headings, description=None):
        content = []
        for chunk in chunks:
            content += chunk + ['']
        lines_ = trim(content)
        return {'slug': slug_, 'title': title, 'lines': lines_, 'words': words(lines_), 'keep': keep_headings,
                'description': description}

    claimed = set()
    for p in manifest_pages:
        chunks = []
        for s in p['sections']:
            found = None
            for u in units:
                if u['heading'] == s:
                    found = shift_headings(u['lines'], 0)
                    break
                own, subs = subsections(u)
                for (lvl, text, sl) in subs:
                    if text == s:
                        found = shift_headings(sl, -1)
            if found is None:
                raise SystemExit('%s: the manifest names a section that does not exist: %s' % (plugin, s))
            claimed.add(s)
            chunks.append(found)
        pages.append(make_page(p['slug'], p['title'], chunks, True, p.get('description')))

    for u in units:
        if u['heading'] in in_manifest or u['heading'] in forced_hub:
            if u['heading'] in forced_hub:
                hub_sections.append(u)
            continue
        own, all_subs = subsections(u)
        subs = [s for s in all_subs if s[1] not in in_manifest]
        # What is left of the section once the manifest has claimed some of its subsections.
        remaining = u['lines'] if len(subs) == len(all_subs) else own + [l for s in subs for l in s[2]]
        total = words(remaining)
        if total < MIN_CONCEPT_WORDS:
            hub_sections.append({'heading': u['heading'], 'lines': remaining, 'level': 2})
        elif total > SPLIT_ABOVE and subs and all(words(s[2]) >= 100 for s in subs[:1]):
            # The section's own text becomes one page, and its subsections the others.
            groups = []
            for sub in subs:
                if groups and sum(words(s[2]) for s in groups[-1]) < MERGE_BELOW:
                    groups[-1].append(sub)
                else:
                    groups.append([sub])
            if len(groups) > 1 and sum(words(s[2]) for s in groups[-1]) < MERGE_BELOW:
                tail = groups.pop()
                groups[-1].extend(tail)
            if words(own) >= MIN_CONCEPT_WORDS:
                pages.append(make_page(page_slug(u['heading']), u['heading'], [shift_headings(own[1:], 0)], False))
            else:
                # The section's own text is too short for a page, so it stays on the hub, under its heading.
                hub_sections.append({'heading': u['heading'], 'lines': trim(own) + [''], 'level': 2})
            for g in groups:
                if len(g) == 1:
                    pages.append(make_page(page_slug(g[0][1]), g[0][1], [shift_headings(g[0][2][1:], -2)], False))
                else:
                    title = g[0][1]
                    pages.append(make_page(page_slug(title), title, [shift_headings(s[2], -1) for s in g], True))
        else:
            pages.append(make_page(page_slug(u['heading']), u['heading'], [shift_headings(remaining[1:], -1)], False))

    # Unique slugs within the plugin.
    seen = {}
    for p in pages:
        base = p['slug'][:70].rstrip('-') or 'page'
        seen[base] = seen.get(base, 0) + 1
        p['slug'] = base if seen[base] == 1 else '%s-%d' % (base, seen[base])

    # 4. Each guide becomes a page of its own, named after its first slot. The page and the reference page
    # of that slot link to each other, once.
    guide_out, guide_pages = {}, []
    for gid, g in enumerate(guides):
        inner = [lines[i] for i in range(g['start'] + 1, g['end']) if owner[i] == gid]
        text = '\n'.join(shift_headings(trim(inner), 1 - g['level'])).strip()
        primary = g['slots'][0]
        url = '/plugins/%s/%s/' % (plugin, primary)
        guide_pages.append({'slot': primary, 'slots': g['slots'], 'heading': g['heading'], 'md': text, 'url': url})
        for s_ in g['slots']:
            guide_out[s_] = {'url': url, 'heading': g['heading']}

    # 5. Where an old anchor went, so a link to it can still find it.
    moved = {}
    for g in guides:
        moved[slug(g['heading'])] = '/plugins/%s/%s/' % (plugin, g['slots'][0])
    for p in pages:
        url = '/plugins/%s/%s/' % (plugin, p['slug'])
        moved.setdefault(slug(p['title']), url)
        for (_, lvl, text) in headings_of(p['lines']):
            moved.setdefault(slug(text), url + '#' + slug(text))
    kept = {slug(t) for (_, _, t) in headings_of(intro + [l for u in hub_sections for l in u['lines']])}
    moved = {a: b for a, b in moved.items() if a not in kept}
    for g in guide_pages:
        g['md'] = relink(g['md'], moved)

    return {'front': front, 'intro': intro, 'hub_sections': hub_sections, 'pages': pages,
            'guides': guide_out, 'guide_pages': guide_pages, 'moved': moved, 'plugin': plugin}


def describe(page):
    """The description of a topic page: the manifest's, else its title followed by its first sentence."""
    if page.get('description'):
        return page['description']
    text = '%s - %s' % (page['title'], first_sentence(page['lines']))
    return text if len(text) <= 220 else text[:217].rstrip() + '...'


def relink(text, moved):
    """Points in-page links to a section that moved at its new address."""
    return re.sub(r'\]\(#([^)\s]+)\)', lambda m: '](%s)' % moved[m.group(1)] if m.group(1) in moved else m.group(0), text)


def linkify_slots(lines, names, urls=None):
    """Bullets such as "* __[io.file.load]__ - ..." link to the page of the slot."""
    out = []
    for line in lines:
        m = re.match(r'(\*\s+)(__|\*\*)\[([^\]]+)\]\2(.*)', line)
        if m and m.group(3) in names:
            out.append('%s%s[\\[%s\\]](%s)%s%s' % (m.group(1), m.group(2), m.group(3), (urls or {}).get(m.group(3)) or slot_url(m.group(3)), m.group(2), m.group(4)))
        else:
            out.append(line)
    return out


def hub_markdown(result, names, urls=None):
    """The hub page body, without front matter."""
    lines = linkify_slots(result['intro'], names, urls)
    for u in result['hub_sections']:
        lines += [''] + linkify_slots(u['lines'], names, urls)
    if result['pages']:
        lines += ['', '## Topics', '']
        for p in result['pages']:
            lines.append('* [%s](/plugins/%s/%s/) - %s' % (p['title'], result['plugin'], p['slug'], p.get('description') or first_sentence(p['lines'])))
    return relink('\n'.join(trim(lines)) + '\n', result['moved'])


def page_markdown(result, page, index):
    """A concept page body, with its place in the series."""
    plugin, pages = result['plugin'], result['pages']
    lead = 'This page is part of the [%s](/plugins/%s/) documentation.' % (plugin, plugin)
    body = [lead, ''] + page['lines']
    nav = []
    if index > 0:
        nav.append('[&larr; %s](/plugins/%s/%s/)' % (pages[index - 1]['title'], plugin, pages[index - 1]['slug']))
    nav.append('[all of %s](/plugins/%s/)' % (plugin, plugin))
    if index + 1 < len(pages):
        nav.append('[%s &rarr;](/plugins/%s/%s/)' % (pages[index + 1]['title'], plugin, pages[index + 1]['slug']))
    body += ['', '---', '', ' | '.join(nav)]
    return relink('\n'.join(body) + '\n', result['moved'])


# ------------------------------------------------------------------------------------
# Guide pages: one for every slot.
# ------------------------------------------------------------------------------------

def token_in(name, text):
    return re.search(r'(?<![\w.\-])%s(?![\w\-]|\.\w)' % re.escape(name), text)


def section_showing(sources, name, modes=(True, False)):
    """The smallest section, in the given line lists, that shows the slot in a code sample, else one that names it."""
    for want_code in modes:
        for lines in sources:
            fence, marks = False, []
            for i, line in enumerate(lines):
                if line.startswith('```'):
                    fence = not fence
                elif not fence:
                    h = re.match(r'(#{2,6}) ', line)
                    if h:
                        marks.append((i, len(h.group(1))))
            spans = []
            for k, (i, lvl) in enumerate(marks):
                e = next((j for (j, l) in marks[k + 1:] if l <= lvl), len(lines))
                spans.append((i, e, lvl))
            best = None
            for (i, e, lvl) in spans:
                body = lines[i + 1:e]
                text = '\n'.join(body)
                if want_code:
                    blocks = re.findall(r'```.*?```', text, re.S)
                    hit = any(token_in(name, b) for b in blocks)
                else:
                    hit = ('[%s]' % name) in text
                if hit and (best is None or e - i < best[1] - best[0]):
                    best = (i, e, lvl)
            if best:
                i, e, lvl = best
                return shift_headings(trim(lines[i + 1:e]), 1 - lvl)
    return None


def example_in(lines, name):
    """The paragraph before the first code sample using the slot, and the sample, from text without headings."""
    i = 0
    while i < len(lines):
        if lines[i].startswith('```'):
            j = i + 1
            while j < len(lines) and not lines[j].startswith('```'):
                j += 1
            if token_in(name, '\n'.join(lines[i:j + 1])):
                k = i
                while k > 0 and lines[k - 1].strip():
                    k -= 1
                if k == i:
                    k = i - 1
                    while k > 0 and not lines[k - 1].strip():
                        k -= 1
                    while k > 0 and lines[k - 1].strip():
                        k -= 1
                return trim(lines[max(k, 0):j + 1])
            i = j
        i += 1
    return None


def show(sources, name):
    """What the documentation shows of a slot: a section with a code sample, else the sample, else a section naming it."""
    found = section_showing(sources, name, (True,))
    for lines in sources:
        found = found or example_in(lines, name)
    return found or section_showing(sources, name, (False,))


def collect(magic, names):
    """
    The plan of every README, plus the guide page of every slot: its own "How to use" section when the README has
    one, else the section of the plugin's documentation that shows it. Returns {'results', 'guides', 'urls'},
    where guides is {plugin: [page]} and urls is {slot: address of its guide page}.
    """
    results = {}
    for readme in sorted(glob.glob(os.path.join(magic, 'plugins', '*', 'README.md'))):
        plugin = os.path.basename(os.path.dirname(readme))
        with open(readme, encoding='utf-8-sig') as f:
            results[plugin] = plan(f.read(), plugin, names, load_manifest(plugin))

    guides = {p: list(r['guide_pages']) for p, r in results.items()}
    urls = {s_: g['url'] for p in guides for g in guides[p] for s_ in g['slots']}

    # A guide somebody wrote as a page of its own, "guide: true" without "generated: true", is used as it is.
    for path in glob.glob(os.path.join(ROOT, 'plugins', '*', '*', 'index.md')):
        with open(path, encoding='utf-8') as f:
            text = f.read()
        if 'guide: true' in text and 'generated: true' not in text:
            front = split_front_matter(text)[0]
            url = '/' + os.path.relpath(os.path.dirname(path), ROOT).replace(os.sep, '/') + '/'
            for s_ in json.loads(front.get('slots', '[]')):
                urls[s_] = url

    # A data.* slot the README has no section for is the database neutral front of the sql.* slot of the same name,
    # and shares its guide. Without this, a hand written page that merely uses it in a sample would claim it.
    for name in names:
        if name.startswith('data.') and name not in urls and 'sql.' + name[5:] in urls:
            urls[name] = urls['sql.' + name[5:]]

    def sources_of(plugin, hand_pages=()):
        r = results.get(plugin)
        found = ([r['intro']] + [u['lines'] for u in r['hub_sections']] + [p_['lines'] for p_ in r['pages']]) if r else []
        return found + (list(hand_pages) if plugin == 'magic.lambda' else [])

    owned, described = {}, {}
    for plugin, r in results.items():
        for line in r['intro'] + [l for u in r['hub_sections'] for l in u['lines']] + [l for pg in r['pages'] for l in pg['lines']]:
            m = re.match(r'\*\s+(?:__|\*\*)?\\?\[+([^\]\\]+)\]?(?:__|\*\*)?\s*-\s*(.*)', line)
            if m and m.group(1) in names:
                owned.setdefault(m.group(1), plugin)
                described.setdefault(m.group(1), m.group(2).strip())

    # The hand written pages of magic.lambda document the core keywords, which no README lists.
    hand = []
    for path in sorted(glob.glob(os.path.join(ROOT, 'plugins', 'magic.lambda', '*', 'index.md'))):
        with open(path, encoding='utf-8') as f:
            text = f.read()
        if 'generated: true' not in text:
            hand.append(split_front_matter(text)[1].split('\n'))
    # A guide without a code sample gets the section of the plugin's documentation that shows its slot in one.
    for plugin, pages_ in guides.items():
        for g in pages_:
            if '```' not in g['md']:
                body = show(sources_of(plugin, hand), g['slot'])
                for other in guides[plugin]:
                    if not body and other is not g:
                        body = example_in(other['md'].split('\n'), g['slot'])
                if body:
                    g['md'] = g['md'] + '\n\n' + '\n'.join(body)

    for lines in hand:
        text = '\n'.join(lines)
        for name in names:
            if name not in owned and name not in urls and (('[%s]' % name) in text or (('.' in name or '-' in name) and token_in(name, text))):
                owned[name] = 'magic.lambda'

    for name in sorted(owned):
        if name in urls:
            continue
        plugin = owned[name]
        r = results.get(plugin)
        sources = ([r['intro']] if r else []) + ([u['lines'] for u in r['hub_sections']] if r else []) + ([p['lines'] for p in r['pages']] if r else [])
        if plugin == 'magic.lambda':
            sources += hand
        body = show(sources, name)
        md = '\n'.join(body) if body else ''
        if not md:
            md = described.get(name, '')
        if not md:
            continue
        # A slot can be named like a topic page of the plugin, whose address must stay.
        taken = {pg['slug'] for pg in r['pages']} if r else set()
        for h in glob.glob(os.path.join(ROOT, 'plugins', plugin, '*', 'index.md')):
            with open(h, encoding='utf-8') as f:
                if 'guide: true' not in f.read():
                    taken.add(os.path.basename(os.path.dirname(h)))
        url = '/plugins/%s/%s/' % (plugin, name + '-slot' if name in taken else name)
        guides.setdefault(plugin, []).append({'slot': name, 'slots': [name], 'heading': name, 'md': md, 'url': url})
        urls[name] = url
    return {'results': results, 'guides': guides, 'urls': urls}


# ------------------------------------------------------------------------------------
# A dry run that prints what each README would become.
# ------------------------------------------------------------------------------------

def load_manifest(plugin):
    path = os.path.join(ROOT, '.github', 'split', plugin + '.json')
    if os.path.exists(path):
        with open(path, encoding='utf-8') as f:
            return json.load(f)
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--report', required=True, metavar='MAGIC_CHECKOUT')
    ap.add_argument('--slots')
    args = ap.parse_args()
    names = load_slot_names(args.slots)
    total_pages = total_guides = 0
    for readme in sorted(glob.glob(os.path.join(args.report, 'plugins', '*', 'README.md'))):
        plugin = os.path.basename(os.path.dirname(readme))
        with open(readme, encoding='utf-8-sig') as f:
            r = plan(f.read(), plugin, names, load_manifest(plugin))
        hub_words = len(hub_markdown(r, names).split())
        total_pages += len(r['pages'])
        total_guides += len(r['guides'])
        if not r['pages'] and not r['guides']:
            continue
        print('\n%s: hub %d words, %d guides moved to slot pages, %d concept pages' % (plugin, hub_words, len(r['guides']), len(r['pages'])))
        for p in r['pages']:
            print('   %5d  /%s/  %s' % (p['words'], p['slug'], p['title'][:60]))
    print('\ntotal concept pages: %d, slot guides: %d' % (total_pages, total_guides))


if __name__ == '__main__':
    main()

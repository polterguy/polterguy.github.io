#!/usr/bin/env python3
"""
Builds the generated slot reference: one markdown page per plugin, from the [Slot(...)]
attributes and signature classes in the C# source of the Magic repository.

Usage: build-slot-reference.py <magic-checkout> [--out <docs-root>] [--plugin <name>]

The source is read, never built, so this runs anywhere with python and a checkout of
https://github.com/polterguy/magic. Each [Slot] attribute stack on one class is one
slot: the first attribute is the primary name, the others are listed as aliases.
Arguments come from the signature class named by SignatureType; the forms understood
are `new SlotChild { ... }` initialisers, the Option/List/Map helpers, and signature
classes forwarding to a base constructor. A slot whose signature uses another form is
still listed, just without an arguments table.

Hand-written guides stay where they are. Each entry links to the guide section for the
slot when a heading such as "How to use [io.file.load]" exists in the plugin's page.
"""

import argparse
import glob
import os
import re

STR = r'"((?:[^"\\]|\\.)*)"'
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def unescape(s):
    return s.replace('\\"', '"').replace('\\\\', '\\').replace('\\n', ' ')


def read(path):
    with open(path, encoding='utf-8-sig', errors='ignore') as f:
        return f.read()


def attribute_spans(text):
    """Yields (start, end) of every [Slot(...)] attribute, honouring strings and parentheses."""
    for m in re.finditer(r'\[Slot\(', text):
        i, depth, in_str = m.end(), 1, False
        while i < len(text) and depth:
            c = text[i]
            if in_str:
                if c == '\\':
                    i += 1
                elif c == '"':
                    in_str = False
            elif c == '"':
                in_str = True
            elif c == '(':
                depth += 1
            elif c == ')':
                depth -= 1
            i += 1
        yield m.start(), i + 1  # include the closing ]


def field(body, name):
    m = re.search(r'\b%s\s*=\s*%s' % (name, STR), body)
    return unescape(m.group(1)) if m else None


def parse_slots(text):
    """Returns a list of slots found in one C# file, aliases grouped by class."""
    spans = list(attribute_spans(text))
    groups, current = [], []
    for start, end in spans:
        if current and text[current[-1][1]:start].strip() == '':
            current.append((start, end))
        else:
            if current:
                groups.append(current)
            current = [(start, end)]
    if current:
        groups.append(current)

    slots = []
    for group in groups:
        tail = text[group[-1][1]:]
        cls = re.match(r'\s*(?:public|internal)\s+(?:sealed\s+|static\s+)?class\s+(\w+)', tail)
        # One entry per [Slot] attribute, except attributes saying exactly the same thing,
        # which are aliases of the first one (such as [load-file] and [io.file.load]).
        entries = []
        for start, end in group:
            body = text[start:end]
            name = field(body, 'Name')
            if not name:
                continue
            sig = re.search(r'SignatureType\s*=\s*typeof\(([\w.:]+)\)', body)
            entry = {
                'names': [name],
                'class': cls.group(1) if cls else None,
                'description': field(body, 'Description') or '',
                'value_kind': field(body, 'ValueKind'),
                'value_description': field(body, 'ValueDescription'),
                'value_required': bool(re.search(r'ValueRequired\s*=\s*true', body)),
                'returns': field(body, 'ReturnsDescription'),
                'signature': re.split(r'[.:]', sig.group(1))[-1] if sig else None,
            }
            same = next((e for e in entries if all(
                e[k] == entry[k] for k in ('description', 'value_kind', 'value_description',
                                           'value_required', 'returns', 'signature'))), None)
            if same:
                same['names'].append(name)
            else:
                entries.append(entry)
        slots += entries
    return slots


def parse_children(body):
    """Parses SlotChild declarations of one section, ignoring children nested inside others."""
    args = []
    # Helper calls: Option("name", "type", "description", required?)
    for h in re.finditer(r'\b(Option|List|Map)\(\s*' + STR + r'\s*,\s*' + STR + r'\s*,\s*' + STR + r'(?:\s*,\s*(true|false))?', body):
        kind = h.group(1)
        args.append({
            'name': unescape(h.group(2)),
            'type': 'list' if kind == 'List' else 'map' if kind == 'Map' else unescape(h.group(3)),
            'description': unescape(h.group(4)),
            'required': h.group(5) == 'true',
        })
    # Initialisers, keeping only those at the shallowest indentation.
    decls = list(re.finditer(r'^([ \t]*)new\s+SlotChild\s*\n\1\{(.*?)\n\1\}', body, re.S | re.M))
    if decls:
        shallow = min(len(d.group(1)) for d in decls)
        for d in decls:
            if len(d.group(1)) != shallow:
                continue
            block = d.group(2)
            name = field(block.split('Children')[0], 'Name') or field(block, 'Name')
            if name:
                args.append({
                    'name': name,
                    'type': field(block, 'Type') or '',
                    'description': field(block, 'Description') or '',
                    'required': bool(re.search(r'Required\s*=\s*true', block)),
                })
    else:
        for h in re.finditer(r'new\s+SlotChild\s*\{(.*?)\}', body, re.S):
            name = field(h.group(1), 'Name')
            if name:
                args.append({
                    'name': name,
                    'type': field(h.group(1), 'Type') or '',
                    'description': field(h.group(1), 'Description') or '',
                    'required': bool(re.search(r'Required\s*=\s*true', h.group(1))),
                })
    return args


def parse_signatures(text):
    """Maps signature class name -> {'args': [...], 'out': [...]}, for the forms we understand."""
    result = {}
    classes = list(re.finditer(r'class\s+(\w+)\s*(?::\s*([\w.<>, ]+?))?\s*\{', text))
    for idx, m in enumerate(classes):
        end = classes[idx + 1].start() if idx + 1 < len(classes) else len(text)
        body = text[m.end():end]
        inputs, _, outputs = body.partition('OutputChildren')
        args = parse_children(inputs)
        # Forwarding to a base constructor: : base("type", "kind", "description")
        b = re.search(r':\s*base\(\s*' + STR + r'\s*,\s*' + STR + r'\s*,\s*' + STR, body)
        if b and not args:
            args.append({'name': '*', 'type': unescape(b.group(1)),
                         'description': unescape(b.group(3)), 'required': True})
        result[m.group(1)] = {'args': args, 'out': parse_children(outputs) if outputs else [],
                              'base': (m.group(2) or '').strip()}
    # Inherit from a base class when a signature declares nothing of its own.
    for name, sig in result.items():
        if not sig['args'] and sig['base'] in result:
            sig['args'] = result[sig['base']]['args']
        if not sig['out'] and sig['base'] in result:
            sig['out'] = result[sig['base']]['out']
    return result


def slug(heading):
    s = heading.lower()
    s = re.sub(r'[^a-z0-9 _-]', '', s)
    return re.sub(r'\s+', '-', s.strip())


def guide_anchors(docs_root, plugin):
    """Maps slot name -> anchor of the first heading in the plugin's guide naming it."""
    anchors = {}
    for path in sorted(glob.glob(os.path.join(docs_root, 'plugins', plugin, '**', '*.md'), recursive=True)):
        for line in read(path).splitlines():
            h = re.match(r'#{2,4}\s+(.*)', line)
            if not h:
                continue
            for name in re.findall(r'\[([^\]]+)\]', h.group(1)):
                rel = os.path.relpath(os.path.dirname(path), docs_root).replace(os.sep, '/')
                anchors.setdefault(name, '/%s/#%s' % (rel, slug(h.group(1))))
    return anchors


def md_cell(s):
    return (s or '').replace('|', '\\|').replace('\n', ' ')


def render_plugin(plugin, slots, sigs, anchors):
    out = ['---',
           'title: %s slot reference' % plugin,
           'description: Every slot in %s with its value, arguments and return value, generated from the source code.' % plugin,
           'generated: true',
           '---', '',
           '_This page is generated from the `[Slot]` attributes in the source code of '
           '[%s](https://github.com/polterguy/magic/tree/master/plugins/%s). '
           'Do not edit it; improve the attribute instead. The hand-written guide is at '
           '[%s](/plugins/%s/)._' % (plugin, plugin, plugin, plugin), '']
    for slot in sorted(slots, key=lambda s: s['names'][0]):
        name = slot['names'][0]
        out.append('## [%s]' % name)
        out.append('')
        out.append(slot['description'].rstrip('.') + '.' if slot['description'] else '_No description yet._')
        out.append('')
        if len(slot['names']) > 1:
            out.append('Aliases: %s' % ', '.join('**[%s]**' % n for n in slot['names'][1:]))
            out.append('')
        if slot['value_description'] or slot['value_kind']:
            req = 'required' if slot['value_required'] else 'optional'
            kind = ' (`%s`)' % slot['value_kind'] if slot['value_kind'] else ''
            out.append('* **Value**%s, %s: %s' % (kind, req, slot['value_description'] or ''))
        if slot['returns']:
            out.append('* **Returns**: %s' % slot['returns'])
        sig = sigs.get(slot['signature'], {}) if slot['signature'] else {}
        args, out_nodes = sig.get('args', []), sig.get('out', [])
        if args:
            out.append('')
            out.append('| Argument | Type | Required | Description |')
            out.append('|---|---|---|---|')
            for a in args:
                out.append('| `[%s]` | %s | %s | %s |' % (a['name'], md_cell(a['type']),
                           'yes' if a['required'] else 'no', md_cell(a['description'])))
        if out_nodes:
            out.append('')
            out.append('| Returned node | Type | Description |')
            out.append('|---|---|---|')
            for a in out_nodes:
                out.append('| `[%s]` | %s | %s |' % (a['name'], md_cell(a['type']), md_cell(a['description'])))
        guide = next((anchors[n] for n in slot['names'] if n in anchors), None)
        if guide:
            out.append('')
            out.append('Guide: [How to use [%s]](%s)' % (name, guide))
        out.append('')
    return '\n'.join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('magic')
    ap.add_argument('--out', default=ROOT)
    ap.add_argument('--plugin')
    args = ap.parse_args()

    plugins_dir = os.path.join(args.magic, 'plugins')
    names = sorted(d for d in os.listdir(plugins_dir)
                   if os.path.isdir(os.path.join(plugins_dir, d)) and d.startswith('magic.')
                   and not d.endswith('.tests'))
    if args.plugin:
        names = [args.plugin]
    index = []
    gaps = []
    for plugin in names:
        slots, sigs = [], {}
        for path in glob.glob(os.path.join(plugins_dir, plugin, '**', '*.cs'), recursive=True):
            if '/obj/' in path or '/bin/' in path or '.tests' in path:
                continue
            text = read(path)
            slots += parse_slots(text)
            if 'ISlotSignature' in text or 'SlotChild' in text:
                sigs.update(parse_signatures(text))
        if not slots:
            continue
        for s in slots:
            if not s['description']:
                gaps.append('%s: [%s] has no description' % (plugin, s['names'][0]))
        folder = os.path.join(args.out, 'reference', 'slots', plugin)
        os.makedirs(folder, exist_ok=True)
        anchors = guide_anchors(args.out if os.path.isdir(os.path.join(args.out, 'plugins')) else ROOT, plugin)
        with open(os.path.join(folder, 'index.md'), 'w', encoding='utf-8') as f:
            f.write(render_plugin(plugin, slots, sigs, anchors) + '\n')
        index.append((plugin, len(slots)))
    if not args.plugin:
        os.makedirs(os.path.join(args.out, 'reference', 'slots'), exist_ok=True)
        with open(os.path.join(args.out, 'reference', 'slots', 'index.md'), 'w', encoding='utf-8') as f:
            f.write('---\ntitle: Slot reference\n'
                    'description: Every C# slot in Magic Cloud with its value, arguments and return value, generated from the source code.\n'
                    'generated: true\n---\n\n'
                    '_Generated from the `[Slot]` attributes in the source code. '
                    'Guides and examples live in the [plugin documentation](/plugins/)._\n\n')
            for plugin, count in index:
                f.write('* [%s](/reference/slots/%s/) - %d slots\n' % (plugin, plugin, count))
    for g in gaps:
        print('gap:', g)
    print('generated %d plugin pages' % len(index))


if __name__ == '__main__':
    main()

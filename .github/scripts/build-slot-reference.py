#!/usr/bin/env python3
"""
Builds the generated slot reference under reference/slots/, from the running system.

Nothing here reads source code. A read-only Hyperlambda endpoint on hyperlambda.dev lists
every compiled slot with the slots [vocabulary], [slot.description] and
[slot.signature], and this script renders what comes back. The endpoint is public, since
it reads metadata that is public in the open source code and runs nothing a caller sends,
and is throttled per IP address and overall, so no credentials are needed.

Usage: build-slot-reference.py [--input slots.json] [--min-slots 300]

With --input the endpoint is not called, which is how to run this offline. The file is
the endpoint's response, a list of objects with [name], [description] and [signature].

The script refuses to write anything when fewer than --min-slots slots come back, since
a truncated answer must never replace the reference. Hand-written guides are untouched,
and each entry links to the section of a guide that names its slot.
"""

import argparse
import glob
import json
import os
import re
import shutil
import sys
import urllib.error
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, 'reference', 'slots')
ENDPOINT_URL = 'https://hyperlambda.dev/magic/modules/docs/slots-nodes'
PLAYGROUND_URL = 'https://hyperlambda.dev/magic/modules/docs/playground'

# Cloudflare in front of the server refuses the default user agent of most http libraries.
USER_AGENT = 'magic-docs-sync/1.0 (+https://docs.ainiro.io/reference/slots/)'


def read(path):
    with open(path, encoding='utf-8-sig') as f:
        return f.read().replace('\r\n', '\n')


# ------------------------------------------------------------------------------------
# Fetching.
# ------------------------------------------------------------------------------------

def fetch():
    request = urllib.request.Request(ENDPOINT_URL, headers={'User-Agent': USER_AGENT})
    try:
        with urllib.request.urlopen(request, timeout=120) as response:
            return json.load(response)
    except urllib.error.HTTPError as e:
        sys.exit('The slot endpoint answered %d: %s' % (e.code, e.read().decode()[:300]))


# ------------------------------------------------------------------------------------
# Signatures arrive as nested JSON, and are turned back into nodes for rendering.
# ------------------------------------------------------------------------------------

def from_json(obj, name=''):
    """Object keys become named nodes, and list items unnamed ones, exactly as Magic wrote them."""
    node = {'name': name, 'value': None, 'children': []}
    if isinstance(obj, dict):
        node['children'] = [from_json(v, k) for k, v in obj.items()]
    elif isinstance(obj, list):
        node['children'] = [from_json(v, '.') for v in obj]
    else:
        node['value'] = obj
    return node


def child(node, name):
    return next((c for c in node['children'] if c['name'] == name), None) if node else None


def value(node, name, default=None):
    c = child(node, name)
    return c['value'] if c and c['value'] is not None else default


# ------------------------------------------------------------------------------------
# Rendering.
# ------------------------------------------------------------------------------------

def has_liquid(text):
    return '{{' in text or '{%' in text


def raw(text):
    return '{% raw %}' + text + '{% endraw %}' if has_liquid(text) else text


def cell(text):
    return str(text if text is not None else '').replace('|', '\\|').replace('\n', ' ').strip()


def label(name):
    return {'.': '_unnamed child node_', '*': '_any node name_'}.get(name, '`[%s]`' % name)


MAX_DEPTH = 3


def argument_rows(nodes, cut, path=()):
    """
    One row per argument. A node that repeats one of its own ancestors is recursion in the
    contract and is skipped, and nesting stops at MAX_DEPTH, both recorded in [cut].
    """
    rows = []
    for n in nodes:
        name = n['name']
        if name in path and name not in ('*', '.'):
            cut.append(name)
            continue
        description = value(n, 'description', '')
        parts = [description.rstrip('.') + '.' if description else '']
        if value(n, 'default') is not None:
            parts.append('Default: `%s`.' % value(n, 'default'))
        if value(n, 'cardinality') in ('ZeroOrMore', 'OneOrMore'):
            parts.append('Can be repeated.')
        if value(n, 'exclusive-with'):
            parts.append('Exclusive with `[%s]`.' % value(n, 'exclusive-with'))
        shown = ' / '.join(label(p) for p in path + (name,))
        rows.append('| %s | %s | %s | %s |' % (
            shown, cell(value(n, 'type', '')), 'yes' if value(n, 'required') is True else 'no',
            cell(' '.join(p for p in parts if p))))
        nested = child(n, 'children')
        if nested:
            if len(path) + 1 >= MAX_DEPTH:
                cut.append(name)
            else:
                rows += argument_rows(nested['children'], cut, path + (name,))
    return rows


def table(head, rows):
    return ['| ' + ' | '.join(head) + ' |', '|' + '---|' * len(head)] + rows


def render_entry(entry, anchors):
    tree = entry['tree']
    out = ['## [%s]' % entry['names'][0], '']
    out.append((entry['description'].rstrip('.') + '.') if entry['description'] else '_No description yet._')
    out.append('')
    if len(entry['names']) > 1:
        out += ['Aliases: ' + ', '.join('**[%s]**' % n for n in entry['names'][1:]), '']

    facts = []
    inp = child(tree, 'input')
    if inp:
        kind = ' (`%s`)' % value(inp, 'kind') if value(inp, 'kind') else ''
        facts.append('* **Value**%s, %s: %s' % (
            kind, 'required' if value(inp, 'required') is True else 'optional', value(inp, 'description', '')))
    outp = child(tree, 'output')
    if outp and value(outp, 'description'):
        facts.append('* **Returns**: %s' % value(outp, 'description'))
    scope = child(tree, 'scope')
    if scope:
        bits = []
        if value(scope, 'requires'):
            bits.append('requires `%s`' % value(scope, 'requires'))
        if value(scope, 'provides'):
            bits.append('provides `%s`' % value(scope, 'provides'))
        facts.append('* **Scope**: %s%s' % ('; '.join(bits), (' - ' + value(scope, 'description')) if value(scope, 'description') else ''))
    out += facts + ([''] if facts else [])

    NOTE = '_Nodes nested deeper than %d levels, and nodes that repeat one of their own ancestors, are not listed._' % MAX_DEPTH
    children = child(tree, 'children')
    if children and children['children']:
        cut = []
        out += table(['Argument', 'Type', 'Required', 'Description'], argument_rows(children['children'], cut)) + ['']
        if cut:
            out += [NOTE, '']

    returned = child(outp, 'children') if outp else None
    if returned and returned['children']:
        cut = []
        out += ['Returned nodes:', ''] + table(['Node', 'Type', 'Required', 'Description'],
                                              argument_rows(returned['children'], cut)) + ['']
        if cut:
            out += [NOTE, '']

    constraints = child(tree, 'constraints')
    if constraints:
        for c in constraints['children']:
            values = child(c, 'values')
            listed = ', '.join('`[%s]`' % v['value'] for v in values['children']) if values else ''
            out.append('* **Constraint** (%s): %s%s' % (
                value(c, 'kind', c['name']), value(c, 'description', ''), (' (%s)' % listed) if listed else ''))
        out.append('')

    guide = next((anchors[n] for n in entry['names'] if n in anchors), None)
    if guide:
        out += ['Guide: [How to use [%s]](%s)' % (entry['names'][0], guide), '']
    return out


def slug(heading):
    return re.sub(r'\s+', '-', re.sub(r'[^a-z0-9 _-]', '', heading.lower()).strip())


def guide_anchors():
    anchors = {}
    for path in sorted(glob.glob(os.path.join(ROOT, 'plugins', '**', '*.md'), recursive=True)):
        for line in read(path).splitlines():
            h = re.match(r'#{2,4}\s+(.*)', line)
            if h:
                for name in re.findall(r'\[([^\]]+)\]', h.group(1)):
                    rel = os.path.relpath(os.path.dirname(path), ROOT).replace(os.sep, '/')
                    anchors.setdefault(name, '/%s/#%s' % (rel, slug(h.group(1))))
    return anchors


def group_entries(records):
    """One entry per distinct contract; slots saying exactly the same thing are aliases."""
    groups = {}
    for r in records:
        groups.setdefault((r.get('description') or '', json.dumps(r.get('signature'), sort_keys=True)), []).append(r['name'])
    entries = []
    for (description, signature), names in groups.items():
        names.sort(key=lambda n: ('.' not in n, n))
        entries.append({'names': names, 'description': description, 'tree': from_json(json.loads(signature))})
    return entries


def namespace(entry):
    primary = entry['names'][0]
    return primary.split('.')[0] if '.' in primary else 'core'


def code_block(text, lang):
    return '\n'.join(['```' + lang, raw(text.strip('\n')), '```'])


def endpoint_numbers(endpoint):
    """The throttles declared by the slot endpoint itself, as (limit, window) per kind."""
    found = {}
    for limit, window, per in re.findall(r'limit:int:(\d+)\s+window:int:(\d+)\s+per:(\w+)', endpoint):
        found[per] = (int(limit), int(window))
    return {'ip_limit': found['ip'][0], 'ip_window': found['ip'][1],
            'all_limit': found['global'][0], 'all_window': found['global'][1]}


def policy_numbers(sandbox):
    def number(key):
        m = re.search(r'^\s*%s:int:(\d+)' % re.escape(key), sandbox, re.M)
        return int(m.group(1)) if m else None
    slots = re.search(r'^\s{9}slots\n((?:\s{12}\S.*\n)+)', sandbox, re.M)
    return {
        'limit': number('limit'), 'window': number('window'), 'timeout': number('timeout') // 1000,
        'max': number('max-hyperlambda'),
        'slots': len(slots.group(1).splitlines()) if slots else 0,
    }


# ------------------------------------------------------------------------------------
# The reference page itself, which is also the story of how it is built.
# ------------------------------------------------------------------------------------

EXAMPLES = [
    ('List the slot names',
     '[vocabulary] returns the slots you are allowed to see. With a prefix it filters, so `vocabulary:strings.` returns only the string slots.',
     'vocabulary:strings.\nreturn-nodes:x:@vocabulary/*\n', None),
    ('Get one description',
     None,
     'slot.description:strings.concat\nreturn-value:x:@slot.description\n', 'Concatenates strings'),
    ('Get every description',
     'The same loop the full reference uses, without the signature.',
     'vocabulary\n.result\nfor-each:x:@vocabulary/*\n   slot.description:x:@.dp/#\n   .entry\n      .\n'
     '         name:x:@.dp/#\n         description:x:@slot.description\n   unwrap:x:@.entry/*/*\n'
     '   add:x:@.result\n      get-nodes:x:@.entry/*\nreturn-nodes:x:@.result/*\n', None),
    ('Get one signature as Hyperlambda',
     '[slot.signature] returns a tree, and [lambda2hyper] writes any tree back as Hyperlambda text. [lambda2json] would give you JSON instead.',
     'slot.signature:convert\nlambda2hyper:x:@slot.signature/*\nreturn-value:x:@lambda2hyper\n', None),
    ('Get only the arguments of a slot',
     None,
     'slot.signature:convert\n.result\nfor-each:x:@slot.signature/*/children/*\n   get-name:x:@.dp/#\n'
     '   .entry\n      .\n         name:x:@get-name\n         type:x:@.dp/#/*/type\n'
     '         required:x:@.dp/#/*/required\n         description:x:@.dp/#/*/description\n'
     '   unwrap:x:@.entry/*/*\n   add:x:@.result\n      get-nodes:x:@.entry/*\nreturn-nodes:x:@.result/*\n',
     '[{"name": "type", "type": "string", "required": true, "description": "Target Hyperlambda type name"}]'),
    ('Get only the required arguments',
     None,
     'slot.signature:convert\n.result\nfor-each:x:@slot.signature/*/children/*\n   if\n      eq:x:@.dp/#/*/required\n'
     '         .:bool:true\n      .lambda\n         get-name:x:@.dp/#\n         unwrap:x:+/*/*\n'
     '         add:x:@.result\n            .\n               .:x:@get-name\nreturn-nodes:x:@.result/*\n',
     '["type"]'),
]


def faq(p):
    return [
        ('How is this slot reference generated?',
         'Automatically, from the running system. A GitHub Actions workflow asks a Hyperlambda endpoint on hyperlambda.dev for every compiled slot. '
         'The endpoint runs a short Hyperlambda program that lists the slots with [vocabulary] and reads each slot\'s description and signature '
         'with [slot.description] and [slot.signature]. A Python script renders the answer as the pages in this section.'),
        ('Why is it generated instead of written by hand?',
         'A slot describes itself in the same place its code lives, so the reference cannot drift away from the implementation. '
         'If an entry is thin or wrong, the fix is to improve the slot\'s own metadata, and the next run publishes it.'),
        ('What is homoiconicity?',
         'A language is homoiconic when its programs are stored in a data structure the language itself can read and change. '
         'In Hyperlambda a program is a tree of nodes, and so is the metadata that describes every slot, so a program can ask the system about itself '
         'and process the answer with the same tools it uses for any other data.'),
        ('What is meta programming, and where is it here?',
         'Meta programming is code that reads, generates or transforms code. This reference is a Hyperlambda program whose input is the definition of Hyperlambda itself: '
         'it lists the language\'s own slots, reads their contracts, and the result becomes the documentation.'),
        ('Can I run my own Hyperlambda against the public sandbox?',
         'Yes. POST your code as JSON to %s, with no account or key. It is rate limited to %d requests per %d seconds per IP address, '
         'runs for at most %d seconds, and accepts at most %d characters of code.' % (PLAYGROUND_URL, p['limit'], p['window'], p['timeout'], p['max'])),
        ('Is it safe to let anybody run code on that server?',
         'The sandbox only runs code whose every slot is on a whitelist of %d slots: introspection, tree handling, strings and arithmetic. '
         'Code that touches files, databases, the network, configuration or anything else is rejected before it runs, and every call is rate limited and time limited.' % p['slots']),
        ('Can I get the whole reference as data?',
         'Yes. GET %s returns every compiled slot as a JSON array of objects with the fields name, description and signature, where the signature is the slot\'s contract as nested JSON. '
         'It needs no account or key. The answer is about 640 KB, so keep a copy rather than asking again.' % ENDPOINT_URL),
        ('Is it safe to leave that endpoint open?',
         'It only reads metadata that is already public in the open source code, and it runs nothing that the caller sends. '
         'It is throttled to %d requests per %d seconds per IP address and %d per %d seconds for everybody together, and answers 429 beyond that.'
         % (p['ip_limit'], p['ip_window'], p['all_limit'], p['all_window'])),
        ('Why does the sandbox show fewer slots than this reference?',
         'The sandbox runs your code, so it can only describe the %d slots it is itself allowed to call. A slot can only be described by code that is allowed to call it, '
         'so a sandbox that described everything could also run everything. Use the slot endpoint for the whole language and the sandbox to experiment.' % p['slots']),

        ('How do I get only the descriptions, or only the arguments, of some slots?',
         'Use [vocabulary] with a prefix to pick slots by name, [slot.description] for one description, and [slot.signature] for the input, arguments and output of one slot. '
         'The examples on this page show each of them, and all of them run in the public sandbox.'),
        ('How do I fix a missing or wrong description?',
         'Change the metadata on the slot in the source code of Magic Cloud, its description or its signature. The next run of the pipeline publishes it here.'),
        ('How often is the reference updated?',
         'Once a week, and on demand from the Actions tab of the documentation repository.'),
        ('What is Hyperlambda?',
         'Hyperlambda is a declarative programming language where the source code is a tree of nodes rather than free-form text. '
         'It runs on Magic Cloud, an open source, MIT licensed platform that builds and runs an entire backend.'),
        ('Is Hyperlambda Turing complete?',
         'Yes. Slots such as [if], [for-each] and [while] give it branching and loops, which is what makes it Turing complete.'),
        ('Why do I get error code 1010 when I call the endpoint from a script?',
         'The server sits behind Cloudflare, which rejects requests that carry no User-Agent header, or the default one of an http library such as Python\'s urllib. '
         'Send any descriptive User-Agent and the request goes through.'),
    ]


def render_index(counts, total, endpoint, sandbox, workflow, p):
    lines = [
        '---',
        'title: Slot reference',
        'description: Every slot in Magic Cloud and Hyperlambda with its arguments and return value, generated by asking the running system about itself.',
        'generated: true',
        'faq:',
    ]
    for q, a in faq(p):
        lines += ['  - q: ' + json.dumps(q, ensure_ascii=False), '    a: ' + json.dumps(a, ensure_ascii=False)]
    lines += ['---', '']

    lines += [
        'Every slot in Magic Cloud and Hyperlambda, **%d in total**, with its arguments and return value. '
        'Start with the **core keywords**, such as [if] and [for-each], or pick a namespace. '
        '[How this reference is built](#this-reference-was-not-written-it-was-asked-for) is explained further down.' % total,
        '',
        '## Slots by namespace',
        '',
    ]
    for ns, n in counts:
        lines.append('* [%s](/reference/slots/%s/) - %d %s' % (
            'core keywords' if ns == 'core' else ns + '.*', ns, n, 'slot' if n == 1 else 'slots'))
    lines += ['']

    lines += [
        '## This reference was not written. It was asked for.',
        '',
        'Every page in this section is generated, and what it is generated from is not the source code but the **running system**. '
        'Each slot in Magic Cloud carries its own name, description, arguments and return value as metadata, and Hyperlambda can read that metadata at runtime. '
        'Once a week a GitHub Actions workflow asks for it, receives **%d slots**, and renders the pages you are reading. '
        'Nobody parses source files, scrapes anything or keeps a second copy that can go stale.' % total,
        '',
        '### Why this is possible: homoiconicity',
        '',
        'Hyperlambda is homoiconic. A program is a tree of nodes, and a tree of nodes is also the data structure the program works on. '
        'A slot is an ordinary node, and asking about slots is an ordinary function call: **[vocabulary]** lists their names, '
        '**[slot.description]** returns what one of them does, **[slot.signature]** returns its contract as a tree, and **[lambda2hyper]** writes any tree back as Hyperlambda text. '
        'Meta programming is not a library you import here, it is what the language does by default. This documentation is a Hyperlambda program '
        'whose input is the definition of Hyperlambda itself.',
        '',
        '### The code that produced this reference',
        '',
        'This is the complete Hyperlambda file behind the endpoint the pipeline calls. This is dogfooding in its purest form: the language documents itself with its own code.',
        '',
        code_block(endpoint, 'hyperlambda'),
        '',
        'It begins with two throttles, one per IP address and one for everybody together, and has no authentication, since there is nothing to protect: it reads metadata that is '
        'public in the open source code and runs nothing a caller sends. Everything after that is slots, and nothing else. '
        'It lists the compiled slots, reads the description and the signature of each, and returns the signature as **nodes**. Magic turns nodes into JSON by itself, '
        'since a tree of nodes already is a tree of JSON objects, so there is no serialising step, no text format to agree on and nothing to parse. '
        'One detail shows how it works. A constraint is named after its kind and can occur more than once, which a JSON object cannot hold as a key, '
        'so the loop in the middle renames every constraint, at any depth, to an unnamed node with its kind as a child, using the `**` selector to reach them all in one expression. '
        'Magic then writes them as a list. A Python script renders the result as markdown.',
        '',
        '### Get the whole reference yourself',
        '',
        'The endpoint above is public. There is no account, no key and no secret. To protect the server it is throttled to **%d requests per %d seconds per IP address**, '
        'and to **%d per %d seconds** for everybody together, and beyond that it answers `429`. The answer is about 640 KB, so keep a copy rather than asking again.'
        % (p['ip_limit'], p['ip_window'], p['all_limit'], p['all_window']),
        '',
        '```bash',
        'curl -s %s' % ENDPOINT_URL,
        '```',
        '',
        'It returns a JSON array with one object per slot, with the fields `name`, `description` and `signature`. The signature is the contract of the slot as nested JSON: '
        '`input` is the value the slot takes, `children` are its arguments, `constraints` are the rules between them, `scope` says where it can be used, and `output` is what it returns. '
        'Arguments without a name, because they are positional, come as a list. With `jq` you can ask it questions.',
        '',
        '#### List every slot name',
        '',
        '```bash',
        "curl -s %s | jq -r '.[].name'" % ENDPOINT_URL,
        '```',
        '',
        '#### Get the description of one slot',
        '',
        '```bash',
        "curl -s %s | jq -r '.[] | select(.name == \"strings.concat\") | .description'" % ENDPOINT_URL,
        '```',
        '',
        '#### Get the full signature of one slot',
        '',
        '```bash',
        "curl -s %s | jq '.[] | select(.name == \"data.read\") | .signature'" % ENDPOINT_URL,
        '```',
        '',
        '#### List the arguments of a slot',
        '',
        '```bash',
        "curl -s %s | jq -r '.[] | select(.name == \"data.create\") | .signature.children | keys[]'" % ENDPOINT_URL,
        '```',
        '',
        '#### List only the required arguments of a slot',
        '',
        '```bash',
        "curl -s %s | jq -r '.[] | select(.name == \"data.create\") | .signature.children | to_entries[] | select(.value.required == true) | .key'" % ENDPOINT_URL,
        '```',
        '',
        '#### Find the slots whose description mentions something',
        '',
        '```bash',
        "curl -s %s | jq -r '.[] | select((.description // \"\") | test(\"rows\")) | .name'" % ENDPOINT_URL,
        '```',
        '',
        'The public sandbox below sees fewer slots than this endpoint. It runs **your** code, so it can only describe the **%d slots** it is itself allowed to call. '
        'A slot can only be described by code that is allowed to call it, so a sandbox that described everything could also run everything. '
        'Use the endpoint for the whole language, and the sandbox to experiment.' % p['slots'],
        '',
        '### The public sandbox',
        '',
        'Anybody can send Hyperlambda to **`POST %s`**, with no account and no key. It is rate limited to **%d requests per %d seconds** per IP address, '
        'stops after **%d seconds**, and accepts up to **%d characters**. Every slot your code uses is checked against the whitelist before anything runs, '
        'so code that touches files, databases, the network or configuration is rejected rather than executed. '
        'Send `{"describe": true}` to get the exact vocabulary, limits and timeout without running anything. '
        'AI agents can find it in [/.well-known/hyperlambda-agent](https://hyperlambda.dev/.well-known/hyperlambda-agent), and it is yours to experiment with.' % (PLAYGROUND_URL, p['limit'], p['window'], p['timeout'], p['max']),
        '',
        'Save any example below as `example.hl` and send it like this.',
        '',
        '```bash',
        'jq -Rs \'{hyperlambda: .}\' example.hl | curl -s %s \\' % PLAYGROUND_URL,
        '  -H "Content-Type: application/json" -d @-',
        '```',
        '',
    ]
    for title, text, code, result in EXAMPLES:
        lines += ['#### ' + title, '']
        if text:
            lines += [text, '']
        lines += [code_block(code, 'hyperlambda'), '']
        if result:
            lines += ['Returns `%s`.' % result, '']

    lines += [
        'This is the complete source of the sandbox endpoint, generated by the Sandbox API generator in Magic Cloud. The policy near the top is the whole whitelist.',
        '',
        '<details markdown="1">',
        '<summary>Show the entire sandbox endpoint</summary>',
        '',
        code_block(sandbox, 'hyperlambda'),
        '',
        '</details>',
        '',
        '### The pipeline',
        '',
        'This is the complete GitHub Actions workflow. It needs no credentials, since the endpoint is public.',
        '',
        '<details markdown="1">',
        '<summary>Show the entire workflow</summary>',
        '',
        code_block(workflow, 'yaml'),
        '',
        '</details>',
        '',
        '{% include faq.html %}',
        '',
    ]
    return '\n'.join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--input')
    ap.add_argument('--min-slots', type=int, default=300)
    args = ap.parse_args()

    data = json.loads(read(args.input)) if args.input else fetch()
    records = data.get('result', data) if isinstance(data, dict) else data
    if not isinstance(records, list) or len(records) < args.min_slots:
        sys.exit('Only %d slots came back and at least %d are expected, so nothing was written.'
                 % (len(records) if isinstance(records, list) else 0, args.min_slots))

    entries = group_entries(records)
    anchors = guide_anchors()
    by_ns = {}
    for e in entries:
        by_ns.setdefault(namespace(e), []).append(e)

    # Only generated pages are removed, never anything written by hand.
    if os.path.isdir(OUT):
        for name in os.listdir(OUT):
            path = os.path.join(OUT, name)
            index = os.path.join(path, 'index.md')
            if os.path.isdir(path) and os.path.exists(index) and 'generated: true' in read(index):
                shutil.rmtree(path)
    os.makedirs(OUT, exist_ok=True)

    counts = []
    for ns in sorted(by_ns, key=lambda n: (n != 'core', n)):
        group = sorted(by_ns[ns], key=lambda e: e['names'][0])
        title = 'Core keywords' if ns == 'core' else '%s.* slots' % ns
        body = ['---', 'title: %s' % title,
                'description: The %d slots %s in Magic Cloud and Hyperlambda, with their arguments and return values, generated from the running system.'
                % (len(group), 'that make up the core keywords' if ns == 'core' else 'named %s.*' % ns),
                'generated: true', '---', '',
                '_Generated from the running system, see [how this reference is built](/reference/slots/). Do not edit this page._', '']
        for e in group:
            body += render_entry(e, anchors)
        text = '\n'.join(body)
        os.makedirs(os.path.join(OUT, ns), exist_ok=True)
        with open(os.path.join(OUT, ns, 'index.md'), 'w', encoding='utf-8') as f:
            f.write(raw(text) + '\n')
        counts.append((ns, len(group)))

    endpoint = read(os.path.join(ROOT, '.github', 'endpoint', 'slots-nodes.get.hl'))
    sandbox = read(os.path.join(ROOT, '.github', 'endpoint', 'playground.post.hl'))
    workflow = read(os.path.join(ROOT, '.github', 'workflows', 'slot-reference.yml'))
    numbers = dict(policy_numbers(sandbox), **endpoint_numbers(endpoint))
    page = render_index(counts, len(entries), endpoint, sandbox, workflow, numbers)
    with open(os.path.join(OUT, 'index.md'), 'w', encoding='utf-8') as f:
        f.write(page)
    print('wrote %d entries in %d namespaces' % (len(entries), len(counts)))


if __name__ == '__main__':
    main()

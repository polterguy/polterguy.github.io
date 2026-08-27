#!/usr/bin/env python3
"""
Builds llms-full.txt: every documentation page concatenated into one markdown file,
so an agent can ingest the whole corpus in a single fetch.

This runs OUTSIDE Jekyll deliberately. A Liquid template cannot do this job: reading
another page's `content` from a template yields Jekyll's *rendered HTML*, not the
markdown source, which produced a file 28% larger and made entirely of
`<code class="language-plaintext highlighter-rouge">` noise. There is no Liquid filter
that reverses that, and GitHub Pages permits no plugin that could. So the sources are
read directly here instead, and .github/workflows/llms-full.yml keeps the output in
sync on every push.
"""

import os
import re
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SITE = "https://docs.ainiro.io"
OUT = os.path.join(ROOT, "llms-full.txt")

HEADER = """# Magic Cloud Documentation — Full Text

Every page of the Magic Cloud documentation, concatenated into one file, so an
agent can ingest the whole corpus in a single fetch instead of crawling the site.
Generated from the same markdown sources that build https://docs.ainiro.io.

Magic Cloud is an MIT-licensed, self-hosted platform that builds and runs an
entire backend — database, secured REST API, business logic, background jobs,
authentication and role-based access control — and exposes all of it to AI agents
over MCP. It runs Hyperlambda, a declarative language whose source is a tree
structure rather than free-form text.

Curated index of this site: {site}/llms.txt
Source code: https://github.com/polterguy/magic

Each page below starts with a level-one heading carrying its title, followed by
the URL it is published at. Headings inside a page start at level two.
""".format(site=SITE)


def find_pages():
    """Every published markdown page. Mirrors what jekyll-sitemap emits."""
    for dirpath, dirnames, filenames in os.walk(ROOT):
        # Jekyll ignores underscore dirs; skip VCS and tooling dirs too.
        dirnames[:] = [d for d in dirnames if not d.startswith((".", "_"))]
        for name in filenames:
            if name.endswith(".md"):
                yield os.path.relpath(os.path.join(dirpath, name), ROOT)


def split_front_matter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}, text
    return (yaml.safe_load(m.group(1)) or {}), text[m.end():]


def render_faq(front):
    """The faq.html include renders the page's `faq:` front matter, not body text.
    Dropping the include would silently delete that content, so render it here."""
    items = front.get("faq") or []
    if not items:
        return ""
    out = ["## Frequently asked questions", ""]
    for item in items:
        out.append("**{}**".format(str(item.get("q", "")).strip()))
        out.append("")
        out.append(str(item.get("a", "")).strip())
        out.append("")
    return "\n".join(out)


def expand_includes(body, front, path):
    body = body.replace("{% include faq.html %}", render_faq(front))

    def video(m):
        return "Video: https://www.youtube.com/watch?v={}".format(m.group(1))

    body = re.sub(r'\{%\s*include video id="([^"]+)"[^%]*%\}', video, body)
    return body


def clean(body, front, path):
    # Liquid raw guards protect {{ }} from Jekyll; outside Jekyll they are noise.
    body = re.sub(r"^[ \t]*\{%-?\s*(end)?raw\s*-?%\}[ \t]*\n", "", body, flags=re.M)
    body = re.sub(r"\{%-?\s*(end)?raw\s*-?%\}\s*", "", body)

    body = expand_includes(body, front, path)

    # Site-relative links break outside the site; make them absolute.
    body = re.sub(r"\]\((/[^)]*)\)", r"](%s\1)" % SITE, body)

    leftovers = re.findall(r"\{%[^%]*%\}", body)
    if leftovers:
        print("ERROR: unhandled Liquid in {}: {}".format(path, leftovers[:3]), file=sys.stderr)
        raise SystemExit(1)
    return body.strip()


def url_for(path):
    return "/" + path.replace("index.md", "").replace(".md", "")


def main():
    pages = []
    for path in find_pages():
        front, body = split_front_matter(open(os.path.join(ROOT, path), encoding="utf-8").read())
        pages.append((url_for(path), front, clean(body, front, path), path))
    pages.sort(key=lambda p: p[0])

    chunks = [HEADER]
    for url, front, body, _ in pages:
        chunks.append("\n# {}\n".format(front.get("title") or url))
        chunks.append("URL: {}{}".format(SITE, url))
        if front.get("description"):
            chunks.append("Description: {}".format(front["description"]))
        chunks.append("\n" + body + "\n")

    open(OUT, "w", encoding="utf-8").write("\n".join(chunks).rstrip() + "\n")
    print("wrote {} ({} pages, {:,} bytes)".format(OUT, len(pages), os.path.getsize(OUT)))


if __name__ == "__main__":
    main()

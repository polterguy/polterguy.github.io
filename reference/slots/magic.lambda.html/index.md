---
title: magic.lambda.html slot reference
description: Every slot in magic.lambda.html with its value, arguments and return value, generated from the source code.
generated: true
---

_This page is generated from the `[Slot]` attributes in the source code of [magic.lambda.html](https://github.com/polterguy/magic/tree/master/plugins/magic.lambda.html). Do not edit it; improve the attribute instead. The hand-written guide is at [magic.lambda.html](/plugins/magic.lambda.html/)._

## [html-decode]

HTML decodes the specified string.

* **Value** (`html-encoded`), required: HTML encoded text to decode
* **Returns**: Resolves to the decoded text

Guide: [How to use [html-decode]](/plugins/magic.lambda.html/#how-to-use-html-decode)

## [html2lambda]

Transforms HTML into a lambda hierarchy.

* **Value** (`html`), required: HTML markup to transform
* **Returns**: Resolves to the parsed HTML hierarchy as child nodes

Guide: [How to use [html2lambda]](/plugins/magic.lambda.html/#how-to-use-html2lambda)

## [html2markdown]

Transforms HTML into Markdown.

* **Value** (`html`), required: HTML markup to transform
* **Returns**: Resolves to the generated Markdown

| Argument | Type | Required | Description |
|---|---|---|---|
| `[url]` | string | no | Base URL used when resolving links |
| `[images]` | bool | no | Whether images should be emitted |
| `[code]` | bool | no | Whether code blocks should be emitted |
| `[lists]` | bool | no | Whether lists should be emitted |

Guide: [How to use [html2markdown]](/plugins/magic.lambda.html/#how-to-use-html2markdown)

## [lambda2html]

Transforms a lambda hierarchy into HTML.

* **Value** (`html-tree`), required: Expression selecting the lambda hierarchy to transform
* **Returns**: Resolves to the generated HTML markup

Guide: [How to use [lambda2html]](/plugins/magic.lambda.html/#how-to-use-lambda2html)

## [markdown2html]

Transforms Markdown into HTML.

* **Value** (`markdown`), required: Markdown text to transform
* **Returns**: Resolves to the HTML in value and any YAML front matter as child nodes

| Argument | Type | Required | Description |
|---|---|---|---|
| `[media]` | bool | no | Whether media link extensions should be enabled |

Guide: [How to use [markdown2html]](/plugins/magic.lambda.html/#how-to-use-markdown2html)


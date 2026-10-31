---
title: "[markdown2html]"
description: "markdown2html is a core slot of Magic Cloud. Transforms Markdown into HTML."
generated: true
llms: false
slot_json: "/reference/slots/core/markdown2html/slot.json"
---

`markdown2html` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Transforms Markdown into HTML.

* **Value** (`markdown`), required: Markdown text to transform
* **Returns**: Resolves to the HTML in value and any YAML front matter as child nodes

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[media]` | bool | no | Whether media link extensions should be enabled. |

Guide: [How to use [markdown2html]](/plugins/magic.lambda.html/html2markdown/#front-matter-and-markdown2html)

### Guide

[How to use `markdown2html`](/plugins/magic.lambda.html/markdown2html/)

### JSON declaration

This is the complete declaration of `markdown2html`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "markdown2html",
  "description": "Transforms Markdown into HTML",
  "signature": {
    "input": {
      "kind": "markdown",
      "description": "Markdown text to transform",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "media": {
        "type": "bool",
        "description": "Whether media link extensions should be enabled",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      }
    },
    "output": {
      "mode": "Both",
      "kind": "html,text",
      "description": "Resolves to the HTML in value and any YAML front matter as child nodes"
    }
  }
}
```

</details>

---

[&larr; `map`](/reference/slots/core/map/) | [all core slots](/reference/slots/core/) | [`mt` &rarr;](/reference/slots/core/mt/)


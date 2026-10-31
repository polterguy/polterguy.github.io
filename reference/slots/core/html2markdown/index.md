---
title: "[html2markdown]"
description: "html2markdown is a core slot of Magic Cloud. Transforms HTML into Markdown."
generated: true
llms: false
slot_json: "/reference/slots/core/html2markdown/slot.json"
---

`html2markdown` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Transforms HTML into Markdown.

* **Value** (`html`), required: HTML markup to transform
* **Returns**: Resolves to the generated Markdown

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[url]` | string | no | Base URL used when resolving links. |
| `[images]` | bool | no | Whether images should be emitted. Default: `true`. |
| `[code]` | bool | no | Whether code blocks should be emitted. Default: `true`. |
| `[lists]` | bool | no | Whether lists should be emitted. Default: `true`. |

Guide: [How to use [html2markdown]](/plugins/magic.lambda.html/#how-to-use-html2markdown)

### JSON declaration

This is the complete declaration of `html2markdown`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "html2markdown",
  "description": "Transforms HTML into Markdown",
  "signature": {
    "input": {
      "kind": "html",
      "description": "HTML markup to transform",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "url": {
        "type": "string",
        "kind": "url",
        "description": "Base URL used when resolving links",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      },
      "images": {
        "type": "bool",
        "description": "Whether images should be emitted",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "true",
        "role": "Option",
        "projection": "Value"
      },
      "code": {
        "type": "bool",
        "description": "Whether code blocks should be emitted",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "true",
        "role": "Option",
        "projection": "Value"
      },
      "lists": {
        "type": "bool",
        "description": "Whether lists should be emitted",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "true",
        "role": "Option",
        "projection": "Value"
      }
    },
    "output": {
      "mode": "Value",
      "kind": "markdown,text",
      "description": "Resolves to the generated Markdown"
    }
  }
}
```

</details>

---

[&larr; `html2lambda`](/reference/slots/core/html2lambda/) | [all core slots](/reference/slots/core/) | [`html2pdf` &rarr;](/reference/slots/core/html2pdf/)


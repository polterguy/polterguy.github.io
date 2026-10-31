---
title: "[pdf2text]"
description: "pdf2text is a core slot of Magic Cloud. Extracts text from a PDF file or stream."
generated: true
llms: false
slot_json: "/reference/slots/core/pdf2text/slot.json"
---

`pdf2text` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Extracts text from a PDF file or stream.

* **Value** (`pdf-file,pdf-content,binary-content`), required: PDF file path, bytes, or stream to extract text from
* **Returns**: Returns extracted text in value or, when preserving pages, one child node per page

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[preserve-pages]` | bool | no | Whether to return one child node per page instead of one combined value. Default: `false`. |

Guide: [How to use [pdf2text]](/plugins/magic.lambda.pdf/#how-to-use-pdf2text)

### JSON declaration

This is the complete declaration of `pdf2text`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "pdf2text",
  "description": "Extracts text from a PDF file or stream",
  "signature": {
    "input": {
      "kind": "pdf-file,pdf-content,binary-content",
      "description": "PDF file path, bytes, or stream to extract text from",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "preserve-pages": {
        "type": "bool",
        "description": "Whether to return one child node per page instead of one combined value",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "false",
        "role": "Option",
        "projection": "Value"
      }
    },
    "output": {
      "mode": "Both",
      "kind": "text",
      "description": "Returns extracted text in value or, when preserving pages, one child node per page"
    }
  }
}
```

</details>

---

[&larr; `or`](/reference/slots/core/or/) | [all core slots](/reference/slots/core/) | [`reference` &rarr;](/reference/slots/core/reference/)


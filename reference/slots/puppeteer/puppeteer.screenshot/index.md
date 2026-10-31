---
title: "[puppeteer.screenshot]"
description: "puppeteer.screenshot is a slot in the puppeteer namespace of Magic Cloud. Captures a screenshot of the page."
generated: true
llms: false
slot_json: "/reference/slots/puppeteer/puppeteer.screenshot/slot.json"
---

`puppeteer.screenshot` is a slot in the `puppeteer` namespace, in Hyperlambda, the language of Magic Cloud. Captures a screenshot of the page.

* **Value** (`puppeteer-session`), required: Puppeteer session ID
* **Returns**: Resolves to the screenshot image bytes
* **Scope**: requires `puppeteer-session`

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[filename]` | string | yes | Destination filename. |
| `[full-page]` | bool | no | Whether to capture the full page. Default: `false`. |
| `[type]` | string | no | Image type. |
| `[quality]` | int | no | JPEG/WebP image quality. |

### Guide

[How to use `puppeteer.screenshot`](/plugins/magic.lambda.puppeteer/puppeteer.screenshot/)

### JSON declaration

This is the complete declaration of `puppeteer.screenshot`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "puppeteer.screenshot",
  "description": "Captures a screenshot of the page",
  "signature": {
    "input": {
      "kind": "puppeteer-session",
      "description": "Puppeteer session ID",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "filename": {
        "type": "string",
        "kind": "image-file",
        "description": "Destination filename",
        "required": true,
        "mode": "ValueOrExpression",
        "cardinality": "ExactlyOne",
        "role": "Option",
        "projection": "Value"
      },
      "full-page": {
        "type": "bool",
        "description": "Whether to capture the full page",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "false",
        "role": "Option",
        "projection": "Value"
      },
      "type": {
        "type": "string",
        "kind": "image-format",
        "description": "Image type",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      },
      "quality": {
        "type": "int",
        "description": "JPEG/WebP image quality",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      }
    },
    "scope": {
      "requires": "puppeteer-session"
    },
    "output": {
      "mode": "Value",
      "kind": "image,binary-content",
      "description": "Resolves to the screenshot image bytes"
    }
  }
}
```

</details>

---

[&larr; `puppeteer.press`](/reference/slots/puppeteer/puppeteer.press/) | [all `puppeteer.*` slots](/reference/slots/puppeteer/) | [`puppeteer.select` &rarr;](/reference/slots/puppeteer/puppeteer.select/)


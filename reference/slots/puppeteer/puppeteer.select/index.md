---
title: "[puppeteer.select]"
description: "puppeteer.select is a slot in the puppeteer namespace of Magic Cloud. Selects an option in a select element."
generated: true
llms: false
slot_json: "/reference/slots/puppeteer/puppeteer.select/slot.json"
---

`puppeteer.select` is a slot in the `puppeteer` namespace, in Hyperlambda, the language of Magic Cloud. Selects an option in a select element.

* **Value** (`puppeteer-session`), required: Puppeteer session ID
* **Scope**: requires `puppeteer-session`

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| `[selector]` | string | yes | CSS selector. |
| `[values]` | string\|lambda | no | Option values to select. |
| `[values]` / _unnamed child node_ | string | no | Argument value. Can be repeated. |

Guide: [How to use [puppeteer.select]](/plugins/magic.lambda.puppeteer/#puppeteerselect)

### JSON declaration

This is the complete declaration of `puppeteer.select`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "puppeteer.select",
  "description": "Selects an option in a select element",
  "signature": {
    "input": {
      "kind": "puppeteer-session",
      "description": "Puppeteer session ID",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "selector": {
        "type": "string",
        "kind": "css-selector",
        "description": "CSS selector",
        "required": true,
        "mode": "ValueOrExpression",
        "cardinality": "ExactlyOne",
        "role": "Option",
        "projection": "Value"
      },
      "values": {
        "type": "string|lambda",
        "description": "Option values to select",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Arguments",
        "projection": "ArgumentBag",
        "children": [
          {
            "type": "string",
            "kind": "javascript-argument",
            "description": "Argument value",
            "required": false,
            "mode": "ValueOrExpression",
            "cardinality": "ZeroOrMore",
            "role": "Option",
            "projection": "Value"
          }
        ]
      }
    },
    "scope": {
      "requires": "puppeteer-session"
    }
  }
}
```

</details>

---

[&larr; `puppeteer.screenshot`](/reference/slots/puppeteer/puppeteer.screenshot/) | [all `puppeteer.*` slots](/reference/slots/puppeteer/) | [`puppeteer.title` &rarr;](/reference/slots/puppeteer/puppeteer.title/)


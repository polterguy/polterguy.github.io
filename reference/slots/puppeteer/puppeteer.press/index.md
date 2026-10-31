---
title: "[puppeteer.press]"
description: "puppeteer.press is a slot in the puppeteer namespace of Magic Cloud. Sends a key press to the page."
generated: true
llms: false
slot_json: "/reference/slots/puppeteer/puppeteer.press/slot.json"
---

`puppeteer.press` is a slot in the `puppeteer` namespace, in Hyperlambda, the language of Magic Cloud. Sends a key press to the page.

* **Value** (`puppeteer-session`), required: Puppeteer session ID
* **Scope**: requires `puppeteer-session`

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| `[delay]` | int | no | Delay in milliseconds between key down and up. |
| `[key]` | string | no | Key to press. |
| `[selector]` | string | yes | CSS selector. |

Guide: [How to use [puppeteer.press]](/plugins/magic.lambda.puppeteer/#puppeteerpress)

### JSON declaration

This is the complete declaration of `puppeteer.press`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "puppeteer.press",
  "description": "Sends a key press to the page",
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
      "key": {
        "type": "string",
        "kind": "keyboard-key",
        "description": "Key to press",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      },
      "delay": {
        "type": "int",
        "description": "Delay in milliseconds between key down and up",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
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

[&larr; `puppeteer.goto`](/reference/slots/puppeteer/puppeteer.goto/) | [all `puppeteer.*` slots](/reference/slots/puppeteer/) | [`puppeteer.screenshot` &rarr;](/reference/slots/puppeteer/puppeteer.screenshot/)


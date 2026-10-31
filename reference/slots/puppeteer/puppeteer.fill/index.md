---
title: "[puppeteer.fill]"
description: "puppeteer.fill is a slot in the puppeteer namespace of Magic Cloud. Fills an input element with text."
generated: true
llms: false
slot_json: "/reference/slots/puppeteer/puppeteer.fill/slot.json"
---

`puppeteer.fill` is a slot in the `puppeteer` namespace, in Hyperlambda, the language of Magic Cloud. Fills an input element with text.

* **Value** (`puppeteer-session`), required: Puppeteer session ID
* **Scope**: requires `puppeteer-session`

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[selector]` | string | yes | CSS selector. |
| `[text]` | string | no | Text to send. |
| `[config-key]` | string | no | Configuration key resolving the text to send. |
| `[delay]` | int | no | Delay in milliseconds between key presses. |

### Constraints

* **ExactlyOneOf**: Provide either [text] or [config-key] (`[text]`, `[config-key]`)

Guide: [How to use [puppeteer.fill]](/plugins/magic.lambda.puppeteer/#puppeteerfill)

### JSON declaration

This is the complete declaration of `puppeteer.fill`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "puppeteer.fill",
  "description": "Fills an input element with text",
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
      "text": {
        "type": "string",
        "kind": "form-text,text",
        "description": "Text to send",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      },
      "config-key": {
        "type": "string",
        "kind": "config-key",
        "description": "Configuration key resolving the text to send",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      },
      "delay": {
        "type": "int",
        "description": "Delay in milliseconds between key presses",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      }
    },
    "constraints": [
      {
        "description": "Provide either [text] or [config-key]",
        "values": [
          "text",
          "config-key"
        ],
        "kind": "ExactlyOneOf"
      }
    ],
    "scope": {
      "requires": "puppeteer-session"
    }
  }
}
```

</details>

---

[&larr; `puppeteer.evaluate`](/reference/slots/puppeteer/puppeteer.evaluate/) | [all `puppeteer.*` slots](/reference/slots/puppeteer/) | [`puppeteer.goto` &rarr;](/reference/slots/puppeteer/puppeteer.goto/)


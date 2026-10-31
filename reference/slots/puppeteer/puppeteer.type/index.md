---
title: "[puppeteer.type]"
description: "puppeteer.type is a slot in the puppeteer namespace of Magic Cloud. Types text into an element."
generated: true
llms: "guide"
slot_json: "/reference/slots/puppeteer/puppeteer.type/slot.json"
---

`puppeteer.type` is a slot in the `puppeteer` namespace, in Hyperlambda, the language of Magic Cloud. Types text into an element.

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

### Guide

<!-- guide -->
Types text into a selector.

Arguments:

* Slot value - Session identifier.
* `selector` - CSS selector to type into.
* `text` - Text to type.
* `config-key` - Configuration key resolving the text value.
* `delay` - Delay between key presses in milliseconds.

Supply exactly one of `text` or `config-key`.

Examples:

```
puppeteer.type:SESSION_ID
   selector:"#name"
   text:"Thomas Hansen"
```

```
puppeteer.type:SESSION_ID
   selector:"#info"
   text:"Hello from AI agent"
   delay:25
```

```
puppeteer.type:SESSION_ID
   selector:"#password"
   config-key:"magic:secrets:example-password"
```
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.puppeteer](/plugins/magic.lambda.puppeteer/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `puppeteer.type`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "puppeteer.type",
  "description": "Types text into an element",
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

[&larr; `puppeteer.title`](/reference/slots/puppeteer/puppeteer.title/) | [all `puppeteer.*` slots](/reference/slots/puppeteer/) | [`puppeteer.url` &rarr;](/reference/slots/puppeteer/puppeteer.url/)


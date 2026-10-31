---
title: "[puppeteer.wait-for-selector]"
description: "puppeteer.wait-for-selector is a slot in the puppeteer namespace of Magic Cloud. Waits for a selector to appear."
generated: true
llms: "guide"
slot_json: "/reference/slots/puppeteer/puppeteer.wait-for-selector/slot.json"
---

`puppeteer.wait-for-selector` is a slot in the `puppeteer` namespace, in Hyperlambda, the language of Magic Cloud. Waits for a selector to appear.

* **Value** (`puppeteer-session`), required: Puppeteer session ID
* **Scope**: requires `puppeteer-session`

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[selector]` | string | yes | CSS selector. |
| `[timeout]` | int | no | Wait timeout in milliseconds. |
| `[visible]` | bool | no | Wait until selector is visible. |
| `[hidden]` | bool | no | Wait until selector is hidden. |

### Guide

<!-- guide -->
Waits until a selector appears in the DOM.

Arguments:

* Slot value - Session identifier.
* `selector` - CSS selector to wait for.
* `timeout` - Timeout in milliseconds.
* `visible` - Boolean. Require element to be visible.
* `hidden` - Boolean. Require element to be hidden.

Examples:

```
puppeteer.wait-for-selector:SESSION_ID
   selector:"#name"
   visible:true
```
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.puppeteer](/plugins/magic.lambda.puppeteer/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `puppeteer.wait-for-selector`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "puppeteer.wait-for-selector",
  "description": "Waits for a selector to appear",
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
      "timeout": {
        "type": "int",
        "description": "Wait timeout in milliseconds",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      },
      "visible": {
        "type": "bool",
        "description": "Wait until selector is visible",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      },
      "hidden": {
        "type": "bool",
        "description": "Wait until selector is hidden",
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

[&larr; `puppeteer.url`](/reference/slots/puppeteer/puppeteer.url/) | [all `puppeteer.*` slots](/reference/slots/puppeteer/) | [`puppeteer.wait-for-url` &rarr;](/reference/slots/puppeteer/puppeteer.wait-for-url/)


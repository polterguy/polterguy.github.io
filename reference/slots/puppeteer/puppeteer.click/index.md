---
title: "[puppeteer.click]"
description: "puppeteer.click is a slot in the puppeteer namespace of Magic Cloud. Clicks an element on the page."
generated: true
llms: "guide"
slot_json: "/reference/slots/puppeteer/puppeteer.click/slot.json"
---

`puppeteer.click` is a slot in the `puppeteer` namespace, in Hyperlambda, the language of Magic Cloud. Clicks an element on the page.

* **Value** (`puppeteer-session`), required: Puppeteer session ID
* **Scope**: requires `puppeteer-session`

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[selector]` | string | yes | CSS selector. |
| `[button]` | string | no | Mouse button to click. Default: `left`. |
| `[click-count]` | int | no | Number of clicks. |
| `[delay]` | int | no | Delay in milliseconds between mouse down and up. |

### Guide

<!-- guide -->
Clicks a selector.

Arguments:

* Slot value - Session identifier.
* `selector` - CSS selector to click.
* `button` - Mouse button: `left`, `middle`, or `right`.
* `click-count` - Number of clicks.
* `delay` - Delay between down and up in milliseconds.

Examples:

```
puppeteer.click:SESSION_ID
   selector:"#submit_contact_form_button"
```

```
puppeteer.click:SESSION_ID
   selector:"#submit_contact_form_button"
   click-count:2
```
<!-- /guide -->

### JSON declaration

This is the complete declaration of `puppeteer.click`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "puppeteer.click",
  "description": "Clicks an element on the page",
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
      "button": {
        "type": "string",
        "kind": "mouse-button",
        "description": "Mouse button to click",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "left",
        "role": "Option",
        "projection": "Value"
      },
      "click-count": {
        "type": "int",
        "kind": "click-count",
        "description": "Number of clicks",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      },
      "delay": {
        "type": "int",
        "description": "Delay in milliseconds between mouse down and up",
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

[all `puppeteer.*` slots](/reference/slots/puppeteer/) | [`puppeteer.close` &rarr;](/reference/slots/puppeteer/puppeteer.close/)


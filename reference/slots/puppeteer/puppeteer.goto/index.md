---
title: "[puppeteer.goto]"
description: "puppeteer.goto is a slot in the puppeteer namespace of Magic Cloud. Navigates the current page to a URL."
generated: true
llms: "guide"
slot_json: "/reference/slots/puppeteer/puppeteer.goto/slot.json"
---

`puppeteer.goto` is a slot in the `puppeteer` namespace, in Hyperlambda, the language of Magic Cloud. Navigates the current page to a URL.

* **Value** (`puppeteer-session`), required: Puppeteer session ID
* **Returns**: Resolves to the resolved page URL after navigation
* **Scope**: requires `puppeteer-session`

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[url]` | string | yes | URL to navigate to. |
| `[timeout]` | int | no | Navigation timeout in milliseconds. |
| `[wait-until]` | string | no | Navigation completion condition: load, domcontentloaded, networkidle0, or networkidle2. |

### Guide

<!-- guide -->
Navigates to a URL.

Arguments:

* Slot value - Session identifier.
* `url` - URL to navigate to.
* `timeout` - Navigation timeout in milliseconds.
* `wait-until` - One of `load`, `domcontentloaded`, `networkidle0`, `networkidle2`.

Examples:

```
puppeteer.goto:SESSION_ID
   url:"https://ainiro.io"
```

```
puppeteer.goto:SESSION_ID
   url:"https://ainiro.io"
   timeout:30000
   wait-until:networkidle2
```
<!-- /guide -->

### JSON declaration

This is the complete declaration of `puppeteer.goto`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "puppeteer.goto",
  "description": "Navigates the current page to a URL",
  "signature": {
    "input": {
      "kind": "puppeteer-session",
      "description": "Puppeteer session ID",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "url": {
        "type": "string",
        "kind": "url",
        "description": "URL to navigate to",
        "required": true,
        "mode": "ValueOrExpression",
        "cardinality": "ExactlyOne",
        "role": "Option",
        "projection": "Value"
      },
      "timeout": {
        "type": "int",
        "description": "Navigation timeout in milliseconds",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      },
      "wait-until": {
        "type": "string",
        "kind": "puppeteer-wait-until",
        "description": "Navigation completion condition: load, domcontentloaded, networkidle0, or networkidle2",
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
      "kind": "url,puppeteer-page-loaded,text",
      "description": "Resolves to the resolved page URL after navigation"
    }
  }
}
```

</details>

---

[&larr; `puppeteer.fill`](/reference/slots/puppeteer/puppeteer.fill/) | [all `puppeteer.*` slots](/reference/slots/puppeteer/) | [`puppeteer.press` &rarr;](/reference/slots/puppeteer/puppeteer.press/)


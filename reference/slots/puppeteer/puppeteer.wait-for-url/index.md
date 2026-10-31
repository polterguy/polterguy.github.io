---
title: "[puppeteer.wait-for-url]"
description: "puppeteer.wait-for-url is a slot in the puppeteer namespace of Magic Cloud. Waits for the page URL to match a condition."
generated: true
llms: "guide"
slot_json: "/reference/slots/puppeteer/puppeteer.wait-for-url/slot.json"
---

`puppeteer.wait-for-url` is a slot in the `puppeteer` namespace, in Hyperlambda, the language of Magic Cloud. Waits for the page URL to match a condition.

* **Value** (`puppeteer-session`), required: Puppeteer session ID
* **Scope**: requires `puppeteer-session`

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[url]` | string | yes | URL pattern to wait for. |
| `[timeout]` | int | no | Wait timeout in milliseconds. |

### Guide

<!-- guide -->
Waits until the page URL matches.

Arguments:

* Slot value - Session identifier.
* `url` - URL string to wait for.
* `timeout` - Timeout in milliseconds.

Examples:

```
puppeteer.wait-for-url:SESSION_ID
   url:"https://ainiro.io/contact-us"
```
<!-- /guide -->

### JSON declaration

This is the complete declaration of `puppeteer.wait-for-url`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "puppeteer.wait-for-url",
  "description": "Waits for the page URL to match a condition",
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
        "kind": "url-pattern",
        "description": "URL pattern to wait for",
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

[&larr; `puppeteer.wait-for-selector`](/reference/slots/puppeteer/puppeteer.wait-for-selector/) | [all `puppeteer.*` slots](/reference/slots/puppeteer/)


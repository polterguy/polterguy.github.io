---
title: "[puppeteer.content]"
description: "puppeteer.content is a slot in the puppeteer namespace of Magic Cloud. Returns the current page HTML content."
generated: true
llms: false
slot_json: "/reference/slots/puppeteer/puppeteer.content/slot.json"
---

`puppeteer.content` is a slot in the `puppeteer` namespace, in Hyperlambda, the language of Magic Cloud. Returns the current page HTML content.

* **Value** (`puppeteer-session`), required: Puppeteer session ID
* **Returns**: Resolves to the current page HTML content
* **Scope**: requires `puppeteer-session`

### Guide

[How to use `puppeteer.content`](/plugins/magic.lambda.puppeteer/puppeteer.content/)

### JSON declaration

This is the complete declaration of `puppeteer.content`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "puppeteer.content",
  "description": "Returns the current page HTML content",
  "signature": {
    "input": {
      "kind": "puppeteer-session",
      "description": "Puppeteer session ID",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "scope": {
      "requires": "puppeteer-session"
    },
    "output": {
      "mode": "Value",
      "kind": "html,text",
      "description": "Resolves to the current page HTML content"
    }
  }
}
```

</details>

---

[&larr; `puppeteer.connect`](/reference/slots/puppeteer/puppeteer.connect/) | [all `puppeteer.*` slots](/reference/slots/puppeteer/) | [`puppeteer.evaluate` &rarr;](/reference/slots/puppeteer/puppeteer.evaluate/)


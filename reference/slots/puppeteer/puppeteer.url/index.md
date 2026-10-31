---
title: "[puppeteer.url]"
description: "puppeteer.url is a slot in the puppeteer namespace of Magic Cloud. Returns the current page URL."
generated: true
llms: false
slot_json: "/reference/slots/puppeteer/puppeteer.url/slot.json"
---

`puppeteer.url` is a slot in the `puppeteer` namespace, in Hyperlambda, the language of Magic Cloud. Returns the current page URL.

* **Value** (`puppeteer-session`), required: Puppeteer session ID
* **Returns**: Resolves to the current page URL
* **Scope**: requires `puppeteer-session`

### Guide

[How to use `puppeteer.url`](/plugins/magic.lambda.puppeteer/puppeteer.url/)

### JSON declaration

This is the complete declaration of `puppeteer.url`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "puppeteer.url",
  "description": "Returns the current page URL",
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
      "kind": "url,text",
      "description": "Resolves to the current page URL"
    }
  }
}
```

</details>

---

[&larr; `puppeteer.type`](/reference/slots/puppeteer/puppeteer.type/) | [all `puppeteer.*` slots](/reference/slots/puppeteer/) | [`puppeteer.wait-for-selector` &rarr;](/reference/slots/puppeteer/puppeteer.wait-for-selector/)


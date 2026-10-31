---
title: "[puppeteer.close]"
description: "puppeteer.close is a slot in the puppeteer namespace of Magic Cloud. Closes a Puppeteer session."
generated: true
llms: false
slot_json: "/reference/slots/puppeteer/puppeteer.close/slot.json"
---

`puppeteer.close` is a slot in the `puppeteer` namespace, in Hyperlambda, the language of Magic Cloud. Closes a Puppeteer session.

* **Value** (`puppeteer-session`), required: Puppeteer session ID
* **Scope**: requires `puppeteer-session`

### Guide

[How to use `puppeteer.close`](/plugins/magic.lambda.puppeteer/puppeteer.close/)

### JSON declaration

This is the complete declaration of `puppeteer.close`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "puppeteer.close",
  "description": "Closes a Puppeteer session",
  "signature": {
    "input": {
      "kind": "puppeteer-session",
      "description": "Puppeteer session ID",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "scope": {
      "requires": "puppeteer-session"
    }
  }
}
```

</details>

---

[&larr; `puppeteer.click`](/reference/slots/puppeteer/puppeteer.click/) | [all `puppeteer.*` slots](/reference/slots/puppeteer/) | [`puppeteer.connect` &rarr;](/reference/slots/puppeteer/puppeteer.connect/)


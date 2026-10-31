---
title: "[puppeteer.title]"
description: "puppeteer.title is a slot in the puppeteer namespace of Magic Cloud. Returns the current page title."
generated: true
llms: false
slot_json: "/reference/slots/puppeteer/puppeteer.title/slot.json"
---

`puppeteer.title` is a slot in the `puppeteer` namespace, in Hyperlambda, the language of Magic Cloud. Returns the current page title.

* **Value** (`puppeteer-session`), required: Puppeteer session ID
* **Returns**: Resolves to the current page title
* **Scope**: requires `puppeteer-session`

Guide: [How to use [puppeteer.title]](/plugins/magic.lambda.puppeteer/#puppeteertitle)

### JSON declaration

This is the complete declaration of `puppeteer.title`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "puppeteer.title",
  "description": "Returns the current page title",
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
      "kind": "page-title,text",
      "description": "Resolves to the current page title"
    }
  }
}
```

</details>

---

[&larr; `puppeteer.select`](/reference/slots/puppeteer/puppeteer.select/) | [all `puppeteer.*` slots](/reference/slots/puppeteer/) | [`puppeteer.type` &rarr;](/reference/slots/puppeteer/puppeteer.type/)


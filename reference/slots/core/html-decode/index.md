---
title: "[html-decode]"
description: "html-decode is a core slot of Magic Cloud. HTML decodes the specified string."
generated: true
llms: false
slot_json: "/reference/slots/core/html-decode/slot.json"
---

`html-decode` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. HTML decodes the specified string.

* **Value** (`html-encoded`), required: HTML encoded text to decode
* **Returns**: Resolves to the decoded text

Guide: [How to use [html-decode]](/plugins/magic.lambda.html/#how-to-use-html-decode)

### JSON declaration

This is the complete declaration of `html-decode`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "html-decode",
  "description": "HTML decodes the specified string",
  "signature": {
    "input": {
      "kind": "html-encoded",
      "description": "HTML encoded text to decode",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "output": {
      "mode": "Value",
      "kind": "html,text",
      "description": "Resolves to the decoded text"
    }
  }
}
```

</details>

---

[&larr; `get-value`](/reference/slots/core/get-value/) | [all core slots](/reference/slots/core/) | [`html2lambda` &rarr;](/reference/slots/core/html2lambda/)


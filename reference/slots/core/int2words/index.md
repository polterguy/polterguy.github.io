---
title: "[int2words]"
description: "int2words is a core slot of Magic Cloud. Spells an integer out in English words (e.g. 557 becomes 'five hundred and fifty seven'); handy for invoices and cheques."
generated: true
llms: false
slot_json: "/reference/slots/core/int2words/slot.json"
---

`int2words` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Spells an integer out in English words (e.g. 557 becomes 'five hundred and fifty seven'); handy for invoices and cheques.

* **Value** (`integer,number`), required: Integer value to convert to words
* **Returns**: Resolves to the supplied integer written as words

### Guide

[How to use `int2words`](/plugins/magic.lambda/int2words/)

### JSON declaration

This is the complete declaration of `int2words`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "int2words",
  "description": "Spells an integer out in English words (e.g. 557 becomes 'five hundred and fifty seven'); handy for invoices and cheques",
  "signature": {
    "input": {
      "kind": "integer,number",
      "description": "Integer value to convert to words",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "output": {
      "mode": "Value",
      "kind": "text",
      "description": "Resolves to the supplied integer written as words"
    }
  }
}
```

</details>

---

[&larr; `insert-before`](/reference/slots/core/insert-before/) | [all core slots](/reference/slots/core/) | [`invoke` &rarr;](/reference/slots/core/invoke/)


---
title: "[not-null]"
description: "not-null is a core slot of Magic Cloud. Returns true if the specified node or expression is not null."
generated: true
llms: false
slot_json: "/reference/slots/core/not-null/slot.json"
---

`not-null` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Returns true if the specified node or expression is not null.

* **Value** (`node-list,single-object`), required: Expression selecting the value to test for null
* **Returns**: Returns true if the expression resolves to a non-null value

### Guide

[How to use `not-null`](/plugins/magic.lambda/not-null/)

### JSON declaration

This is the complete declaration of `not-null`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "not-null",
  "description": "Returns true if the specified node or expression is not null",
  "signature": {
    "input": {
      "kind": "node-list,single-object",
      "description": "Expression selecting the value to test for null",
      "required": true,
      "mode": "Expression"
    },
    "output": {
      "mode": "Value",
      "kind": "boolean",
      "description": "Returns true if the expression resolves to a non-null value"
    }
  }
}
```

</details>

---

[&larr; `not-exists`](/reference/slots/core/not-exists/) | [all core slots](/reference/slots/core/) | [`null` &rarr;](/reference/slots/core/null/)


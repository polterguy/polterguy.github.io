---
title: "[null]"
description: "null is a core slot of Magic Cloud. Returns true if the specified node or expression is null."
generated: true
llms: false
slot_json: "/reference/slots/core/null/slot.json"
---

`null` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Returns true if the specified node or expression is null.

* **Value** (`node-list,single-object`), required: Expression selecting the value to test for null
* **Returns**: Returns true if the expression resolves to a null value

Guide: [How to use [null]](/plugins/magic.lambda/nodes/#how-to-use-null)

### Guide

[How to use `null`](/plugins/magic.lambda/null/)

### JSON declaration

This is the complete declaration of `null`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "null",
  "description": "Returns true if the specified node or expression is null",
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
      "description": "Returns true if the expression resolves to a null value"
    }
  }
}
```

</details>

---

[&larr; `not-null`](/reference/slots/core/not-null/) | [all core slots](/reference/slots/core/) | [`or` &rarr;](/reference/slots/core/or/)


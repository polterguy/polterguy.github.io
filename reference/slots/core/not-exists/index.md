---
title: "[not-exists]"
description: "not-exists is a core slot of Magic Cloud. Returns true if the specified node or expression does not exist."
generated: true
llms: false
slot_json: "/reference/slots/core/not-exists/slot.json"
---

`not-exists` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Returns true if the specified node or expression does not exist.

* **Value** (`node-list,single-object`), required: Expression selecting the nodes to test for
* **Returns**: Returns true if the expression resolves to no nodes

Guide: [How to use [not-exists]](/plugins/magic.lambda/nodes/#how-to-use-not-exists)

### Guide

[How to use `not-exists`](/plugins/magic.lambda/not-exists/)

### JSON declaration

This is the complete declaration of `not-exists`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "not-exists",
  "description": "Returns true if the specified node or expression does not exist",
  "signature": {
    "input": {
      "kind": "node-list,single-object",
      "description": "Expression selecting the nodes to test for",
      "required": true,
      "mode": "Expression"
    },
    "output": {
      "mode": "Value",
      "kind": "boolean",
      "description": "Returns true if the expression resolves to no nodes"
    }
  }
}
```

</details>

---

[&larr; `not`](/reference/slots/core/not/) | [all core slots](/reference/slots/core/) | [`not-null` &rarr;](/reference/slots/core/not-null/)


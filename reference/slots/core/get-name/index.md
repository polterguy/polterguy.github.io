---
title: "[get-name]"
description: "get-name is a core slot of Magic Cloud. Returns the name of the first matching node."
generated: true
llms: false
slot_json: "/reference/slots/core/get-name/slot.json"
---

`get-name` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Returns the name of the first matching node.

* **Value** (`single-object`), required: Expression selecting the node whose name should be retrieved
* **Returns**: Resolves to the name of the first matching node

### Guide

[How to use `get-name`](/plugins/magic.lambda/get-name/)

### JSON declaration

This is the complete declaration of `get-name`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "get-name",
  "description": "Returns the name of the first matching node",
  "signature": {
    "input": {
      "kind": "single-object",
      "description": "Expression selecting the node whose name should be retrieved",
      "required": true,
      "mode": "Expression"
    },
    "output": {
      "mode": "Value",
      "kind": "node-name,text",
      "description": "Resolves to the name of the first matching node"
    }
  }
}
```

</details>

---

[&larr; `get-first-value`](/reference/slots/core/get-first-value/) | [all core slots](/reference/slots/core/) | [`get-nodes` &rarr;](/reference/slots/core/get-nodes/)


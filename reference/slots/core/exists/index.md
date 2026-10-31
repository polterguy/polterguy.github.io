---
title: "[exists]"
description: "exists is a core slot of Magic Cloud. Returns true if the specified node or expression exists."
generated: true
llms: false
slot_json: "/reference/slots/core/exists/slot.json"
---

`exists` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Returns true if the specified node or expression exists.

* **Value** (`node-list,single-object`), required: Expression selecting the nodes to test for
* **Returns**: Returns true if the expression resolves to one or more nodes

Guide: [How to use [exists]](/plugins/magic.lambda/nodes/#how-to-use-exists)

### Guide

[How to use `exists`](/plugins/magic.lambda/exists/)

### JSON declaration

This is the complete declaration of `exists`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "exists",
  "description": "Returns true if the specified node or expression exists",
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
      "description": "Returns true if the expression resolves to one or more nodes"
    }
  }
}
```

</details>

---

[&larr; `execute-file`](/reference/slots/core/execute-file/) | [all core slots](/reference/slots/core/) | [`filter` &rarr;](/reference/slots/core/filter/)


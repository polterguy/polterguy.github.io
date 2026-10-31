---
title: "[remove-nodes]"
description: "remove-nodes is a core slot of Magic Cloud. Removes nodes from the lambda graph."
generated: true
llms: false
slot_json: "/reference/slots/core/remove-nodes/slot.json"
---

`remove-nodes` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Removes nodes from the lambda graph.

* **Value** (`node-list,single-object`), required: Expression selecting the node or nodes to remove

Guide: [How to use [remove-nodes]](/plugins/magic.lambda/nodes/#how-to-use-remove-nodes)

### JSON declaration

This is the complete declaration of `remove-nodes`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "remove-nodes",
  "description": "Removes nodes from the lambda graph",
  "signature": {
    "input": {
      "kind": "node-list,single-object",
      "description": "Expression selecting the node or nodes to remove",
      "required": true,
      "mode": "Expression"
    }
  }
}
```

</details>

---

[&larr; `reference`](/reference/slots/core/reference/) | [all core slots](/reference/slots/core/) | [`return` &rarr;](/reference/slots/core/return/)


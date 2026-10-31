---
title: "[add]"
description: "add is a core slot of Magic Cloud. Appends source nodes to selected destination containers."
generated: true
llms: false
slot_json: "/reference/slots/core/add/slot.json"
---

`add` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Appends source nodes to selected destination containers.

* **Value** (`node-list,single-object`), required: Expression selecting destination container node or nodes whose children should receive the source nodes

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | yes | Source container or node-producing slot evaluated before its child nodes are applied to the selected target location. Can be repeated. |

Guide: [How to use [add]](/plugins/magic.lambda/nodes/#how-to-use-add)

### Guide

[How to use `add`](/plugins/magic.lambda/add/)

### JSON declaration

This is the complete declaration of `add`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "add",
  "description": "Appends source nodes to selected destination containers",
  "signature": {
    "input": {
      "kind": "node-list,single-object",
      "description": "Expression selecting destination container node or nodes whose children should receive the source nodes",
      "required": true,
      "mode": "Expression"
    },
    "children": {
      "*": {
        "type": "lambda",
        "kind": "node-list",
        "description": "Source container or node-producing slot evaluated before its child nodes are applied to the selected target location",
        "required": true,
        "mode": "ExecutableLambda",
        "cardinality": "OneOrMore",
        "role": "SourceContainer",
        "evaluation": "EvalSelf",
        "projection": "ChildrenOfChildren"
      }
    }
  }
}
```

</details>

---

[all core slots](/reference/slots/core/) | [`and` &rarr;](/reference/slots/core/and/)


---
title: "[return-nodes]"
description: "return-nodes is a core slot of Magic Cloud. Returns child nodes or evaluated nodes to the nearest caller."
generated: true
llms: false
slot_json: "/reference/slots/core/return-nodes/slot.json"
---

`return-nodes` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Returns child nodes or evaluated nodes to the nearest caller.

* **Value** (`node-list`), optional: Expression evaluating to the nodes to return; omit to return the literal child nodes instead
* **Returns**: Returns child nodes to the nearest caller

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | no | Returned child node. Can be repeated. |

### Guide

[How to use `return-nodes`](/plugins/magic.lambda.slots/return-nodes/)

### JSON declaration

This is the complete declaration of `return-nodes`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "return-nodes",
  "description": "Returns child nodes or evaluated nodes to the nearest caller",
  "signature": {
    "input": {
      "kind": "node-list",
      "description": "Expression evaluating to the nodes to return; omit to return the literal child nodes instead",
      "required": false,
      "mode": "Expression"
    },
    "children": {
      "*": {
        "type": "lambda",
        "description": "Returned child node",
        "required": false,
        "mode": "SourceLambda",
        "cardinality": "ZeroOrMore",
        "role": "Payload",
        "projection": "Self"
      }
    },
    "output": {
      "mode": "Lambda",
      "kind": "node-list",
      "description": "Returns child nodes to the nearest caller"
    }
  }
}
```

</details>

---

[&larr; `return`](/reference/slots/core/return/) | [all core slots](/reference/slots/core/) | [`return-value` &rarr;](/reference/slots/core/return-value/)


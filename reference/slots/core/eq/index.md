---
title: "[eq]"
description: "eq is a core slot of Magic Cloud. Returns true if two operands are equal."
generated: true
llms: false
slot_json: "/reference/slots/core/eq/slot.json"
---

`eq` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Returns true if two operands are equal.

* **Returns**: Resolves to true if the operands are equal

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | object | yes | Operand evaluated before comparison. |

Guide: [How to use [eq]](/plugins/magic.lambda/conditions/#how-to-use-eq)

### JSON declaration

This is the complete declaration of `eq`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "eq",
  "description": "Returns true if two operands are equal",
  "signature": {
    "children": {
      "*": {
        "type": "object",
        "description": "Operand evaluated before comparison",
        "required": true,
        "mode": "ExecutableLambda",
        "cardinality": "ExactlyTwo",
        "role": "OperandPaired",
        "evaluation": "EvalSelf",
        "projection": "Value"
      }
    },
    "output": {
      "mode": "Value",
      "kind": "boolean",
      "description": "Resolves to true if the operands are equal"
    }
  }
}
```

</details>

---

[&larr; `else-if`](/reference/slots/core/else-if/) | [all core slots](/reference/slots/core/) | [`eval` &rarr;](/reference/slots/core/eval/)


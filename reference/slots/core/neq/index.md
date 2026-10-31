---
title: "[neq]"
description: "neq is a core slot of Magic Cloud. Returns true if two operands are not equal."
generated: true
llms: false
slot_json: "/reference/slots/core/neq/slot.json"
---

`neq` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Returns true if two operands are not equal.

* **Returns**: Resolves to true if the operands are not equal

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | object | yes | Operand evaluated before comparison. |

### Guide

[How to use `neq`](/plugins/magic.lambda/neq/)

### JSON declaration

This is the complete declaration of `neq`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "neq",
  "description": "Returns true if two operands are not equal",
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
      "description": "Resolves to true if the operands are not equal"
    }
  }
}
```

</details>

---

[&larr; `mte`](/reference/slots/core/mte/) | [all core slots](/reference/slots/core/) | [`not` &rarr;](/reference/slots/core/not/)


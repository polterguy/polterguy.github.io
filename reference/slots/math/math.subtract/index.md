---
title: "[math.subtract]"
description: "math.subtract is a slot in the math namespace of Magic Cloud. Subtracts numeric values."
generated: true
llms: false
slot_json: "/reference/slots/math/math.subtract/slot.json"
---

`math.subtract` is a slot in the `math` namespace, in Hyperlambda, the language of Magic Cloud. Subtracts numeric values.

* **Returns**: Resolves to the difference of the supplied operands

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | number | yes | Numeric operand evaluated before calculating the result. |

### Guide

[How to use `math.subtract`](/plugins/magic.lambda.math/math.subtract/)

### JSON declaration

This is the complete declaration of `math.subtract`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "math.subtract",
  "description": "Subtracts numeric values",
  "signature": {
    "children": {
      "*": {
        "type": "number",
        "kind": "number",
        "description": "Numeric operand evaluated before calculating the result",
        "required": true,
        "mode": "ExecutableLambda",
        "cardinality": "TwoOrMore",
        "role": "OperandPaired",
        "evaluation": "EvalSelf",
        "projection": "Value"
      }
    },
    "output": {
      "mode": "Value",
      "kind": "number",
      "description": "Resolves to the difference of the supplied operands"
    }
  }
}
```

</details>

---

[&larr; `math.sqrt`](/reference/slots/math/math.sqrt/) | [all `math.*` slots](/reference/slots/math/)


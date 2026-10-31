---
title: "[math.add]"
description: "math.add is a slot in the math namespace of Magic Cloud. Adds numeric values."
generated: true
llms: false
slot_json: "/reference/slots/math/math.add/slot.json"
---

`math.add` is a slot in the `math` namespace, in Hyperlambda, the language of Magic Cloud. Adds numeric values.

* **Returns**: Resolves to the sum of the supplied operands

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | number | yes | Numeric operand evaluated before calculating the result. |

### Guide

[How to use `math.add`](/plugins/magic.lambda.math/math.add/)

### JSON declaration

This is the complete declaration of `math.add`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "math.add",
  "description": "Adds numeric values",
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
      "description": "Resolves to the sum of the supplied operands"
    }
  }
}
```

</details>

---

[&larr; `math.abs`](/reference/slots/math/math.abs/) | [all `math.*` slots](/reference/slots/math/) | [`math.ceil` &rarr;](/reference/slots/math/math.ceil/)


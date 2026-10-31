---
title: "[math.divide]"
description: "math.divide is a slot in the math namespace of Magic Cloud. Divides numeric values."
generated: true
llms: false
slot_json: "/reference/slots/math/math.divide/slot.json"
---

`math.divide` is a slot in the `math` namespace, in Hyperlambda, the language of Magic Cloud. Divides numeric values.

* **Returns**: Resolves to the quotient of the supplied operands

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | number | yes | Numeric operand evaluated before calculating the result. |

Guide: [How to use [math.divide]](/plugins/magic.lambda.math/#how-to-use-mathdivide)

### JSON declaration

This is the complete declaration of `math.divide`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "math.divide",
  "description": "Divides numeric values",
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
      "description": "Resolves to the quotient of the supplied operands"
    }
  }
}
```

</details>

---

[&larr; `math.decrement`](/reference/slots/math/math.decrement/) | [all `math.*` slots](/reference/slots/math/) | [`math.dot` &rarr;](/reference/slots/math/math.dot/)


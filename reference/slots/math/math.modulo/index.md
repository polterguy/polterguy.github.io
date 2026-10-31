---
title: "[math.modulo]"
description: "math.modulo is a slot in the math namespace of Magic Cloud. Calculates the remainder of a division."
generated: true
llms: false
slot_json: "/reference/slots/math/math.modulo/slot.json"
---

`math.modulo` is a slot in the `math` namespace, in Hyperlambda, the language of Magic Cloud. Calculates the remainder of a division.

* **Returns**: Resolves to the remainder of the modulo operation

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | number | yes | Numeric operand evaluated before calculating the result. |

Guide: [How to use [math.modulo]](/plugins/magic.lambda.math/#how-to-use-mathmodulo)

### JSON declaration

This is the complete declaration of `math.modulo`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "math.modulo",
  "description": "Calculates the remainder of a division",
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
      "description": "Resolves to the remainder of the modulo operation"
    }
  }
}
```

</details>

---

[&larr; `math.min`](/reference/slots/math/math.min/) | [all `math.*` slots](/reference/slots/math/) | [`math.multiply` &rarr;](/reference/slots/math/math.multiply/)


---
title: "[math.max]"
description: "math.max is a slot in the math namespace of Magic Cloud. Returns the largest value from the supplied inputs."
generated: true
llms: false
slot_json: "/reference/slots/math/math.max/slot.json"
---

`math.max` is a slot in the `math` namespace, in Hyperlambda, the language of Magic Cloud. Returns the largest value from the supplied inputs.

* **Returns**: Resolves to the largest supplied value

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | number | yes | Numeric operand evaluated before calculating the result. |

### Guide

[How to use `math.max`](/plugins/magic.lambda.math/math.max/)

### JSON declaration

This is the complete declaration of `math.max`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "math.max",
  "description": "Returns the largest value from the supplied inputs",
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
      "description": "Resolves to the largest supplied value"
    }
  }
}
```

</details>

---

[&larr; `math.increment`](/reference/slots/math/math.increment/) | [all `math.*` slots](/reference/slots/math/) | [`math.min` &rarr;](/reference/slots/math/math.min/)


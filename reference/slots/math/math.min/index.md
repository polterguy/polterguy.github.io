---
title: "[math.min]"
description: "math.min is a slot in the math namespace of Magic Cloud. Returns the smallest value from the supplied inputs."
generated: true
llms: false
slot_json: "/reference/slots/math/math.min/slot.json"
---

`math.min` is a slot in the `math` namespace, in Hyperlambda, the language of Magic Cloud. Returns the smallest value from the supplied inputs.

* **Returns**: Resolves to the smallest supplied value

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | number | yes | Numeric operand evaluated before calculating the result. |

Guide: [How to use [math.min]](/plugins/magic.lambda.math/#how-to-use-mathmin)

### JSON declaration

This is the complete declaration of `math.min`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "math.min",
  "description": "Returns the smallest value from the supplied inputs",
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
      "description": "Resolves to the smallest supplied value"
    }
  }
}
```

</details>

---

[&larr; `math.max`](/reference/slots/math/math.max/) | [all `math.*` slots](/reference/slots/math/) | [`math.modulo` &rarr;](/reference/slots/math/math.modulo/)


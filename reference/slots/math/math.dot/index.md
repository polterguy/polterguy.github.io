---
title: "[math.dot]"
description: "math.dot is a slot in the math namespace of Magic Cloud. Calculates the dot product of two vectors from child nodes."
generated: true
llms: false
slot_json: "/reference/slots/math/math.dot/slot.json"
---

`math.dot` is a slot in the `math` namespace, in Hyperlambda, the language of Magic Cloud. Calculates the dot product of two vectors from child nodes.

* **Returns**: Resolves to the dot product of the two supplied vectors

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | yes | Vector operand evaluated before calculating the dot product. |

Guide: [How to use [math.dot]](/plugins/magic.lambda.math/#how-to-use-mathdot)

### JSON declaration

This is the complete declaration of `math.dot`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "math.dot",
  "description": "Calculates the dot product of two vectors from child nodes",
  "signature": {
    "children": {
      "*": {
        "type": "lambda",
        "description": "Vector operand evaluated before calculating the dot product",
        "required": true,
        "mode": "ExecutableLambda",
        "cardinality": "ExactlyTwo",
        "role": "OperandPaired",
        "evaluation": "EvalSelf",
        "projection": "Children"
      }
    },
    "output": {
      "mode": "Value",
      "kind": "number",
      "description": "Resolves to the dot product of the two supplied vectors"
    }
  }
}
```

</details>

---

[&larr; `math.divide`](/reference/slots/math/math.divide/) | [all `math.*` slots](/reference/slots/math/) | [`math.floor` &rarr;](/reference/slots/math/math.floor/)


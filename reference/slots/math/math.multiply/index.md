---
title: "[math.multiply]"
description: "math.multiply is a slot in the math namespace of Magic Cloud. Multiplies numeric values."
generated: true
llms: "guide"
slot_json: "/reference/slots/math/math.multiply/slot.json"
---

`math.multiply` is a slot in the `math` namespace, in Hyperlambda, the language of Magic Cloud. Multiplies numeric values.

* **Returns**: Resolves to the product of the supplied operands

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | number | yes | Numeric operand evaluated before calculating the result. |

### Guide

<!-- guide -->
This slot multiplies two or more values with each other, and can be given as many arguments as you wish,
such as the following illustrates.

```
.arg:int:5
math.multiply
   get-value:x:@.arg
   .:int:3
```

It accepts both slot invocations, retrieving some value by invoking a slot, in addition to static values such as
illustrated above where we provide the number 3 as one of its values.
<!-- /guide -->

### JSON declaration

This is the complete declaration of `math.multiply`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "math.multiply",
  "description": "Multiplies numeric values",
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
      "description": "Resolves to the product of the supplied operands"
    }
  }
}
```

</details>

---

[&larr; `math.modulo`](/reference/slots/math/math.modulo/) | [all `math.*` slots](/reference/slots/math/) | [`math.random` &rarr;](/reference/slots/math/math.random/)


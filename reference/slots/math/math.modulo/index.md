---
title: "[math.modulo]"
description: "math.modulo is a slot in the math namespace of Magic Cloud. Calculates the remainder of a division."
generated: true
llms: "guide"
slot_json: "/reference/slots/math/math.modulo/slot.json"
---

`math.modulo` is a slot in the `math` namespace, in Hyperlambda, the language of Magic Cloud. Calculates the remainder of a division.

* **Returns**: Resolves to the remainder of the modulo operation

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | number | yes | Numeric operand evaluated before calculating the result. |

### Guide

<!-- guide -->
This slot calculates the modulo of two or more values with each other, and can be given as many arguments as you wish,
such as the following illustrates.

```
.arg:int:5
math.modulo
   get-value:x:@.arg
   .:int:2
```

It accepts both slot invocations, retrieving some value by invoking a slot, in addition to static values such as
illustrated above where we provide the number 2 as one of its values.
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.math](/plugins/magic.lambda.math/) plugin, which documents every slot it contains.

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


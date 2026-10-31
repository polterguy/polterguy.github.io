---
title: "[math.round]"
description: "math.round is a slot in the math namespace of Magic Cloud. Rounds a number."
generated: true
llms: "guide"
slot_json: "/reference/slots/math/math.round/slot.json"
---

`math.round` is a slot in the `math` namespace, in Hyperlambda, the language of Magic Cloud. Rounds a number.

* **Value** (`number`), required: Numeric value to round
* **Returns**: Resolves to the rounded value

### Guide

<!-- guide -->
This slot rounds its input to the nearest whole number, using .NET's `Math.Round`, which rounds halfway values to the nearest even number. The slot takes a numeric value, which can be a
constant or an expression, and replaces its value with the rounded result.
<!-- /guide -->

### JSON declaration

This is the complete declaration of `math.round`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "math.round",
  "description": "Rounds a number",
  "signature": {
    "input": {
      "kind": "number",
      "description": "Numeric value to round",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "output": {
      "mode": "Value",
      "kind": "number",
      "description": "Resolves to the rounded value"
    }
  }
}
```

</details>

---

[&larr; `math.random`](/reference/slots/math/math.random/) | [all `math.*` slots](/reference/slots/math/) | [`math.sin` &rarr;](/reference/slots/math/math.sin/)


---
title: "[math.floor]"
description: "math.floor is a slot in the math namespace of Magic Cloud. Rounds a number down."
generated: true
llms: "guide"
slot_json: "/reference/slots/math/math.floor/slot.json"
---

`math.floor` is a slot in the `math` namespace, in Hyperlambda, the language of Magic Cloud. Rounds a number down.

* **Value** (`number`), required: Numeric value to round
* **Returns**: Resolves to the rounded-down value

### Guide

<!-- guide -->
This slot rounds its input down to the nearest whole number. The slot takes a numeric value, which can be a
constant or an expression, and replaces its value with the rounded result.
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.math](/plugins/magic.lambda.math/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `math.floor`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "math.floor",
  "description": "Rounds a number down",
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
      "description": "Resolves to the rounded-down value"
    }
  }
}
```

</details>

---

[&larr; `math.dot`](/reference/slots/math/math.dot/) | [all `math.*` slots](/reference/slots/math/) | [`math.increment` &rarr;](/reference/slots/math/math.increment/)


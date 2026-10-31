---
title: "[math.cos]"
description: "math.cos is a slot in the math namespace of Magic Cloud. Calculates the cosine of the specified value."
generated: true
llms: false
slot_json: "/reference/slots/math/math.cos/slot.json"
---

`math.cos` is a slot in the `math` namespace, in Hyperlambda, the language of Magic Cloud. Calculates the cosine of the specified value.

* **Value** (`number`), required: Numeric value to transform
* **Returns**: Resolves to the cosine of the supplied angle

### Guide

[How to use `math.cos`](/plugins/magic.lambda.math/math.cos/)

### JSON declaration

This is the complete declaration of `math.cos`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "math.cos",
  "description": "Calculates the cosine of the specified value",
  "signature": {
    "input": {
      "kind": "number",
      "description": "Numeric value to transform",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "output": {
      "mode": "Value",
      "kind": "number",
      "description": "Resolves to the cosine of the supplied angle"
    }
  }
}
```

</details>

---

[&larr; `math.ceil`](/reference/slots/math/math.ceil/) | [all `math.*` slots](/reference/slots/math/) | [`math.decrement` &rarr;](/reference/slots/math/math.decrement/)


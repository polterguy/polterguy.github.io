---
title: "[math.abs]"
description: "math.abs is a slot in the math namespace of Magic Cloud. Returns the absolute value."
generated: true
llms: false
slot_json: "/reference/slots/math/math.abs/slot.json"
---

`math.abs` is a slot in the `math` namespace, in Hyperlambda, the language of Magic Cloud. Returns the absolute value.

* **Value** (`number`), required: Numeric value to transform
* **Returns**: Resolves to the absolute value

### Guide

[How to use `math.abs`](/plugins/magic.lambda.math/math.abs/)

### JSON declaration

This is the complete declaration of `math.abs`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "math.abs",
  "description": "Returns the absolute value",
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
      "description": "Resolves to the absolute value"
    }
  }
}
```

</details>

---

[all `math.*` slots](/reference/slots/math/) | [`math.add` &rarr;](/reference/slots/math/math.add/)


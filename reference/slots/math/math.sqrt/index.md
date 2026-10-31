---
title: "[math.sqrt]"
description: "math.sqrt is a slot in the math namespace of Magic Cloud. Calculates the square root of the specified value."
generated: true
llms: false
slot_json: "/reference/slots/math/math.sqrt/slot.json"
---

`math.sqrt` is a slot in the `math` namespace, in Hyperlambda, the language of Magic Cloud. Calculates the square root of the specified value.

* **Value** (`number`), required: Numeric value to transform
* **Returns**: Resolves to the square root of the supplied value

Guide: [How to use [math.sqrt]](/plugins/magic.lambda.math/#how-to-use-mathsqrt)

### JSON declaration

This is the complete declaration of `math.sqrt`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "math.sqrt",
  "description": "Calculates the square root of the specified value",
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
      "description": "Resolves to the square root of the supplied value"
    }
  }
}
```

</details>

---

[&larr; `math.sin`](/reference/slots/math/math.sin/) | [all `math.*` slots](/reference/slots/math/) | [`math.subtract` &rarr;](/reference/slots/math/math.subtract/)


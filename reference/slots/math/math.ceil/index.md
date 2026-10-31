---
title: "[math.ceil]"
description: "math.ceil is a slot in the math namespace of Magic Cloud. Rounds a number up."
generated: true
llms: false
slot_json: "/reference/slots/math/math.ceil/slot.json"
---

`math.ceil` is a slot in the `math` namespace, in Hyperlambda, the language of Magic Cloud. Rounds a number up.

* **Value** (`number`), required: Numeric value to round
* **Returns**: Resolves to the rounded-up value

Guide: [How to use [math.ceil]](/plugins/magic.lambda.math/#how-to-use-mathceil)

### JSON declaration

This is the complete declaration of `math.ceil`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "math.ceil",
  "description": "Rounds a number up",
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
      "description": "Resolves to the rounded-up value"
    }
  }
}
```

</details>

---

[&larr; `math.add`](/reference/slots/math/math.add/) | [all `math.*` slots](/reference/slots/math/) | [`math.cos` &rarr;](/reference/slots/math/math.cos/)


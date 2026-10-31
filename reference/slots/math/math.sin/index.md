---
title: "[math.sin]"
description: "math.sin is a slot in the math namespace of Magic Cloud. Calculates the sine of the specified value."
generated: true
llms: "guide"
slot_json: "/reference/slots/math/math.sin/slot.json"
---

`math.sin` is a slot in the `math` namespace, in Hyperlambda, the language of Magic Cloud. Calculates the sine of the specified value.

* **Value** (`number`), required: Numeric value to transform
* **Returns**: Resolves to the sine of the supplied angle

### Guide

<!-- guide -->
This slot returns the sin value of its input.

```
math.sin:x:@.arguments/*/number
```
<!-- /guide -->

### JSON declaration

This is the complete declaration of `math.sin`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "math.sin",
  "description": "Calculates the sine of the specified value",
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
      "description": "Resolves to the sine of the supplied angle"
    }
  }
}
```

</details>

---

[&larr; `math.round`](/reference/slots/math/math.round/) | [all `math.*` slots](/reference/slots/math/) | [`math.sqrt` &rarr;](/reference/slots/math/math.sqrt/)


---
title: "[math.random]"
description: "math.random is a slot in the math namespace of Magic Cloud. Returns a random number from optional child-node bounds."
generated: true
llms: false
slot_json: "/reference/slots/math/math.random/slot.json"
---

`math.random` is a slot in the `math` namespace, in Hyperlambda, the language of Magic Cloud. Returns a random number from optional child-node bounds.

* **Returns**: Resolves to a random double, or a random integer when bounds are supplied

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| `[max]` | int | no | Exclusive upper bound; when supplied without [min], the lower bound is 0. |
| `[min]` | int | no | Inclusive lower bound; requires [max] and must appear before it. |

### Constraints

* **Requires**: [min] requires [max] (`[max]`)

Guide: [How to use [math.random]](/plugins/magic.lambda.math/#how-to-use-mathrandom)

### JSON declaration

This is the complete declaration of `math.random`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "math.random",
  "description": "Returns a random number from optional child-node bounds",
  "signature": {
    "children": {
      "min": {
        "type": "int",
        "kind": "validator-min-integer",
        "description": "Inclusive lower bound; requires [max] and must appear before it",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      },
      "max": {
        "type": "int",
        "kind": "validator-max-integer",
        "description": "Exclusive upper bound; when supplied without [min], the lower bound is 0",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      }
    },
    "constraints": [
      {
        "target": "min",
        "description": "[min] requires [max]",
        "values": [
          "max"
        ],
        "kind": "Requires"
      }
    ],
    "output": {
      "mode": "Value",
      "kind": "number",
      "description": "Resolves to a random double, or a random integer when bounds are supplied"
    }
  }
}
```

</details>

---

[&larr; `math.multiply`](/reference/slots/math/math.multiply/) | [all `math.*` slots](/reference/slots/math/) | [`math.round` &rarr;](/reference/slots/math/math.round/)


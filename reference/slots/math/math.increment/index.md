---
title: "[math.increment]"
description: "math.increment is a slot in the math namespace of Magic Cloud. Increments the numeric nodes selected by the input expression."
generated: true
llms: false
slot_json: "/reference/slots/math/math.increment/slot.json"
---

`math.increment` is a slot in the `math` namespace, in Hyperlambda, the language of Magic Cloud. Increments the numeric nodes selected by the input expression.

* **Value** (`numeric-node`), required: Expression selecting the numeric node or nodes to increment

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[step]` | number | no | Amount to add to or subtract from each selected node. Default: `1`. |

### Guide

[How to use `math.increment`](/plugins/magic.lambda.math/math.increment/)

### JSON declaration

This is the complete declaration of `math.increment`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "math.increment",
  "description": "Increments the numeric nodes selected by the input expression",
  "signature": {
    "input": {
      "kind": "numeric-node",
      "description": "Expression selecting the numeric node or nodes to increment",
      "required": true,
      "mode": "Expression"
    },
    "children": {
      "step": {
        "type": "number",
        "description": "Amount to add to or subtract from each selected node",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "1",
        "role": "Option",
        "projection": "Value"
      }
    }
  }
}
```

</details>

---

[&larr; `math.floor`](/reference/slots/math/math.floor/) | [all `math.*` slots](/reference/slots/math/) | [`math.max` &rarr;](/reference/slots/math/math.max/)


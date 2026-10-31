---
title: "[math.decrement]"
description: "math.decrement is a slot in the math namespace of Magic Cloud. Decrements the numeric nodes selected by the input expression."
generated: true
llms: false
slot_json: "/reference/slots/math/math.decrement/slot.json"
---

`math.decrement` is a slot in the `math` namespace, in Hyperlambda, the language of Magic Cloud. Decrements the numeric nodes selected by the input expression.

* **Value** (`numeric-node`), required: Expression selecting the numeric node or nodes to decrement

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[step]` | number | no | Amount to add to or subtract from each selected node. Default: `1`. |

Guide: [How to use [math.decrement]](/plugins/magic.lambda.math/#how-to-use-mathdecrement)

### JSON declaration

This is the complete declaration of `math.decrement`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "math.decrement",
  "description": "Decrements the numeric nodes selected by the input expression",
  "signature": {
    "input": {
      "kind": "numeric-node",
      "description": "Expression selecting the numeric node or nodes to decrement",
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

[&larr; `math.cos`](/reference/slots/math/math.cos/) | [all `math.*` slots](/reference/slots/math/) | [`math.divide` &rarr;](/reference/slots/math/math.divide/)


---
title: "[validators.default]"
description: "validators.default is a slot in the validators namespace of Magic Cloud. Adds default child nodes to the nodes selected by the input expression."
generated: true
llms: false
slot_json: "/reference/slots/validators/validators.default/slot.json"
---

`validators.default` is a slot in the `validators` namespace, in Hyperlambda, the language of Magic Cloud. Adds default child nodes to the nodes selected by the input expression.

* **Value** (`lambda-object`), required: Expression selecting the node or nodes to apply defaults to

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | object | yes | Default child node cloned into each selected node when missing. Can be repeated. |

### Guide

[How to use `validators.default`](/plugins/magic.lambda.validators/validators.default/)

### JSON declaration

This is the complete declaration of `validators.default`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "validators.default",
  "description": "Adds default child nodes to the nodes selected by the input expression",
  "signature": {
    "input": {
      "kind": "lambda-object",
      "description": "Expression selecting the node or nodes to apply defaults to",
      "required": true,
      "mode": "Expression"
    },
    "children": {
      "*": {
        "type": "object",
        "description": "Default child node cloned into each selected node when missing",
        "required": true,
        "mode": "ValueOrExpression",
        "cardinality": "OneOrMore",
        "role": "DynamicMap",
        "projection": "StructuredTree"
      }
    }
  }
}
```

</details>

---

[&larr; `validators.date`](/reference/slots/validators/validators.date/) | [all `validators.*` slots](/reference/slots/validators/) | [`validators.email` &rarr;](/reference/slots/validators/validators.email/)


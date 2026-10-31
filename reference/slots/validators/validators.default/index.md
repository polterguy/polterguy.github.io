---
title: "[validators.default]"
description: "validators.default is a slot in the validators namespace of Magic Cloud. Adds default child nodes to the nodes selected by the input expression."
generated: true
llms: "guide"
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

<!-- guide -->
This validator takes one or more arguments with any name and any value, and if this node does not exist as
a child of the node collection specified as its expression value, it appends the node to it.
If the node exists but has a null value, it sets its value to the value of the argument.


```
.arguments
validators.default:x:@.arguments
   foo1:bar1
```
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.validators](/plugins/magic.lambda.validators/) plugin, which documents every slot it contains.

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


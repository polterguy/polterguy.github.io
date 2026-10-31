---
title: "[return-nodes]"
description: "return-nodes is a core slot of Magic Cloud. Returns child nodes or evaluated nodes to the nearest caller."
generated: true
llms: "guide"
slot_json: "/reference/slots/core/return-nodes/slot.json"
---

`return-nodes` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Returns child nodes or evaluated nodes to the nearest caller.

* **Value** (`node-list`), optional: Expression evaluating to the nodes to return; omit to return the literal child nodes instead
* **Returns**: Returns child nodes to the nearest caller

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | no | Returned child node. Can be repeated. |

### Guide

<!-- guide -->
Returns a bunch of nodes (lambda) from your slot. Can only be invoked from the inside of
a dynamically created slot, and other slots explicitly creating a return context. An example can be
found below.

```
slots.create:foo
   return-nodes
      integer-value:int:57
      string-value:Foo bar

signal:foo
```
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.slots](/plugins/magic.lambda.slots/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `return-nodes`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "return-nodes",
  "description": "Returns child nodes or evaluated nodes to the nearest caller",
  "signature": {
    "input": {
      "kind": "node-list",
      "description": "Expression evaluating to the nodes to return; omit to return the literal child nodes instead",
      "required": false,
      "mode": "Expression"
    },
    "children": {
      "*": {
        "type": "lambda",
        "description": "Returned child node",
        "required": false,
        "mode": "SourceLambda",
        "cardinality": "ZeroOrMore",
        "role": "Payload",
        "projection": "Self"
      }
    },
    "output": {
      "mode": "Lambda",
      "kind": "node-list",
      "description": "Returns child nodes to the nearest caller"
    }
  }
}
```

</details>

---

[&larr; `return`](/reference/slots/core/return/) | [all core slots](/reference/slots/core/) | [`return-value` &rarr;](/reference/slots/core/return-value/)


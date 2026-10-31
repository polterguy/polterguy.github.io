---
title: "[map]"
description: "map is a core slot of Magic Cloud. Maps selected nodes into a new result set using the child lambda."
generated: true
llms: false
slot_json: "/reference/slots/core/map/slot.json"
---

`map` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Maps selected nodes into a new result set using the child lambda.

* **Value** (`node-list`), required: Expression selecting the nodes to map
* **Returns**: Resolves to one mapped output item per selected node, using the value or nodes returned by the child lambda

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | yes | Mapper body evaluated once per selected node; each returned value becomes a [.] node and returned child nodes are added to the mapped result. Can be repeated. |

### Guide

[How to use `map`](/plugins/magic.lambda/map/)

### JSON declaration

This is the complete declaration of `map`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "map",
  "description": "Maps selected nodes into a new result set using the child lambda",
  "signature": {
    "input": {
      "kind": "node-list",
      "description": "Expression selecting the nodes to map",
      "required": true,
      "mode": "Expression"
    },
    "children": {
      "*": {
        "type": "lambda",
        "description": "Mapper body evaluated once per selected node; each returned value becomes a [.] node and returned child nodes are added to the mapped result",
        "required": true,
        "mode": "ExecutableLambda",
        "cardinality": "OneOrMore",
        "role": "ExecutableBody",
        "evaluation": "EvalSelf",
        "projection": "ReturnedResult"
      }
    },
    "output": {
      "mode": "Lambda",
      "kind": "node-list",
      "description": "Resolves to one mapped output item per selected node, using the value or nodes returned by the child lambda"
    }
  }
}
```

</details>

---

[&larr; `lte`](/reference/slots/core/lte/) | [all core slots](/reference/slots/core/) | [`markdown2html` &rarr;](/reference/slots/core/markdown2html/)


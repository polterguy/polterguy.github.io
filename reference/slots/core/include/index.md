---
title: "[include]"
description: "include is a core slot of Magic Cloud. Evaluates child slots and includes all returned nodes into each selected node."
generated: true
llms: false
slot_json: "/reference/slots/core/include/slot.json"
---

`include` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Evaluates child slots and includes all returned nodes into each selected node.

* **Value** (`node-list`), required: Expression selecting the destination node or nodes to include into
* **Returns**: Resolves to the matched destination nodes after all returned child nodes have been included

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | yes | Executable body evaluated once per selected node; all returned child nodes are included into that selected node. Can be repeated. |

Guide: [How to use [include]](/plugins/magic.lambda/nodes/#how-to-use-include)

### JSON declaration

This is the complete declaration of `include`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "include",
  "description": "Evaluates child slots and includes all returned nodes into each selected node",
  "signature": {
    "input": {
      "kind": "node-list",
      "description": "Expression selecting the destination node or nodes to include into",
      "required": true,
      "mode": "Expression"
    },
    "children": {
      "*": {
        "type": "lambda",
        "description": "Executable body evaluated once per selected node; all returned child nodes are included into that selected node",
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
      "description": "Resolves to the matched destination nodes after all returned child nodes have been included"
    }
  }
}
```

</details>

---

[&larr; `if`](/reference/slots/core/if/) | [all core slots](/reference/slots/core/) | [`insert-after` &rarr;](/reference/slots/core/insert-after/)


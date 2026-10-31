---
title: "[insert-after]"
description: "insert-after is a core slot of Magic Cloud. Inserts nodes after the specified target node."
generated: true
llms: false
slot_json: "/reference/slots/core/insert-after/slot.json"
---

`insert-after` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Inserts nodes after the specified target node.

* **Value** (`node-list,single-object`), required: Expression selecting the target node or nodes to insert after

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | yes | Source container or node-producing slot evaluated before its child nodes are applied to the selected target location. Can be repeated. |

Guide: [How to use [insert-after]](/plugins/magic.lambda/nodes/#how-to-use-insert-after)

### Related documentation

* Part of the [magic.lambda](/plugins/magic.lambda/) plugin, which documents every slot it contains.
* Discussed in [Modifying your lambda object](/plugins/magic.lambda/nodes/).

### JSON declaration

This is the complete declaration of `insert-after`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "insert-after",
  "description": "Inserts nodes after the specified target node",
  "signature": {
    "input": {
      "kind": "node-list,single-object",
      "description": "Expression selecting the target node or nodes to insert after",
      "required": true,
      "mode": "Expression"
    },
    "children": {
      "*": {
        "type": "lambda",
        "kind": "node-list",
        "description": "Source container or node-producing slot evaluated before its child nodes are applied to the selected target location",
        "required": true,
        "mode": "ExecutableLambda",
        "cardinality": "OneOrMore",
        "role": "SourceContainer",
        "evaluation": "EvalSelf",
        "projection": "ChildrenOfChildren"
      }
    }
  }
}
```

</details>

---

[&larr; `include`](/reference/slots/core/include/) | [all core slots](/reference/slots/core/) | [`insert-before` &rarr;](/reference/slots/core/insert-before/)


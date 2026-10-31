---
title: "[for-each]"
description: "for-each is a core slot of Magic Cloud. Iterates over the nodes matching the expression and evaluates the child lambda once per node as [.dp]."
generated: true
llms: false
slot_json: "/reference/slots/core/for-each/slot.json"
---

`for-each` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Iterates over the nodes matching the expression and evaluates the child lambda once per node as [.dp].

* **Value** (`node-list`), required: Expression selecting the nodes to iterate

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | yes | Loop body evaluated once per selected node. Can be repeated. |

Guide: [How to use [for-each]](/plugins/magic.lambda/loops/#how-to-use-for-each)

### JSON declaration

This is the complete declaration of `for-each`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "for-each",
  "description": "Iterates over the nodes matching the expression and evaluates the child lambda once per node as [.dp]",
  "signature": {
    "input": {
      "kind": "node-list",
      "description": "Expression selecting the nodes to iterate",
      "required": true,
      "mode": "Expression"
    },
    "children": {
      "*": {
        "type": "lambda",
        "description": "Loop body evaluated once per selected node",
        "required": true,
        "mode": "ExecutableLambda",
        "cardinality": "OneOrMore",
        "role": "ExecutableBody",
        "evaluation": "EvalSelf",
        "projection": "Self"
      }
    }
  }
}
```

</details>

---

[&larr; `floatArray2bytes`](/reference/slots/core/floatArray2bytes/) | [all core slots](/reference/slots/core/) | [`fork` &rarr;](/reference/slots/core/fork/)


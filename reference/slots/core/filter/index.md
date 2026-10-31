---
title: "[filter]"
description: "filter is a core slot of Magic Cloud. Filters selected nodes using the child lambda as a predicate."
generated: true
llms: false
slot_json: "/reference/slots/core/filter/slot.json"
---

`filter` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Filters selected nodes using the child lambda as a predicate.

* **Value** (`node-list`), required: Expression selecting the nodes to filter
* **Returns**: Resolves to clones of the selected nodes whose predicate body returns true

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | yes | Predicate body evaluated once per selected node; the selected node is kept when the body returns true. Can be repeated. |

Guide: [How to use [filter]](/plugins/magic.lambda/nodes/#how-to-use-filter)

### JSON declaration

This is the complete declaration of `filter`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "filter",
  "description": "Filters selected nodes using the child lambda as a predicate",
  "signature": {
    "input": {
      "kind": "node-list",
      "description": "Expression selecting the nodes to filter",
      "required": true,
      "mode": "Expression"
    },
    "children": {
      "*": {
        "type": "lambda",
        "kind": "boolean",
        "description": "Predicate body evaluated once per selected node; the selected node is kept when the body returns true",
        "required": true,
        "mode": "ExecutableLambda",
        "cardinality": "OneOrMore",
        "role": "Condition",
        "evaluation": "EvalSelf",
        "projection": "ReturnedResult"
      }
    },
    "output": {
      "mode": "Lambda",
      "kind": "node-list",
      "description": "Resolves to clones of the selected nodes whose predicate body returns true"
    }
  }
}
```

</details>

---

[&larr; `exists`](/reference/slots/core/exists/) | [all core slots](/reference/slots/core/) | [`floatArray2bytes` &rarr;](/reference/slots/core/floatArray2bytes/)


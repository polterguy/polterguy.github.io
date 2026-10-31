---
title: "[sort]"
description: "sort is a core slot of Magic Cloud. Sorts selected nodes using the child lambda as a comparer."
generated: true
llms: false
slot_json: "/reference/slots/core/sort/slot.json"
---

`sort` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Sorts selected nodes using the child lambda as a comparer.

* **Value** (`node-list`), required: Expression selecting the nodes to sort
* **Returns**: Resolves to the sorted nodes selected by the expression as child nodes

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | no | Comparer body evaluated with [.lhs], [.rhs], and [.result] injected. Can be repeated. |

Guide: [How to use [sort]](/plugins/magic.lambda/types/#how-to-use-sort)

### JSON declaration

This is the complete declaration of `sort`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "sort",
  "description": "Sorts selected nodes using the child lambda as a comparer",
  "signature": {
    "input": {
      "kind": "node-list",
      "description": "Expression selecting the nodes to sort",
      "required": true,
      "mode": "Expression"
    },
    "children": {
      "*": {
        "type": "lambda",
        "description": "Comparer body evaluated with [.lhs], [.rhs], and [.result] injected",
        "required": false,
        "mode": "ExecutableLambda",
        "cardinality": "ZeroOrMore",
        "role": "ExecutableBody",
        "evaluation": "EvalSelf",
        "projection": "Self"
      }
    },
    "output": {
      "mode": "Lambda",
      "kind": "node-list",
      "description": "Resolves to the sorted nodes selected by the expression as child nodes"
    }
  }
}
```

</details>

---

[&larr; `sleep`](/reference/slots/core/sleep/) | [all core slots](/reference/slots/core/) | [`switch` &rarr;](/reference/slots/core/switch/)


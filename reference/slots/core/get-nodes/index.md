---
title: "[get-nodes]"
description: "get-nodes is a core slot of Magic Cloud. Returns clones of every node matching the expression as children of the current node."
generated: true
llms: false
slot_json: "/reference/slots/core/get-nodes/slot.json"
---

`get-nodes` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Returns clones of every node matching the expression as children of the current node.

* **Value** (`node-list`), required: Expression selecting the nodes to retrieve
* **Returns**: Resolves to the nodes matched by the expression as child nodes

Guide: [How to use [get-nodes]](/plugins/magic.lambda/nodes/#how-to-use-get-nodes)

### Related documentation

* Part of the [magic.lambda](/plugins/magic.lambda/) plugin, which documents every slot it contains.
* Discussed in [Modifying your lambda object](/plugins/magic.lambda/nodes/).

### JSON declaration

This is the complete declaration of `get-nodes`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "get-nodes",
  "description": "Returns clones of every node matching the expression as children of the current node",
  "signature": {
    "input": {
      "kind": "node-list",
      "description": "Expression selecting the nodes to retrieve",
      "required": true,
      "mode": "Expression"
    },
    "output": {
      "mode": "Lambda",
      "kind": "node-list",
      "element-kind": "node",
      "description": "Resolves to the nodes matched by the expression as child nodes"
    }
  }
}
```

</details>

---

[&larr; `get-name`](/reference/slots/core/get-name/) | [all core slots](/reference/slots/core/) | [`get-value` &rarr;](/reference/slots/core/get-value/)


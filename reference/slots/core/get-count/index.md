---
title: "[get-count]"
description: "get-count is a core slot of Magic Cloud. Returns the number of matching nodes."
generated: true
llms: false
slot_json: "/reference/slots/core/get-count/slot.json"
---

`get-count` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Returns the number of matching nodes.

* **Value** (`node-list`), required: Expression selecting the nodes to count
* **Returns**: Resolves to the number of nodes matched by the expression

Guide: [How to use [get-count]](/plugins/magic.lambda/nodes/#how-to-use-get-count)

### Related documentation

* Part of the [magic.lambda](/plugins/magic.lambda/) plugin, which documents every slot it contains.
* Discussed in [Modifying your lambda object](/plugins/magic.lambda/nodes/).

### JSON declaration

This is the complete declaration of `get-count`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "get-count",
  "description": "Returns the number of matching nodes",
  "signature": {
    "input": {
      "kind": "node-list",
      "description": "Expression selecting the nodes to count",
      "required": true,
      "mode": "Expression"
    },
    "output": {
      "mode": "Value",
      "kind": "number",
      "description": "Resolves to the number of nodes matched by the expression"
    }
  }
}
```

</details>

---

[&larr; `get-context`](/reference/slots/core/get-context/) | [all core slots](/reference/slots/core/) | [`get-first-value` &rarr;](/reference/slots/core/get-first-value/)


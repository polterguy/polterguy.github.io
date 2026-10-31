---
title: "[get-value]"
description: "get-value is a core slot of Magic Cloud. Returns the value of the first matching node."
generated: true
llms: false
slot_json: "/reference/slots/core/get-value/slot.json"
---

`get-value` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Returns the value of the first matching node.

* **Value** (`single-object`), required: Expression selecting the node whose value should be retrieved
* **Returns**: Resolves to the value of the first matching node

Guide: [How to use [get-value]](/plugins/magic.lambda/nodes/#how-to-use-get-value)

### Related documentation

* Part of the [magic.lambda](/plugins/magic.lambda/) plugin, which documents every slot it contains.
* Discussed in [Branching and conditional execution](/plugins/magic.lambda/branching/).
* Discussed in [Comparison and boolean logic](/plugins/magic.lambda/conditions/).
* Discussed in [Executing lambda objects](/plugins/magic.lambda/executing/).
* Discussed in [Hyperlambda loops](/plugins/magic.lambda/loops/).
* Discussed in [Modifying your lambda object](/plugins/magic.lambda/nodes/).
* Discussed in [Types and conversion](/plugins/magic.lambda/types/).

### JSON declaration

This is the complete declaration of `get-value`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "get-value",
  "description": "Returns the value of the first matching node",
  "signature": {
    "input": {
      "kind": "single-object",
      "description": "Expression selecting the node whose value should be retrieved",
      "required": true,
      "mode": "Expression"
    },
    "output": {
      "mode": "Value",
      "description": "Resolves to the value of the first matching node"
    }
  }
}
```

</details>

---

[&larr; `get-nodes`](/reference/slots/core/get-nodes/) | [all core slots](/reference/slots/core/) | [`html-decode` &rarr;](/reference/slots/core/html-decode/)


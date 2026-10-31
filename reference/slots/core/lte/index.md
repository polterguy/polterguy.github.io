---
title: "[lte]"
description: "lte is a core slot of Magic Cloud. Returns true if the first operand is less than or equal to the second operand."
generated: true
llms: false
slot_json: "/reference/slots/core/lte/slot.json"
---

`lte` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Returns true if the first operand is less than or equal to the second operand.

* **Returns**: Resolves to true if the first operand is less than or equal to the second operand

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | object | yes | Operand evaluated before comparison. |

Guide: [How to use [lte]](/plugins/magic.lambda/conditions/#how-to-use-lte)

### Related documentation

* Part of the [magic.lambda](/plugins/magic.lambda/) plugin, which documents every slot it contains.
* Discussed in [Comparison and boolean logic](/plugins/magic.lambda/conditions/).

### JSON declaration

This is the complete declaration of `lte`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "lte",
  "description": "Returns true if the first operand is less than or equal to the second operand",
  "signature": {
    "children": {
      "*": {
        "type": "object",
        "description": "Operand evaluated before comparison",
        "required": true,
        "mode": "ExecutableLambda",
        "cardinality": "ExactlyTwo",
        "role": "OperandPaired",
        "evaluation": "EvalSelf",
        "projection": "Value"
      }
    },
    "output": {
      "mode": "Value",
      "kind": "boolean",
      "description": "Resolves to true if the first operand is less than or equal to the second operand"
    }
  }
}
```

</details>

---

[&larr; `lt`](/reference/slots/core/lt/) | [all core slots](/reference/slots/core/) | [`map` &rarr;](/reference/slots/core/map/)


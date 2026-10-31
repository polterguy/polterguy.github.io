---
title: "[mte]"
description: "mte is a core slot of Magic Cloud. Returns true if the first operand is greater than or equal to the second operand."
generated: true
llms: false
slot_json: "/reference/slots/core/mte/slot.json"
---

`mte` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Returns true if the first operand is greater than or equal to the second operand.

* **Returns**: Resolves to true if the first operand is greater than or equal to the second operand

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | object | yes | Operand evaluated before comparison. |

Guide: [How to use [mte]](/plugins/magic.lambda/conditions/#how-to-use-mte)

### Related documentation

* Part of the [magic.lambda](/plugins/magic.lambda/) plugin, which documents every slot it contains.
* Discussed in [Comparison and boolean logic](/plugins/magic.lambda/conditions/).

### JSON declaration

This is the complete declaration of `mte`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "mte",
  "description": "Returns true if the first operand is greater than or equal to the second operand",
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
      "description": "Resolves to true if the first operand is greater than or equal to the second operand"
    }
  }
}
```

</details>

---

[&larr; `mt`](/reference/slots/core/mt/) | [all core slots](/reference/slots/core/) | [`neq` &rarr;](/reference/slots/core/neq/)


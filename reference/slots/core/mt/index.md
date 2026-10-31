---
title: "[mt]"
description: "mt is a core slot of Magic Cloud. Returns true if the first operand is greater than the second operand."
generated: true
llms: false
slot_json: "/reference/slots/core/mt/slot.json"
---

`mt` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Returns true if the first operand is greater than the second operand.

* **Returns**: Resolves to true if the first operand is greater than the second operand

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | object | yes | Operand evaluated before comparison. |

Guide: [How to use [mt]](/plugins/magic.lambda/conditions/#how-to-use-mt)

### Guide

[How to use `mt`](/plugins/magic.lambda/mt/)

### JSON declaration

This is the complete declaration of `mt`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "mt",
  "description": "Returns true if the first operand is greater than the second operand",
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
      "description": "Resolves to true if the first operand is greater than the second operand"
    }
  }
}
```

</details>

---

[&larr; `markdown2html`](/reference/slots/core/markdown2html/) | [all core slots](/reference/slots/core/) | [`mte` &rarr;](/reference/slots/core/mte/)


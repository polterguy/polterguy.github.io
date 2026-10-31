---
title: "[and]"
description: "and is a core slot of Magic Cloud. Returns true if all children evaluate to true."
generated: true
llms: false
slot_json: "/reference/slots/core/and/slot.json"
---

`and` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Returns true if all children evaluate to true.

* **Returns**: Resolves to true if all operands evaluate to true

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | yes | Executable operand returning a boolean value. |

Guide: [How to use [and]](/plugins/magic.lambda/conditions/#how-to-use-and)

### Guide

[How to use `and`](/plugins/magic.lambda/and/)

### JSON declaration

This is the complete declaration of `and`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "and",
  "description": "Returns true if all children evaluate to true",
  "signature": {
    "children": {
      "*": {
        "type": "lambda",
        "kind": "boolean",
        "description": "Executable operand returning a boolean value",
        "required": true,
        "mode": "ExecutableLambda",
        "cardinality": "TwoOrMore",
        "role": "Operand",
        "evaluation": "EvalSelf",
        "projection": "Self"
      }
    },
    "output": {
      "mode": "Value",
      "kind": "boolean",
      "description": "Resolves to true if all operands evaluate to true"
    }
  }
}
```

</details>

---

[&larr; `add`](/reference/slots/core/add/) | [all core slots](/reference/slots/core/) | [`apply` &rarr;](/reference/slots/core/apply/)


---
title: "[lt]"
description: "lt is a core slot of Magic Cloud. Returns true if the first operand is less than the second operand."
generated: true
llms: false
slot_json: "/reference/slots/core/lt/slot.json"
---

`lt` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Returns true if the first operand is less than the second operand.

* **Returns**: Resolves to true if the first operand is less than the second operand

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | object | yes | Operand evaluated before comparison. |

Guide: [How to use [lt]](/plugins/magic.lambda/conditions/#how-to-use-lt)

### JSON declaration

This is the complete declaration of `lt`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "lt",
  "description": "Returns true if the first operand is less than the second operand",
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
      "description": "Resolves to true if the first operand is less than the second operand"
    }
  }
}
```

</details>

---

[&larr; `lambda2yaml`](/reference/slots/core/lambda2yaml/) | [all core slots](/reference/slots/core/) | [`lte` &rarr;](/reference/slots/core/lte/)


---
title: "[not]"
description: "not is a core slot of Magic Cloud. Negates a boolean expression."
generated: true
llms: false
slot_json: "/reference/slots/core/not/slot.json"
---

`not` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Negates a boolean expression.

* **Returns**: Resolves to true if the operand evaluates to false

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | yes | Executable operand returning a boolean value. |

Guide: [How to use [not]](/plugins/magic.lambda/conditions/#how-to-use-not)

### JSON declaration

This is the complete declaration of `not`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "not",
  "description": "Negates a boolean expression",
  "signature": {
    "children": {
      "*": {
        "type": "lambda",
        "kind": "boolean",
        "description": "Executable operand returning a boolean value",
        "required": true,
        "mode": "ExecutableLambda",
        "cardinality": "ExactlyOne",
        "role": "Operand",
        "evaluation": "EvalSelf",
        "projection": "Self"
      }
    },
    "output": {
      "mode": "Value",
      "kind": "boolean",
      "description": "Resolves to true if the operand evaluates to false"
    }
  }
}
```

</details>

---

[&larr; `neq`](/reference/slots/core/neq/) | [all core slots](/reference/slots/core/) | [`not-exists` &rarr;](/reference/slots/core/not-exists/)


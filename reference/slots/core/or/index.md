---
title: "[or]"
description: "or is a core slot of Magic Cloud. Returns true if any child expression evaluates to true."
generated: true
llms: false
slot_json: "/reference/slots/core/or/slot.json"
---

`or` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Returns true if any child expression evaluates to true.

* **Returns**: Resolves to true if any operand evaluates to true

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | yes | Executable operand returning a boolean value. |

Guide: [How to use [or]](/plugins/magic.lambda/conditions/#how-to-use-or)

### Guide

[How to use `or`](/plugins/magic.lambda/or/)

### JSON declaration

This is the complete declaration of `or`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "or",
  "description": "Returns true if any child expression evaluates to true",
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
      "description": "Resolves to true if any operand evaluates to true"
    }
  }
}
```

</details>

---

[&larr; `null`](/reference/slots/core/null/) | [all core slots](/reference/slots/core/) | [`pdf2text` &rarr;](/reference/slots/core/pdf2text/)


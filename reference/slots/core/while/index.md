---
title: "[while]"
description: "while is a core slot of Magic Cloud. Repeats execution while a condition is true."
generated: true
llms: false
slot_json: "/reference/slots/core/while/slot.json"
---

`while` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Repeats execution while a condition is true.

* **Scope**: provides `while`

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | yes | Condition node evaluated for truthiness. |
| `[.lambda]` | lambda | yes | Executable lambda block. |

Guide: [How to use [while]](/plugins/magic.lambda/loops/#how-to-use-while)

### JSON declaration

This is the complete declaration of `while`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "while",
  "description": "Repeats execution while a condition is true",
  "signature": {
    "children": {
      "*": {
        "type": "lambda",
        "kind": "boolean",
        "description": "Condition node evaluated for truthiness",
        "required": true,
        "mode": "ExecutableLambda",
        "cardinality": "ExactlyOne",
        "role": "Condition",
        "evaluation": "EvalSelf",
        "projection": "Value"
      },
      ".lambda": {
        "type": "lambda",
        "description": "Executable lambda block",
        "required": true,
        "mode": "ExecutableLambda",
        "cardinality": "ExactlyOne",
        "role": "LambdaBlock",
        "evaluation": "EvalBlock",
        "projection": "Self"
      }
    },
    "scope": {
      "provides": "while"
    }
  }
}
```

</details>

---

[&larr; `vocabulary`](/reference/slots/core/vocabulary/) | [all core slots](/reference/slots/core/) | [`whitelist` &rarr;](/reference/slots/core/whitelist/)


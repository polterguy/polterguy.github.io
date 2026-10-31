---
title: "[if]"
description: "if is a core slot of Magic Cloud. Evaluates the child lambda only if the condition is true; chain with [else-if] and [else] for additional branches."
generated: true
llms: false
slot_json: "/reference/slots/core/if/slot.json"
---

`if` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Evaluates the child lambda only if the condition is true; chain with [else-if] and [else] for additional branches.

* **Scope**: provides `if`

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | yes | Condition node evaluated for truthiness. |
| `[.lambda]` | lambda | yes | Executable lambda block. |

Guide: [How to use [if]](/plugins/magic.lambda/branching/#how-to-use-if)

### JSON declaration

This is the complete declaration of `if`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "if",
  "description": "Evaluates the child lambda only if the condition is true; chain with [else-if] and [else] for additional branches",
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
      "provides": "if"
    }
  }
}
```

</details>

---

[&larr; `hyper2lambda`](/reference/slots/core/hyper2lambda/) | [all core slots](/reference/slots/core/) | [`include` &rarr;](/reference/slots/core/include/)


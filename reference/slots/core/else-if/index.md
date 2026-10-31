---
title: "[else-if]"
description: "else-if is a core slot of Magic Cloud. Evaluates the child lambda when its condition is true and no preceding [if]/[else-if] branch matched."
generated: true
llms: false
slot_json: "/reference/slots/core/else-if/slot.json"
---

`else-if` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Evaluates the child lambda when its condition is true and no preceding [if]/[else-if] branch matched.

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | yes | Condition node evaluated for truthiness. |
| `[.lambda]` | lambda | yes | Executable lambda block. |

### Constraints

* **PreviousSiblingMustBeOneOf**: Previous sibling must be one of the listed slot names (`[if]`, `[else-if]`)

Guide: [How to use [else-if]](/plugins/magic.lambda/branching/#how-to-use-else-if)

### JSON declaration

This is the complete declaration of `else-if`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "else-if",
  "description": "Evaluates the child lambda when its condition is true and no preceding [if]/[else-if] branch matched",
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
    "constraints": [
      {
        "description": "Previous sibling must be one of the listed slot names",
        "values": [
          "if",
          "else-if"
        ],
        "kind": "PreviousSiblingMustBeOneOf"
      }
    ]
  }
}
```

</details>

---

[&larr; `else`](/reference/slots/core/else/) | [all core slots](/reference/slots/core/) | [`eq` &rarr;](/reference/slots/core/eq/)


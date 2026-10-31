---
title: "[else]"
description: "else is a core slot of Magic Cloud. Evaluates its child lambda when every preceding [if] and [else-if] condition was false."
generated: true
llms: false
slot_json: "/reference/slots/core/else/slot.json"
---

`else` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Evaluates its child lambda when every preceding [if] and [else-if] condition was false.

* **Scope**: provides `if`

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | yes | Fallback branch body evaluated when previous conditions fail. Can be repeated. |

### Constraints

* **PreviousSiblingMustBeOneOf**: Previous sibling must be one of the listed slot names (`[if]`, `[else-if]`)

Guide: [How to use [else]](/plugins/magic.lambda/branching/#how-to-use-else)

### Guide

[How to use `else`](/plugins/magic.lambda/else/)

### JSON declaration

This is the complete declaration of `else`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "else",
  "description": "Evaluates its child lambda when every preceding [if] and [else-if] condition was false",
  "signature": {
    "children": {
      "*": {
        "type": "lambda",
        "description": "Fallback branch body evaluated when previous conditions fail",
        "required": true,
        "mode": "ExecutableLambda",
        "cardinality": "OneOrMore",
        "role": "ExecutableBody",
        "evaluation": "EvalSelf",
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
    ],
    "scope": {
      "provides": "if"
    }
  }
}
```

</details>

---

[&larr; `default`](/reference/slots/core/default/) | [all core slots](/reference/slots/core/) | [`else-if` &rarr;](/reference/slots/core/else-if/)


---
title: "[switch]"
description: "switch is a core slot of Magic Cloud. Evaluates one of several branches based on the input value."
generated: true
llms: false
slot_json: "/reference/slots/core/switch/slot.json"
---

`switch` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Evaluates one of several branches based on the input value.

* **Value** (`switch-value`), required: Value to compare against the child [case] values

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[case]` | object | yes | Case branch matching the switch value. Can be repeated. |
| `[case]` / _any node name_ | lambda | yes | Branch body executed when the case matches. Can be repeated. |
| `[default]` | lambda | no | Fallback branch when no case matches. |
| `[default]` / _any node name_ | lambda | yes | Fallback branch body. Can be repeated. |

### Constraints

* **OnlyChildren**: Only the listed child names are accepted (`[case]`, `[default]`)

Guide: [How to use [switch]](/plugins/magic.lambda/branching/#how-to-use-switch)

### Related documentation

* Part of the [magic.lambda](/plugins/magic.lambda/) plugin, which documents every slot it contains.
* Discussed in [Branching and conditional execution](/plugins/magic.lambda/branching/).

### JSON declaration

This is the complete declaration of `switch`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "switch",
  "description": "Evaluates one of several branches based on the input value",
  "signature": {
    "input": {
      "kind": "switch-value",
      "description": "Value to compare against the child [case] values",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "case": {
        "type": "object",
        "kind": "switch-value",
        "description": "Case branch matching the switch value",
        "required": true,
        "mode": "ValueOrExpression",
        "cardinality": "OneOrMore",
        "role": "Branch",
        "evaluation": "EvalSelf",
        "projection": "Self",
        "children": {
          "*": {
            "type": "lambda",
            "description": "Branch body executed when the case matches",
            "required": true,
            "mode": "ExecutableLambda",
            "cardinality": "OneOrMore",
            "role": "ExecutableBody",
            "evaluation": "EvalSelf",
            "projection": "Self"
          }
        }
      },
      "default": {
        "type": "lambda",
        "description": "Fallback branch when no case matches",
        "required": false,
        "mode": "ExecutableLambda",
        "cardinality": "ZeroOrOne",
        "role": "Branch",
        "evaluation": "EvalSelf",
        "projection": "Self",
        "children": {
          "*": {
            "type": "lambda",
            "description": "Fallback branch body",
            "required": true,
            "mode": "ExecutableLambda",
            "cardinality": "OneOrMore",
            "role": "ExecutableBody",
            "evaluation": "EvalSelf",
            "projection": "Self"
          }
        }
      }
    },
    "constraints": [
      {
        "description": "Only the listed child names are accepted",
        "values": [
          "case",
          "default"
        ],
        "kind": "OnlyChildren"
      }
    ]
  }
}
```

</details>

---

[&larr; `sort`](/reference/slots/core/sort/) | [all core slots](/reference/slots/core/) | [`throw` &rarr;](/reference/slots/core/throw/)


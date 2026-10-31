---
title: "[case]"
description: "case is a core slot of Magic Cloud. Evaluates a single case branch inside [switch]."
generated: true
llms: false
slot_json: "/reference/slots/core/case/slot.json"
---

`case` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Evaluates a single case branch inside [switch].

* **Value** (`switch-value`), required: Case value to match against the [switch] input value

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | yes | Case branch body executed by the parent [switch]. Can be repeated. |

### Constraints

* **ParentMustBe**: Parent node must have the listed slot name (`[switch]`)

### Related documentation

* Part of the [magic.lambda](/plugins/magic.lambda/) plugin, which documents every slot it contains.
* Discussed in [Branching and conditional execution](/plugins/magic.lambda/branching/).

### JSON declaration

This is the complete declaration of `case`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "case",
  "description": "Evaluates a single case branch inside [switch]",
  "signature": {
    "input": {
      "kind": "switch-value",
      "description": "Case value to match against the [switch] input value",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "*": {
        "type": "lambda",
        "description": "Case branch body executed by the parent [switch]",
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
        "description": "Parent node must have the listed slot name",
        "values": [
          "switch"
        ],
        "kind": "ParentMustBe"
      }
    ]
  }
}
```

</details>

---

[&larr; `apply`](/reference/slots/core/apply/) | [all core slots](/reference/slots/core/) | [`compose` &rarr;](/reference/slots/core/compose/)


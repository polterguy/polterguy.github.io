---
title: "[default]"
description: "default is a core slot of Magic Cloud. Evaluates the default branch inside [switch]."
generated: true
llms: false
slot_json: "/reference/slots/core/default/slot.json"
---

`default` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Evaluates the default branch inside [switch].

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | yes | Default branch body executed by the parent [switch]. Can be repeated. |

### Constraints

* **ParentMustBe**: Parent node must have the listed slot name (`[switch]`)

### JSON declaration

This is the complete declaration of `default`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "default",
  "description": "Evaluates the default branch inside [switch]",
  "signature": {
    "children": {
      "*": {
        "type": "lambda",
        "description": "Default branch body executed by the parent [switch]",
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

[&larr; `csv2lambda`](/reference/slots/core/csv2lambda/) | [all core slots](/reference/slots/core/) | [`else` &rarr;](/reference/slots/core/else/)


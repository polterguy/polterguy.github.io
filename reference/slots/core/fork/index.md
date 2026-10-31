---
title: "[fork]"
description: "fork is a core slot of Magic Cloud. Spawns a fire-and-forget background thread that evaluates the child lambda; the parent continues immediately."
generated: true
llms: false
slot_json: "/reference/slots/core/fork/slot.json"
---

`fork` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Spawns a fire-and-forget background thread that evaluates the child lambda; the parent continues immediately.

* **Scope**: provides `fork`

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | yes | Executable child slot evaluated on the forked thread. Can be repeated. |

Guide: [How to use [fork]](/plugins/magic.lambda.threading/#how-to-use-fork)

### JSON declaration

This is the complete declaration of `fork`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "fork",
  "description": "Spawns a fire-and-forget background thread that evaluates the child lambda; the parent continues immediately",
  "signature": {
    "children": {
      "*": {
        "type": "lambda",
        "description": "Executable child slot evaluated on the forked thread",
        "required": true,
        "mode": "ExecutableLambda",
        "cardinality": "OneOrMore",
        "role": "ExecutableBody",
        "evaluation": "EvalSelf",
        "projection": "Self"
      }
    },
    "scope": {
      "provides": "fork"
    }
  }
}
```

</details>

---

[&larr; `for-each`](/reference/slots/core/for-each/) | [all core slots](/reference/slots/core/) | [`format` &rarr;](/reference/slots/core/format/)


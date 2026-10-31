---
title: "[try]"
description: "try is a core slot of Magic Cloud. Evaluates the protected body; pair with [.catch] to handle exceptions and/or [.finally] to always run cleanup."
generated: true
llms: false
slot_json: "/reference/slots/core/try/slot.json"
---

`try` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Evaluates the protected body; pair with [.catch] to handle exceptions and/or [.finally] to always run cleanup.

* **Scope**: provides `try`

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | no | Protected body evaluated by [try]. Can be repeated. |

### Constraints

* **NextSiblingMustBeOneOf**: Must be followed by [.catch] and/or [.finally]; a bare [try] is a no-op because uncaught exceptions re-throw and [.finally] alone would run regardless (`[.catch]`, `[.finally]`)

Guide: [How to use [try]](/plugins/magic.lambda/exceptions/#how-to-use-try)

### Related documentation

* Part of the [magic.lambda](/plugins/magic.lambda/) plugin, which documents every slot it contains.
* Discussed in [Hyperlambda exceptions](/plugins/magic.lambda/exceptions/).

### JSON declaration

This is the complete declaration of `try`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "try",
  "description": "Evaluates the protected body; pair with [.catch] to handle exceptions and/or [.finally] to always run cleanup",
  "signature": {
    "children": {
      "*": {
        "type": "lambda",
        "description": "Protected body evaluated by [try]",
        "required": false,
        "mode": "ExecutableLambda",
        "cardinality": "ZeroOrMore",
        "role": "ExecutableBody",
        "evaluation": "EvalSelf",
        "projection": "Self"
      }
    },
    "constraints": [
      {
        "description": "Must be followed by [.catch] and/or [.finally]; a bare [try] is a no-op because uncaught exceptions re-throw and [.finally] alone would run regardless",
        "values": [
          ".catch",
          ".finally"
        ],
        "kind": "NextSiblingMustBeOneOf"
      }
    ],
    "scope": {
      "provides": "try"
    }
  }
}
```

</details>

---

[&larr; `time`](/reference/slots/core/time/) | [all core slots](/reference/slots/core/) | [`try-signal` &rarr;](/reference/slots/core/try-signal/)


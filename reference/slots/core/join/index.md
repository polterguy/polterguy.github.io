---
title: "[join]"
description: "join is a core slot of Magic Cloud. Waits for one or more child [fork] operations to finish before proceeding."
generated: true
llms: false
slot_json: "/reference/slots/core/join/slot.json"
---

`join` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Waits for one or more child [fork] operations to finish before proceeding.

* **Returns**: Resolves to the completed [fork] child nodes with evaluated body node values and children preserved
* **Scope**: provides `join`

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[fork]` | lambda | yes | Fork body to start and wait for; evaluated body node values and children are preserved in the completed fork node. Can be repeated. |

### Guide

[How to use `join`](/plugins/magic.lambda.threading/join/)

### JSON declaration

This is the complete declaration of `join`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "join",
  "description": "Waits for one or more child [fork] operations to finish before proceeding",
  "signature": {
    "children": {
      "fork": {
        "type": "lambda",
        "description": "Fork body to start and wait for; evaluated body node values and children are preserved in the completed fork node",
        "required": true,
        "mode": "ExecutableLambda",
        "cardinality": "OneOrMore",
        "role": "ExecutableBody",
        "evaluation": "SerializeLambda",
        "projection": "Self"
      }
    },
    "scope": {
      "provides": "join"
    },
    "output": {
      "mode": "Lambda",
      "kind": "fork-result-list,node-list",
      "description": "Resolves to the completed [fork] child nodes with evaluated body node values and children preserved"
    }
  }
}
```

</details>

---

[&larr; `invoke`](/reference/slots/core/invoke/) | [all core slots](/reference/slots/core/) | [`json2lambda` &rarr;](/reference/slots/core/json2lambda/)


---
title: "[join]"
description: "join is a core slot of Magic Cloud. Waits for one or more child [fork] operations to finish before proceeding."
generated: true
llms: "guide"
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

<!-- guide -->
Joins all child **[\[fork\]](/reference/slots/core/fork/)** invocations, implying the slot will wait until all forks directly below it
has finished executing, and automatically copy the result of the **[\[fork\]](/reference/slots/core/fork/)** into the original node.

```
join
   fork
      http.get:"https://servergardens.com"
   fork
      http.get:"https://gaiasoul.com"
```

As an analogy for what occurs above, imagine the two rivers from our above **[\[fork\]](/reference/slots/core/fork/)** analogy
that forked from one larger river into two smaller rivers, for then again to join up and becoming one
large river again further down.
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.threading](/plugins/magic.lambda.threading/) plugin, which documents every slot it contains.

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


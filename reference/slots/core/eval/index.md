---
title: "[eval]"
description: "eval is a core slot of Magic Cloud. Executes a lambda block; use it to run a node tree dynamically or to scope a group of statements."
generated: true
llms: false
slot_json: "/reference/slots/core/eval/slot.json"
---

`eval` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Executes a lambda block; use it to run a node tree dynamically or to scope a group of statements.

* **Value** (`lambda-object,lambda-tree`), optional: Expression selecting the Hyperlambda nodes to evaluate; alternatively supply literal executable children

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | no | Executable child slot evaluated in order. Can be repeated. |

Guide: [How to use [eval]](/plugins/magic.lambda/executing/#how-to-use-eval)

### JSON declaration

This is the complete declaration of `eval`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "eval",
  "description": "Executes a lambda block; use it to run a node tree dynamically or to scope a group of statements",
  "signature": {
    "input": {
      "kind": "lambda-object,lambda-tree",
      "description": "Expression selecting the Hyperlambda nodes to evaluate; alternatively supply literal executable children",
      "required": false,
      "mode": "Expression"
    },
    "children": {
      "*": {
        "type": "lambda",
        "description": "Executable child slot evaluated in order",
        "required": false,
        "mode": "ExecutableLambda",
        "cardinality": "ZeroOrMore",
        "role": "ExecutableBody",
        "evaluation": "EvalSelf",
        "projection": "Self"
      }
    }
  }
}
```

</details>

---

[&larr; `eq`](/reference/slots/core/eq/) | [all core slots](/reference/slots/core/) | [`execute` &rarr;](/reference/slots/core/execute/)


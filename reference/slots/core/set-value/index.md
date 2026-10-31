---
title: "[set-value]"
description: "set-value is a core slot of Magic Cloud. Sets node values in the lambda graph."
generated: true
llms: false
slot_json: "/reference/slots/core/set-value/slot.json"
---

`set-value` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Sets node values in the lambda graph.

* **Value** (`node-list,single-object`), required: Expression selecting the node or nodes whose value should be changed

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | object | no | Single source child evaluated before its value is consumed; omit to set the destination to null. |

### Guide

[How to use `set-value`](/plugins/magic.lambda/set-value/)

### JSON declaration

This is the complete declaration of `set-value`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "set-value",
  "description": "Sets node values in the lambda graph",
  "signature": {
    "input": {
      "kind": "node-list,single-object",
      "description": "Expression selecting the node or nodes whose value should be changed",
      "required": true,
      "mode": "Expression"
    },
    "children": {
      "*": {
        "type": "object",
        "description": "Single source child evaluated before its value is consumed; omit to set the destination to null",
        "required": false,
        "mode": "ExecutableLambda",
        "cardinality": "ZeroOrOne",
        "role": "SourceExpression",
        "evaluation": "EvalSelf",
        "projection": "Value"
      }
    }
  }
}
```

</details>

---

[&larr; `set-name`](/reference/slots/core/set-name/) | [all core slots](/reference/slots/core/) | [`set-x` &rarr;](/reference/slots/core/set-x/)


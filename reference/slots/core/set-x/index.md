---
title: "[set-x]"
description: "set-x is a core slot of Magic Cloud. Sets node values without evaluating expressions in the source."
generated: true
llms: false
slot_json: "/reference/slots/core/set-x/slot.json"
---

`set-x` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Sets node values without evaluating expressions in the source.

* **Value** (`node-list,single-object`), required: Expression selecting the node or nodes whose value should be changed

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | object | no | Single source child evaluated before its value is consumed; omit to set the destination to null. |

Guide: [How to use [set-x]](/plugins/magic.lambda/nodes/#how-to-use-set-x)

### Related documentation

* Part of the [magic.lambda](/plugins/magic.lambda/) plugin, which documents every slot it contains.
* Discussed in [Modifying your lambda object](/plugins/magic.lambda/nodes/).

### JSON declaration

This is the complete declaration of `set-x`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "set-x",
  "description": "Sets node values without evaluating expressions in the source",
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

[&larr; `set-value`](/reference/slots/core/set-value/) | [all core slots](/reference/slots/core/) | [`signal` &rarr;](/reference/slots/core/signal/)


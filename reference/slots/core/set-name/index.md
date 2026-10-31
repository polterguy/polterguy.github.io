---
title: "[set-name]"
description: "set-name is a core slot of Magic Cloud. Sets the name of matching nodes."
generated: true
llms: false
slot_json: "/reference/slots/core/set-name/slot.json"
---

`set-name` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Sets the name of matching nodes.

* **Value** (`node-list,single-object`), required: Expression selecting the node or nodes whose name should be changed

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | string | no | Single source child evaluated to a string; the resolved value becomes the new node name. Omit to set the name to null. |

Guide: [How to use [set-name]](/plugins/magic.lambda/nodes/#how-to-use-set-name)

### JSON declaration

This is the complete declaration of `set-name`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "set-name",
  "description": "Sets the name of matching nodes",
  "signature": {
    "input": {
      "kind": "node-list,single-object",
      "description": "Expression selecting the node or nodes whose name should be changed",
      "required": true,
      "mode": "Expression"
    },
    "children": {
      "*": {
        "type": "string",
        "kind": "text",
        "description": "Single source child evaluated to a string; the resolved value becomes the new node name. Omit to set the name to null.",
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

[&larr; `semaphore`](/reference/slots/core/semaphore/) | [all core slots](/reference/slots/core/) | [`set-value` &rarr;](/reference/slots/core/set-value/)


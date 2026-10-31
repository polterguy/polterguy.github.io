---
title: "[get-first-value]"
description: "get-first-value is a core slot of Magic Cloud. Returns the first non-null value produced by candidate child nodes."
generated: true
llms: false
slot_json: "/reference/slots/core/get-first-value/slot.json"
---

`get-first-value` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Returns the first non-null value produced by candidate child nodes.

* **Returns**: Resolves to the first non-null value produced by the candidate child nodes

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | yes | Candidate value source evaluated until the first non-null value is produced. Can be repeated. |

Guide: [How to use [get-first-value]](/plugins/magic.lambda/nodes/#how-to-use-get-first-value)

### JSON declaration

This is the complete declaration of `get-first-value`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "get-first-value",
  "description": "Returns the first non-null value produced by candidate child nodes",
  "signature": {
    "children": {
      "*": {
        "type": "lambda",
        "description": "Candidate value source evaluated until the first non-null value is produced",
        "required": true,
        "mode": "ExecutableLambda",
        "cardinality": "OneOrMore",
        "role": "Operand",
        "evaluation": "EvalSelf",
        "projection": "Value"
      }
    },
    "output": {
      "mode": "Value",
      "description": "Resolves to the first non-null value produced by the candidate child nodes"
    }
  }
}
```

</details>

---

[&larr; `get-count`](/reference/slots/core/get-count/) | [all core slots](/reference/slots/core/) | [`get-name` &rarr;](/reference/slots/core/get-name/)


---
title: "[try-signal]"
description: "try-signal is a core slot of Magic Cloud. Invokes a dynamic slot if it exists and ignores missing slots."
generated: true
llms: false
slot_json: "/reference/slots/core/try-signal/slot.json"
---

`try-signal` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Invokes a dynamic slot if it exists and ignores missing slots.

* **Value** (`dynamic-slot-name`), required: Name of the dynamic slot to try invoking
* **Returns**: Resolves to the invoked slot's value result and any returned child nodes

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | object | no | Named argument passed to the dynamic slot as a child of [.arguments]. Can be repeated. |

### Returned nodes

| Node | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | no | Returned child node produced by the invoked dynamic slot. Can be repeated. |

Guide: [How to use [try-signal]](/plugins/magic.lambda.slots/#how-to-use-try-signal)

### JSON declaration

This is the complete declaration of `try-signal`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "try-signal",
  "description": "Invokes a dynamic slot if it exists and ignores missing slots",
  "signature": {
    "input": {
      "kind": "dynamic-slot-name",
      "description": "Name of the dynamic slot to try invoking",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "*": {
        "type": "object",
        "kind": "value",
        "description": "Named argument passed to the dynamic slot as a child of [.arguments]",
        "required": false,
        "mode": "Arguments",
        "cardinality": "ZeroOrMore",
        "role": "Arguments",
        "projection": "ArgumentBag"
      }
    },
    "output": {
      "mode": "Both",
      "kind": "lambda-result",
      "description": "Resolves to the invoked slot's value result and any returned child nodes",
      "children": {
        "*": {
          "type": "lambda",
          "kind": "dynamic-slot-result-node",
          "description": "Returned child node produced by the invoked dynamic slot",
          "required": false,
          "mode": "Value",
          "cardinality": "ZeroOrMore",
          "role": "Payload",
          "projection": "Self"
        }
      }
    }
  }
}
```

</details>

---

[&larr; `try`](/reference/slots/core/try/) | [all core slots](/reference/slots/core/) | [`type` &rarr;](/reference/slots/core/type/)


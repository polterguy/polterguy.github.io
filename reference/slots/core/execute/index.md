---
title: "[execute]"
description: "execute is a core slot of Magic Cloud. Invokes a dynamic slot after unwrapping descendant expressions."
generated: true
llms: false
slot_json: "/reference/slots/core/execute/slot.json"
---

`execute` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Invokes a dynamic slot after unwrapping descendant expressions.

* **Value** (`dynamic-slot-name`), required: Name of the dynamic slot to invoke
* **Returns**: Resolves to the invoked slot's value result and any returned child nodes

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | object | no | Named argument passed to the dynamic slot as a child of [.arguments]. Can be repeated. |

### Returned nodes

| Node | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | no | Returned child node produced by the invoked dynamic slot after descendant expressions are unwrapped. Can be repeated. |

### Guide

[How to use `execute`](/plugins/magic.lambda.slots/execute/)

### JSON declaration

This is the complete declaration of `execute`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "execute",
  "description": "Invokes a dynamic slot after unwrapping descendant expressions",
  "signature": {
    "input": {
      "kind": "dynamic-slot-name",
      "description": "Name of the dynamic slot to invoke",
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
        "preprocess": "UnwrapExpressions",
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
          "description": "Returned child node produced by the invoked dynamic slot after descendant expressions are unwrapped",
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

[&larr; `eval`](/reference/slots/core/eval/) | [all core slots](/reference/slots/core/) | [`execute-file` &rarr;](/reference/slots/core/execute-file/)


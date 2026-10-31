---
title: "[yield]"
description: "yield is a core slot of Magic Cloud. Returns multiple child nodes or evaluated nodes to the caller."
generated: true
llms: false
slot_json: "/reference/slots/core/yield/slot.json"
---

`yield` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Returns multiple child nodes or evaluated nodes to the caller.

* **Returns**: Returns child nodes to the caller

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | no | Returned child node after descendant expressions are unwrapped. Can be repeated. |

### JSON declaration

This is the complete declaration of `yield`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "yield",
  "description": "Returns multiple child nodes or evaluated nodes to the caller",
  "signature": {
    "children": {
      "*": {
        "type": "lambda",
        "description": "Returned child node after descendant expressions are unwrapped",
        "required": false,
        "mode": "SourceLambda",
        "cardinality": "ZeroOrMore",
        "role": "Payload",
        "evaluation": "UnwrapDescendants",
        "projection": "Self"
      }
    },
    "output": {
      "mode": "Lambda",
      "kind": "node-list",
      "description": "Returns child nodes to the caller"
    }
  }
}
```

</details>

---

[&larr; `yaml2lambda`](/reference/slots/core/yaml2lambda/) | [all core slots](/reference/slots/core/)


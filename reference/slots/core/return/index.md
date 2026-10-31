---
title: "[return]"
description: "return is a core slot of Magic Cloud. Returns a value, expression result, or child nodes to the nearest caller."
generated: true
llms: false
slot_json: "/reference/slots/core/return/slot.json"
---

`return` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Returns a value, expression result, or child nodes to the nearest caller.

* **Value** (`return-value,node-list`), optional: Value or expression to return when no child nodes are supplied; one expression match returns its value, multiple matches return cloned nodes
* **Returns**: Resolves to the supplied value and/or returned child nodes captured by the nearest caller

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | object | no | Child node forwarded to the nearest caller without evaluation; when children exist, all children are returned as-is. Can be repeated. |

### Guide

[How to use `return`](/plugins/magic.lambda.slots/return/)

### JSON declaration

This is the complete declaration of `return`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "return",
  "description": "Returns a value, expression result, or child nodes to the nearest caller",
  "signature": {
    "input": {
      "kind": "return-value,node-list",
      "description": "Value or expression to return when no child nodes are supplied; one expression match returns its value, multiple matches return cloned nodes",
      "required": false,
      "mode": "ValueOrExpression"
    },
    "children": {
      "*": {
        "type": "object",
        "description": "Child node forwarded to the nearest caller without evaluation; when children exist, all children are returned as-is",
        "required": false,
        "mode": "SourceLambda",
        "cardinality": "ZeroOrMore",
        "role": "Payload",
        "projection": "Self"
      }
    },
    "output": {
      "mode": "Both",
      "kind": "return-value,node-list",
      "description": "Resolves to the supplied value and/or returned child nodes captured by the nearest caller"
    }
  }
}
```

</details>

---

[&larr; `remove-nodes`](/reference/slots/core/remove-nodes/) | [all core slots](/reference/slots/core/) | [`return-nodes` &rarr;](/reference/slots/core/return-nodes/)


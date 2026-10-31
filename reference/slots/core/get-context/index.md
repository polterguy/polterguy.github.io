---
title: "[get-context]"
description: "get-context is a core slot of Magic Cloud. Returns a stack value or context object from the current execution context."
generated: true
llms: false
slot_json: "/reference/slots/core/get-context/slot.json"
---

`get-context` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Returns a stack value or context object from the current execution context.

* **Value** (`context-name`), required: Context name to retrieve
* **Returns**: Resolves to the requested stack value or context object
* **Scope**: requires `context` - Requires a named context created by [context] using the same input value

Guide: [How to use [get-context]](/plugins/magic.lambda/nodes/#how-to-use-get-context)

### Guide

[How to use `get-context`](/plugins/magic.lambda/get-context/)

### JSON declaration

This is the complete declaration of `get-context`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "get-context",
  "description": "Returns a stack value or context object from the current execution context",
  "signature": {
    "input": {
      "kind": "context-name",
      "description": "Context name to retrieve",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "scope": {
      "requires": "context",
      "description": "Requires a named context created by [context] using the same input value"
    },
    "output": {
      "mode": "Value",
      "kind": "context-value",
      "description": "Resolves to the requested stack value or context object"
    }
  }
}
```

</details>

---

[&larr; `format`](/reference/slots/core/format/) | [all core slots](/reference/slots/core/) | [`get-count` &rarr;](/reference/slots/core/get-count/)


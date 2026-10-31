---
title: "[context]"
description: "context is a core slot of Magic Cloud. Creates a named stack context object retrievable with [get-context] while evaluating a lambda block."
generated: true
llms: false
slot_json: "/reference/slots/core/context/slot.json"
---

`context` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Creates a named stack context object retrievable with [get-context] while evaluating a lambda block.

* **Value** (`context-name`), required: Context name to create on the stack while evaluating the lambda block
* **Scope**: provides `context` - Creates a named context scope retrievable by [get-context] using the same input value

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| `[.lambda]` | lambda | yes | Body evaluated while the context value is scoped. |
| `[value]` | object | yes | Value stored in the named stack context. |

Guide: [How to use [context]](/plugins/magic.lambda/types/#how-to-use-context)

### JSON declaration

This is the complete declaration of `context`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "context",
  "description": "Creates a named stack context object retrievable with [get-context] while evaluating a lambda block",
  "signature": {
    "input": {
      "kind": "context-name",
      "description": "Context name to create on the stack while evaluating the lambda block",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "value": {
        "type": "object",
        "description": "Value stored in the named stack context",
        "required": true,
        "mode": "ValueOrExpression",
        "cardinality": "ExactlyOne",
        "role": "Option",
        "projection": "Value"
      },
      ".lambda": {
        "type": "lambda",
        "description": "Body evaluated while the context value is scoped",
        "required": true,
        "mode": "ExecutableLambda",
        "cardinality": "ExactlyOne",
        "role": "LambdaBlock",
        "evaluation": "EvalBlock",
        "projection": "Self"
      }
    },
    "scope": {
      "provides": "context",
      "description": "Creates a named context scope retrievable by [get-context] using the same input value"
    }
  }
}
```

</details>

---

[&larr; `compose`](/reference/slots/core/compose/) | [all core slots](/reference/slots/core/) | [`convert` &rarr;](/reference/slots/core/convert/)


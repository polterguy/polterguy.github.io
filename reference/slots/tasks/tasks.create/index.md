---
title: "[tasks.create]"
description: "tasks.create is a slot in the tasks namespace of Magic Cloud. Saves a named task containing a Hyperlambda body that can later be scheduled or executed on demand."
generated: true
llms: false
slot_json: "/reference/slots/tasks/tasks.create/slot.json"
---

`tasks.create` is a slot in the `tasks` namespace, in Hyperlambda, the language of Magic Cloud. Saves a named task containing a Hyperlambda body that can later be scheduled or executed on demand.

* **Value** (`task-id`), required: Task ID to create

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[.lambda]` | lambda | yes | Task body serialized and executed later. |
| `[description]` | string | no | Optional task description. |
| `[due]` | DateTime | no | Optional one-time due date. |
| `[repeats]` | string | no | Optional repeat pattern. |

### Guide

[How to use `tasks.create`](/plugins/magic.lambda.scheduler/tasks.create/)

### JSON declaration

This is the complete declaration of `tasks.create`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "tasks.create",
  "description": "Saves a named task containing a Hyperlambda body that can later be scheduled or executed on demand",
  "signature": {
    "input": {
      "kind": "task-id",
      "description": "Task ID to create",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "description": {
        "type": "string",
        "kind": "task-description",
        "description": "Optional task description",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      },
      "due": {
        "type": "DateTime",
        "kind": "date",
        "description": "Optional one-time due date",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      },
      "repeats": {
        "type": "string",
        "kind": "task-repeat-pattern",
        "description": "Optional repeat pattern",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      },
      ".lambda": {
        "type": "lambda",
        "description": "Task body serialized and executed later",
        "required": true,
        "mode": "ExecutableLambda",
        "cardinality": "ExactlyOne",
        "role": "LambdaBlock",
        "evaluation": "SerializeLambda",
        "projection": "Children"
      }
    }
  }
}
```

</details>

---

[&larr; `tasks.count`](/reference/slots/tasks/tasks.count/) | [all `tasks.*` slots](/reference/slots/tasks/) | [`tasks.delete` &rarr;](/reference/slots/tasks/tasks.delete/)


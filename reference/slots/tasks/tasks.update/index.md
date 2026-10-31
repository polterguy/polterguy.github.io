---
title: "[tasks.update]"
description: "tasks.update is a slot in the tasks namespace of Magic Cloud. Overwrites a stored task's body or description without altering its existing schedules."
generated: true
llms: false
slot_json: "/reference/slots/tasks/tasks.update/slot.json"
---

`tasks.update` is a slot in the `tasks` namespace, in Hyperlambda, the language of Magic Cloud. Overwrites a stored task's body or description without altering its existing schedules.

* **Value** (`task-id`), optional: Task ID to update

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| `[.lambda]` | lambda | yes | Task body serialized and executed later. |
| `[description]` | string | no | Optional task description. |
| `[due]` | DateTime | no | Optional one-time due date. |
| `[repeats]` | string | no | Optional repeat pattern. |

### JSON declaration

This is the complete declaration of `tasks.update`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "tasks.update",
  "description": "Overwrites a stored task's body or description without altering its existing schedules",
  "signature": {
    "input": {
      "kind": "task-id",
      "description": "Task ID to update",
      "required": false,
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

[&larr; `tasks.schedule.delete`](/reference/slots/tasks/tasks.schedule.delete/) | [all `tasks.*` slots](/reference/slots/tasks/)


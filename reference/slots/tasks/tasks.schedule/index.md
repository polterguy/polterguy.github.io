---
title: "[tasks.schedule]"
description: "tasks.schedule is a slot in the tasks namespace of Magic Cloud. Schedules a stored task for future execution; use [due] for a one-shot run or [repeats] for a recurring pattern."
generated: true
llms: false
slot_json: "/reference/slots/tasks/tasks.schedule/slot.json"
---

`tasks.schedule` is a slot in the `tasks` namespace, in Hyperlambda, the language of Magic Cloud. Schedules a stored task for future execution; use [due] for a one-shot run or [repeats] for a recurring pattern.

* **Value** (`task-id`), optional: Task ID to schedule
* **Returns**: Resolves to the created schedule ID

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| `[due]` | DateTime | no | One-time due date. |
| `[repeats]` | string | no | Repeat pattern. |

### Constraints

* **AtLeastOneOf**: At least one schedule source must be supplied (`[due]`, `[repeats]`)

Guide: [How to use [tasks.schedule]](/plugins/magic.lambda.scheduler/#how-to-use-tasksschedule)

### JSON declaration

This is the complete declaration of `tasks.schedule`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "tasks.schedule",
  "description": "Schedules a stored task for future execution; use [due] for a one-shot run or [repeats] for a recurring pattern",
  "signature": {
    "input": {
      "kind": "task-id",
      "description": "Task ID to schedule",
      "required": false,
      "mode": "ValueOrExpression"
    },
    "children": {
      "due": {
        "type": "DateTime",
        "kind": "date",
        "description": "One-time due date",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      },
      "repeats": {
        "type": "string",
        "kind": "task-repeat-pattern",
        "description": "Repeat pattern",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      }
    },
    "constraints": [
      {
        "description": "At least one schedule source must be supplied",
        "values": [
          "due",
          "repeats"
        ],
        "kind": "AtLeastOneOf"
      }
    ],
    "output": {
      "mode": "Value",
      "kind": "schedule-id,text",
      "description": "Resolves to the created schedule ID"
    }
  }
}
```

</details>

---

[&larr; `tasks.list`](/reference/slots/tasks/tasks.list/) | [all `tasks.*` slots](/reference/slots/tasks/) | [`tasks.schedule.delete` &rarr;](/reference/slots/tasks/tasks.schedule.delete/)


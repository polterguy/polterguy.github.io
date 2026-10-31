---
title: "[tasks.get]"
description: "tasks.get is a slot in the tasks namespace of Magic Cloud. Looks up a single stored task by ID and returns its body, description, and next due date."
generated: true
llms: false
slot_json: "/reference/slots/tasks/tasks.get/slot.json"
---

`tasks.get` is a slot in the `tasks` namespace, in Hyperlambda, the language of Magic Cloud. Looks up a single stored task by ID and returns its body, description, and next due date.

* **Value** (`task-id`), required: Task ID to retrieve
* **Returns**: Resolves to the task fields as child nodes, optionally including a [schedules] node

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| `[schedules]` | bool | no | Whether to include schedules for the task. |

Guide: [How to use [tasks.get]](/plugins/magic.lambda.scheduler/#how-to-use-tasksget)

### JSON declaration

This is the complete declaration of `tasks.get`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "tasks.get",
  "description": "Looks up a single stored task by ID and returns its body, description, and next due date",
  "signature": {
    "input": {
      "kind": "task-id",
      "description": "Task ID to retrieve",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "schedules": {
        "type": "bool",
        "description": "Whether to include schedules for the task",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      }
    },
    "output": {
      "mode": "Lambda",
      "kind": "task,lambda-tree",
      "description": "Resolves to the task fields as child nodes, optionally including a [schedules] node"
    }
  }
}
```

</details>

---

[&larr; `tasks.execute`](/reference/slots/tasks/tasks.execute/) | [all `tasks.*` slots](/reference/slots/tasks/) | [`tasks.list` &rarr;](/reference/slots/tasks/tasks.list/)


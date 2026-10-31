---
title: "[tasks.delete]"
description: "tasks.delete is a slot in the tasks namespace of Magic Cloud. Removes a stored task by ID along with any of its scheduled future runs."
generated: true
llms: false
slot_json: "/reference/slots/tasks/tasks.delete/slot.json"
---

`tasks.delete` is a slot in the `tasks` namespace, in Hyperlambda, the language of Magic Cloud. Removes a stored task by ID along with any of its scheduled future runs.

* **Value** (`task-id`), required: Task ID to delete

### Guide

[How to use `tasks.delete`](/plugins/magic.lambda.scheduler/tasks.delete/)

### JSON declaration

This is the complete declaration of `tasks.delete`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "tasks.delete",
  "description": "Removes a stored task by ID along with any of its scheduled future runs",
  "signature": {
    "input": {
      "kind": "task-id",
      "description": "Task ID to delete",
      "required": true,
      "mode": "ValueOrExpression"
    }
  }
}
```

</details>

---

[&larr; `tasks.create`](/reference/slots/tasks/tasks.create/) | [all `tasks.*` slots](/reference/slots/tasks/) | [`tasks.execute` &rarr;](/reference/slots/tasks/tasks.execute/)


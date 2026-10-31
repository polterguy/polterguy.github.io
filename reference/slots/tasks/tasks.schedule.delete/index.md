---
title: "[tasks.schedule.delete]"
description: "tasks.schedule.delete is a slot in the tasks namespace of Magic Cloud. Cancels a previously-created schedule by ID, leaving the task itself intact."
generated: true
llms: false
slot_json: "/reference/slots/tasks/tasks.schedule.delete/slot.json"
---

`tasks.schedule.delete` is a slot in the `tasks` namespace, in Hyperlambda, the language of Magic Cloud. Cancels a previously-created schedule by ID, leaving the task itself intact.

* **Value** (`schedule-id,integer,number`), required: Schedule ID to delete

### Guide

[How to use `tasks.schedule.delete`](/plugins/magic.lambda.scheduler/tasks.schedule.delete/)

### JSON declaration

This is the complete declaration of `tasks.schedule.delete`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "tasks.schedule.delete",
  "description": "Cancels a previously-created schedule by ID, leaving the task itself intact",
  "signature": {
    "input": {
      "kind": "schedule-id,integer,number",
      "description": "Schedule ID to delete",
      "required": true,
      "mode": "ValueOrExpression"
    }
  }
}
```

</details>

---

[&larr; `tasks.schedule`](/reference/slots/tasks/tasks.schedule/) | [all `tasks.*` slots](/reference/slots/tasks/) | [`tasks.update` &rarr;](/reference/slots/tasks/tasks.update/)


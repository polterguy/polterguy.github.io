---
title: "[tasks.execute]"
description: "tasks.execute is a slot in the tasks namespace of Magic Cloud. Runs a stored task synchronously right now, ignoring its schedule; handy for ad-hoc invocations or testing."
generated: true
llms: false
slot_json: "/reference/slots/tasks/tasks.execute/slot.json"
---

`tasks.execute` is a slot in the `tasks` namespace, in Hyperlambda, the language of Magic Cloud. Runs a stored task synchronously right now, ignoring its schedule; handy for ad-hoc invocations or testing.

* **Value** (`task-id`), optional: Task ID to execute

### Guide

[How to use `tasks.execute`](/plugins/magic.lambda.scheduler/tasks.execute/)

### JSON declaration

This is the complete declaration of `tasks.execute`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "tasks.execute",
  "description": "Runs a stored task synchronously right now, ignoring its schedule; handy for ad-hoc invocations or testing",
  "signature": {
    "input": {
      "kind": "task-id",
      "description": "Task ID to execute",
      "required": false,
      "mode": "ValueOrExpression"
    }
  }
}
```

</details>

---

[&larr; `tasks.delete`](/reference/slots/tasks/tasks.delete/) | [all `tasks.*` slots](/reference/slots/tasks/) | [`tasks.get` &rarr;](/reference/slots/tasks/tasks.get/)


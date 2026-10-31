---
title: "[tasks.execute]"
description: "tasks.execute is a slot in the tasks namespace of Magic Cloud. Runs a stored task synchronously right now, ignoring its schedule; handy for ad-hoc invocations or testing."
generated: true
llms: "guide"
slot_json: "/reference/slots/tasks/tasks.execute/slot.json"
---

`tasks.execute` is a slot in the `tasks` namespace, in Hyperlambda, the language of Magic Cloud. Runs a stored task synchronously right now, ignoring its schedule; handy for ad-hoc invocations or testing.

* **Value** (`task-id`), required: Task ID to execute

### Guide

<!-- guide -->
You can explicitly execute a persisted task by invoking **[tasks.execute]** and pass
in the ID of your task. Below is an example, that assumes you have created the above _"foo-bar-task-4"_ task
first.

```
tasks.execute:foo-bar-task-4
```

Notice, if you try to execute a non-existing task, an exception will be thrown.
<!-- /guide -->

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
      "required": true,
      "mode": "ValueOrExpression"
    }
  }
}
```

</details>

---

[&larr; `tasks.delete`](/reference/slots/tasks/tasks.delete/) | [all `tasks.*` slots](/reference/slots/tasks/) | [`tasks.get` &rarr;](/reference/slots/tasks/tasks.get/)


---
title: "How to use [tasks.delete]"
description: "How to use [tasks.delete] - Use the [tasks.delete] signal to delete a task."
generated: true
guide: true
---

The reference page of [`tasks.delete`](/reference/slots/tasks/tasks.delete/) has its arguments, constraints and declaration.

Use the **[tasks.delete]** signal to delete a task. This will also delete all future schedules for your task and
automatically dispose any timers associated with the task. An example can be found below.

```
tasks.delete:task-id
```

Besides from the task ID, the delete task signal doesn't take any arguments.

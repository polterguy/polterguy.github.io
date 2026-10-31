---
title: "How to use [tasks.get]"
description: "How to use [tasks.get] - To inspect a task you can use the following."
generated: true
guide: true
---

This is the guide to [`tasks.get`](/reference/slots/tasks/tasks.get/), whose reference page has its arguments, constraints and declaration.

To inspect a task you can use the following.

```
tasks.get:task-id
```

The above will return the Hyperlambda for your task, in addition to your task's description. If you add
a **[schedules]** argument and set its value to boolean `true`, this slot will also return all schedules
associated with the task.

```
tasks.get:task-id
   schedules:true
```

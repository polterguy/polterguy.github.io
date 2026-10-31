---
title: "How to use [tasks.update]"
description: "How to use [tasks.update] - This slot replaces the body, and optionally the description, of an existing task, without changing its schedules."
generated: true
guide: true
---

The reference page of [`tasks.update`](/reference/slots/tasks/tasks.update/) has its arguments, constraints and declaration.

This slot replaces the body, and optionally the description, of an existing task, without changing its schedules. Below is an example.

```
tasks.update:foo-bar-task-1
   description:An updated description.
   .lambda
      log.info:Executing the updated foo-bar-task-1
```

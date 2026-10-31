---
title: "How to use [tasks.execute]"
description: "How to use [tasks.execute] - You can explicitly execute a persisted task by invoking [tasks.execute] and pass in the ID of your task."
generated: true
guide: true
---

This is the guide to [`tasks.execute`](/reference/slots/tasks/tasks.execute/), whose reference page has its arguments, constraints and declaration.

You can explicitly execute a persisted task by invoking **[tasks.execute]** and pass
in the ID of your task. Below is an example, that assumes you have created the above _"foo-bar-task-4"_ task
first.

```
tasks.execute:foo-bar-task-4
```

Notice, if you try to execute a non-existing task, an exception will be thrown.

---
title: "How to use [tasks.list]"
description: "How to use [tasks.list] - To list tasks, you can use the [tasks.list] signal."
generated: true
guide: true
---

This is the guide to [`tasks.list`](/reference/slots/tasks/tasks.list/), whose reference page has its arguments, constraints and declaration.

To list tasks, you can use the **[tasks.list]** signal. This slot optionally
handles an **[offset]** and a **[limit]** argument, allowing you to page, which might be
useful if you have a lot of tasks in your system. If no **[limit]** is specified, this signal
will only return the first 10 tasks, including the task's Hyperlambda, but not its repetition
pattern(s), or due date(s). Below is an example.

```
tasks.list
   offset:20
   limit:10
```

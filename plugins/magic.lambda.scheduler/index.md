---
title: magic.lambda.scheduler
moved_anchors: {"how-to-use-taskscreate": "/reference/slots/tasks/tasks.create/#guide", "how-to-use-tasksdelete": "/reference/slots/tasks/tasks.delete/#guide", "how-to-use-tasksexecute": "/reference/slots/tasks/tasks.execute/#guide", "how-to-use-tasksget": "/reference/slots/tasks/tasks.get/#guide", "how-to-use-taskslist": "/reference/slots/tasks/tasks.list/#guide", "how-to-use-tasksschedule": "/reference/slots/tasks/tasks.schedule/#guide"}
---

This project gives you the ability to create persisted and scheduled Hyperlambda tasks
for Magic. More specifically it provides the following slots.

* __[\[tasks.create\]](/reference/slots/tasks/tasks.create/)__ - Creates a new task
* __[\[tasks.get\]](/reference/slots/tasks/tasks.get/)__ - Returns an existing task
* __[\[tasks.list\]](/reference/slots/tasks/tasks.list/)__ - Lists all tasks
* __[\[tasks.update\]](/reference/slots/tasks/tasks.update/)__ - Updates an existing task
* __[\[tasks.count\]](/reference/slots/tasks/tasks.count/)__ - Counts tasks in system
* __[\[tasks.execute\]](/reference/slots/tasks/tasks.execute/)__ - Executes an existing task
* __[\[tasks.delete\]](/reference/slots/tasks/tasks.delete/)__ - Deletes a task
* __[\[tasks.schedule\]](/reference/slots/tasks/tasks.schedule/)__ - Schedules an existing task
* __[\[tasks.schedule.delete\]](/reference/slots/tasks/tasks.schedule.delete/)__ - Deletes an existing schedule
* __[tasks.scheduler.start]__ - Starts the task scheduler


## How Hyperlambda tasks are stored

All tasks are persisted into your `magic` database, either in MySQL, SQLite, PostgreSQL, or Microsoft SQL Server.
This implies that even if your server is stopped, all scheduled tasks and persisted tasks will automatically
load up again, and be available and re-scheduled as the server is restarted. This _might_ imply that
all tasks in the past are immediately executed, which is important for you to understand, since any tasks
with a due date in the past, are executed immediately as the server restarts again.
Tasks are by default persisted into your `tasks` table, and schedules are persisted into your
`task_due` table.


## How to use Hyperlambda tasks as business process workflows

Hyperlambda tasks allows you to persist a _"function invocation"_ for later to execute it, once some specific condition
occurs - Effectively giving you the most important features from Microsoft Workflow Foundation, without the
ridiculous XML and WYSIWYG features - In addition to that this also is a .Net Core library, contrary
to MWF that only works for the full .Net Framework. The Hyperlambda task scheduler is also probably at
least somewhere between 200 and 400 times faster than MWF, due to not using reflection during execution.

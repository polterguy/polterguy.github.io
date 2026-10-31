---
title: magic.lambda.scheduler
moved_anchors: {"how-to-use-taskscount": "/plugins/magic.lambda.scheduler/tasks.count/", "how-to-use-taskscreate": "/plugins/magic.lambda.scheduler/tasks.create/", "how-to-use-tasksdelete": "/plugins/magic.lambda.scheduler/tasks.delete/", "how-to-use-tasksexecute": "/plugins/magic.lambda.scheduler/tasks.execute/", "how-to-use-tasksget": "/plugins/magic.lambda.scheduler/tasks.get/", "how-to-use-taskslist": "/plugins/magic.lambda.scheduler/tasks.list/", "how-to-use-tasksschedule": "/plugins/magic.lambda.scheduler/tasks.schedule/", "how-to-use-tasksscheduledelete": "/plugins/magic.lambda.scheduler/tasks.schedule.delete/", "how-to-use-tasksupdate": "/plugins/magic.lambda.scheduler/tasks.update/"}
---

This project gives you the ability to create persisted and scheduled Hyperlambda tasks
for Magic. More specifically it provides the following slots.

* __[\[tasks.create\]](/plugins/magic.lambda.scheduler/tasks.create/)__ - Creates a new task
* __[\[tasks.get\]](/plugins/magic.lambda.scheduler/tasks.get/)__ - Returns an existing task
* __[\[tasks.list\]](/plugins/magic.lambda.scheduler/tasks.list/)__ - Lists all tasks
* __[\[tasks.update\]](/plugins/magic.lambda.scheduler/tasks.update/)__ - Updates an existing task
* __[\[tasks.count\]](/plugins/magic.lambda.scheduler/tasks.count/)__ - Counts tasks in system
* __[\[tasks.execute\]](/plugins/magic.lambda.scheduler/tasks.execute/)__ - Executes an existing task
* __[\[tasks.delete\]](/plugins/magic.lambda.scheduler/tasks.delete/)__ - Deletes a task
* __[\[tasks.schedule\]](/plugins/magic.lambda.scheduler/tasks.schedule/)__ - Schedules an existing task
* __[\[tasks.schedule.delete\]](/plugins/magic.lambda.scheduler/tasks.schedule.delete/)__ - Deletes an existing schedule
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

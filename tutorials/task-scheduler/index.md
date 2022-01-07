---
title: The Hyperlambda task scheduler
description: This article shows you how to create, persist and schedule Hyperlambda tasks, allowing you to create scheduled Hyperlambda jobs, periodically executing your Hyperlambda, and/or trigger execution of serialised Hyperlambda invocations due to some event.
---

# The Hyperlambda task scheduler

In this tutorial we will cover the following parts of Magic and Hyperlambda.

* How to create and persist tasks
* How to schedule persisted tasks
* How to automate creation of tasks and persist these for future execution

With Magic you can create and administrate tasks, in addition to schedule tasks for execution some point into
the future. This works by persisting dynamically declared Hyperlambda snippets into your Magic database, which
again is just a thin wrapper around your C# slots, allowing you to dynamically orchestrate C# code to be
periodically executed if you wish. Watch the following video where I illustrate this idea.

<div class="video">
<iframe width="560" height="315" style="position:absolute; top:0; left:0; width:100%; height:100%;" src="https://www.youtube.com/embed/tX7WJgPwJxE" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Administrating tasks

In addition to the high level UI parts you can see in the above video, Magic also allows you to automate
the process of both creating tasks, deleting tasks, executing tasks, and administrating tasks and schedules
in general. Combined with the fact that Hyperlambda happens to be a Turing Complete high level programming
language, this also lends itself to business process workflows, and similar ideas, where some function invocation
is dynamically created, persisted into your database, for then to be executed later due to some trigger happening
in another part of your system. In such a way the task scheduler in Magic also replaces Microsoft Workflow
Foundation, with something that's somewhere between 200 to 400 times faster and more scalable than MWF. In addition to that it
consumes about 1/100 of the amount of memory that MWF consumes. And of course the thing is `async` to the bone.
Below you can see some example Hyperlambda you could paste into your tasks to create a dummy task that simply
creates a log entry for you.

## Creating a scheduled task

The following Hyperlambda can be used to create a simple task.

```
/*
 * Log something into the database.
 */
log.info:Your tasks was executed
```

If you create a task with the above Hyperlambda such as illustrated in the following screenshot, and
you schedule your tasks with a `5.seconds` repetition pattern, you can see one new log entry created every
5 seconds.

![Task Scheduler screenshot](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/task-scheduler.jpg)

## Automating your tasks

Magic also allows you to manually administrate your tasks, and automate the administration of tasks,
by exposing an API that allows you to create, read, update, and delete tasks. For instance to create
a task you could use something such as the following.

```
tasks.create:foo-bar-task-1
   .lambda

      /*
       * Your task's lambda object goes here
       */
      log.info:Executing foo-bar-task-1
```

The above creates a task with the ID of _"foo-bar-task-1"_. If you later want to execute your
task, you can do that by invoking **[tasks.execute]** and pass in the ID you gave your task
as you created it. This actually allows you to create and decorate _"function invocations"_, which
are persisted into your database, and later executed according to its ID.

## Internals

Tasks will be persisted into your magic database in the `tasks` table and schedules will be persisted
into your `task_due` table. This implies that
if you take backup of your database, tasks will still exists in your backup, including their Hyperlambda
and next schedule date. When a task is done executing its scheduled execution, its next
schedule time will be calculated. This avoids exhausting your web server due to misconfigured tasks, and/or
flooding the server with tasks your server is not able to execute. To see the complete documentation
for the task scheduler in Magic you can check out the [magic.lambda.scheduler](/documentation/magic.lambda.scheduler/).

* [Continue with Cryptographically signed HTTP invocations](/tutorials/crypto-lambda-http/)

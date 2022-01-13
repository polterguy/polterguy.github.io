---
title: The Hyperlambda task scheduler
description: This article shows you how to create, persist, and schedule Hyperlambda tasks, allowing you to create scheduled Hyperlambda jobs, periodically executing, and/or trigger execution of serialised Hyperlambda invocations due to some event.
---

# The Hyperlambda task scheduler

This tutorial covers the following parts of Magic and Hyperlambda.

* How to create, persist, and execute tasks
* How to schedule persisted tasks
* How to automate creation of tasks, and persist these for future execution
* How these features allows us to easily create long lasting transactions by allowing us to persist function _invocations_

With Hyperlambda you can create and administrate tasks, in addition to scheduling tasks for execution at some point in
the future. This works by persisting dynamically declared Hyperlambda snippets into your Magic database, which
again is just a thin wrapper around your C# slots, allowing you to dynamically orchestrate C# code to be
periodically executed if you wish.

## Administrating tasks

Magic allows you to automate the process of both creating tasks, deleting tasks, executing tasks, and administrating
tasks and schedules.
Combined with the fact that Hyperlambda happens to be a Turing complete high level programming
language, this also lends itself to business process workflows, and similar ideas, where some function invocation
is dynamically created, persisted into your database, for then to be executed later due to some trigger happening
in another part of your system. In such a way the task scheduler in Magic replaces Microsoft Workflow
Foundation, with something that's somewhere between 200 to 400 times faster and more scalable than MWF - In addition to that it
consumes about 1/10th of the memory MWF consumes. Hyperlambda tasks are also `async` to the bone.
Below you can see some example Hyperlambda you can paste into your tasks to create a dummy task that simply
creates a log entry for you. Open your _"Tasks"_ menu item, click the plus button, give your task a name, click your task
to select it for editing, and paste the following into its Hyperlambda editor.

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

To schedule your task for execution every 5 seconds, click the clock icon on your task, and fill out a repetition
pattern such as follows. Make sure you check the _"Repeating"_ checkbox before you provide your repetition pattern.

![Scheduling your tasks](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/scheduling-task.jpg)

If you click the _"Create"_ button and wait 5 seconds for then to have a look at your server's log, you will see
how your task executed after 5 seconds. And if you wait another 5 seconds and refresh your browser, you will see another
log entry created. You can also provide a humanly readable description to your task, making it easier for others
to understand what it does.

## Automating your tasks

Magic also allows you to automagically administrate your tasks, and automate the administration of tasks,
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
task, you can do that by invoking **[tasks.execute]** and pass in the id/name you gave your task
as you created it. This allows you to create and decorate _"function invocations"_, which
are persisted into your database, and later executed according to its id/name, possibly due
to some trigger occurring in a completely different part of your system.

### Workflows

The task scheduler's ability to automate task administration allows you to create, decorate, and persist
a _"function invocation"_, contrary to persisting a function itself, which of course is useful for long lasting transactions,
and having triggers occurring in your system as a response to something else occurring. For instance, imagine a registration
form, where once the user has confirmed his or her email address, some piece of logic should be executed.
An example could be as follows.

1. Update the user's account and set its status to _"verified"_
2. Assign the user to a role granting him or her access to parts of the system only accessible for verified users
3. Send the user a _"welcome as a registered users"_ email

The above could easily be implemented as a dynamic Hyperlambda snippet, persisted as a task, for then
to be triggered as the user clicks the _"Verify your email address"_ link in an email sent to the user
as he filled out his or her email address. Constructs such as the above is often referred to as _"business process workflows"_,
and becomes incredibly useful as your application's complexity increases. For instance, the above idea allows
you to almost completely ignore different versions of your system, eliminating backwards compatibility problems,
simply due to the fact that your tasks are entirely created as Turing Complete Hyperlambda snippets, and
persisted into your database. Implying as you upgrade your system and change its _"API"_, previously
persisted tasks will execute the _"old"_ code as if nothing changed, while anyone creating a task from
that point an onwards, will have the _"new"_ code persisted into the database. Below
is how the above _"business process workflow"_ could be turned into a Hyperlambda task and persisted into
your Hyperlambda tasks database.

```
tasks.create:user.confirm-email.workflow.1147
   .lambda

      signal:users.status.verified
         user-id:1147

      signal:users.add-to-role
         used-id:1147
         role:verified

      signal:emails.send
         template:/etc/foo-module/welcome.html
         email:john@doe.com
         name:John Doe

      // Deleting "self" after a successful invocation.
      tasks.delete:user.confirm-email.workflow.1147
```

When the user verifies his or her email address, you could have code resembling the following being executed.

```
tasks.execute:user.confirm-email.workflow.1147
```

Such business process workflows typically implies having long lasting transactions, executed as a consequence of
triggers raised in completely different systems, and or manually raised triggers, triggering due to human intervention,
allowing you to create _"transactions"_ that might in theory require weeks and months of time before considered
to be _"completed"_.

## Task related slots

The following task related slots exists in Magic.

* __[tasks.count]__ - Counts tasks matching an optional filter
* __[tasks.create]__ - Creates a new task
* __[tasks.delete]__ - Deletes an existing task
* __[tasks.execute]__ - Executes an existing task
* __[tasks.get]__ - Returns an existing task
* __[tasks.list]__ - Lists all tasks optionally matching the specified filter
* __[tasks.update]__ - Updates an existing task
* __[tasks.schedule]__ - Creates a new schedule for an existing task
* __[tasks.schedule.delete]__ - Deletes an existing schedule
* __[tasks.scheduler.start]__ - Starts the task scheduler. Notice, only for internal usage

Refer to the [magic.lambda.scheduler](/documentation/magic.lambda.scheduler/) for information about the above slots.

## Internals

Tasks will be persisted into your magic database in the `tasks` table and schedules will be persisted
into your `task_due` table. This implies that
if you take backup of your database, tasks will still exists in your backup, including their Hyperlambda
and upcoming execution date, if any. When a repeating task is done executing, its next
schedule time will be calculated. This avoids exhausting your web server due to misconfigured tasks, and/or
flooding the server with tasks your server is not able to execute. To see the complete documentation
for the task scheduler in Magic you can check out the [magic.lambda.scheduler](/documentation/magic.lambda.scheduler/).

* Continue with [Cryptographically signed HTTP invocations](/tutorials/crypto-lambda-http/)

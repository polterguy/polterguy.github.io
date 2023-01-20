---
title: Persist and schedule tasks
description: You can easily create Hyperlambda code that you save for later execution, for then to schedule your task to be executed in the future.
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/og-tasks.jpg"
---

# The tasks component

The tasks component allows you to create and administrate persisted Hyperlambda tasks, and/or schedule
tasks for executing, either in a repeating pattern somehow, or at an exact date and time in the future.

![Hyperlambda task scheduler](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/scheduling-task.jpg)

The idea of the task scheduler is first of all to allow for creating dynamically persisted tasks that can be triggered
by some future event, facilitating for _"Business Process Workflows"_ - In addition to scheduling your
tasks to be executed at some specific date and time in the future, and/or in a repeating fashion. Since tasks
are dynamically created Hyperlambda snippets of code, this allows you to dynamically create and orchestrate
_"business process workflows"_ using the task scheduler, in addition to that you have no constraints
in regards to what you want your scheduled tasks can do, contrary to most other task schedulers, that
are built upon statically compiled programming languages.

## Task scheduler internals

The task scheduler will persist your tasks into its Magic's database in the table called _"tasks"_,
in addition to your _"task\_due"_ table for schedules. This implies that even if your server for some
reasons _"drops"_, and/or is rebooted, the tasks will automatically be re-scheduled as your server restarts.

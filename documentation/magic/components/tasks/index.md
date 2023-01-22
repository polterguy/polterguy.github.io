---
title: Persist and schedule tasks
description: You can easily create Hyperlambda code that you save for later execution, for then to schedule your task to be executed in the future.
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/scheduling-task.jpg"
---

# The tasks component

The tasks component allows you to create and administrate persisted Hyperlambda tasks, and/or schedule
tasks for executing, either in a repeating pattern somehow, or at an exact date and time in the future.
A Magic task again, is really nothing but a snippet of Hyperlambda code, that is persisted into
your Magic database, and such can be recalled at any point in the future to be executed at will.

![Hyperlambda task scheduler](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/scheduling-task.jpg)

## The idee behind the task component

The idea behind the task scheduler is first of all to allow for creating dynamically persisted tasks that can be triggered
by some future event, facilitating for _"Business Process Workflows"_ - In addition to scheduling your
tasks to be executed at some specific date and time in the future, and/or in a repeating fashion. Since tasks
are dynamically created Hyperlambda snippets of code, this allows you to dynamically create and orchestrate
_"business process workflows"_ using the task scheduler, in addition to that you have no restrictions
in regards to what you want your scheduled tasks to do, contrary to most other task schedulers, that
are often built upon statically compiled programming languages.

## Tasks internals

Your tasks will be saved into your Magic database and its table called _"tasks"_,
in addition to your _"task\_due"_ table for schedules. This implies that even if your server for some
reasons _"drops"_, and/or is rebooted, your tasks will automatically be re-scheduled as your server restarts.

## Scheduling tasks

Tasks can be scheduled according to a whole range of different patterns. First of all you can schedule
a task to be executed at some specific date and time in the future. This is done by simply choosing
a date and time in the future when you want your task to execute.

![Hyperlambda task scheduler](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/scheduling-tasks.jpg)



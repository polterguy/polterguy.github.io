---
title: Task Manager
description: You can easily create Hyperlambda code that you save for later execution, for then to schedule your task to be executed in the future.
og_image: "/images/scheduling-task.jpg"
header:
  image: /assets/images/wizard-magically-bending-time-and-space.webp
---

The Task Manager component allows you to create and administrate persisted Hyperlambda tasks, and/or schedule
tasks for executing, either in a repeating pattern somehow, or at an exact date and time in the future.
A Magic task is just a snippet of Hyperlambda code, that is persisted into
your Magic database, and such can be recalled at any point in the future to be executed at will.

![Hyperlambda task scheduler](/images/scheduling-task.jpg)

## The idea behind the task component

The idea behind the task scheduler is first of all to allow for creating dynamically persisted tasks that can be triggered
by some future event - In addition to scheduling your
tasks to be executed at some specific date and time in the future, and/or in a repeating pattern. Since tasks
are dynamically created Hyperlambda snippets of code, this makes the system very flexible contrary to most other
task schedulers, that are often built upon statically compiled programming languages.

## Tasks internals

Your tasks will be saved into your Magic database and its table called _"tasks"_,
in addition to your _"task\_due"_ table for schedules. This implies that even if your server for some
reasons _"drops"_, and/or is rebooted, your tasks will automatically be re-scheduled as your server restarts.
Notice, for tasks repeating every nth unit, this process is not 100% perfect, since it might imply
the execution date for your tasks are being moved forward if your server reboots for some reasons.

## Scheduling tasks

Tasks can be scheduled according to a whole range of different patterns. First of all you can schedule
a task to be executed at some specific date and time in the future. This is done by simply choosing
a date and time in the future when you want your task to execute.

![Hyperlambda task scheduler](/images/scheduling-tasks.jpg)

In addition to scheduling a task to be executed at a specific date and time in the future, you
can also schedule your task to be repeated according to some sort of repetition pattern. The simplest
pattern here is _"every n unit"_, where n can be any integer, and unit can be any of seconds, minutes,
hours, days, weeks and months.

Slightly more complex repetition units can be provided by choosing a custom repetition pattern.
There exists two such custom repetition patterns in Magic out of the box, and they are as follows.

* `MM.dd.HH.mm.ss` - Where the entities are in sequence months, days in months, hours, minutes and seconds.
* `ww.HH.mm.ss` - Where the entities are weekdays, hour, minute and second.

Notice, MM, dd, and ww can have double asterix (\*\*) as their values, implying _"whatever value"_.
MM, dd and ww can also have multiple values, separated by the pipe character (|), to provide multiple values
for these types. To for instance create a task that is execute on the 5th and 15th of January and February
you could use a task such as follows; _"01|02.5|15.05.00.00"_. This is because both the day and the month
parts of a monthly repetition value can be piped together declaring multiple months and days, where
the task will be executed at any of the days and months you declare in your repetition value. The same
is true for the weekdays depetition pattern. If you want to create a scheduled task that repeats
every Monday and Friday, you can use a pattern such as follows; _"Monday|Friday.23.59.59"_. This task
will execute one second to midnight both Mondays and Fridays.

To understand which repetition pattern is which, simply count the number of periods in your value,
and if there are 4 periods, it's a month/day type of pattern. If there are only 3 periods in your
pattern, it's a weekday pattern.

To understand tasks more in details, you can read read about the [magic.lambda.scheduler](/plugins/magic.lambda.scheduler/).



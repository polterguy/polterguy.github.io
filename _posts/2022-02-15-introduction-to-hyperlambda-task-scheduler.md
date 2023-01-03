---
layout: post
author: thomas
title: An introduction to the Hyperlambda Task Scheduler
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/scheduling-task.jpg"
description: Magic's Hyperlambda Task Scheduler allows you to dynamically create Hyperlambda tasks and schedule your Hyperlambda for future execution.
canonical_url: https://aista.com/blog/introduction-to-hyperlambda-task-scheduler/
---

One of my favourite features with Magic is how easy it is to create and administrate scheduled tasks in the system.
Create a new task, add some Hyperlambda to it, and schedule it to execute at whatever interval you need for it
to execute. Below is a screenshot of Magic's task scheduler to give you an idea.

![Scheduling your task](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/scheduling-task.jpg)

The simplest task you can possibly create is probably something resembling the following.

```
/*
 * Task Hyperlambda.
 */
log.info:Your task was executed
```

If you use Magic's task scheduler to create a new task, give your task a name, paste in the above Hyperlambda
into your code editor, for then to schedule the task to execute every 5 seconds as illustrated in the above
screenshot - You will see log entries being created every 5 seconds. Make sure you click the _"Repeating"_
checkbox before you apply your repetition pattern of `5.seconds`.

The idea of Magic's task scheduler of course is that as developers we often have tasks that needs to be
executed periodically for some reasons. This might include syndicating some other data source, massaging
its result, creating aggregated results, and storing the result locally in our own database for some reasons.
This exact use case is easily achieved using the HTTP slots in Magic, such as illustrated below.

```
http.get:"https://docs.aista.com"
```

If you execute the above Hyperlambda in your _"Evaluator"_ menu item, you'll see how Magic retrieves
the HTML for our documentation landing page. A more relevant use case of course would probably imply
invoking some API returning JSON of some sort, for then to massage the JSON, and put it into some
temporary storage of some sort - But that's an exercise for later.

## Performance

Magic's task scheduler allows you to create literally thousands of such scheduled tasks due to how
it schedules your tasks for execution. This makes it almost impossible for you to create tasks that
exhausts your server. The Hyperlambda below for instance creates 5,000 tasks for you, and schedules
your tasks to execute every 120 seconds. Not only is Magic able to create 5,000 tasks and persist
these into your database without choking in some few seconds, it is also able to schedule and execute
all 5,000 tasks without making your server beg for mercy due to being exhausted of resources.

```
/*
 * Creating 5,000 scheduled tasks and executing all tasks every 2 minutes.
 */
.no:int:1
while
   lt
      get-value:x:@.no
      .:int:5000
   .lambda

      // Making sure we get a unique name for our task.
      guid.new
      convert:x:-
         type:string

      // Creating our task.
      tasks.create:x:@convert
         repeats:120.seconds
         .lambda

            // Task's Hyperlambda
            log.info:Scheduled task executed

      // Incrementing while loop counter.
      math.increment:x:@.no
```

If you execute the above Hyperlambda and wait for a couple of minutes, you'll see your log starting to fill
up with log entries. Below is a screenshot.

![Log showing 5,000 tasks executing](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/blogs/thousands-of-tasks.jpg)

Notice, even though Magic can easily execute 5,000 background tasks in parallel, you might want to delete
your tasks now, by executing the following Hyperlambda. If you don't delete your tasks now, your development
machine will inevitably run out of hard disc space after a while due to your log database filling up your
computer's hard disc. Execute the following Hyperlambda in your _"Evaluator"_ component to delete all your tasks.

```
// Listing all 5,000 tasks.
tasks.list
   limit:5000

// Looping through all tasks and deleting them.
for-each:x:-/*/*/id
   tasks.delete:x:@.dp/#
```

## Business process workflows

As you've probably realised by now, due to that tasks can be automatically created, persisted, and executed,
your Hyperlambda tasks lends themselves to what is often referred to as _"Business Process Workflows"_,
implying long transactions, and dynamically persisted _"function invocations"_. An example might
be a registration form where once the user registers, you want some task to execute as he or she is
verifying their email address, such as enabling his or her account, etc. During the registration
process you can easily dynamically create and persist the task that enables the account, but wait
until the user actually confirms his or her email address before you execute your task. Above of course
is an example of how to dynamically create tasks, but dynamically executing tasks is just
as easy by using the **[tasks.execute]** slot that allows you to execute a specific task by
name. If you want to read more about this you can read the [following article](/tutorials/task-scheduler/)
that describes the idea in some more details. You might also benefit from reading
the [reference documentation](/documentation/magic.lambda.scheduler/) for Magic's task scheduler.

## Internals

Magic actually stores your tasks into your MySQL/PostgreSQL/SQL Server database. This is possible because
Hyperlambda is fundamentally plain text, allowing you to persist Hyperlambda into anything capable of
handling text. If you open up your SQL dashboard item and execute the following SQL you can
actually see how your task is persisted. Make sure you select the `magic` database before executing the
following SQL.

```sql
select * from tasks
```

Below is a screenshot showing one task, and its associated Hyperlambda.

![How tasks are persisted](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/blogs/sql-task.jpg)

This implies among other things that if your server drops or is restarted for some reasons, both your
tasks and schedules will automatically reload and come back up again as you start your server again.
In the video below you can see me demonstrate the task scheduler.

<div class="video">
<iframe width="560" height="315" style="position:absolute; top:0; left:0; width:100%; height:100%;" src="https://www.youtube.com/embed/60le6DVMmZw" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

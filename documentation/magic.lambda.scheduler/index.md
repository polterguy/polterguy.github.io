
# Magic Lambda Scheduler

This project provides the ability to create persisted, and/or scheduled Hyperlambda tasks,
for [Magic](https://github.com/polterguy.magic). More specifically it provides the following slots.

* __[tasks.create]__ - Creates a new task.
* __[tasks.get]__ - Returns an existing task.
* __[tasks.list]__ - Lists all tasks.
* __[tasks.execute]__ - Executes an existing task.
* __[tasks.delete]__ - Deletes a task.
* __[scheduler.stop]__ - Stops the scheduler, implying no tasks will be executed at their scheduled time.
* __[scheduler.start]__ - Starts the scheduler, if there are any upcoming scheduled tasks.
* __[scheduler.next]__ - Returns the date and time of the next scheduled task, if any.
* __[scheduler.running]__ - Returns true if the scheduler is running.

## Creating a task

To create a task without an execution date and no repetition pattern, you can use something such as the following.

```
tasks.create:foo-bar-task-1
   .lambda

      /*
       * Your task's lambda object goes here
       */
      log.info:Executing foo-bar-task-1
```

The name or ID of your task in the above example becomes _"foo-bar-task-1"_, and the task can be referenced later
using this name. The name must be unique, otherwise any previously created tasks with the same name will be silently
overwritten. A task can also optionally have a **[description]** argument, which is a humanly friendly written
description, describing what your task does. Below is an example.

```
tasks.create:foo-bar-task-2
   description:This task will do a little bit of foo and some bar afterwards.
   .lambda
      log.info:Executing foo-bar-task-2
```

**Notice** - Your task's **[id]** argument, can only contain alpha numeric characters, 
a-z, 0-9 - In addition to the special characters `.`, `-` and `_`.

## Executing a task

You can explicitly execute a persisted task at will by invoking **[tasks.execute]**, and passing
in the ID of your task. Below is an example, that assumes you have created the above _"foo-bar-task-1"_ task
first.

```
tasks.execute:foo-bar-task-1
```

**Notice** - This slot does _not_ synchronize access to your tasks, such as when executing a scheduled task
at its scheduled date does. This allows you to have multiple tasks executed simultaneously, contrary to a
scheduled task that will never be executed simultaneously as another scheduled task is executing.

## Workflows and Magic Tasks

The above allows you to persist a _"function invocation"_ for later to execute it, once some specified condition
occurs - Effectively giving you the most important features from Microsoft Workflow Foundation, without the
ridiculous XML and WYSIWYG parts from MWF - In addition to that this also is a .Net Core library, contrary
to MWF.

This allows you to create and persist a function _invocation_, for then to later execute it, as some condition occurs,
arguably giving you _"workflow capabilities"_ in your projects.

**Notice** - By creating your own `ISlot` implementation, you can easily create your own C# classes that are Magic
Signals, allowing you to persist an invocation to your method/class - For then to later execute this method as some
condition occurs. Refer to the [documentation for Magic Lambda](https://github.com/polterguy/magic.lambda) to see how this
is done, and more specifically the _"Extending Hyperlambda"_ section.

## Scheduled tasks

If you want to create a _scheduled_ task, you can choose to have the task execute once in the future, at a specified
date and time, by applying a **[due]** argument.

```
tasks.create:foo-bar-task-3
   due:date:"2020-12-24T17:00"
   .lambda
      log.info:Executing foo-bar-task-3
```

The above **[due]** argument is a UTC date and time in the future for when you want your task to be scheduled
for execution. After the task has been executed, it will never execute again, unless you manually execute it,
or assign a **[repeats]** pattern to it by invoking the slot that schedules existing tasks.

**Notice** - You _cannot_ create a task with a due date being in the past, and all dates are assumed to be in
the UTC timezone.

### Repeating tasks

There are 3 basic **[repeats]** patterns for the Magic Lambda Scheduler, in addition to that you can extend
it with your own parametrized repeating `IPattern` implementation. The built in repetition patterns,
are as follows.

* `x.units` - Units can be one of _"seconds"_, _"minutes"_, _"hours"_, _"days"_, _"weeks"_ or _"months"_ - And
`x` can be any integer value.
* `MM.dd.HH.mm.ss` - Where the entities are in sequence months, days in months, hour, minute and second.
* `ww.HH.mm.ss` - Where the entities are weekdays, hour, minute and second.

Notice, MM, dd, and ww can have double asterix (\*\*) as their values, implying _"whatever value"_.
MM, dd and ww can also have multiple values, separated by the pipe character (|), to provide multiple values
for these types. See examples of this further below in this documentation.

### Intervals

Evaluating your task every second/minute/hour/etc can be done by using something such as the following.

```
tasks.create:task-id
   repeats:50.seconds
   .lambda
      log.info:Executing repeating task
```

The above will evaluate your task every 50 second. The above _"seconds"_ can be exchanged with _"minutes"_, _"hours"_, _"days"_, _"weeks"_ or _"months"_. Notice, this allows you to have very large values, to have tasks that are
repeating _very rarely_, such as the following illustrates.

```
tasks.create:task-id
   repeats:3650.days
   .lambda
      log.info:Executing seldomly repeating task once every 10 year
```

The above task will only be evaluated every 3650 days, which becomes once every 10 years. Below is a list of
all valid units types.

* seconds
* minutes
* hours
* days
* weeks
* months

### Periodically scheduled tasks

To create a task that is executed on the first day of _every_ month, at 5PM, you can use the following
repetition pattern.

```
tasks.create:task-id
   repeats:**.01.05.00.00
   .lambda
      log.info:It is the 1st of the month, any month, and the time is 5AM at night.
```

Hours must be supplied as _"military hours"_, implying from 00:00 to 23:59, where for instance 22 equals 10PM UTC time.
Also notice how we provided a double asterix (\*\*) for the month parts, implying _"any month"_. We could also have provided
multiple days, and/or months, such as the following illustrates. The Hyperlambda below will create a task that is executed
in January and February, but only on the 5th and 15th of these months.

```
tasks.create:task-id
   repeats:01|02.5|15.05.00.00
   .lambda
      log.info:It is the 5th or the 15th of January or February, and the time is 5AM at night.
```

By using the double asterix for month and day of month, you can create a task that is executed _every_ day, at
some specific time of the day (UTC time). Below is an example.

```
tasks.create:task-id
   repeats:**.**.22.00.00
   .lambda
      log.info:It is the 10PM now.
```

### Weekdays pattern

If you use the weekdays pattern, you can create any combinations of weekdays, allowing you to supply multiple
weekdays in a single repetition pattern. Below is an exhaustive list of all possible weekdays.

* Monday
* Tuesday
* Wednesday
* Thursday
* Friday
* Saturday
* Sunday

To evaluate a task every Saturday and Sunday for instance, you can use `saturday|sunday` as your weekday.
Below is an example. Notice, weekdays are case insensitive.

```
tasks.create:task-id
   repeats:saturday|SUNDAY.22.00.00
   .lambda
      log.info:It is Saturday or Sunday, and the time is 22PM.
```

You can also provide a double asterix (\*\*) for the weekdays pattern, implying _"all days of the week"_.

### Creating your own repetition patter

In addition to the above 3 types of repetition patterns, you can also create your own repetition pattern type,
by implementing the `IPattern` interface on one of your own types, and registering your type create function
by using the `PatternFactory.AddExtensionPattern` method. If you do, you'll have to reference your repetition
pattern type using _"ext:"_, combined with its resolver key. Implying if you register your `IPattern` type such
that it resolves using for instance _"my-pattern"_ as its key, you'll have to use _"ext:my-pattern:args"
to reference it later, as you wish to create an instance of your custom pattern type. The _"args"_ part
are any arguments supplied to your pattern during creation. Below is an example that creates a custom
repetition pattern.

```csharp
private class ExtPattern : IPattern
{
    readonly string _args;
    public string Value => "ext:custom-pattern:" + _args;

    public ExtPattern(string args)
    {
        _args = args;
    }

    public DateTime Next()
    {
        return new DateTime(2030, 11, 11, 11, 11, 57);
    }
}
```

Of course, the above `IPattern` will statically resolve to the 11th of November 2030, at 23:11:57. But
the idea is that the `args` supplied during creation, can be used to parametrize your pattern, and
calculate the next due date for your schedule.

After you have declared your custom `IPattern` type, you'll need to inform the `PatternFactory` class
that you want to use the above class, and resolve it using some specific key from your schedules.
This is accomplished using something resembling the following code.

```csharp
PatternFactory.AddExtensionPattern(
    "custom-type",
    str =>
    {
        return new ExtPattern(str);
    });
```

The above code will ensure that every time you use _"custom-type"_ as a repetition pattern type,
the create function above will be invoked, allowing you to create and decorate an instance of your
custom `IPattern` type. The `str` argument to your above create function, will be everything
after the `ext:custom-type:` parts, when creating an instance of your pattern.

To use the above pattern in your own code, you can use something such as the following.

```
tasks.create:custom-repetition-pattern
   repeats:"ext:custom-pattern:some-arguments-here"
   .lambda
      log.info:Executing custom-repetition-pattern
```

In the above **[repeat]** argument, the `ext` parts informs the scheduler that you want to use a
custom repetition pattern, the `custom-pattern` parts resolves to your `IPattern` create function,
and the _"some-arguments-here"_ parts will be passed into your above `ExtPattern` constructor.

### Internals

A background thread will be used for executing scheduled tasks, and only _one_ background thread - Which implies
that no tasks will ever be executing in parallel, to avoid thread starvation, due to logical errors in your schedules.
All tasks are executed asynchronously, implying the execution thread will be released back to the operating system,
as the thread is waiting for IO data, from socket connections, etc - Assuming you use the async slots where relevant.

When a repeating task has finished executed, the next due date for the task's execution will be calculated using
its interval pattern - Implying that if you use a 5 second pattern, the schedule for its next execution, will be
calculated 5 seconds from when the task _finished_ executing, which might not necessarily imply that your tasks
are executed exactly every 5 seconds, depending upon how much time your task requires to execute. The interval
pattern declares how many units to count to before executing the task again, from when the task _finished_ executing.

## Deleting a task

Use the **[tasks.delete]** signal to delete a task. This will also delete all future schedules for your task.
An example can be found below.

```
tasks.delete:task-id
```

Besides from the task ID, the delete task signal doesn't take any arguments.

## Inspecting a task

To inspect a task you can use the following.

```
tasks.get:task-id
```

Besides from the task ID, the get task slot doesn't take any arguments. Using this signal, will return the
task's due date(s) in addition to the task itself.

## Listing tasks

To list tasks, you can use the **[tasks.list]** signal. This slot optionally
handles an **[offset]** and a **[limit]** argument, allowing you to page, which might be
useful if you have a lot of tasks in your system. If no **[limit]** is specified, this signal
will only return the first 10 tasks, including the task's Hyperlambda, but not its repetition
pattern, or due date. Below is an example.

```
tasks.list
   offset:20
   limit:10
```

## Miscelaneous slots

The **[scheduler.stop]** will stop the scheduler, meaning no repeating tasks or tasks with a due date in
the future will execute. Notice, if you create a new task with a due date, and/or a repetition pattern,
the scheduler will automatically start again. When you start the scheduler again, using for
instance **[scheduler.start]**, all tasks will automatically resume, and tasks that have due dates in
the past, will immediately start executing.

To determine if the task scheduler is running or not, you can invoke **[scheduler.running]**, which will
return `true` if the scheduler is running. Notice, if you have no scheduled tasks, it will always
return false. And regardless of whether or not the scheduler is running or not, you can always explicitly
execute a task by using **[tasks.execute]**.

To return the date and time for the next scheduled task, you can raise the **[scheduler.next]** signal.

## Persisting tasks

All tasks are persisted into your selected database type of choice, either MySQL or Microsoft SQL Server.
Which implies that even if the server is stopped, all scheduled tasks and normal tasks will automatically
load up again, and be available to the scheduler as the server is restarted. This _might_ imply that
all tasks in the past are immediately executed, which is important for you to understand.

Tasks are by default persisted into your `magic.tasks` table, and schedules are persisted into your
`magic.task_due` table.

## Quality gates

- [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.scheduler&metric=alert_status)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.scheduler)
- [![Bugs](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.scheduler&metric=bugs)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.scheduler)
- [![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.scheduler&metric=code_smells)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.scheduler)
- [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.scheduler&metric=coverage)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.scheduler)
- [![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.scheduler&metric=duplicated_lines_density)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.scheduler)
- [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.scheduler&metric=ncloc)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.scheduler)
- [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.scheduler&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.scheduler)
- [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.scheduler&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.scheduler)
- [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.scheduler&metric=security_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.scheduler)
- [![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.scheduler&metric=sqale_index)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.scheduler)
- [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.scheduler&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.scheduler)

## License

This project is the copyright(c) 2020-2021 of Thomas Hansen thomas@servergardens.com, and is licensed under the terms
of the LGPL version 3, as published by the Free Software Foundation. See the enclosed LICENSE file for details.

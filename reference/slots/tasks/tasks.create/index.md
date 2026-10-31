---
title: "[tasks.create]"
description: "tasks.create is a slot in the tasks namespace of Magic Cloud. Saves a named task containing a Hyperlambda body that can later be scheduled or executed on demand."
generated: true
llms: "guide"
slot_json: "/reference/slots/tasks/tasks.create/slot.json"
---

`tasks.create` is a slot in the `tasks` namespace, in Hyperlambda, the language of Magic Cloud. Saves a named task containing a Hyperlambda body that can later be scheduled or executed on demand.

* **Value** (`task-id`), required: Task ID to create

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[.lambda]` | lambda | yes | Task body serialized and executed later. |
| `[description]` | string | no | Optional task description. |
| `[due]` | DateTime | no | Optional one-time due date. |
| `[repeats]` | string | no | Optional repeat pattern. |

### Guide

<!-- guide -->
To create and persist a task you can use something such as the following.

```
tasks.create:foo-bar-task-1
   .lambda

      // Your task's lambda object goes here
      log.info:Executing foo-bar-task-1
```

The name or ID of your task in the above example becomes _"foo-bar-task-1"_, and the task can be referenced later
using this name. The name must be unique, otherwise an exception will be thrown. A task can also optionally have
a **[description]** argument, which is a humanly readable description, describing what your task does. Below is
an example.

```
tasks.create:foo-bar-task-2
   description:This task will do a little bit of foo and some bar afterwards.
   .lambda

      log.info:Executing foo-bar-task-2
```

**Notice** - Your task's **[id]** argument, can only contain alpha numeric characters, 
a-z, 0-9 - In addition to the following special characters; `.`, `-` and `_`.
When you create a task, you can also optionally schedule it simultaneously, by providing any amount of **[due]**
dates, and/or **[repeats]** patterns, which will create and schedule the task at the same time. Below is an example.

```
tasks.create:foo-bar-task-3
   due:date:"2025-01-01T23:59:27"
   repeats:5.seconds
   repeats:3.hours
   due:date:"2030-01-01T23:59:27"
   .lambda

      log.info:Executing foo-bar-task-2
```

The above schedules your task for being executed once in the year of 2025, another time in the year of 2030,
in addition to once every 3 hours and once every 5 seconds. This document will describe in details how schedules
works further down.

You can also _update_ an existing task by using the **[\[tasks.update\]](/reference/slots/tasks/tasks.update/)** slot. This slot allows you to update
a task's description and its Hyperlambda, but you _cannot_ associate schedules with your task using this
slot. If you've already created your task and you need to (re) schedule it, you'll need to combine the
slots **[\[tasks.schedule\]](/reference/slots/tasks/tasks.schedule/)** and **[\[tasks.schedule.delete\]](/reference/slots/tasks/tasks.schedule.delete/)** together. Below is an example of first creating
a task for then to update it. Any existing schedules you've already associated with your task as you update
it will not be changed.

```
tasks.create:foo-bar-task-4
   .lambda

      log.info:Executing foo-bar-task-1

tasks.update:foo-bar-task-4
   description:This is the foo bar task
   .lambda

      log.info:Another log entry now!
```
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.scheduler](/plugins/magic.lambda.scheduler/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `tasks.create`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "tasks.create",
  "description": "Saves a named task containing a Hyperlambda body that can later be scheduled or executed on demand",
  "signature": {
    "input": {
      "kind": "task-id",
      "description": "Task ID to create",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "description": {
        "type": "string",
        "kind": "task-description",
        "description": "Optional task description",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      },
      "due": {
        "type": "DateTime",
        "kind": "date",
        "description": "Optional one-time due date",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      },
      "repeats": {
        "type": "string",
        "kind": "task-repeat-pattern",
        "description": "Optional repeat pattern",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      },
      ".lambda": {
        "type": "lambda",
        "description": "Task body serialized and executed later",
        "required": true,
        "mode": "ExecutableLambda",
        "cardinality": "ExactlyOne",
        "role": "LambdaBlock",
        "evaluation": "SerializeLambda",
        "projection": "Children"
      }
    }
  }
}
```

</details>

---

[&larr; `tasks.count`](/reference/slots/tasks/tasks.count/) | [all `tasks.*` slots](/reference/slots/tasks/) | [`tasks.delete` &rarr;](/reference/slots/tasks/tasks.delete/)


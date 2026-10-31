---
title: magic.lambda.scheduler slot reference
description: Every slot in magic.lambda.scheduler with its value, arguments and return value, generated from the source code.
generated: true
---

_This page is generated from the `[Slot]` attributes in the source code of [magic.lambda.scheduler](https://github.com/polterguy/magic/tree/master/plugins/magic.lambda.scheduler). Do not edit it; improve the attribute instead. The hand-written guide is at [magic.lambda.scheduler](/plugins/magic.lambda.scheduler/)._

## [tasks.count]

Counts scheduled tasks.

* **Value** (`task-id`), optional: Optional filter for task IDs
* **Returns**: Resolves to the number of scheduled tasks matching the optional filter

## [tasks.create]

Saves a named task containing a Hyperlambda body that can later be scheduled or executed on demand.

* **Value** (`task-id`), required: Task ID to create

| Argument | Type | Required | Description |
|---|---|---|---|
| `[description]` | string | no | Optional task description |
| `[due]` | DateTime | no | Optional one-time due date |
| `[repeats]` | string | no | Optional repeat pattern |

| Returned node | Type | Description |
|---|---|---|
| `[.lambda]` | lambda | Task body serialized and executed later |

Guide: [How to use [tasks.create]](/plugins/magic.lambda.scheduler/#how-to-use-taskscreate)

## [tasks.delete]

Removes a stored task by ID along with any of its scheduled future runs.

* **Value** (`task-id`), required: Task ID to delete

Guide: [How to use [tasks.delete]](/plugins/magic.lambda.scheduler/#how-to-use-tasksdelete)

## [tasks.execute]

Runs a stored task synchronously right now, ignoring its schedule; handy for ad-hoc invocations or testing.

* **Value** (`task-id`), required: Task ID to execute

Guide: [How to use [tasks.execute]](/plugins/magic.lambda.scheduler/#how-to-use-tasksexecute)

## [tasks.get]

Looks up a single stored task by ID and returns its body, description, and next due date.

* **Value** (`task-id`), required: Task ID to retrieve
* **Returns**: Resolves to the task fields as child nodes, optionally including a [schedules] node

| Argument | Type | Required | Description |
|---|---|---|---|
| `[schedules]` | bool | no | Whether to include schedules for the task |

| Returned node | Type | Description |
|---|---|---|
| `[.lambda]` | lambda | Task body serialized and executed later |

Guide: [How to use [tasks.get]](/plugins/magic.lambda.scheduler/#how-to-use-tasksget)

## [tasks.list]

Returns all stored tasks; supports an optional ID filter and pagination via [limit] and [offset].

* **Value** (`task-id`), optional: Optional filter for task IDs
* **Returns**: Returns one child node per task with its task metadata

| Argument | Type | Required | Description |
|---|---|---|---|
| `[offset]` | long | no | Number of tasks to skip |
| `[limit]` | long | no | Maximum number of tasks to return |

| Returned node | Type | Description |
|---|---|---|
| `[.]` | lambda | One task record returned by [tasks.list] |

Guide: [How to use [tasks.list]](/plugins/magic.lambda.scheduler/#how-to-use-taskslist)

## [tasks.schedule]

Schedules a stored task for future execution; use [due] for a one-shot run or [repeats] for a recurring pattern.

* **Value** (`task-id`), optional: Task ID to schedule
* **Returns**: Resolves to the created schedule ID

| Argument | Type | Required | Description |
|---|---|---|---|
| `[due]` | DateTime | no | One-time due date |
| `[repeats]` | string | no | Repeat pattern |

| Returned node | Type | Description |
|---|---|---|
| `[.lambda]` | lambda | Task body serialized and executed later |

Guide: [How to use [tasks.schedule]](/plugins/magic.lambda.scheduler/#how-to-use-tasksschedule)

## [tasks.schedule.delete]

Cancels a previously-created schedule by ID, leaving the task itself intact.

* **Value** (`schedule-id,integer,number`), required: Schedule ID to delete

## [tasks.update]

Overwrites a stored task's body or description without altering its existing schedules.

* **Value** (`task-id`), optional: Task ID to update

| Argument | Type | Required | Description |
|---|---|---|---|
| `[description]` | string | no | Optional task description |
| `[due]` | DateTime | no | Optional one-time due date |
| `[repeats]` | string | no | Optional repeat pattern |

| Returned node | Type | Description |
|---|---|---|
| `[.lambda]` | lambda | Task body serialized and executed later |


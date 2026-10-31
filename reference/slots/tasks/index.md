---
title: "tasks.* slots"
description: "The 9 slots named tasks.* in Magic Cloud and Hyperlambda, each with its own page."
generated: true
---

9 slots, each with its own page and JSON declaration. See [how this reference is built](/reference/slots/).

| Slot | Description |
|---|---|
| [`tasks.count`](/reference/slots/tasks/tasks.count/) | Counts scheduled tasks. |
| [`tasks.create`](/reference/slots/tasks/tasks.create/) | Saves a named task containing a Hyperlambda body that can later be scheduled or executed on demand. |
| [`tasks.delete`](/reference/slots/tasks/tasks.delete/) | Removes a stored task by ID along with any of its scheduled future runs. |
| [`tasks.execute`](/reference/slots/tasks/tasks.execute/) | Runs a stored task synchronously right now, ignoring its schedule; handy for ad-hoc invocations or testing. |
| [`tasks.get`](/reference/slots/tasks/tasks.get/) | Looks up a single stored task by ID and returns its body, description, and next due date. |
| [`tasks.list`](/reference/slots/tasks/tasks.list/) | Returns all stored tasks; supports an optional ID filter and pagination via [limit] and [offset]. |
| [`tasks.schedule`](/reference/slots/tasks/tasks.schedule/) | Schedules a stored task for future execution; use [due] for a one-shot run or [repeats] for a recurring pattern. |
| [`tasks.schedule.delete`](/reference/slots/tasks/tasks.schedule.delete/) | Cancels a previously-created schedule by ID, leaving the task itself intact. |
| [`tasks.update`](/reference/slots/tasks/tasks.update/) | Overwrites a stored task's body or description without altering its existing schedules. |


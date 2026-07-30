---
title: Task endpoints
description: Magic's built-in task endpoints, creating, updating, deleting, scheduling and listing background tasks.
header:
  image: /assets/images/hero/endpoints-top.png
  og_image: /assets/images/hero/endpoints-top-og.png
  image_description: Task endpoints
---

## Task related endpoints

These are endpoints related to administrating tasks, and/or due dates for executing tasks. To understand the
task scheduler and how it works please refer to the [Task Manager](/dashboard/task-manager/).

### GET magic/system/tasks/list

This endpoint returns a list of all your tasks, optionally matching the specified query parameters.

* __[offset]__ - Offset of where to start returning tasks
* __[limit]__ - Maximum number of tasks to return
* __[filter]__ - Filter parameter the task must match

All the above arguments are optional, and the endpoint can only be invoked by a root user.
This endpoint is not intended for you to consume in your own code.

### GET magic/system/tasks/get

This endpoint returns the declaration for the specified **[name]** task, where name is the ID or name
of your task. This endpoint can only be invoked by a root user, and it requires the following query argument(s).

* __[name]__ - Name or id of task to return

This endpoint is not intended for you to consume in your own code.

### GET magic/system/tasks/count

Returns the number of tasks in your system, optionally matching the specified **[filter]** filtering argument.
This endpoint can only be invoked by a root user. The endpoint requires the following argument(s).

* __[filter]__ - Optional filter criteria that must be found in the task's description or id for the task to be considered a match

This endpoint is not intended for you to consume in your own code.

### POST magic/system/tasks/create

This endpoint creates a new task in your backend. The endpoint requires the following payload.

```
{
  "id": "foo",
  "description": "foo",
  "hyperlambda": "foo"
}
```

The above arguments imply the following.

* __[id]__ - ID or name of task. Must be unique and non-existing
* __[description]__ - Humanly readable description of your task. Optional
* __[hyperlambda]__ - Actual Hyperlambda to be associated with your task

This endpoint can only be invoked by a root user.
This endpoint is not intended for you to consume in your own code.

### POST magic/system/tasks/update

This endpoint updates an existing task, and requires the following payload.

```
{
  "id": "foo",
  "description": "foo",
  "hyperlambda": "foo"
}
```

The above arguments are the same as when creating a new task and imply the following.

* __[id]__ - The id or name of the task you want to update
* __[description]__ - The new description of the task
* __[hyperlambda]__ - The new Hyperlambda associated with your task

This endpoint is not intended for you to consume in your own code.

### DELETE magic/system/tasks/delete

This endpoint deletes a previously persisted task with the specified **[id]**. This endpoint
can only be invoked by a root user. The endpoint requires the following query argument(s).

* __[id]__ - Id of task to delete

This endpoint is not intended for you to consume in your own code.

### POST magic/system/tasks/due/add

This endpoint adds a due date, or a repetition pattern, to a previously persisted task. It requires
the following payload.

```
{
  "id": "foo",
  "due": "2022-01-31T11:16:09.492Z",
  "repeats": "foo"
}
```

The above arguments imply the following.

* __[id]__ - ID or name of task you want to associate your schedule with
* __[due]__ - A date and time for when you want to execute the task. Mutually exclusive with the **[repeats]** argument
* __[repeats]__ - A repetition value for the task. Mutually exclusive with the **[due]** argument

To understand how the **[repeats]** works see the documentation
for [magic.lambda.scheduler](/plugins/magic.lambda.scheduler/). This endpoint can only be invoked by a root user.

This endpoint is not intended for you to consume in your own code.

### DELETE magic/system/tasks/due/delete

This endpoint deletes the specified **[id]** due/repeats instance in your backend. This endpoint can
only be invoked by a root user. The endpoint requires the following query argument(s).

* __[id]__ - Id of due date object to delete

This endpoint is not intended for you to consume in your own code.

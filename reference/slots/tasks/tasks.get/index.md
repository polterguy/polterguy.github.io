---
title: "[tasks.get]"
description: "tasks.get is a slot in the tasks namespace of Magic Cloud. Looks up a single stored task by ID and returns its body, description, and next due date."
generated: true
llms: "guide"
slot_json: "/reference/slots/tasks/tasks.get/slot.json"
---

`tasks.get` is a slot in the `tasks` namespace, in Hyperlambda, the language of Magic Cloud. Looks up a single stored task by ID and returns its body, description, and next due date.

* **Value** (`task-id`), required: Task ID to retrieve
* **Returns**: Resolves to the task fields as child nodes, optionally including a [schedules] node

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[schedules]` | bool | no | Whether to include schedules for the task. |

### Guide

<!-- guide -->
To inspect a task you can use the following.

```
tasks.get:task-id
```

The above will return the Hyperlambda for your task, in addition to your task's description. If you add
a **[schedules]** argument and set its value to boolean `true`, this slot will also return all schedules
associated with the task.

```
tasks.get:task-id
   schedules:true
```
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.scheduler](/plugins/magic.lambda.scheduler/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `tasks.get`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "tasks.get",
  "description": "Looks up a single stored task by ID and returns its body, description, and next due date",
  "signature": {
    "input": {
      "kind": "task-id",
      "description": "Task ID to retrieve",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "schedules": {
        "type": "bool",
        "description": "Whether to include schedules for the task",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      }
    },
    "output": {
      "mode": "Lambda",
      "kind": "task,lambda-tree",
      "description": "Resolves to the task fields as child nodes, optionally including a [schedules] node"
    }
  }
}
```

</details>

---

[&larr; `tasks.execute`](/reference/slots/tasks/tasks.execute/) | [all `tasks.*` slots](/reference/slots/tasks/) | [`tasks.list` &rarr;](/reference/slots/tasks/tasks.list/)


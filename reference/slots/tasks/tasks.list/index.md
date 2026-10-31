---
title: "[tasks.list]"
description: "tasks.list is a slot in the tasks namespace of Magic Cloud. Returns all stored tasks; supports an optional ID filter and pagination via [limit] and [offset]."
generated: true
llms: "guide"
slot_json: "/reference/slots/tasks/tasks.list/slot.json"
---

`tasks.list` is a slot in the `tasks` namespace, in Hyperlambda, the language of Magic Cloud. Returns all stored tasks; supports an optional ID filter and pagination via [limit] and [offset].

* **Value** (`task-id`), optional: Optional filter for task IDs
* **Returns**: Returns one child node per task with its task metadata

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[offset]` | long | no | Number of tasks to skip. |
| `[limit]` | long | no | Maximum number of tasks to return. |

### Returned nodes

| Node | Type | Required | Description |
|---|---|---|---|
| _unnamed child node_ | lambda | no | One task record returned by [tasks.list]. Can be repeated. |
| _unnamed child node_ / `[id]` | string | no | Task identifier. |
| _unnamed child node_ / `[created]` | date | no | Task creation timestamp. |
| _unnamed child node_ / `[description]` | string | no | Optional task description. |

### Guide

<!-- guide -->
To list tasks, you can use the **[tasks.list]** signal. This slot optionally
handles an **[offset]** and a **[limit]** argument, allowing you to page, which might be
useful if you have a lot of tasks in your system. If no **[limit]** is specified, this signal
will only return the first 10 tasks, including the task's Hyperlambda, but not its repetition
pattern(s), or due date(s). Below is an example.

```
tasks.list
   offset:20
   limit:10
```
<!-- /guide -->

### JSON declaration

This is the complete declaration of `tasks.list`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "tasks.list",
  "description": "Returns all stored tasks; supports an optional ID filter and pagination via [limit] and [offset]",
  "signature": {
    "input": {
      "kind": "task-id",
      "description": "Optional filter for task IDs",
      "required": false,
      "mode": "ValueOrExpression"
    },
    "children": {
      "offset": {
        "type": "long",
        "description": "Number of tasks to skip",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      },
      "limit": {
        "type": "long",
        "description": "Maximum number of tasks to return",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      }
    },
    "output": {
      "mode": "Lambda",
      "kind": "task-list,node-list",
      "element-kind": "task,lambda-tree",
      "description": "Returns one child node per task with its task metadata",
      "children": [
        {
          "type": "lambda",
          "kind": "task",
          "description": "One task record returned by [tasks.list]",
          "required": false,
          "mode": "Value",
          "cardinality": "ZeroOrMore",
          "role": "StructuredObject",
          "projection": "StructuredTree",
          "children": {
            "id": {
              "type": "string",
              "kind": "task-id",
              "description": "Task identifier",
              "required": false,
              "mode": "Value",
              "cardinality": "ExactlyOne",
              "role": "Option",
              "projection": "Value"
            },
            "created": {
              "type": "date",
              "kind": "date",
              "description": "Task creation timestamp",
              "required": false,
              "mode": "Value",
              "cardinality": "ExactlyOne",
              "role": "Option",
              "projection": "Value"
            },
            "description": {
              "type": "string",
              "kind": "text",
              "description": "Optional task description",
              "required": false,
              "mode": "Value",
              "cardinality": "ZeroOrOne",
              "role": "Option",
              "projection": "Value"
            }
          }
        }
      ]
    }
  }
}
```

</details>

---

[&larr; `tasks.get`](/reference/slots/tasks/tasks.get/) | [all `tasks.*` slots](/reference/slots/tasks/) | [`tasks.schedule` &rarr;](/reference/slots/tasks/tasks.schedule/)


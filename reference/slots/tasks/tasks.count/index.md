---
title: "[tasks.count]"
description: "tasks.count is a slot in the tasks namespace of Magic Cloud. Counts scheduled tasks."
generated: true
llms: false
slot_json: "/reference/slots/tasks/tasks.count/slot.json"
---

`tasks.count` is a slot in the `tasks` namespace, in Hyperlambda, the language of Magic Cloud. Counts scheduled tasks.

* **Value** (`task-id`), optional: Optional filter for task IDs
* **Returns**: Resolves to the number of scheduled tasks matching the optional filter

### JSON declaration

This is the complete declaration of `tasks.count`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "tasks.count",
  "description": "Counts scheduled tasks",
  "signature": {
    "input": {
      "kind": "task-id",
      "description": "Optional filter for task IDs",
      "required": false,
      "mode": "ValueOrExpression"
    },
    "output": {
      "mode": "Value",
      "kind": "integer,number",
      "description": "Resolves to the number of scheduled tasks matching the optional filter"
    }
  }
}
```

</details>

---

[all `tasks.*` slots](/reference/slots/tasks/) | [`tasks.create` &rarr;](/reference/slots/tasks/tasks.create/)


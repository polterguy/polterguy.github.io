---
title: "[execution.kill]"
description: "execution.kill is a slot in the execution namespace of Magic Cloud. Cancels a running execution by execution ID."
generated: true
llms: false
slot_json: "/reference/slots/execution/execution.kill/slot.json"
---

`execution.kill` is a slot in the `execution` namespace, in Hyperlambda, the language of Magic Cloud. Cancels a running execution by execution ID.

* **Value** (`execution-id`), required: Execution ID to cancel
* **Returns**: Returns true if the execution was cancelled

Guide: [How to use [execution.kill]](/plugins/magic.lambda.threading/#how-to-use-executionkill)

### JSON declaration

This is the complete declaration of `execution.kill`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "execution.kill",
  "description": "Cancels a running execution by execution ID",
  "signature": {
    "input": {
      "kind": "execution-id",
      "description": "Execution ID to cancel",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "output": {
      "mode": "Value",
      "kind": "boolean",
      "description": "Returns true if the execution was cancelled"
    }
  }
}
```

</details>

---

[all `execution.*` slots](/reference/slots/execution/) | [`execution.throttle` &rarr;](/reference/slots/execution/execution.throttle/)


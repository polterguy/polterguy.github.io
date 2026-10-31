---
title: "[execution.kill]"
description: "execution.kill is a slot in the execution namespace of Magic Cloud. Cancels a running execution by execution ID."
generated: true
llms: "guide"
slot_json: "/reference/slots/execution/execution.kill/slot.json"
---

`execution.kill` is a slot in the `execution` namespace, in Hyperlambda, the language of Magic Cloud. Cancels a running execution by execution ID.

* **Value** (`execution-id`), required: Execution ID to cancel
* **Returns**: Returns true if the execution was cancelled

### Guide

<!-- guide -->
Cancels another running execution by its execution id. This is useful when you have previously returned
an execution id to a caller and later want to stop that execution from another request or thread.

```
execution.kill:6c5a0bd3f7d64d6382d6cf3e7df5dc7c
```

The slot returns a boolean value indicating whether or not a matching live execution was found and
cancelled.
<!-- /guide -->

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


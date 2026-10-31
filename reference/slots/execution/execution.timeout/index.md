---
title: "[execution.timeout]"
description: "execution.timeout is a slot in the execution namespace of Magic Cloud. Sets a timeout in milliseconds for the current execution."
generated: true
llms: false
slot_json: "/reference/slots/execution/execution.timeout/slot.json"
---

`execution.timeout` is a slot in the `execution` namespace, in Hyperlambda, the language of Magic Cloud. Sets a timeout in milliseconds for the current execution.

* **Value** (`timeout-ms,integer,number`), required: Timeout in milliseconds for the current execution
* **Returns**: Returns true if the timeout was applied

Guide: [How to use [execution.timeout]](/plugins/magic.lambda.threading/#how-to-use-executiontimeout)

### JSON declaration

This is the complete declaration of `execution.timeout`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "execution.timeout",
  "description": "Sets a timeout in milliseconds for the current execution",
  "signature": {
    "input": {
      "kind": "timeout-ms,integer,number",
      "description": "Timeout in milliseconds for the current execution",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "output": {
      "mode": "Value",
      "kind": "boolean",
      "description": "Returns true if the timeout was applied"
    }
  }
}
```

</details>

---

[&larr; `execution.throttle.create`](/reference/slots/execution/execution.throttle.create/) | [all `execution.*` slots](/reference/slots/execution/)


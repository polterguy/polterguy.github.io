---
title: "[execution.timeout]"
description: "execution.timeout is a slot in the execution namespace of Magic Cloud. Sets a timeout in milliseconds for the current execution."
generated: true
llms: "guide"
slot_json: "/reference/slots/execution/execution.timeout/slot.json"
---

`execution.timeout` is a slot in the `execution` namespace, in Hyperlambda, the language of Magic Cloud. Sets a timeout in milliseconds for the current execution.

* **Value** (`timeout-ms,integer,number`), required: Timeout in milliseconds for the current execution
* **Returns**: Returns true if the timeout was applied

### Guide

<!-- guide -->
Configures a timeout for the **current** execution context. The value must be a positive number of
milliseconds and is interpreted relative to _now_.

```
execution.timeout:30000
```

The above means the current execution may continue for at most 30 more seconds. The slot returns a
boolean value indicating whether or not the timeout actually tightened the current deadline.

If multiple timeouts are applied to the same execution, the earliest deadline wins. Any child work
created through **[fork]** inherits the same execution context, implying the timeout applies to
forked work too.
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.threading](/plugins/magic.lambda.threading/) plugin, which documents every slot it contains.

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


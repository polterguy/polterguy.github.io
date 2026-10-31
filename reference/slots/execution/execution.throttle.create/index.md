---
title: "[execution.throttle.create]"
description: "execution.throttle.create is a slot in the execution namespace of Magic Cloud. Creates or replaces a named throttle enforced by [execution.throttle]; declaring an unchanged configuration keeps the existing throttle and its counters, while invoking the slot without arguments deletes the throttle instead."
generated: true
llms: false
slot_json: "/reference/slots/execution/execution.throttle.create/slot.json"
---

`execution.throttle.create` is a slot in the `execution` namespace, in Hyperlambda, the language of Magic Cloud. Creates or replaces a named throttle enforced by [execution.throttle]; declaring an unchanged configuration keeps the existing throttle and its counters, while invoking the slot without arguments deletes the throttle instead.

* **Value** (`throttle-name`), required: Name of the throttle to create, replace or delete

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| `[limit]` | int | no | Maximum number of invocations allowed per window; mandatory when creating a throttle, while invoking the slot without any arguments deletes the throttle instead. |
| `[per]` | string | no | How to partition the limit; 'user' partitions per authenticated username, 'ip' per client IP address, and 'global' shares one limit between all callers. Default: `user when authenticated, otherwise ip`. |
| `[window]` | int | no | Window length in seconds. Default: `60`. |

### JSON declaration

This is the complete declaration of `execution.throttle.create`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "execution.throttle.create",
  "description": "Creates or replaces a named throttle enforced by [execution.throttle]; declaring an unchanged configuration keeps the existing throttle and its counters, while invoking the slot without arguments deletes the throttle instead",
  "signature": {
    "input": {
      "kind": "throttle-name",
      "description": "Name of the throttle to create, replace or delete",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "limit": {
        "type": "int",
        "description": "Maximum number of invocations allowed per window; mandatory when creating a throttle, while invoking the slot without any arguments deletes the throttle instead",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      },
      "window": {
        "type": "int",
        "kind": "duration-seconds",
        "description": "Window length in seconds",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "60",
        "role": "Option",
        "projection": "Value"
      },
      "per": {
        "type": "string",
        "description": "How to partition the limit; 'user' partitions per authenticated username, 'ip' per client IP address, and 'global' shares one limit between all callers",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "user when authenticated, otherwise ip",
        "role": "Option",
        "projection": "Value"
      }
    }
  }
}
```

</details>

---

[&larr; `execution.throttle`](/reference/slots/execution/execution.throttle/) | [all `execution.*` slots](/reference/slots/execution/) | [`execution.timeout` &rarr;](/reference/slots/execution/execution.timeout/)


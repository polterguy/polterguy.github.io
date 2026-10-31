---
title: "[execution.throttle]"
description: "execution.throttle is a slot in the execution namespace of Magic Cloud. Enforces a named throttle previously declared with [execution.throttle.create], throwing a 429 exception once the limit is exceeded."
generated: true
llms: false
slot_json: "/reference/slots/execution/execution.throttle/slot.json"
---

`execution.throttle` is a slot in the `execution` namespace, in Hyperlambda, the language of Magic Cloud. Enforces a named throttle previously declared with [execution.throttle.create], throwing a 429 exception once the limit is exceeded.

* **Value** (`throttle-name`), required: Name of the throttle to enforce, as previously declared with [execution.throttle.create]

Guide: [How to use [execution.throttle]](/plugins/magic.lambda.threading/#how-to-use-executionthrottle)

### JSON declaration

This is the complete declaration of `execution.throttle`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "execution.throttle",
  "description": "Enforces a named throttle previously declared with [execution.throttle.create], throwing a 429 exception once the limit is exceeded",
  "signature": {
    "input": {
      "kind": "throttle-name",
      "description": "Name of the throttle to enforce, as previously declared with [execution.throttle.create]",
      "required": true,
      "mode": "ValueOrExpression"
    }
  }
}
```

</details>

---

[&larr; `execution.kill`](/reference/slots/execution/execution.kill/) | [all `execution.*` slots](/reference/slots/execution/) | [`execution.throttle.create` &rarr;](/reference/slots/execution/execution.throttle.create/)


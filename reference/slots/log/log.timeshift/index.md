---
title: "[log.timeshift]"
description: "log.timeshift is a slot in the log namespace of Magic Cloud. Aggregates log entries into time buckets."
generated: true
llms: false
slot_json: "/reference/slots/log/log.timeshift/slot.json"
---

`log.timeshift` is a slot in the `log` namespace, in Hyperlambda, the language of Magic Cloud. Aggregates log entries into time buckets.

* **Value** (`log-search`), required: Search string or log entry type to aggregate over the last two weeks
* **Returns**: Returns one child node per day with [when] and [count] values for the time bucket

### Guide

[How to use `log.timeshift`](/plugins/magic.lambda.logging/log.timeshift/)

### JSON declaration

This is the complete declaration of `log.timeshift`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "log.timeshift",
  "description": "Aggregates log entries into time buckets",
  "signature": {
    "input": {
      "kind": "log-search",
      "description": "Search string or log entry type to aggregate over the last two weeks",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "output": {
      "mode": "Lambda",
      "kind": "log-timeshift-list,node-list",
      "element-kind": "log-timeshift-bucket",
      "description": "Returns one child node per day with [when] and [count] values for the time bucket"
    }
  }
}
```

</details>

---

[&larr; `log.query`](/reference/slots/log/log.query/) | [all `log.*` slots](/reference/slots/log/)


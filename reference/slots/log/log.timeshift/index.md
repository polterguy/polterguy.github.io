---
title: "[log.timeshift]"
description: "log.timeshift is a slot in the log namespace of Magic Cloud. Aggregates log entries into time buckets."
generated: true
llms: "guide"
slot_json: "/reference/slots/log/log.timeshift/slot.json"
---

`log.timeshift` is a slot in the `log` namespace, in Hyperlambda, the language of Magic Cloud. Aggregates log entries into time buckets.

* **Value** (`log-search`), required: Search string or log entry type to aggregate over the last two weeks
* **Returns**: Returns one child node per day with [when] and [count] values for the time bucket

### Guide

<!-- guide -->
This slot counts the log items matching a search string per day, for the last two weeks, and is useful for
creating a time series of how often something is logged. The value of the slot is mandatory, and must be a
string a log item's content is matched against, or a log entry type. As with filtering, you should invoke
**[\[log.capabilities\]](/reference/slots/log/log.capabilities/)** to verify that your log implementation has `can-timeshift` set to true before relying upon it.

```
log.timeshift:tick
```

The slot returns one unnamed child node per day, starting with today (UTC) and moving backwards in time, and
each child has the following two arguments.

* __[when]__ - The date of the bucket, formatted as `yyyy-MM-dd`
* __[count]__ - Number of matching log items for that day, which is 0 for days without matches

If `tick` was logged twice today, the first returned node would have today's date as its **[when]** and 2 as its
**[count]**, while the second node, representing yesterday, would have a **[count]** of 0.
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.logging](/plugins/magic.lambda.logging/) plugin, which documents every slot it contains.

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


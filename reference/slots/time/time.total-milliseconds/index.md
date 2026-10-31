---
title: "[time.total-milliseconds]"
description: "time.total-milliseconds is a slot in the time namespace of Magic Cloud. Returns the total milliseconds for a TimeSpan value."
generated: true
llms: false
slot_json: "/reference/slots/time/time.total-milliseconds/slot.json"
---

`time.total-milliseconds` is a slot in the `time` namespace, in Hyperlambda, the language of Magic Cloud. Returns the total milliseconds for a TimeSpan value.

* **Value** (`timespan`), required: Time span to measure
* **Returns**: Resolves to the total number of milliseconds in the supplied time span

### Guide

[How to use `time.total-milliseconds`](/plugins/magic.lambda.dates/time.total-milliseconds/)

### JSON declaration

This is the complete declaration of `time.total-milliseconds`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "time.total-milliseconds",
  "description": "Returns the total milliseconds for a TimeSpan value",
  "signature": {
    "input": {
      "kind": "timespan",
      "description": "Time span to measure",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "output": {
      "mode": "Value",
      "kind": "duration-ms,number",
      "description": "Resolves to the total number of milliseconds in the supplied time span"
    }
  }
}
```

</details>

---

[&larr; `time.format`](/reference/slots/time/time.format/) | [all `time.*` slots](/reference/slots/time/)


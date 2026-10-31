---
title: "[date.unix]"
description: "date.unix is a slot in the date namespace of Magic Cloud. Returns the current UTC time as a Unix timestamp."
generated: true
llms: false
slot_json: "/reference/slots/date/date.unix/slot.json"
---

`date.unix` is a slot in the `date` namespace, in Hyperlambda, the language of Magic Cloud. Returns the current UTC time as a Unix timestamp.

* **Returns**: Resolves to the current UTC Unix timestamp in milliseconds

### Guide

[How to use `date.unix`](/plugins/magic.lambda.dates/date.unix/)

### JSON declaration

This is the complete declaration of `date.unix`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "date.unix",
  "description": "Returns the current UTC time as a Unix timestamp",
  "signature": {
    "output": {
      "mode": "Value",
      "kind": "unix-timestamp,integer,number",
      "description": "Resolves to the current UTC Unix timestamp in milliseconds"
    }
  }
}
```

</details>

---

[&larr; `date.now`](/reference/slots/date/date.now/) | [all `date.*` slots](/reference/slots/date/)


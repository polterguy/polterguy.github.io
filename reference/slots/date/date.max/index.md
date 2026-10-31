---
title: "[date.max]"
description: "date.max is a slot in the date namespace of Magic Cloud. Returns the maximum DateTime value."
generated: true
llms: false
slot_json: "/reference/slots/date/date.max/slot.json"
---

`date.max` is a slot in the `date` namespace, in Hyperlambda, the language of Magic Cloud. Returns the maximum DateTime value.

* **Returns**: Resolves to the maximum supported DateTime value

### Guide

[How to use `date.max`](/plugins/magic.lambda.dates/date.max/)

### JSON declaration

This is the complete declaration of `date.max`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "date.max",
  "description": "Returns the maximum DateTime value",
  "signature": {
    "output": {
      "mode": "Value",
      "kind": "date",
      "description": "Resolves to the maximum supported DateTime value"
    }
  }
}
```

</details>

---

[&larr; `date.from-unix`](/reference/slots/date/date.from-unix/) | [all `date.*` slots](/reference/slots/date/) | [`date.min` &rarr;](/reference/slots/date/date.min/)


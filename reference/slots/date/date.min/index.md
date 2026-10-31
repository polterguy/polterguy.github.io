---
title: "[date.min]"
description: "date.min is a slot in the date namespace of Magic Cloud. Returns the minimum DateTime value."
generated: true
llms: "guide"
slot_json: "/reference/slots/date/date.min/slot.json"
---

`date.min` is a slot in the `date` namespace, in Hyperlambda, the language of Magic Cloud. Returns the minimum DateTime value.

* **Returns**: Resolves to the minimum supported DateTime value

### Guide

<!-- guide -->
This slot simply returns the minimum value a date and time object can hold. Usage can be found below.

```
date.min
```
<!-- /guide -->

### JSON declaration

This is the complete declaration of `date.min`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "date.min",
  "description": "Returns the minimum DateTime value",
  "signature": {
    "output": {
      "mode": "Value",
      "kind": "date",
      "description": "Resolves to the minimum supported DateTime value"
    }
  }
}
```

</details>

---

[&larr; `date.max`](/reference/slots/date/date.max/) | [all `date.*` slots](/reference/slots/date/) | [`date.now` &rarr;](/reference/slots/date/date.now/)


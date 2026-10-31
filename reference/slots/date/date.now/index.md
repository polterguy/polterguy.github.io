---
title: "[date.now]"
description: "date.now is a slot in the date namespace of Magic Cloud. Returns the current server time in UTC."
generated: true
llms: "guide"
slot_json: "/reference/slots/date/date.now/slot.json"
---

`date.now` is a slot in the `date` namespace, in Hyperlambda, the language of Magic Cloud. Returns the current server time in UTC.

* **Returns**: Resolves to the current UTC date and time

### Guide

<!-- guide -->
This slot takes no arguments and simply returns the current date and time. Basic usage can be found below.

```
date.now
```
<!-- /guide -->

### JSON declaration

This is the complete declaration of `date.now`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "date.now",
  "description": "Returns the current server time in UTC",
  "signature": {
    "output": {
      "mode": "Value",
      "kind": "date",
      "description": "Resolves to the current UTC date and time"
    }
  }
}
```

</details>

---

[&larr; `date.min`](/reference/slots/date/date.min/) | [all `date.*` slots](/reference/slots/date/) | [`date.unix` &rarr;](/reference/slots/date/date.unix/)


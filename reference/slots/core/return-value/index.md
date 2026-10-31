---
title: "[return-value]"
description: "return-value is a core slot of Magic Cloud. Returns a value to the caller."
generated: true
llms: "guide"
slot_json: "/reference/slots/core/return-value/slot.json"
---

`return-value` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Returns a value to the caller.

* **Value** (`return-value`), required: Value to return to the nearest caller
* **Returns**: Resolves to a value to the caller

### Guide

<!-- guide -->
Returns a single value from your slot. Can only be invoked from the inside of
a dynamically created slot, and other slots explicitly creating a return context. An example can be
found below.

```
slots.create:foo
   return-value:This becomes the returned value from your slot

signal:foo
```
<!-- /guide -->

### JSON declaration

This is the complete declaration of `return-value`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "return-value",
  "description": "Returns a value to the caller",
  "signature": {
    "input": {
      "kind": "return-value",
      "description": "Value to return to the nearest caller",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "output": {
      "mode": "Value",
      "kind": "return-value",
      "description": "Resolves to a value to the caller"
    }
  }
}
```

</details>

---

[&larr; `return-nodes`](/reference/slots/core/return-nodes/) | [all core slots](/reference/slots/core/) | [`semaphore` &rarr;](/reference/slots/core/semaphore/)


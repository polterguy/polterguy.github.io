---
title: "[slots.exists]"
description: "slots.exists is a slot in the slots namespace of Magic Cloud. Returns true if a dynamic slot exists."
generated: true
llms: "guide"
slot_json: "/reference/slots/slots/slots.exists/slot.json"
---

`slots.exists` is a slot in the `slots` namespace, in Hyperlambda, the language of Magic Cloud. Returns true if a dynamic slot exists.

* **Value** (`dynamic-slot-name`), required: Name of the dynamic slot to test for
* **Returns**: Returns true if the slot exists

### Guide

<!-- guide -->
Returns true if the specified slot exists. Example can be found below.

```
slots.create:foo
   return-value:Blah, blah, blah ...

slots.exists:foo
slots.exists:DOES-NOT-EXISTS
```
<!-- /guide -->

### JSON declaration

This is the complete declaration of `slots.exists`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "slots.exists",
  "description": "Returns true if a dynamic slot exists",
  "signature": {
    "input": {
      "kind": "dynamic-slot-name",
      "description": "Name of the dynamic slot to test for",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "output": {
      "mode": "Value",
      "kind": "boolean",
      "description": "Returns true if the slot exists"
    }
  }
}
```

</details>

---

[&larr; `slots.delete`](/reference/slots/slots/slots.delete/) | [all `slots.*` slots](/reference/slots/slots/) | [`slots.get` &rarr;](/reference/slots/slots/slots.get/)


---
title: "[slots.delete]"
description: "slots.delete is a slot in the slots namespace of Magic Cloud. Deletes a dynamic slot."
generated: true
llms: "guide"
slot_json: "/reference/slots/slots/slots.delete/slot.json"
---

`slots.delete` is a slot in the `slots` namespace, in Hyperlambda, the language of Magic Cloud. Deletes a dynamic slot.

* **Value** (`dynamic-slot-name`), required: Name of the dynamic slot to delete

### Guide

<!-- guide -->
Deletes a previously created dynamic slot. The following example _will throw an exception_.

```
slots.create:foo
   return-value:int:57

slots.delete:foo

// Throws exception, since [foo] no longer exists.
slots.get:foo
```
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.slots](/plugins/magic.lambda.slots/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `slots.delete`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "slots.delete",
  "description": "Deletes a dynamic slot",
  "signature": {
    "input": {
      "kind": "dynamic-slot-name",
      "description": "Name of the dynamic slot to delete",
      "required": true,
      "mode": "ValueOrExpression"
    }
  }
}
```

</details>

---

[&larr; `slots.create`](/reference/slots/slots/slots.create/) | [all `slots.*` slots](/reference/slots/slots/) | [`slots.exists` &rarr;](/reference/slots/slots/slots.exists/)


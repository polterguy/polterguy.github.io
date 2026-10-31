---
title: "[slot.description]"
description: "slot.description is a slot in the slot namespace of Magic Cloud. Returns the description for a single compiled slot."
generated: true
llms: false
slot_json: "/reference/slots/slot/slot.description/slot.json"
---

`slot.description` is a slot in the `slot` namespace, in Hyperlambda, the language of Magic Cloud. Returns the description for a single compiled slot.

* **Value** (`slot-name`), required: Name of the compiled slot to inspect
* **Returns**: Resolves to the description of the requested slot

### Guide

[How to use `slot.description`](/plugins/magic.lambda/slot.description/)

### JSON declaration

This is the complete declaration of `slot.description`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "slot.description",
  "description": "Returns the description for a single compiled slot",
  "signature": {
    "input": {
      "kind": "slot-name",
      "description": "Name of the compiled slot to inspect",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "output": {
      "mode": "Value",
      "kind": "slot-description,text",
      "description": "Resolves to the description of the requested slot"
    }
  }
}
```

</details>

---

[all `slot.*` slots](/reference/slots/slot/) | [`slot.signature` &rarr;](/reference/slots/slot/slot.signature/)


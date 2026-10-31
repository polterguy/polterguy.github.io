---
title: "[slot.signature]"
description: "slot.signature is a slot in the slot namespace of Magic Cloud. Returns the documented input and output contract for a single compiled slot."
generated: true
llms: false
slot_json: "/reference/slots/slot/slot.signature/slot.json"
---

`slot.signature` is a slot in the `slot` namespace, in Hyperlambda, the language of Magic Cloud. Returns the documented input and output contract for a single compiled slot.

* **Value** (`slot-name`), required: Name of the compiled slot to inspect
* **Returns**: Resolves to input and output contract metadata for the requested slot

Guide: [How to use [slot.signature]](/plugins/magic.lambda/types/#how-to-use-slotsignature)

### Related documentation

* Part of the [magic.lambda](/plugins/magic.lambda/) plugin, which documents every slot it contains.
* Discussed in [Types and conversion](/plugins/magic.lambda/types/).

### JSON declaration

This is the complete declaration of `slot.signature`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "slot.signature",
  "description": "Returns the documented input and output contract for a single compiled slot",
  "signature": {
    "input": {
      "kind": "slot-name",
      "description": "Name of the compiled slot to inspect",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "output": {
      "mode": "Lambda",
      "kind": "slot-signature,lambda-tree",
      "description": "Resolves to input and output contract metadata for the requested slot"
    }
  }
}
```

</details>

---

[&larr; `slot.description`](/reference/slots/slot/slot.description/) | [all `slot.*` slots](/reference/slots/slot/)


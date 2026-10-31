---
title: "[slots.vocabulary]"
description: "slots.vocabulary is a slot in the slots namespace of Magic Cloud. Lists dynamically created slots."
generated: true
llms: false
slot_json: "/reference/slots/slots/slots.vocabulary/slot.json"
---

`slots.vocabulary` is a slot in the `slots` namespace, in Hyperlambda, the language of Magic Cloud. Lists dynamically created slots.

* **Value** (`dynamic-slot-name`), optional: Optional filter for dynamic slot names
* **Returns**: Resolves to available dynamic slot names as child nodes

### Guide

[How to use `slots.vocabulary`](/plugins/magic.lambda.slots/slots.vocabulary/)

### JSON declaration

This is the complete declaration of `slots.vocabulary`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "slots.vocabulary",
  "description": "Lists dynamically created slots",
  "signature": {
    "input": {
      "kind": "dynamic-slot-name",
      "description": "Optional filter for dynamic slot names",
      "required": false,
      "mode": "ValueOrExpression"
    },
    "output": {
      "mode": "Lambda",
      "kind": "dynamic-slot-name-list,string-list",
      "element-kind": "dynamic-slot-name,text",
      "description": "Resolves to available dynamic slot names as child nodes"
    }
  }
}
```

</details>

---

[&larr; `slots.get`](/reference/slots/slots/slots.get/) | [all `slots.*` slots](/reference/slots/slots/)


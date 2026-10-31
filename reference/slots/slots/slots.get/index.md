---
title: "[slots.get]"
description: "slots.get is a slot in the slots namespace of Magic Cloud. Returns a dynamic slot by name."
generated: true
llms: false
slot_json: "/reference/slots/slots/slots.get/slot.json"
---

`slots.get` is a slot in the `slots` namespace, in Hyperlambda, the language of Magic Cloud. Returns a dynamic slot by name.

* **Value** (`dynamic-slot-name`), required: Name of the dynamic slot to retrieve
* **Returns**: Resolves to the dynamic slot lambda body as child nodes

Guide: [How to use [slots.get]](/plugins/magic.lambda.slots/#how-to-use-slotsget)

### JSON declaration

This is the complete declaration of `slots.get`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "slots.get",
  "description": "Returns a dynamic slot by name",
  "signature": {
    "input": {
      "kind": "dynamic-slot-name",
      "description": "Name of the dynamic slot to retrieve",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "output": {
      "mode": "Lambda",
      "kind": "dynamic-slot-lambda,lambda-object,lambda-tree",
      "description": "Resolves to the dynamic slot lambda body as child nodes"
    }
  }
}
```

</details>

---

[&larr; `slots.exists`](/reference/slots/slots/slots.exists/) | [all `slots.*` slots](/reference/slots/slots/) | [`slots.vocabulary` &rarr;](/reference/slots/slots/slots.vocabulary/)


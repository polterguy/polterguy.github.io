---
title: "[hyperlambda.verify-slots]"
description: "hyperlambda.verify-slots is a slot in the hyperlambda namespace of Magic Cloud. Verifies that all slots referenced in executable statement position of the specified Hyperlambda exist."
generated: true
llms: false
slot_json: "/reference/slots/hyperlambda/hyperlambda.verify-slots/slot.json"
---

`hyperlambda.verify-slots` is a slot in the `hyperlambda` namespace, in Hyperlambda, the language of Magic Cloud. Verifies that all slots referenced in executable statement position of the specified Hyperlambda exist.

* **Value** (`hyperlambda`), optional: Hyperlambda text to verify; alternatively supply an already parsed lambda as children
* **Returns**: Resolves to true when every invocation is statically valid; otherwise lists missing slot names and invalid-invocation diagnostics as child nodes

### Guide

[How to use `hyperlambda.verify-slots`](/plugins/magic.lambda.hyperlambda/hyperlambda.verify-slots/)

### JSON declaration

This is the complete declaration of `hyperlambda.verify-slots`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "hyperlambda.verify-slots",
  "description": "Verifies that all slots referenced in executable statement position of the specified Hyperlambda exist",
  "signature": {
    "input": {
      "kind": "hyperlambda",
      "description": "Hyperlambda text to verify; alternatively supply an already parsed lambda as children",
      "required": false,
      "mode": "ValueOrExpression"
    },
    "output": {
      "mode": "Both",
      "kind": "boolean",
      "element-kind": "text",
      "description": "Resolves to true when every invocation is statically valid; otherwise lists missing slot names and invalid-invocation diagnostics as child nodes"
    }
  }
}
```

</details>

---

[all `hyperlambda.*` slots](/reference/slots/hyperlambda/)


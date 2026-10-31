---
title: "[reference]"
description: "reference is a core slot of Magic Cloud. Returns the first matched node as a live reference so callers can mutate it in place rather than copy its value."
generated: true
llms: false
slot_json: "/reference/slots/core/reference/slot.json"
---

`reference` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Returns the first matched node as a live reference so callers can mutate it in place rather than copy its value.

* **Value** (`single-object`), required: Expression selecting the node to reference
* **Returns**: Resolves to a reference to the first matching node value

Guide: [How to use [reference]](/plugins/magic.lambda/nodes/#how-to-use-reference)

### Guide

[How to use `reference`](/plugins/magic.lambda/reference/)

### JSON declaration

This is the complete declaration of `reference`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "reference",
  "description": "Returns the first matched node as a live reference so callers can mutate it in place rather than copy its value",
  "signature": {
    "input": {
      "kind": "single-object",
      "description": "Expression selecting the node to reference",
      "required": true,
      "mode": "Expression"
    },
    "output": {
      "mode": "Value",
      "kind": "node-reference",
      "description": "Resolves to a reference to the first matching node value"
    }
  }
}
```

</details>

---

[&larr; `pdf2text`](/reference/slots/core/pdf2text/) | [all core slots](/reference/slots/core/) | [`remove-nodes` &rarr;](/reference/slots/core/remove-nodes/)


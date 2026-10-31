---
title: "[type]"
description: "type is a core slot of Magic Cloud. Returns the CLR type name of a value."
generated: true
llms: false
slot_json: "/reference/slots/core/type/slot.json"
---

`type` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Returns the CLR type name of a value.

* **Value** (`single-object`), required: Expression selecting the value whose CLR type should be inspected
* **Returns**: Resolves to the runtime type name of the first matching value

### Guide

[How to use `type`](/plugins/magic.lambda/type/)

### JSON declaration

This is the complete declaration of `type`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "type",
  "description": "Returns the CLR type name of a value",
  "signature": {
    "input": {
      "kind": "single-object",
      "description": "Expression selecting the value whose CLR type should be inspected",
      "required": true,
      "mode": "Expression"
    },
    "output": {
      "mode": "Value",
      "kind": "type-name,text",
      "description": "Resolves to the runtime type name of the first matching value"
    }
  }
}
```

</details>

---

[&larr; `try-signal`](/reference/slots/core/try-signal/) | [all core slots](/reference/slots/core/) | [`types` &rarr;](/reference/slots/core/types/)


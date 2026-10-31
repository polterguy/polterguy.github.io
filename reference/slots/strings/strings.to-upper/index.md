---
title: "[strings.to-upper]"
description: "strings.to-upper is a slot in the strings namespace of Magic Cloud. Transforms input text to uppercase."
generated: true
llms: false
slot_json: "/reference/slots/strings/strings.to-upper/slot.json"
---

`strings.to-upper` is a slot in the `strings` namespace, in Hyperlambda, the language of Magic Cloud. Transforms input text to uppercase.

* **Value** (`text`), required: Text to transform
* **Returns**: Resolves to the uppercased string

### Guide

[How to use `strings.to-upper`](/plugins/magic.lambda.strings/strings.to-upper/)

### JSON declaration

This is the complete declaration of `strings.to-upper`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "strings.to-upper",
  "description": "Transforms input text to uppercase",
  "signature": {
    "input": {
      "kind": "text",
      "description": "Text to transform",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "output": {
      "mode": "Value",
      "kind": "text",
      "description": "Resolves to the uppercased string"
    }
  }
}
```

</details>

---

[&larr; `strings.to-lower`](/reference/slots/strings/strings.to-lower/) | [all `strings.*` slots](/reference/slots/strings/) | [`strings.trim` &rarr;](/reference/slots/strings/strings.trim/)


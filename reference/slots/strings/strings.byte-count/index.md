---
title: "[strings.byte-count]"
description: "strings.byte-count is a slot in the strings namespace of Magic Cloud. Returns the UTF-8 byte length of a string; useful for size checks where multi-byte characters matter."
generated: true
llms: false
slot_json: "/reference/slots/strings/strings.byte-count/slot.json"
---

`strings.byte-count` is a slot in the `strings` namespace, in Hyperlambda, the language of Magic Cloud. Returns the UTF-8 byte length of a string; useful for size checks where multi-byte characters matter.

* **Value** (`text`), required: Text to measure
* **Returns**: Resolves to the number of bytes in the string

### Guide

[How to use `strings.byte-count`](/plugins/magic.lambda.strings/strings.byte-count/)

### JSON declaration

This is the complete declaration of `strings.byte-count`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "strings.byte-count",
  "description": "Returns the UTF-8 byte length of a string; useful for size checks where multi-byte characters matter",
  "signature": {
    "input": {
      "kind": "text",
      "description": "Text to measure",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "output": {
      "mode": "Value",
      "kind": "integer,number",
      "description": "Resolves to the number of bytes in the string"
    }
  }
}
```

</details>

---

[&larr; `strings.builder.append`](/reference/slots/strings/strings.builder.append/) | [all `strings.*` slots](/reference/slots/strings/) | [`strings.capitalize` &rarr;](/reference/slots/strings/strings.capitalize/)


---
title: "[strings.capitalize]"
description: "strings.capitalize is a slot in the strings namespace of Magic Cloud. Returns the input with its first character upper-cased; remainder is left untouched."
generated: true
llms: false
slot_json: "/reference/slots/strings/strings.capitalize/slot.json"
---

`strings.capitalize` is a slot in the `strings` namespace, in Hyperlambda, the language of Magic Cloud. Returns the input with its first character upper-cased; remainder is left untouched.

* **Value** (`text`), required: Text to capitalize
* **Returns**: Resolves to the capitalized string

Guide: [How to use [strings.capitalize]](/plugins/magic.lambda.strings/#how-to-use-stringscapitalize)

### JSON declaration

This is the complete declaration of `strings.capitalize`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "strings.capitalize",
  "description": "Returns the input with its first character upper-cased; remainder is left untouched",
  "signature": {
    "input": {
      "kind": "text",
      "description": "Text to capitalize",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "output": {
      "mode": "Value",
      "kind": "text",
      "description": "Resolves to the capitalized string"
    }
  }
}
```

</details>

---

[&larr; `strings.byte-count`](/reference/slots/strings/strings.byte-count/) | [all `strings.*` slots](/reference/slots/strings/) | [`strings.concat` &rarr;](/reference/slots/strings/strings.concat/)


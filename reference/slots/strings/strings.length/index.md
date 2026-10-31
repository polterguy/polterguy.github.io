---
title: "[strings.length]"
description: "strings.length is a slot in the strings namespace of Magic Cloud. Returns the length of a string."
generated: true
llms: false
slot_json: "/reference/slots/strings/strings.length/slot.json"
---

`strings.length` is a slot in the `strings` namespace, in Hyperlambda, the language of Magic Cloud. Returns the length of a string.

* **Value** (`text`), required: Text to measure
* **Returns**: Resolves to the number of characters in the string

Guide: [How to use [strings.length]](/plugins/magic.lambda.strings/#how-to-use-stringslength)

### JSON declaration

This is the complete declaration of `strings.length`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "strings.length",
  "description": "Returns the length of a string",
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
      "description": "Resolves to the number of characters in the string"
    }
  }
}
```

</details>

---

[&larr; `strings.join`](/reference/slots/strings/strings.join/) | [all `strings.*` slots](/reference/slots/strings/) | [`strings.matches` &rarr;](/reference/slots/strings/strings.matches/)


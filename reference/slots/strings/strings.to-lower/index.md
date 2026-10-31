---
title: "[strings.to-lower]"
description: "strings.to-lower is a slot in the strings namespace of Magic Cloud. Transforms input text to lowercase."
generated: true
llms: "guide"
slot_json: "/reference/slots/strings/strings.to-lower/slot.json"
---

`strings.to-lower` is a slot in the `strings` namespace, in Hyperlambda, the language of Magic Cloud. Transforms input text to lowercase.

* **Value** (`text`), required: Text to transform
* **Returns**: Resolves to the lowercased string

### Guide

<!-- guide -->
Turns every single character in your input string into a lowercase character.

```
strings.to-lower:Thomas Hansen Is Cool

// Results in "thomas hansen is cool"
```
<!-- /guide -->

### JSON declaration

This is the complete declaration of `strings.to-lower`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "strings.to-lower",
  "description": "Transforms input text to lowercase",
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
      "description": "Resolves to the lowercased string"
    }
  }
}
```

</details>

---

[&larr; `strings.substring`](/reference/slots/strings/strings.substring/) | [all `strings.*` slots](/reference/slots/strings/) | [`strings.to-upper` &rarr;](/reference/slots/strings/strings.to-upper/)


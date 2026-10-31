---
title: "[strings.html-encode]"
description: "strings.html-encode is a slot in the strings namespace of Magic Cloud. HTML encodes the specified string."
generated: true
llms: "guide"
slot_json: "/reference/slots/strings/strings.html-encode/slot.json"
---

`strings.html-encode` is a slot in the `strings` namespace, in Hyperlambda, the language of Magic Cloud. HTML encodes the specified string.

* **Value** (`html-unencoded,text`), required: Non-encoded HTML text to encode
* **Returns**: Resolves to the HTML-encoded string

### Guide

<!-- guide -->
HTML encodes a string, replacing characters such as `<`, `>`, `&` and `"` with their HTML entities. The slot
takes a value, which can be a constant or an expression, and replaces its value with the encoded string.
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.strings](/plugins/magic.lambda.strings/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `strings.html-encode`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "strings.html-encode",
  "description": "HTML encodes the specified string",
  "signature": {
    "input": {
      "kind": "html-unencoded,text",
      "description": "Non-encoded HTML text to encode",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "output": {
      "mode": "Value",
      "kind": "html-encoded,text",
      "description": "Resolves to the HTML-encoded string"
    }
  }
}
```

</details>

---

[&larr; `strings.html-decode`](/reference/slots/strings/strings.html-decode/) | [all `strings.*` slots](/reference/slots/strings/) | [`strings.join` &rarr;](/reference/slots/strings/strings.join/)


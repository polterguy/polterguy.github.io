---
title: "[strings.url-encode]"
description: "strings.url-encode is a slot in the strings namespace of Magic Cloud. URL encodes the specified string."
generated: true
llms: false
slot_json: "/reference/slots/strings/strings.url-encode/slot.json"
---

`strings.url-encode` is a slot in the `strings` namespace, in Hyperlambda, the language of Magic Cloud. URL encodes the specified string.

* **Value** (`url-component,text`), required: Text to encode
* **Returns**: Resolves to the URL-encoded string

Guide: [How to use [strings.url-encode]](/plugins/magic.lambda.strings/#how-to-use-stringsurl-encode)

### JSON declaration

This is the complete declaration of `strings.url-encode`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "strings.url-encode",
  "description": "URL encodes the specified string",
  "signature": {
    "input": {
      "kind": "url-component,text",
      "description": "Text to encode",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "output": {
      "mode": "Value",
      "kind": "url-encoded,text",
      "description": "Resolves to the URL-encoded string"
    }
  }
}
```

</details>

---

[&larr; `strings.url-decode`](/reference/slots/strings/strings.url-decode/) | [all `strings.*` slots](/reference/slots/strings/)


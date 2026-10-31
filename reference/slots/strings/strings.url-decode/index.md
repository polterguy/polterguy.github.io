---
title: "[strings.url-decode]"
description: "strings.url-decode is a slot in the strings namespace of Magic Cloud. URL decodes the specified string."
generated: true
llms: false
slot_json: "/reference/slots/strings/strings.url-decode/slot.json"
---

`strings.url-decode` is a slot in the `strings` namespace, in Hyperlambda, the language of Magic Cloud. URL decodes the specified string.

* **Value** (`url-encoded`), required: Text to decode
* **Returns**: Resolves to the URL-decoded string

Guide: [How to use [strings.url-decode]](/plugins/magic.lambda.strings/#how-to-use-stringsurl-decode)

### JSON declaration

This is the complete declaration of `strings.url-decode`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "strings.url-decode",
  "description": "URL decodes the specified string",
  "signature": {
    "input": {
      "kind": "url-encoded",
      "description": "Text to decode",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "output": {
      "mode": "Value",
      "kind": "url-component,text",
      "description": "Resolves to the URL-decoded string"
    }
  }
}
```

</details>

---

[&larr; `strings.trim-start`](/reference/slots/strings/strings.trim-start/) | [all `strings.*` slots](/reference/slots/strings/) | [`strings.url-encode` &rarr;](/reference/slots/strings/strings.url-encode/)


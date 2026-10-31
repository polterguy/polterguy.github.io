---
title: "[strings.html-decode]"
description: "strings.html-decode is a slot in the strings namespace of Magic Cloud. HTML decodes the specified string."
generated: true
llms: false
slot_json: "/reference/slots/strings/strings.html-decode/slot.json"
---

`strings.html-decode` is a slot in the `strings` namespace, in Hyperlambda, the language of Magic Cloud. HTML decodes the specified string.

* **Value** (`html-encoded`), required: HTML encoded text to decode
* **Returns**: Resolves to the decoded HTML markup

Guide: [How to use [strings.html-decode]](/plugins/magic.lambda.strings/#how-to-use-stringshtml-decode)

### JSON declaration

This is the complete declaration of `strings.html-decode`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "strings.html-decode",
  "description": "HTML decodes the specified string",
  "signature": {
    "input": {
      "kind": "html-encoded",
      "description": "HTML encoded text to decode",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "output": {
      "mode": "Value",
      "kind": "html-unencoded,text",
      "description": "Resolves to the decoded HTML markup"
    }
  }
}
```

</details>

---

[&larr; `strings.ends-with`](/reference/slots/strings/strings.ends-with/) | [all `strings.*` slots](/reference/slots/strings/) | [`strings.html-encode` &rarr;](/reference/slots/strings/strings.html-encode/)


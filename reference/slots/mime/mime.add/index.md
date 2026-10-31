---
title: "[mime.add]"
description: "mime.add is a slot in the mime namespace of Magic Cloud. Associates a file extension with a MIME content-type so the server returns the correct Content-Type header for matching responses."
generated: true
llms: false
slot_json: "/reference/slots/mime/mime.add/slot.json"
---

`mime.add` is a slot in the `mime` namespace, in Hyperlambda, the language of Magic Cloud. Associates a file extension with a MIME content-type so the server returns the correct Content-Type header for matching responses.

* **Value** (`content-type`), required: File extension or MIME type key to register

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| _unnamed child node_ | string | yes | MIME type value for the extension/key. |

Guide: [How to use [mime.add]](/plugins/magic.endpoint/#how-to-use-mimeadd)

### JSON declaration

This is the complete declaration of `mime.add`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "mime.add",
  "description": "Associates a file extension with a MIME content-type so the server returns the correct Content-Type header for matching responses",
  "signature": {
    "input": {
      "kind": "content-type",
      "description": "File extension or MIME type key to register",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": [
      {
        "type": "string",
        "kind": "mime-type",
        "description": "MIME type value for the extension/key",
        "required": true,
        "mode": "ExecutableLambda",
        "cardinality": "ExactlyOne",
        "role": "SourceExpression",
        "evaluation": "EvalSelf",
        "projection": "Value"
      }
    ]
  }
}
```

</details>

---

[all `mime.*` slots](/reference/slots/mime/) | [`mime.create` &rarr;](/reference/slots/mime/mime.create/)


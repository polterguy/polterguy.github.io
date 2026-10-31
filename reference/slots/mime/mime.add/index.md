---
title: "[mime.add]"
description: "mime.add is a slot in the mime namespace of Magic Cloud. Associates a file extension with a MIME content-type so the server returns the correct Content-Type header for matching responses."
generated: true
llms: "guide"
slot_json: "/reference/slots/mime/mime.add/slot.json"
---

`mime.add` is a slot in the `mime` namespace, in Hyperlambda, the language of Magic Cloud. Associates a file extension with a MIME content-type so the server returns the correct Content-Type header for matching responses.

* **Value** (`content-type`), required: File extension or MIME type key to register

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _unnamed child node_ | string | yes | MIME type value for the extension/key. |

### Guide

<!-- guide -->
This slot associates a file extension with a MIME type. Notice, it will override previous associations if existing.
Example usage can be found below.

```
mime.add:py
   .:application/python
```

Then later when the endpoint resolver is returning files ending with _".py"_, it will return these with
a `Content-Type` of _"application/python"_.
<!-- /guide -->

### Related documentation

* Part of the [magic.endpoint](/plugins/magic.endpoint/) plugin, which documents every slot it contains.
* Discussed in [Slots related to endpoints and the HTTP context](/plugins/magic.endpoint/slots-related-to-endpoints-and-the-http-context/).

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


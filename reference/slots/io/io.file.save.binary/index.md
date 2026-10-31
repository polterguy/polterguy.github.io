---
title: "[io.file.save.binary]"
description: "io.file.save.binary is a slot in the io namespace of Magic Cloud. Saves a binary file to the server."
generated: true
llms: false
slot_json: "/reference/slots/io/io.file.save.binary/slot.json"
---

`io.file.save.binary` is a slot in the `io` namespace, in Hyperlambda, the language of Magic Cloud. Saves a binary file to the server.

* **Value** (`binary-file`), required: File path to save

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | byte[] | yes | Child node yielding the binary content to save. |

### JSON declaration

This is the complete declaration of `io.file.save.binary`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "io.file.save.binary",
  "description": "Saves a binary file to the server",
  "signature": {
    "input": {
      "kind": "binary-file",
      "description": "File path to save",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "*": {
        "type": "byte[]",
        "kind": "binary-file-content",
        "description": "Child node yielding the binary content to save",
        "required": true,
        "mode": "ExecutableLambda",
        "cardinality": "ExactlyOne"
      }
    }
  }
}
```

</details>

---

[&larr; `io.file.save`](/reference/slots/io/io.file.save/) | [all `io.*` slots](/reference/slots/io/) | [`io.file.search` &rarr;](/reference/slots/io/io.file.search/)


---
title: "[io.file.copy]"
description: "io.file.copy is a slot in the io namespace of Magic Cloud. Copies a file on the server."
generated: true
llms: false
slot_json: "/reference/slots/io/io.file.copy/slot.json"
---

`io.file.copy` is a slot in the `io` namespace, in Hyperlambda, the language of Magic Cloud. Copies a file on the server.

* **Value** (`file-path`), required: Source file path

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | string | yes | Destination path. |

Guide: [How to use [io.file.copy]](/plugins/magic.lambda.io/#how-to-use-iofilecopy)

### JSON declaration

This is the complete declaration of `io.file.copy`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "io.file.copy",
  "description": "Copies a file on the server",
  "signature": {
    "input": {
      "kind": "file-path",
      "description": "Source file path",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "*": {
        "type": "string",
        "kind": "file-path",
        "description": "Destination path",
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

[&larr; `io.content.zip-stream`](/reference/slots/io/io.content.zip-stream/) | [all `io.*` slots](/reference/slots/io/) | [`io.file.delete` &rarr;](/reference/slots/io/io.file.delete/)


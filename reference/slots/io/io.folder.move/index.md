---
title: "[io.folder.move]"
description: "io.folder.move is a slot in the io namespace of Magic Cloud. Moves a folder on the server."
generated: true
llms: false
slot_json: "/reference/slots/io/io.folder.move/slot.json"
---

`io.folder.move` is a slot in the `io` namespace, in Hyperlambda, the language of Magic Cloud. Moves a folder on the server.

* **Value** (`folder-path`), required: Source folder path

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | string | yes | Destination path. |

Guide: [How to use [io.folder.move]](/plugins/magic.lambda.io/#how-to-use-iofoldermove)

### JSON declaration

This is the complete declaration of `io.folder.move`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "io.folder.move",
  "description": "Moves a folder on the server",
  "signature": {
    "input": {
      "kind": "folder-path",
      "description": "Source folder path",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "*": {
        "type": "string",
        "kind": "folder-path",
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

[&larr; `io.folder.list-recursively`](/reference/slots/io/io.folder.list-recursively/) | [all `io.*` slots](/reference/slots/io/) | [`io.path.get-folder` &rarr;](/reference/slots/io/io.path.get-folder/)


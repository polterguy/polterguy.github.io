---
title: "[io.folder.move]"
description: "io.folder.move is a slot in the io namespace of Magic Cloud. Moves a folder on the server."
generated: true
llms: "guide"
slot_json: "/reference/slots/io/io.folder.move/slot.json"
---

`io.folder.move` is a slot in the `io` namespace, in Hyperlambda, the language of Magic Cloud. Moves a folder on the server.

* **Value** (`folder-path`), required: Source folder path

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | string | yes | Destination path. |

### Guide

<!-- guide -->
Moves the specified source folder to its specified destination folder.

```
io.folder.move:/misc/source-folder/
   .:/misc/destination-folder/
```
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.io](/plugins/magic.lambda.io/) plugin, which documents every slot it contains.

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


---
title: "[io.folder.copy]"
description: "io.folder.copy is a slot in the io namespace of Magic Cloud. Copies a folder on the server."
generated: true
llms: "guide"
slot_json: "/reference/slots/io/io.folder.copy/slot.json"
---

`io.folder.copy` is a slot in the `io` namespace, in Hyperlambda, the language of Magic Cloud. Copies a folder on the server.

* **Value** (`folder-path`), required: Source folder path

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | string | yes | Destination path. |

### Guide

<!-- guide -->
Copies the specified source folder to its specified destination folder. Notice, this slot doesn't copy
the folder itself, but rather the folder's content. Below is an example.

```
io.folder.copy:/misc/source-folder/
   .:/misc/destination-folder/
```

After invocation of the above, every single file and folder inside your _"source-folder"_ can now
be found as a copy inside your _"destination-folder"_.
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.io](/plugins/magic.lambda.io/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `io.folder.copy`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "io.folder.copy",
  "description": "Copies a folder on the server",
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

[&larr; `io.file.unzip`](/reference/slots/io/io.file.unzip/) | [all `io.*` slots](/reference/slots/io/) | [`io.folder.create` &rarr;](/reference/slots/io/io.folder.create/)


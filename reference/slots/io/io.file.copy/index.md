---
title: "[io.file.copy]"
description: "io.file.copy is a slot in the io namespace of Magic Cloud. Copies a file on the server."
generated: true
llms: "guide"
slot_json: "/reference/slots/io/io.file.copy/slot.json"
---

`io.file.copy` is a slot in the `io` namespace, in Hyperlambda, the language of Magic Cloud. Copies a file on the server.

* **Value** (`file-path`), required: Source file path

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | string | yes | Destination path. |

### Guide

<!-- guide -->
Copies the specified file to the specified destination folder and file.
Notice, requires the destination folder to exist from before, and the source
file to exist from before. This slot will delete any previously existing destination
file, before starting the copying process. Just like the save slot, this will evaluate
the lambda children before it executes the copying of your file, allowing you to use
the results of slots as the destination path for your file.

```
io.file.copy:/misc/README.md
   .:/misc/backup/README-backup.md
```

Notice, the folder parts of the destination folder is _optional_, and if you don't supply a folder
as a part of the path, the source folder will be used by default.
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.io](/plugins/magic.lambda.io/) plugin, which documents every slot it contains.

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


---
title: "[io.file.move]"
description: "io.file.move is a slot in the io namespace of Magic Cloud. Moves a file on the server."
generated: true
llms: "guide"
slot_json: "/reference/slots/io/io.file.move/slot.json"
---

`io.file.move` is a slot in the `io` namespace, in Hyperlambda, the language of Magic Cloud. Moves a file on the server.

* **Value** (`file-path`), required: Source file path

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | string | yes | Destination path. |

### Guide

<!-- guide -->
Similar to **[io.file.copy]** but deletes the source file after evaluating.

```
io.file.move:/misc/README.md
   .:/misc/backup/README-backup.md
```
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.io](/plugins/magic.lambda.io/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `io.file.move`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "io.file.move",
  "description": "Moves a file on the server",
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

[&larr; `io.file.mixin`](/reference/slots/io/io.file.mixin/) | [all `io.*` slots](/reference/slots/io/) | [`io.file.patch` &rarr;](/reference/slots/io/io.file.patch/)


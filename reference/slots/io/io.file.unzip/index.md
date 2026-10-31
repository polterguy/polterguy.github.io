---
title: "[io.file.unzip]"
description: "io.file.unzip is a slot in the io namespace of Magic Cloud. Extracts a zip archive on the server."
generated: true
llms: "guide"
slot_json: "/reference/slots/io/io.file.unzip/slot.json"
---

`io.file.unzip` is a slot in the `io` namespace, in Hyperlambda, the language of Magic Cloud. Extracts a zip archive on the server.

* **Value** (`zip-file`), required: Zip archive path to extract

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[folder]` | string | no | Destination folder; defaults to the zip file's folder. |
| `[overwrite]` | bool | no | Whether existing extracted files should be overwritten. Default: `false`. |

### Guide

<!-- guide -->
Unzips a ZIP file. Notice, the **[folder]** argument is optional, and the current folder
of the ZIP file you're unzipping will be used if no **[folder]** argument is given.

```
io.file.unzip:/misc/foo.zip
   folder:/misc/backup/
```

Optionally provide **[overwrite]** argument and set its value to boolean true if you want the operation to
overwrite any existing files in the destination folder. Otherwise the operation will throw an exception
if any of the files exists from before.
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.io](/plugins/magic.lambda.io/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `io.file.unzip`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "io.file.unzip",
  "description": "Extracts a zip archive on the server",
  "signature": {
    "input": {
      "kind": "zip-file",
      "description": "Zip archive path to extract",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "folder": {
        "type": "string",
        "kind": "folder-path",
        "description": "Destination folder; defaults to the zip file's folder",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne"
      },
      "overwrite": {
        "type": "bool",
        "kind": "boolean",
        "description": "Whether existing extracted files should be overwritten",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "false"
      }
    }
  }
}
```

</details>

---

[&larr; `io.file.search`](/reference/slots/io/io.file.search/) | [all `io.*` slots](/reference/slots/io/) | [`io.folder.copy` &rarr;](/reference/slots/io/io.folder.copy/)


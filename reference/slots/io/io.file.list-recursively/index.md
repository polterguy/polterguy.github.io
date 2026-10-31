---
title: "[io.file.list-recursively]"
description: "io.file.list-recursively is a slot in the io namespace of Magic Cloud. Lists files recursively in the specified folder."
generated: true
llms: "guide"
slot_json: "/reference/slots/io/io.file.list-recursively/slot.json"
---

`io.file.list-recursively` is a slot in the `io` namespace, in Hyperlambda, the language of Magic Cloud. Lists files recursively in the specified folder.

* **Value** (`folder-path`), required: Folder path to list files from
* **Returns**: Returns one unnamed child node per relative file path, recursively

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[display-hidden]` | bool | no | Whether hidden files or folders should be included. Default: `false`. |
| `[display-system]` | bool | no | Whether system folders such as /system/, /misc/, /data/, and /config/ should be included. Default: `true`. |

### Guide

<!-- guide -->
This slot works like **[io.file.list]**, except it also returns all files inside of nested folders, at any depth, and
not only the files directly inside of the specified folder. It returns one unnamed child node per file, with the
file's path relative to the root folder of your backend, and accepts the following optional arguments.

* **[display-hidden]** - Boolean, defaults to false, which hides files starting with a `.`
* **[display-system]** - Boolean, defaults to true, and if false hides files inside of _"/system/"_, _"/misc/"_, _"/data/"_ and _"/config/"_
<!-- /guide -->

### JSON declaration

This is the complete declaration of `io.file.list-recursively`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "io.file.list-recursively",
  "description": "Lists files recursively in the specified folder",
  "signature": {
    "input": {
      "kind": "folder-path",
      "description": "Folder path to list files from",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "display-hidden": {
        "type": "bool",
        "kind": "boolean",
        "description": "Whether hidden files or folders should be included",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "false"
      },
      "display-system": {
        "type": "bool",
        "kind": "boolean",
        "description": "Whether system folders such as /system/, /misc/, /data/, and /config/ should be included",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "true"
      }
    },
    "output": {
      "mode": "Lambda",
      "kind": "file-path-list,string-list",
      "element-kind": "file-path,text",
      "description": "Returns one unnamed child node per relative file path, recursively"
    }
  }
}
```

</details>

---

[&larr; `io.file.list`](/reference/slots/io/io.file.list/) | [all `io.*` slots](/reference/slots/io/) | [`io.file.load` &rarr;](/reference/slots/io/io.file.load/)


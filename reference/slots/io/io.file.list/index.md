---
title: "[io.file.list]"
description: "io.file.list is a slot in the io namespace of Magic Cloud. Lists files in the specified folder."
generated: true
llms: false
slot_json: "/reference/slots/io/io.file.list/slot.json"
---

`io.file.list` is a slot in the `io` namespace, in Hyperlambda, the language of Magic Cloud. Lists files in the specified folder.

* **Value** (`folder-path`), required: Folder path to list files from
* **Returns**: Returns one unnamed child node per relative file path

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[display-hidden]` | bool | no | Whether hidden files or folders should be included. Default: `false`. |
| `[display-system]` | bool | no | Whether system folders such as /system/, /misc/, /data/, and /config/ should be included. Default: `true`. |

### Guide

[How to use `io.file.list`](/plugins/magic.lambda.io/io.file.list/)

### JSON declaration

This is the complete declaration of `io.file.list`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "io.file.list",
  "description": "Lists files in the specified folder",
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
      "description": "Returns one unnamed child node per relative file path"
    }
  }
}
```

</details>

---

[&larr; `io.file.exists`](/reference/slots/io/io.file.exists/) | [all `io.*` slots](/reference/slots/io/) | [`io.file.list-recursively` &rarr;](/reference/slots/io/io.file.list-recursively/)


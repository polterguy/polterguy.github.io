---
title: "[io.folder.list]"
description: "io.folder.list is a slot in the io namespace of Magic Cloud. Lists folders in the specified folder."
generated: true
llms: false
slot_json: "/reference/slots/io/io.folder.list/slot.json"
---

`io.folder.list` is a slot in the `io` namespace, in Hyperlambda, the language of Magic Cloud. Lists folders in the specified folder.

* **Value** (`folder-path`), required: Folder path to list subfolders from
* **Returns**: Returns one unnamed child node per relative folder path

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| `[display-hidden]` | bool | no | Whether hidden files or folders should be included. Default: `false`. |
| `[display-system]` | bool | no | Whether system folders such as /system/, /misc/, /data/, and /config/ should be included. Default: `true`. |

Guide: [How to use [io.folder.list]](/plugins/magic.lambda.io/#how-to-use-iofolderlist)

### JSON declaration

This is the complete declaration of `io.folder.list`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "io.folder.list",
  "description": "Lists folders in the specified folder",
  "signature": {
    "input": {
      "kind": "folder-path",
      "description": "Folder path to list subfolders from",
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
      "kind": "folder-path-list,string-list",
      "element-kind": "folder-path,text",
      "description": "Returns one unnamed child node per relative folder path"
    }
  }
}
```

</details>

---

[&larr; `io.folder.exists`](/reference/slots/io/io.folder.exists/) | [all `io.*` slots](/reference/slots/io/) | [`io.folder.list-recursively` &rarr;](/reference/slots/io/io.folder.list-recursively/)


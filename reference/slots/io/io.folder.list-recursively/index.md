---
title: "[io.folder.list-recursively]"
description: "io.folder.list-recursively is a slot in the io namespace of Magic Cloud. Lists folders recursively in the specified folder."
generated: true
llms: "guide"
slot_json: "/reference/slots/io/io.folder.list-recursively/slot.json"
---

`io.folder.list-recursively` is a slot in the `io` namespace, in Hyperlambda, the language of Magic Cloud. Lists folders recursively in the specified folder.

* **Value** (`folder-path`), required: Folder path to list subfolders from
* **Returns**: Returns one unnamed child node per relative folder path, recursively

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[display-hidden]` | bool | no | Whether hidden files or folders should be included. Default: `false`. |
| `[display-system]` | bool | no | Whether system folders such as /system/, /misc/, /data/, and /config/ should be included. Default: `true`. |

### Guide

<!-- guide -->
This slot works like **[io.folder.list]**, except it also returns all folders nested inside of the specified folder,
at any depth, and not only its direct sub folders. It returns one unnamed child node per folder, with the folder's
path relative to the root folder of your backend, and accepts the following optional arguments.

* **[display-hidden]** - Boolean, defaults to false, which hides folders starting with a `.`
* **[display-system]** - Boolean, defaults to true, and if false hides folders inside of _"/system/"_, _"/misc/"_, _"/data/"_ and _"/config/"_
<!-- /guide -->

### JSON declaration

This is the complete declaration of `io.folder.list-recursively`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "io.folder.list-recursively",
  "description": "Lists folders recursively in the specified folder",
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
      "description": "Returns one unnamed child node per relative folder path, recursively"
    }
  }
}
```

</details>

---

[&larr; `io.folder.list`](/reference/slots/io/io.folder.list/) | [all `io.*` slots](/reference/slots/io/) | [`io.folder.move` &rarr;](/reference/slots/io/io.folder.move/)


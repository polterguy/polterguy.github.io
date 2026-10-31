---
title: "[io.file.load-recursively]"
description: "io.file.load-recursively is a slot in the io namespace of Magic Cloud. Loads files recursively from the specified folder."
generated: true
llms: "guide"
slot_json: "/reference/slots/io/io.file.load-recursively/slot.json"
---

`io.file.load-recursively` is a slot in the `io` namespace, in Hyperlambda, the language of Magic Cloud. Loads files recursively from the specified folder.

* **Value** (`folder-path`), required: Folder path to load from
* **Returns**: Returns one unnamed child node per loaded file; each entry has a [name] child (relative file path) and a [content] child (file content as string)

### Returned nodes

| Node | Type | Required | Description |
|---|---|---|---|
| _unnamed child node_ | lambda | no | One loaded file entry; access fields via the [name] and [content] children. Can be repeated. |
| _unnamed child node_ / `[name]` | string | yes | Relative file path of the loaded file. |
| _unnamed child node_ / `[content]` | string | yes | Loaded file content as text. |

### Guide

<!-- guide -->
This slot loads the content of all files inside of the specified folder, including all nested folders, as text, and
takes no arguments besides the folder as its value. It returns one unnamed child node per file, and each of these nodes
has the following two children.

* **[name]** - Path of the file relative to the root folder of your backend
* **[content]** - Content of the file as a string, decoded as UTF-8

As with **[io.file.load]**, you should not use this slot on binary files.
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.io](/plugins/magic.lambda.io/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `io.file.load-recursively`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "io.file.load-recursively",
  "description": "Loads files recursively from the specified folder",
  "signature": {
    "input": {
      "kind": "folder-path",
      "description": "Folder path to load from",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "output": {
      "mode": "Lambda",
      "kind": "loaded-file-list,node-list",
      "element-kind": "loaded-file,lambda-tree",
      "description": "Returns one unnamed child node per loaded file; each entry has a [name] child (relative file path) and a [content] child (file content as string)",
      "children": [
        {
          "type": "lambda",
          "kind": "loaded-file",
          "description": "One loaded file entry; access fields via the [name] and [content] children",
          "required": false,
          "mode": "Value",
          "cardinality": "ZeroOrMore",
          "role": "StructuredObject",
          "projection": "StructuredTree",
          "children": {
            "name": {
              "type": "string",
              "kind": "file-path",
              "description": "Relative file path of the loaded file",
              "required": true,
              "mode": "Value",
              "cardinality": "ExactlyOne",
              "role": "Option",
              "projection": "Value"
            },
            "content": {
              "type": "string",
              "kind": "text-file-content",
              "description": "Loaded file content as text",
              "required": true,
              "mode": "Value",
              "cardinality": "ExactlyOne",
              "role": "Payload",
              "projection": "Value"
            }
          }
        }
      ]
    }
  }
}
```

</details>

---

[&larr; `io.file.load`](/reference/slots/io/io.file.load/) | [all `io.*` slots](/reference/slots/io/) | [`io.file.load.binary` &rarr;](/reference/slots/io/io.file.load.binary/)


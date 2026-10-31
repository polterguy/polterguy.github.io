---
title: "[io.path.get-folder]"
description: "io.path.get-folder is a slot in the io namespace of Magic Cloud. Strips the filename from a path and returns just its folder portion (e.g. '/foo/bar/baz.txt' becomes '/foo/bar/')."
generated: true
llms: false
slot_json: "/reference/slots/io/io.path.get-folder/slot.json"
---

`io.path.get-folder` is a slot in the `io` namespace, in Hyperlambda, the language of Magic Cloud. Strips the filename from a path and returns just its folder portion (e.g. '/foo/bar/baz.txt' becomes '/foo/bar/').

* **Value** (`file-path`), required: Path to inspect
* **Returns**: Resolves to the folder portion of the supplied path

Guide: [How to use [io.path.get-folder]](/plugins/magic.lambda.io/#how-to-use-iopathget-folder)

### JSON declaration

This is the complete declaration of `io.path.get-folder`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "io.path.get-folder",
  "description": "Strips the filename from a path and returns just its folder portion (e.g. '/foo/bar/baz.txt' becomes '/foo/bar/')",
  "signature": {
    "input": {
      "kind": "file-path",
      "description": "Path to inspect",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "output": {
      "mode": "Value",
      "kind": "folder-path,text",
      "description": "Resolves to the folder portion of the supplied path"
    }
  }
}
```

</details>

---

[&larr; `io.folder.move`](/reference/slots/io/io.folder.move/) | [all `io.*` slots](/reference/slots/io/) | [`io.stream.close` &rarr;](/reference/slots/io/io.stream.close/)


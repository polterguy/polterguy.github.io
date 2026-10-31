---
title: "[io.path.get-folder]"
description: "io.path.get-folder is a slot in the io namespace of Magic Cloud. Strips the filename from a path and returns just its folder portion (e.g. '/foo/bar/baz.txt' becomes '/foo/bar/')."
generated: true
llms: "guide"
slot_json: "/reference/slots/io/io.path.get-folder/slot.json"
---

`io.path.get-folder` is a slot in the `io` namespace, in Hyperlambda, the language of Magic Cloud. Strips the filename from a path and returns just its folder portion (e.g. '/foo/bar/baz.txt' becomes '/foo/bar/').

* **Value** (`file-path`), required: Path to inspect
* **Returns**: Resolves to the folder portion of the supplied path

### Guide

<!-- guide -->
Strips the filename from a path and returns the folder part of it, always ending with a `/`. If the path already
ends with a `/` it is returned as it is. Below is an example.

```
io.path.get-folder:/foo/howdy/file.hl
```

The above returns `/foo/howdy/`, and the same is returned if you pass in `/foo/howdy/` instead.
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.io](/plugins/magic.lambda.io/) plugin, which documents every slot it contains.

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


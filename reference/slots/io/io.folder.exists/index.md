---
title: "[io.folder.exists]"
description: "io.folder.exists is a slot in the io namespace of Magic Cloud. Returns true if a folder exists."
generated: true
llms: false
slot_json: "/reference/slots/io/io.folder.exists/slot.json"
---

`io.folder.exists` is a slot in the `io` namespace, in Hyperlambda, the language of Magic Cloud. Returns true if a folder exists.

* **Value** (`folder-path`), required: Folder path to test
* **Returns**: Returns true if the folder exists

### Guide

[How to use `io.folder.exists`](/plugins/magic.lambda.io/io.folder.exists/)

### JSON declaration

This is the complete declaration of `io.folder.exists`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "io.folder.exists",
  "description": "Returns true if a folder exists",
  "signature": {
    "input": {
      "kind": "folder-path",
      "description": "Folder path to test",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "output": {
      "mode": "Value",
      "kind": "boolean",
      "description": "Returns true if the folder exists"
    }
  }
}
```

</details>

---

[&larr; `io.folder.delete`](/reference/slots/io/io.folder.delete/) | [all `io.*` slots](/reference/slots/io/) | [`io.folder.list` &rarr;](/reference/slots/io/io.folder.list/)


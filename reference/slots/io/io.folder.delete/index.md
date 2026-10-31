---
title: "[io.folder.delete]"
description: "io.folder.delete is a slot in the io namespace of Magic Cloud. Deletes a folder on the server."
generated: true
llms: false
slot_json: "/reference/slots/io/io.folder.delete/slot.json"
---

`io.folder.delete` is a slot in the `io` namespace, in Hyperlambda, the language of Magic Cloud. Deletes a folder on the server.

* **Value** (`folder-path`), required: Folder path to delete

Guide: [How to use [io.folder.delete]](/plugins/magic.lambda.io/#how-to-use-iofolderdelete)

### JSON declaration

This is the complete declaration of `io.folder.delete`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "io.folder.delete",
  "description": "Deletes a folder on the server",
  "signature": {
    "input": {
      "kind": "folder-path",
      "description": "Folder path to delete",
      "required": true,
      "mode": "ValueOrExpression"
    }
  }
}
```

</details>

---

[&larr; `io.folder.create`](/reference/slots/io/io.folder.create/) | [all `io.*` slots](/reference/slots/io/) | [`io.folder.exists` &rarr;](/reference/slots/io/io.folder.exists/)


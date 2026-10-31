---
title: "[io.folder.create]"
description: "io.folder.create is a slot in the io namespace of Magic Cloud. Creates a folder on the server."
generated: true
llms: false
slot_json: "/reference/slots/io/io.folder.create/slot.json"
---

`io.folder.create` is a slot in the `io` namespace, in Hyperlambda, the language of Magic Cloud. Creates a folder on the server.

* **Value** (`folder-path`), required: Folder path to create

### Guide

[How to use `io.folder.create`](/plugins/magic.lambda.io/io.folder.create/)

### JSON declaration

This is the complete declaration of `io.folder.create`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "io.folder.create",
  "description": "Creates a folder on the server",
  "signature": {
    "input": {
      "kind": "folder-path",
      "description": "Folder path to create",
      "required": true,
      "mode": "ValueOrExpression"
    }
  }
}
```

</details>

---

[&larr; `io.folder.copy`](/reference/slots/io/io.folder.copy/) | [all `io.*` slots](/reference/slots/io/) | [`io.folder.delete` &rarr;](/reference/slots/io/io.folder.delete/)


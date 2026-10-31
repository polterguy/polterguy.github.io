---
title: "[io.file.load]"
description: "io.file.load is a slot in the io namespace of Magic Cloud. Loads a text file from the server."
generated: true
llms: false
slot_json: "/reference/slots/io/io.file.load/slot.json"
---

`io.file.load` is a slot in the `io` namespace, in Hyperlambda, the language of Magic Cloud. Loads a text file from the server.

Also known as: [`load-file`](/reference/slots/core/load-file/).

* **Value** (`file-path`), required: File path to load
* **Returns**: Resolves to the loaded file content

### Guide

[How to use `io.file.load`](/plugins/magic.lambda.io/io.file.load/)

### JSON declaration

This is the complete declaration of `io.file.load`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "io.file.load",
  "description": "Loads a text file from the server",
  "signature": {
    "input": {
      "kind": "file-path",
      "description": "File path to load",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "output": {
      "mode": "Value",
      "kind": "text-file-content,text",
      "description": "Resolves to the loaded file content"
    }
  }
}
```

</details>

---

[&larr; `io.file.list-recursively`](/reference/slots/io/io.file.list-recursively/) | [all `io.*` slots](/reference/slots/io/) | [`io.file.load-recursively` &rarr;](/reference/slots/io/io.file.load-recursively/)


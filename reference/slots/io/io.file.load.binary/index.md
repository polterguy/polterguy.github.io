---
title: "[io.file.load.binary]"
description: "io.file.load.binary is a slot in the io namespace of Magic Cloud. Loads a binary file from the server."
generated: true
llms: false
slot_json: "/reference/slots/io/io.file.load.binary/slot.json"
---

`io.file.load.binary` is a slot in the `io` namespace, in Hyperlambda, the language of Magic Cloud. Loads a binary file from the server.

* **Value** (`binary-file`), required: File path to load
* **Returns**: Resolves to the loaded binary file bytes

### JSON declaration

This is the complete declaration of `io.file.load.binary`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "io.file.load.binary",
  "description": "Loads a binary file from the server",
  "signature": {
    "input": {
      "kind": "binary-file",
      "description": "File path to load",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "output": {
      "mode": "Value",
      "kind": "binary-file-content,binary-content,fingerprint-source",
      "description": "Resolves to the loaded binary file bytes"
    }
  }
}
```

</details>

---

[&larr; `io.file.load-recursively`](/reference/slots/io/io.file.load-recursively/) | [all `io.*` slots](/reference/slots/io/) | [`io.file.mixin` &rarr;](/reference/slots/io/io.file.mixin/)


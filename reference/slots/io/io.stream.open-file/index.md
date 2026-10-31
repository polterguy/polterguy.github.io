---
title: "[io.stream.open-file]"
description: "io.stream.open-file is a slot in the io namespace of Magic Cloud. Opens a file as a read-only stream so large files can be processed without loading them into memory; close with [io.stream.close]."
generated: true
llms: false
slot_json: "/reference/slots/io/io.stream.open-file/slot.json"
---

`io.stream.open-file` is a slot in the `io` namespace, in Hyperlambda, the language of Magic Cloud. Opens a file as a read-only stream so large files can be processed without loading them into memory; close with [io.stream.close].

* **Value** (`file-path`), required: File path to open as a stream
* **Returns**: Resolves to an open file stream

Guide: [How to use [io.stream.open-file]](/plugins/magic.lambda.io/#how-to-use-iostreamopen-file)

### JSON declaration

This is the complete declaration of `io.stream.open-file`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "io.stream.open-file",
  "description": "Opens a file as a read-only stream so large files can be processed without loading them into memory; close with [io.stream.close]",
  "signature": {
    "input": {
      "kind": "file-path",
      "description": "File path to open as a stream",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "output": {
      "mode": "Value",
      "kind": "stream",
      "description": "Resolves to an open file stream"
    }
  }
}
```

</details>

---

[&larr; `io.stream.close`](/reference/slots/io/io.stream.close/) | [all `io.*` slots](/reference/slots/io/) | [`io.stream.read` &rarr;](/reference/slots/io/io.stream.read/)


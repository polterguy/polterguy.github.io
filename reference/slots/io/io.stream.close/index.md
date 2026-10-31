---
title: "[io.stream.close]"
description: "io.stream.close is a slot in the io namespace of Magic Cloud. Closes and disposes a stream previously opened by [io.stream.open-file] or similar; always call to release the file handle."
generated: true
llms: false
slot_json: "/reference/slots/io/io.stream.close/slot.json"
---

`io.stream.close` is a slot in the `io` namespace, in Hyperlambda, the language of Magic Cloud. Closes and disposes a stream previously opened by [io.stream.open-file] or similar; always call to release the file handle.

* **Value** (`stream`), required: Stream instance to close

Guide: [How to use [io.stream.close]](/plugins/magic.lambda.io/#how-to-use-iostreamclose)

### JSON declaration

This is the complete declaration of `io.stream.close`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "io.stream.close",
  "description": "Closes and disposes a stream previously opened by [io.stream.open-file] or similar; always call to release the file handle",
  "signature": {
    "input": {
      "kind": "stream",
      "description": "Stream instance to close",
      "required": true,
      "mode": "Expression"
    }
  }
}
```

</details>

---

[&larr; `io.path.get-folder`](/reference/slots/io/io.path.get-folder/) | [all `io.*` slots](/reference/slots/io/) | [`io.stream.open-file` &rarr;](/reference/slots/io/io.stream.open-file/)


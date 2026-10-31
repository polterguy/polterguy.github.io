---
title: "[io.stream.read]"
description: "io.stream.read is a slot in the io namespace of Magic Cloud. Reads from an open stream."
generated: true
llms: false
slot_json: "/reference/slots/io/io.stream.read/slot.json"
---

`io.stream.read` is a slot in the `io` namespace, in Hyperlambda, the language of Magic Cloud. Reads from an open stream.

* **Value** (`stream`), required: Stream instance to read from
* **Returns**: Resolves to the bytes read from the stream

Guide: [How to use [io.stream.read]](/plugins/magic.lambda.io/#how-to-use-iostreamread)

### JSON declaration

This is the complete declaration of `io.stream.read`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "io.stream.read",
  "description": "Reads from an open stream",
  "signature": {
    "input": {
      "kind": "stream",
      "description": "Stream instance to read from",
      "required": true,
      "mode": "Expression"
    },
    "output": {
      "mode": "Value",
      "kind": "binary-content,fingerprint-source",
      "description": "Resolves to the bytes read from the stream"
    }
  }
}
```

</details>

---

[&larr; `io.stream.open-file`](/reference/slots/io/io.stream.open-file/) | [all `io.*` slots](/reference/slots/io/) | [`io.stream.save-file` &rarr;](/reference/slots/io/io.stream.save-file/)


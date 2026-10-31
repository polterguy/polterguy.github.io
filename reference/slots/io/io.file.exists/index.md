---
title: "[io.file.exists]"
description: "io.file.exists is a slot in the io namespace of Magic Cloud. Returns true if a file exists."
generated: true
llms: "guide"
slot_json: "/reference/slots/io/io.file.exists/slot.json"
---

`io.file.exists` is a slot in the `io` namespace, in Hyperlambda, the language of Magic Cloud. Returns true if a file exists.

* **Value** (`file-path`), required: File path to test
* **Returns**: Returns true if the file exists

### Guide

<!-- guide -->
Returns true if specified file exists from before.

```
io.file.exists:/misc/README.md
```
<!-- /guide -->

### JSON declaration

This is the complete declaration of `io.file.exists`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "io.file.exists",
  "description": "Returns true if a file exists",
  "signature": {
    "input": {
      "kind": "file-path",
      "description": "File path to test",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "output": {
      "mode": "Value",
      "kind": "boolean",
      "description": "Returns true if the file exists"
    }
  }
}
```

</details>

---

[&larr; `io.file.execute`](/reference/slots/io/io.file.execute/) | [all `io.*` slots](/reference/slots/io/) | [`io.file.list` &rarr;](/reference/slots/io/io.file.list/)


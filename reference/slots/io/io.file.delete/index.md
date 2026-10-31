---
title: "[io.file.delete]"
description: "io.file.delete is a slot in the io namespace of Magic Cloud. Deletes a file on the server."
generated: true
llms: "guide"
slot_json: "/reference/slots/io/io.file.delete/slot.json"
---

`io.file.delete` is a slot in the `io` namespace, in Hyperlambda, the language of Magic Cloud. Deletes a file on the server.

* **Value** (`file-path`), required: File path to delete

### Guide

<!-- guide -->
Deletes the specified file. Will throw an exception if the file doesn't exist.

```
io.file.delete:/misc/README2.md
```
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.io](/plugins/magic.lambda.io/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `io.file.delete`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "io.file.delete",
  "description": "Deletes a file on the server",
  "signature": {
    "input": {
      "kind": "file-path",
      "description": "File path to delete",
      "required": true,
      "mode": "ValueOrExpression"
    }
  }
}
```

</details>

---

[&larr; `io.file.copy`](/reference/slots/io/io.file.copy/) | [all `io.*` slots](/reference/slots/io/) | [`io.file.execute` &rarr;](/reference/slots/io/io.file.execute/)


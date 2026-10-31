---
title: "[io.file.save]"
description: "io.file.save is a slot in the io namespace of Magic Cloud. Saves a text file to the server."
generated: true
llms: false
slot_json: "/reference/slots/io/io.file.save/slot.json"
---

`io.file.save` is a slot in the `io` namespace, in Hyperlambda, the language of Magic Cloud. Saves a text file to the server.

Also known as: [`save-file`](/reference/slots/core/save-file/).

* **Value** (`file-path`), required: File path to save

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | string | yes | Child node yielding the text content to save. |

Guide: [How to use [io.file.save]](/plugins/magic.lambda.io/#how-to-use-iofilesave)

### JSON declaration

This is the complete declaration of `io.file.save`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "io.file.save",
  "description": "Saves a text file to the server",
  "signature": {
    "input": {
      "kind": "file-path",
      "description": "File path to save",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "*": {
        "type": "string",
        "kind": "text-file-content,text",
        "description": "Child node yielding the text content to save",
        "required": true,
        "mode": "ExecutableLambda",
        "cardinality": "ExactlyOne"
      }
    }
  }
}
```

</details>

---

[&larr; `io.file.patch`](/reference/slots/io/io.file.patch/) | [all `io.*` slots](/reference/slots/io/) | [`io.file.save.binary` &rarr;](/reference/slots/io/io.file.save.binary/)


---
title: "[io.stream.save-file]"
description: "io.stream.save-file is a slot in the io namespace of Magic Cloud. Writes a stream's contents to disk under the given path; commonly used after uploads or [http.get] downloads."
generated: true
llms: false
slot_json: "/reference/slots/io/io.stream.save-file/slot.json"
---

`io.stream.save-file` is a slot in the `io` namespace, in Hyperlambda, the language of Magic Cloud. Writes a stream's contents to disk under the given path; commonly used after uploads or [http.get] downloads.

* **Value** (`file-path`), required: File path to save the stream to

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | Stream | yes | Child node yielding the stream to save. |
| `[overwrite]` | bool | no | Whether an existing file should be overwritten. Default: `true`. |

Guide: [How to use [io.stream.save-file]](/plugins/magic.lambda.io/#how-to-use-iostreamsave-file)

### JSON declaration

This is the complete declaration of `io.stream.save-file`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "io.stream.save-file",
  "description": "Writes a stream's contents to disk under the given path; commonly used after uploads or [http.get] downloads",
  "signature": {
    "input": {
      "kind": "file-path",
      "description": "File path to save the stream to",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "overwrite": {
        "type": "bool",
        "kind": "boolean",
        "description": "Whether an existing file should be overwritten",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "true"
      },
      "*": {
        "type": "Stream",
        "kind": "stream",
        "description": "Child node yielding the stream to save",
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

[&larr; `io.stream.read`](/reference/slots/io/io.stream.read/) | [all `io.*` slots](/reference/slots/io/)


---
title: "[io.file.patch]"
description: "io.file.patch is a slot in the io namespace of Magic Cloud. Applies a unified-diff patch to a file on disk; useful for surgical edits or replaying generated diffs."
generated: true
llms: false
slot_json: "/reference/slots/io/io.file.patch/slot.json"
---

`io.file.patch` is a slot in the `io` namespace, in Hyperlambda, the language of Magic Cloud. Applies a unified-diff patch to a file on disk; useful for surgical edits or replaying generated diffs.

* **Value** (`file-path`), required: File path to patch

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | string | yes | Unified diff patch content to apply. |

### Guide

[How to use `io.file.patch`](/plugins/magic.lambda.io/io.file.patch/)

### JSON declaration

This is the complete declaration of `io.file.patch`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "io.file.patch",
  "description": "Applies a unified-diff patch to a file on disk; useful for surgical edits or replaying generated diffs",
  "signature": {
    "input": {
      "kind": "file-path",
      "description": "File path to patch",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "*": {
        "type": "string",
        "kind": "unified-diff",
        "description": "Unified diff patch content to apply",
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

[&larr; `io.file.move`](/reference/slots/io/io.file.move/) | [all `io.*` slots](/reference/slots/io/) | [`io.file.save` &rarr;](/reference/slots/io/io.file.save/)


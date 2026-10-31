---
title: "[io.content.zip-stream]"
description: "io.content.zip-stream is a slot in the io namespace of Magic Cloud. Builds an in-memory zip stream from child entries; useful for returning an archive over HTTP without writing to disk."
generated: true
llms: false
slot_json: "/reference/slots/io/io.content.zip-stream/slot.json"
---

`io.content.zip-stream` is a slot in the `io` namespace, in Hyperlambda, the language of Magic Cloud. Builds an in-memory zip stream from child entries; useful for returning an archive over HTTP without writing to disk.

* **Returns**: Resolves to a zip stream containing the supplied entries

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | string | yes | ZIP entry path. Can be repeated. |
| _any node name_ / _any node name_ | string\|byte[] | yes | Entry content. |

### Guide

[How to use `io.content.zip-stream`](/plugins/magic.lambda.io/io.content.zip-stream/)

### JSON declaration

This is the complete declaration of `io.content.zip-stream`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "io.content.zip-stream",
  "description": "Builds an in-memory zip stream from child entries; useful for returning an archive over HTTP without writing to disk",
  "signature": {
    "children": {
      "*": {
        "type": "string",
        "kind": "zip-entry-path",
        "description": "ZIP entry path",
        "required": true,
        "mode": "ExecutableLambda",
        "cardinality": "OneOrMore",
        "children": {
          "*": {
            "type": "string|byte[]",
            "kind": "zip-entry-content",
            "description": "Entry content",
            "required": true,
            "mode": "ExecutableLambda",
            "cardinality": "ExactlyOne"
          }
        }
      }
    },
    "output": {
      "mode": "Value",
      "kind": "zip-stream",
      "description": "Resolves to a zip stream containing the supplied entries"
    }
  }
}
```

</details>

---

[all `io.*` slots](/reference/slots/io/) | [`io.file.copy` &rarr;](/reference/slots/io/io.file.copy/)


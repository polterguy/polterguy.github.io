---
title: "[io.content.zip-stream]"
description: "io.content.zip-stream is a slot in the io namespace of Magic Cloud. Builds an in-memory zip stream from child entries; useful for returning an archive over HTTP without writing to disk."
generated: true
llms: "guide"
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

<!-- guide -->
Creates a memory based ZIP stream you can return over the HTTP response object. Notice,
this doesn't create a zip file, but rather a zip stream, which you can manipulate using other
slots. This slot is useful if you need to return zipped content as your HTTP response for instance.

Notice, both the root arguments (lambda children) of this slot will be evaluated, in addition to
its content nodes, evaluated once for each file declaration node. Notice also that the stream is
a memory based stream, and hence closing it, even in case of an exception, is not necessary.

```
io.content.zip-stream
   .:/foo/x.txt
      .:content of file
```
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.io](/plugins/magic.lambda.io/) plugin, which documents every slot it contains.

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


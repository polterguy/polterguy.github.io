---
title: "[io.stream.save-file]"
description: "io.stream.save-file is a slot in the io namespace of Magic Cloud. Writes a stream's contents to disk under the given path; commonly used after uploads or [http.get] downloads."
generated: true
llms: "guide"
slot_json: "/reference/slots/io/io.stream.save-file/slot.json"
---

`io.stream.save-file` is a slot in the `io` namespace, in Hyperlambda, the language of Magic Cloud. Writes a stream's contents to disk under the given path; commonly used after uploads or [http.get] downloads.

* **Value** (`file-path`), required: File path to save the stream to

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | Stream | yes | Child node yielding the stream to save. |
| `[overwrite]` | bool | no | Whether an existing file should be overwritten. Default: `true`. |

### Guide

<!-- guide -->
Works similarly to **[\[io.file.save\]](/reference/slots/io/io.file.save/)** but instead of taking source content of some kind,
it assumes the source is an open `Stream` of some sort.

```
/*
 * [.stream] here is an open stream, from for instance the HTTP
 * request object, or something similar that somehow is able to open
 * a stream and pass around in Hyperlambda.
 */
.stream
io.stream.save-file:/foo/bar.txt
   get-value:x:@.stream
```

After invoking the above, assuming the **[.stream]** node contains a valid `Stream`
object, the file above will contain the content from the stream.

**Notice** - If the file exists from before the existing file will be deleted, unless you
pass in an **[overwrite]** argument and set its value to false, at which point an exception
will be thrown if the file exists from before.
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.io](/plugins/magic.lambda.io/) plugin, which documents every slot it contains.

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


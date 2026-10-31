---
title: "[io.file.load]"
description: "io.file.load is a slot in the io namespace of Magic Cloud. Loads a text file from the server."
generated: true
llms: "guide"
slot_json: "/reference/slots/io/io.file.load/slot.json"
---

`io.file.load` is a slot in the `io` namespace, in Hyperlambda, the language of Magic Cloud. Loads a text file from the server.

Also known as: [`load-file`](/reference/slots/core/load-file/).

* **Value** (`file-path`), required: File path to load
* **Returns**: Resolves to the loaded file content

### Guide

<!-- guide -->
Loads the specified text file from disc. This slot can _only load text files_. Or to be specific,
there are no ways you can change binary files, hence loading a binary file is for the most parts
not something you should do. Although there _might_ exist exceptions to this.

```
io.file.load:/misc/README.md
```

**Notice** - If you want to load binary content you should use the **[io.file.load.binary]** override.
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.io](/plugins/magic.lambda.io/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `io.file.load`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "io.file.load",
  "description": "Loads a text file from the server",
  "signature": {
    "input": {
      "kind": "file-path",
      "description": "File path to load",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "output": {
      "mode": "Value",
      "kind": "text-file-content,text",
      "description": "Resolves to the loaded file content"
    }
  }
}
```

</details>

---

[&larr; `io.file.list-recursively`](/reference/slots/io/io.file.list-recursively/) | [all `io.*` slots](/reference/slots/io/) | [`io.file.load-recursively` &rarr;](/reference/slots/io/io.file.load-recursively/)


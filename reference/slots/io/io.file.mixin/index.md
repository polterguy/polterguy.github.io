---
title: "[io.file.mixin]"
description: "io.file.mixin is a slot in the io namespace of Magic Cloud. Loads a static file, applies same-named Hyperlambda codebehind, and returns the mixed result."
generated: true
llms: false
slot_json: "/reference/slots/io/io.file.mixin/slot.json"
---

`io.file.mixin` is a slot in the `io` namespace, in Hyperlambda, the language of Magic Cloud. Loads a static file, applies same-named Hyperlambda codebehind, and returns the mixed result.

* **Value** (`file-path`), required: Path to the static file to mix with its same-named .hl codebehind file
* **Returns**: Resolves to the mixed file content in value and any codebehind-produced child nodes

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | object | no | Optional argument available to codebehind lambda loaded for the mixed file. Can be repeated. |

Guide: [How to use [io.file.mixin]](/plugins/magic.lambda.io/#how-to-use-iofilemixin)

### JSON declaration

This is the complete declaration of `io.file.mixin`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "io.file.mixin",
  "description": "Loads a static file, applies same-named Hyperlambda codebehind, and returns the mixed result",
  "signature": {
    "input": {
      "kind": "file-path",
      "description": "Path to the static file to mix with its same-named .hl codebehind file",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "*": {
        "type": "object",
        "kind": "value",
        "description": "Optional argument available to codebehind lambda loaded for the mixed file",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrMore",
        "role": "Arguments",
        "projection": "ArgumentBag"
      }
    },
    "output": {
      "mode": "Both",
      "kind": "mixed-file-content,text",
      "description": "Resolves to the mixed file content in value and any codebehind-produced child nodes"
    }
  }
}
```

</details>

---

[&larr; `io.file.load.binary`](/reference/slots/io/io.file.load.binary/) | [all `io.*` slots](/reference/slots/io/) | [`io.file.move` &rarr;](/reference/slots/io/io.file.move/)


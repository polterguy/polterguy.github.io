---
title: "[json2lambda-stream]"
description: "json2lambda-stream is a core slot of Magic Cloud. Transforms JSON stream content into a lambda hierarchy."
generated: true
llms: "guide"
slot_json: "/reference/slots/core/json2lambda-stream/slot.json"
---

`json2lambda-stream` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Transforms JSON stream content into a lambda hierarchy.

* **Value** (`stream`), required: JSON stream to transform
* **Returns**: Resolves to the parsed lambda hierarchy as child nodes

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[encoding]` | string | no | Text encoding used to read the JSON stream. Default: `utf-8`. |

### Guide

<!-- guide -->
This slot does the same as **[json2lambda]**, except it reads the JSON from a stream instead of from a string,
such as a stream opened with **[io.stream.open-file]**, which you can read about in the _"magic.lambda.io"_ project.
The value of the slot must be an expression leading to the stream, and the slot throws an exception if
no stream is found. The resulting lambda hierarchy is returned as children of the slot node, and both JSON objects
and JSON arrays are supported.

The slot accepts the following argument.

* __[encoding]__ - Text encoding used to read the stream, defaults to `utf-8`. Streams using another encoding, such as `utf-16` or `iso-8859-1`, are converted to UTF-8 before they are parsed
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.json](/plugins/magic.lambda.json/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `json2lambda-stream`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "json2lambda-stream",
  "description": "Transforms JSON stream content into a lambda hierarchy",
  "signature": {
    "input": {
      "kind": "stream",
      "description": "JSON stream to transform",
      "required": true,
      "mode": "Expression"
    },
    "children": {
      "encoding": {
        "type": "string",
        "kind": "text-encoding",
        "description": "Text encoding used to read the JSON stream",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "utf-8",
        "role": "Option",
        "projection": "Value"
      }
    },
    "output": {
      "mode": "Lambda",
      "kind": "lambda-tree",
      "description": "Resolves to the parsed lambda hierarchy as child nodes"
    }
  }
}
```

</details>

---

[&larr; `json2lambda`](/reference/slots/core/json2lambda/) | [all core slots](/reference/slots/core/) | [`json2yaml` &rarr;](/reference/slots/core/json2yaml/)


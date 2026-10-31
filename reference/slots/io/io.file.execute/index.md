---
title: "[io.file.execute]"
description: "io.file.execute is a slot in the io namespace of Magic Cloud. Loads a Hyperlambda file and evaluates it as if it were inlined; child nodes become its [.arguments]."
generated: true
llms: false
slot_json: "/reference/slots/io/io.file.execute/slot.json"
---

`io.file.execute` is a slot in the `io` namespace, in Hyperlambda, the language of Magic Cloud. Loads a Hyperlambda file and evaluates it as if it were inlined; child nodes become its [.arguments].

* **Value** (`hyperlambda-file`), required: File path to execute
* **Returns**: Resolves to the executed file's value result and any returned child nodes

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | object | no | Named argument passed to the executed file as a child of [.arguments]. Can be repeated. |

### Returned nodes

| Node | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | no | Returned child node produced by the executed Hyperlambda file. Can be repeated. |

Guide: [How to use [io.file.execute]](/plugins/magic.lambda.io/#how-to-use-iofileexecute)

### JSON declaration

This is the complete declaration of `io.file.execute`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "io.file.execute",
  "description": "Loads a Hyperlambda file and evaluates it as if it were inlined; child nodes become its [.arguments]",
  "signature": {
    "input": {
      "kind": "hyperlambda-file",
      "description": "File path to execute",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "*": {
        "type": "object",
        "kind": "value",
        "description": "Named argument passed to the executed file as a child of [.arguments]",
        "required": false,
        "mode": "Arguments",
        "cardinality": "ZeroOrMore",
        "role": "Arguments",
        "projection": "ArgumentBag"
      }
    },
    "output": {
      "mode": "Both",
      "kind": "lambda-result",
      "description": "Resolves to the executed file's value result and any returned child nodes",
      "children": {
        "*": {
          "type": "lambda",
          "kind": "hyperlambda-result-node",
          "description": "Returned child node produced by the executed Hyperlambda file",
          "required": false,
          "mode": "Value",
          "cardinality": "ZeroOrMore",
          "role": "Payload",
          "projection": "Self"
        }
      }
    }
  }
}
```

</details>

---

[&larr; `io.file.delete`](/reference/slots/io/io.file.delete/) | [all `io.*` slots](/reference/slots/io/) | [`io.file.exists` &rarr;](/reference/slots/io/io.file.exists/)


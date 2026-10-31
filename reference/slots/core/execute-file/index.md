---
title: "[execute-file]"
description: "execute-file is a core slot of Magic Cloud. Loads a Hyperlambda file and evaluates it as if it were inlined; child nodes become its [.arguments]."
generated: true
llms: false
slot_json: "/reference/slots/core/execute-file/slot.json"
---

`execute-file` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Loads a Hyperlambda file and evaluates it as if it were inlined; child nodes become its [.arguments].

* **Value** (`hyperlambda-file`), required: File path to execute
* **Returns**: Resolves to the executed file's value result and any returned child nodes

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | object | no | Named argument passed to the executed file as a child of [.arguments]. Can be repeated. |

### Returned nodes

| Node | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | no | Returned child node produced by the executed Hyperlambda file. Can be repeated. |

Guide: [How to use [execute-file]](/plugins/magic.lambda.io/#how-to-use-execute-file)

### JSON declaration

This is the complete declaration of `execute-file`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "execute-file",
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
        "preprocess": "UnwrapExpressions",
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

[&larr; `execute`](/reference/slots/core/execute/) | [all core slots](/reference/slots/core/) | [`exists` &rarr;](/reference/slots/core/exists/)


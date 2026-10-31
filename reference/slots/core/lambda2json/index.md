---
title: "[lambda2json]"
description: "lambda2json is a core slot of Magic Cloud. Transforms a lambda hierarchy into JSON."
generated: true
llms: "guide"
slot_json: "/reference/slots/core/lambda2json/slot.json"
---

`lambda2json` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Transforms a lambda hierarchy into JSON.

* **Value** (`node-list,lambda-tree`), required: Expression selecting the lambda hierarchy to transform
* **Returns**: Resolves to the generated JSON string

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[format]` | bool | no | Whether to pretty-print the JSON output. Default: `false`. |

### Guide

<!-- guide -->
This guide covers [`lambda2json`](/reference/slots/core/lambda2json/), [`json2lambda`](/reference/slots/core/json2lambda/) together.

```
.json:@"{""property"": ""value""}"
json2lambda:x:-
lambda2json:x:-/*
```

The **[lambda2json]** slot can optionally take a **[\[format\]](/reference/slots/core/format/)** argument, with a boolean _"true"_ value, which implies the
resulting JSON will be indented and nicely formated, making it more readable.

**Notice** - Although all JSON can be transformed into lambda, the opposite is not necessarily true. This is because
lambda allows for having multiple nodes with the same name for instance, which would result in a JSON object with
multiple properties having the same key. Hence, have this in mind as you persist your lambda objects into JSON.
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.json](/plugins/magic.lambda.json/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `lambda2json`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "lambda2json",
  "description": "Transforms a lambda hierarchy into JSON",
  "signature": {
    "input": {
      "kind": "node-list,lambda-tree",
      "description": "Expression selecting the lambda hierarchy to transform",
      "required": true,
      "mode": "Expression"
    },
    "children": {
      "format": {
        "type": "bool",
        "description": "Whether to pretty-print the JSON output",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "false",
        "role": "Option",
        "projection": "Value"
      }
    },
    "output": {
      "mode": "Value",
      "kind": "json,text",
      "description": "Resolves to the generated JSON string"
    }
  }
}
```

</details>

---

[&larr; `lambda2hyper`](/reference/slots/core/lambda2hyper/) | [all core slots](/reference/slots/core/) | [`lambda2xml` &rarr;](/reference/slots/core/lambda2xml/)


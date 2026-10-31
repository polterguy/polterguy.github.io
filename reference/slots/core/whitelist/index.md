---
title: "[whitelist]"
description: "whitelist is a core slot of Magic Cloud. Evaluates a lambda with a restricted whitelist of allowed slots."
generated: true
llms: false
slot_json: "/reference/slots/core/whitelist/slot.json"
---

`whitelist` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Evaluates a lambda with a restricted whitelist of allowed slots.

* **Returns**: Resolves to the evaluated lambda's value result and any returned child nodes
* **Scope**: provides `whitelist`

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[vocabulary]` | lambda | yes | Allowed slot names for the restricted evaluation scope. |
| `[vocabulary]` / _any node name_ | string | yes | Allowed native slot name (e.g. add, set-value, if) that the body is permitted to invoke. Can be repeated. |
| `[.lambda]` | lambda | yes | Executable lambda block. |

Guide: [How to use [whitelist]](/plugins/magic.lambda.io/#restricting-file-access-with-whitelist)

### Guide

[How to use `whitelist`](/plugins/magic.lambda/whitelist/)

### JSON declaration

This is the complete declaration of `whitelist`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "whitelist",
  "description": "Evaluates a lambda with a restricted whitelist of allowed slots",
  "signature": {
    "children": {
      "vocabulary": {
        "type": "lambda",
        "description": "Allowed slot names for the restricted evaluation scope",
        "required": true,
        "mode": "Value",
        "cardinality": "ExactlyOne",
        "role": "StructuredObject",
        "projection": "Children",
        "children": {
          "*": {
            "type": "string",
            "kind": "native-slot-name",
            "description": "Allowed native slot name (e.g. add, set-value, if) that the body is permitted to invoke",
            "required": true,
            "mode": "Value",
            "cardinality": "OneOrMore",
            "role": "DynamicMap",
            "projection": "Value"
          }
        }
      },
      ".lambda": {
        "type": "lambda",
        "description": "Executable lambda block",
        "required": true,
        "mode": "ExecutableLambda",
        "cardinality": "ExactlyOne",
        "role": "LambdaBlock",
        "evaluation": "EvalBlock",
        "projection": "Self"
      }
    },
    "scope": {
      "provides": "whitelist"
    },
    "output": {
      "mode": "Both",
      "kind": "lambda-result",
      "description": "Resolves to the evaluated lambda's value result and any returned child nodes"
    }
  }
}
```

</details>

---

[&larr; `while`](/reference/slots/core/while/) | [all core slots](/reference/slots/core/) | [`xml2lambda` &rarr;](/reference/slots/core/xml2lambda/)


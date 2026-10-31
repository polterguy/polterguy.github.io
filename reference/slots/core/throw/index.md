---
title: "[throw]"
description: "throw is a core slot of Magic Cloud. Aborts execution by throwing an exception with the given message; optionally attach status code and public flag."
generated: true
llms: false
slot_json: "/reference/slots/core/throw/slot.json"
---

`throw` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Aborts execution by throwing an exception with the given message; optionally attach status code and public flag.

* **Value** (`exception-message,text`), optional: Exception message to throw

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| `[field]` | string | no | Optional form field or control ID associated with the exception. |
| `[public]` | bool | no | Whether the exception message may be returned to clients. Default: `false`. |
| `[status]` | int | no | HTTP status code associated with the exception. Default: `500`. |

Guide: [How to use [throw]](/plugins/magic.lambda/exceptions/#how-to-use-throw)

### JSON declaration

This is the complete declaration of `throw`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "throw",
  "description": "Aborts execution by throwing an exception with the given message; optionally attach status code and public flag",
  "signature": {
    "input": {
      "kind": "exception-message,text",
      "description": "Exception message to throw",
      "required": false,
      "mode": "ValueOrExpression"
    },
    "children": {
      "public": {
        "type": "bool",
        "description": "Whether the exception message may be returned to clients",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "false",
        "role": "Option",
        "projection": "Value"
      },
      "status": {
        "type": "int",
        "kind": "http-status-code",
        "description": "HTTP status code associated with the exception",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "500",
        "role": "Option",
        "projection": "Value"
      },
      "field": {
        "type": "string",
        "kind": "form-field-id",
        "description": "Optional form field or control ID associated with the exception",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      }
    }
  }
}
```

</details>

---

[&larr; `switch`](/reference/slots/core/switch/) | [all core slots](/reference/slots/core/) | [`time` &rarr;](/reference/slots/core/time/)


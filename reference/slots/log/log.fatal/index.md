---
title: "[log.fatal]"
description: "log.fatal is a slot in the log namespace of Magic Cloud. Writes a fatal-level log entry; reserve for unrecoverable failures that warrant immediate attention."
generated: true
llms: false
slot_json: "/reference/slots/log/log.fatal/slot.json"
---

`log.fatal` is a slot in the `log` namespace, in Hyperlambda, the language of Magic Cloud. Writes a fatal-level log entry; reserve for unrecoverable failures that warrant immediate attention.

* **Value** (`log-message,text`), required: Log message to write
* **Returns**: Id of the log entry created, or null if the configured log level filtered it out

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | string | no | Metadata entry stored with the log item when the slot has an input value; otherwise evaluated content fragment. Can be repeated. |
| `[exception]` | string | no | Exception text attached to error and fatal log entries. |

### Guide

[How to use `log.fatal`](/plugins/magic.lambda.logging/log.fatal/)

### JSON declaration

This is the complete declaration of `log.fatal`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "log.fatal",
  "description": "Writes a fatal-level log entry; reserve for unrecoverable failures that warrant immediate attention",
  "signature": {
    "input": {
      "kind": "log-message,text",
      "description": "Log message to write",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "*": {
        "type": "string",
        "kind": "log-metadata",
        "description": "Metadata entry stored with the log item when the slot has an input value; otherwise evaluated content fragment",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrMore",
        "role": "DynamicMap",
        "evaluation": "EvalSelf",
        "projection": "Value"
      },
      "exception": {
        "type": "string",
        "kind": "exception-text",
        "description": "Exception text attached to error and fatal log entries",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      }
    },
    "output": {
      "mode": "Value",
      "kind": "log-entry-id",
      "description": "Id of the log entry created, or null if the configured log level filtered it out"
    }
  }
}
```

</details>

---

[&larr; `log.error`](/reference/slots/log/log.error/) | [all `log.*` slots](/reference/slots/log/) | [`log.get` &rarr;](/reference/slots/log/log.get/)


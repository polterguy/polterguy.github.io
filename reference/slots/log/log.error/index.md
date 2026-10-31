---
title: "[log.error]"
description: "log.error is a slot in the log namespace of Magic Cloud. Writes an error-level log entry; use for caught exceptions or failed operations that need follow-up."
generated: true
llms: false
slot_json: "/reference/slots/log/log.error/slot.json"
---

`log.error` is a slot in the `log` namespace, in Hyperlambda, the language of Magic Cloud. Writes an error-level log entry; use for caught exceptions or failed operations that need follow-up.

* **Value** (`log-message,text`), required: Log message to write
* **Returns**: Id of the log entry created, or null if the configured log level filtered it out

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | string | no | Metadata entry stored with the log item when the slot has an input value; otherwise evaluated content fragment. Can be repeated. |
| `[exception]` | string | no | Exception text attached to error and fatal log entries. |

### JSON declaration

This is the complete declaration of `log.error`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "log.error",
  "description": "Writes an error-level log entry; use for caught exceptions or failed operations that need follow-up",
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

[&larr; `log.debug`](/reference/slots/log/log.debug/) | [all `log.*` slots](/reference/slots/log/) | [`log.fatal` &rarr;](/reference/slots/log/log.fatal/)


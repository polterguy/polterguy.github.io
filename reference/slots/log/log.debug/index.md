---
title: "[log.debug]"
description: "log.debug is a slot in the log namespace of Magic Cloud. Writes a debug-level log entry; useful during development for high-volume diagnostic detail."
generated: true
llms: false
slot_json: "/reference/slots/log/log.debug/slot.json"
---

`log.debug` is a slot in the `log` namespace, in Hyperlambda, the language of Magic Cloud. Writes a debug-level log entry; useful during development for high-volume diagnostic detail.

* **Value** (`log-message,text`), required: Log message to write
* **Returns**: Id of the log entry created, or null if the configured log level filtered it out

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | string | no | Metadata entry stored with the log item when the slot has an input value; otherwise evaluated content fragment. Can be repeated. |

### JSON declaration

This is the complete declaration of `log.debug`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "log.debug",
  "description": "Writes a debug-level log entry; useful during development for high-volume diagnostic detail",
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

[&larr; `log.count`](/reference/slots/log/log.count/) | [all `log.*` slots](/reference/slots/log/) | [`log.error` &rarr;](/reference/slots/log/log.error/)


---
title: "[log.info]"
description: "log.info is a slot in the log namespace of Magic Cloud. Writes an informational log entry capturing routine, non-error events of interest."
generated: true
llms: false
slot_json: "/reference/slots/log/log.info/slot.json"
---

`log.info` is a slot in the `log` namespace, in Hyperlambda, the language of Magic Cloud. Writes an informational log entry capturing routine, non-error events of interest.

* **Value** (`log-message,text`), required: Log message to write
* **Returns**: Id of the log entry created, or null if the configured log level filtered it out

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | string | no | Metadata entry stored with the log item when the slot has an input value; otherwise evaluated content fragment. Can be repeated. |

### Related documentation

* Part of the [magic.lambda.logging](/plugins/magic.lambda.logging/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `log.info`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "log.info",
  "description": "Writes an informational log entry capturing routine, non-error events of interest",
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

[&larr; `log.get`](/reference/slots/log/log.get/) | [all `log.*` slots](/reference/slots/log/) | [`log.query` &rarr;](/reference/slots/log/log.query/)


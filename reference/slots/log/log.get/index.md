---
title: "[log.get]"
description: "log.get is a slot in the log namespace of Magic Cloud. Returns a log entry by ID."
generated: true
llms: false
slot_json: "/reference/slots/log/log.get/slot.json"
---

`log.get` is a slot in the `log` namespace, in Hyperlambda, the language of Magic Cloud. Returns a log entry by ID.

* **Value** (`log-entry-id,integer,number`), required: ID of the log entry to retrieve
* **Returns**: Resolves to the log entry as child nodes

### Guide

[How to use `log.get`](/plugins/magic.lambda.logging/log.get/)

### JSON declaration

This is the complete declaration of `log.get`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "log.get",
  "description": "Returns a log entry by ID",
  "signature": {
    "input": {
      "kind": "log-entry-id,integer,number",
      "description": "ID of the log entry to retrieve",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "output": {
      "mode": "Lambda",
      "kind": "log-entry,lambda-tree",
      "description": "Resolves to the log entry as child nodes"
    }
  }
}
```

</details>

---

[&larr; `log.fatal`](/reference/slots/log/log.fatal/) | [all `log.*` slots](/reference/slots/log/) | [`log.info` &rarr;](/reference/slots/log/log.info/)


---
title: "[log.count]"
description: "log.count is a slot in the log namespace of Magic Cloud. Returns the total number of log entries, optionally restricted to a single content type."
generated: true
llms: false
slot_json: "/reference/slots/log/log.count/slot.json"
---

`log.count` is a slot in the `log` namespace, in Hyperlambda, the language of Magic Cloud. Returns the total number of log entries, optionally restricted to a single content type.

* **Value** (`content-type`), optional: Optional content type filter
* **Returns**: Resolves to the number of log entries matching the optional query

### Related documentation

* Part of the [magic.lambda.logging](/plugins/magic.lambda.logging/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `log.count`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "log.count",
  "description": "Returns the total number of log entries, optionally restricted to a single content type",
  "signature": {
    "input": {
      "kind": "content-type",
      "description": "Optional content type filter",
      "required": false,
      "mode": "ValueOrExpression"
    },
    "output": {
      "mode": "Value",
      "kind": "integer,number",
      "description": "Resolves to the number of log entries matching the optional query"
    }
  }
}
```

</details>

---

[&larr; `log.capabilities`](/reference/slots/log/log.capabilities/) | [all `log.*` slots](/reference/slots/log/) | [`log.debug` &rarr;](/reference/slots/log/log.debug/)


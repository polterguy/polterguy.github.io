---
title: "[log.query]"
description: "log.query is a slot in the log namespace of Magic Cloud. Returns recent log entries with most-recent-first ordering; supports optional content-type filtering and pagination."
generated: true
llms: false
slot_json: "/reference/slots/log/log.query/slot.json"
---

`log.query` is a slot in the `log` namespace, in Hyperlambda, the language of Magic Cloud. Returns recent log entries with most-recent-first ordering; supports optional content-type filtering and pagination.

* **Value** (`content-type`), optional: Optional content type filter
* **Returns**: Returns matching log entries as child nodes

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[max]` | int | no | Maximum number of log entries to return. Default: `10`. |
| `[from]` | object | no | Cursor or timestamp to query from. |

### Guide

[How to use `log.query`](/plugins/magic.lambda.logging/log.query/)

### JSON declaration

This is the complete declaration of `log.query`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "log.query",
  "description": "Returns recent log entries with most-recent-first ordering; supports optional content-type filtering and pagination",
  "signature": {
    "input": {
      "kind": "content-type",
      "description": "Optional content type filter",
      "required": false,
      "mode": "ValueOrExpression"
    },
    "children": {
      "max": {
        "type": "int",
        "description": "Maximum number of log entries to return",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "10",
        "role": "Option",
        "projection": "Value"
      },
      "from": {
        "type": "object",
        "description": "Cursor or timestamp to query from",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      }
    },
    "output": {
      "mode": "Lambda",
      "kind": "log-entry-list,node-list",
      "element-kind": "log-entry,lambda-tree",
      "description": "Returns matching log entries as child nodes"
    }
  }
}
```

</details>

---

[&larr; `log.info`](/reference/slots/log/log.info/) | [all `log.*` slots](/reference/slots/log/) | [`log.timeshift` &rarr;](/reference/slots/log/log.timeshift/)


---
title: "[sockets.users.count]"
description: "sockets.users.count is a slot in the sockets namespace of Magic Cloud. Counts connected socket users, optionally filtered by username."
generated: true
llms: false
slot_json: "/reference/slots/sockets/sockets.users.count/slot.json"
---

`sockets.users.count` is a slot in the `sockets` namespace, in Hyperlambda, the language of Magic Cloud. Counts connected socket users, optionally filtered by username.

* **Returns**: Resolves to the number of connected socket users matching the optional filter

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[filter]` | string | no | Username filter. |

### Guide

[How to use `sockets.users.count`](/plugins/magic.lambda.sockets/sockets.users.count/)

### JSON declaration

This is the complete declaration of `sockets.users.count`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "sockets.users.count",
  "description": "Counts connected socket users, optionally filtered by username",
  "signature": {
    "children": {
      "filter": {
        "type": "string",
        "kind": "username",
        "description": "Username filter",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      }
    },
    "output": {
      "mode": "Value",
      "kind": "integer,number",
      "description": "Resolves to the number of connected socket users matching the optional filter"
    }
  }
}
```

</details>

---

[&larr; `sockets.users`](/reference/slots/sockets/sockets.users/) | [all `sockets.*` slots](/reference/slots/sockets/)


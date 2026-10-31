---
title: "[sockets.users]"
description: "sockets.users is a slot in the sockets namespace of Magic Cloud. Lists connected socket users, optionally filtered by username."
generated: true
llms: false
slot_json: "/reference/slots/sockets/sockets.users/slot.json"
---

`sockets.users` is a slot in the `sockets` namespace, in Hyperlambda, the language of Magic Cloud. Lists connected socket users, optionally filtered by username.

* **Returns**: Returns one child node per connected socket user matching the optional filter

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| `[filter]` | string | no | Username filter. |
| `[limit]` | int | no | Maximum number of users to return. Default: `10`. |
| `[offset]` | int | no | Number of matching users to skip. Default: `0`. |

### JSON declaration

This is the complete declaration of `sockets.users`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "sockets.users",
  "description": "Lists connected socket users, optionally filtered by username",
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
      },
      "offset": {
        "type": "int",
        "description": "Number of matching users to skip",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "0",
        "role": "Option",
        "projection": "Value"
      },
      "limit": {
        "type": "int",
        "description": "Maximum number of users to return",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "10",
        "role": "Option",
        "projection": "Value"
      }
    },
    "output": {
      "mode": "Lambda",
      "kind": "socket-user-list,node-list",
      "element-kind": "socket-user,lambda-tree",
      "description": "Returns one child node per connected socket user matching the optional filter"
    }
  }
}
```

</details>

---

[&larr; `sockets.user.remove-from-group`](/reference/slots/sockets/sockets.user.remove-from-group/) | [all `sockets.*` slots](/reference/slots/sockets/) | [`sockets.users.count` &rarr;](/reference/slots/sockets/sockets.users.count/)


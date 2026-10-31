---
title: "[sockets.connection.enter-group]"
description: "sockets.connection.enter-group is a slot in the sockets namespace of Magic Cloud. Adds the current connection to a socket group."
generated: true
llms: false
slot_json: "/reference/slots/sockets/sockets.connection.enter-group/slot.json"
---

`sockets.connection.enter-group` is a slot in the `sockets` namespace, in Hyperlambda, the language of Magic Cloud. Adds the current connection to a socket group.

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| `[group]` | string | yes | Socket group name. |

### JSON declaration

This is the complete declaration of `sockets.connection.enter-group`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "sockets.connection.enter-group",
  "description": "Adds the current connection to a socket group",
  "signature": {
    "children": {
      "group": {
        "type": "string",
        "kind": "socket-group",
        "description": "Socket group name",
        "required": true,
        "mode": "ValueOrExpression",
        "cardinality": "ExactlyOne",
        "role": "Option",
        "projection": "Value"
      }
    }
  }
}
```

</details>

---

[all `sockets.*` slots](/reference/slots/sockets/) | [`sockets.connection.leave-group` &rarr;](/reference/slots/sockets/sockets.connection.leave-group/)


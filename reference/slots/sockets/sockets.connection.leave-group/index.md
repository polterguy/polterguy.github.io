---
title: "[sockets.connection.leave-group]"
description: "sockets.connection.leave-group is a slot in the sockets namespace of Magic Cloud. Removes the current connection from a socket group."
generated: true
llms: false
slot_json: "/reference/slots/sockets/sockets.connection.leave-group/slot.json"
---

`sockets.connection.leave-group` is a slot in the `sockets` namespace, in Hyperlambda, the language of Magic Cloud. Removes the current connection from a socket group.

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[group]` | string | yes | Socket group name. |

### JSON declaration

This is the complete declaration of `sockets.connection.leave-group`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "sockets.connection.leave-group",
  "description": "Removes the current connection from a socket group",
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

[&larr; `sockets.connection.enter-group`](/reference/slots/sockets/sockets.connection.enter-group/) | [all `sockets.*` slots](/reference/slots/sockets/) | [`sockets.signal` &rarr;](/reference/slots/sockets/sockets.signal/)


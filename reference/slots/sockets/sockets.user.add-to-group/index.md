---
title: "[sockets.user.add-to-group]"
description: "sockets.user.add-to-group is a slot in the sockets namespace of Magic Cloud. Adds a user to a socket group."
generated: true
llms: false
slot_json: "/reference/slots/sockets/sockets.user.add-to-group/slot.json"
---

`sockets.user.add-to-group` is a slot in the `sockets` namespace, in Hyperlambda, the language of Magic Cloud. Adds a user to a socket group.

* **Value** (`username`), required: Username to add to the socket group

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[group]` | string | yes | Socket group name. |

### JSON declaration

This is the complete declaration of `sockets.user.add-to-group`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "sockets.user.add-to-group",
  "description": "Adds a user to a socket group",
  "signature": {
    "input": {
      "kind": "username",
      "description": "Username to add to the socket group",
      "required": true,
      "mode": "ValueOrExpression"
    },
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

[&larr; `sockets.signal`](/reference/slots/sockets/sockets.signal/) | [all `sockets.*` slots](/reference/slots/sockets/) | [`sockets.user.remove-from-group` &rarr;](/reference/slots/sockets/sockets.user.remove-from-group/)


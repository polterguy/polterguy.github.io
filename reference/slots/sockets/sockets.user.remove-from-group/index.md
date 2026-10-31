---
title: "[sockets.user.remove-from-group]"
description: "sockets.user.remove-from-group is a slot in the sockets namespace of Magic Cloud. Removes a user from a socket group."
generated: true
llms: false
slot_json: "/reference/slots/sockets/sockets.user.remove-from-group/slot.json"
---

`sockets.user.remove-from-group` is a slot in the `sockets` namespace, in Hyperlambda, the language of Magic Cloud. Removes a user from a socket group.

* **Value** (`username`), required: Username to remove from the socket group

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[group]` | string | yes | Socket group name. |

### Guide

[How to use `sockets.user.remove-from-group`](/plugins/magic.lambda.sockets/sockets.user.remove-from-group/)

### JSON declaration

This is the complete declaration of `sockets.user.remove-from-group`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "sockets.user.remove-from-group",
  "description": "Removes a user from a socket group",
  "signature": {
    "input": {
      "kind": "username",
      "description": "Username to remove from the socket group",
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

[&larr; `sockets.user.add-to-group`](/reference/slots/sockets/sockets.user.add-to-group/) | [all `sockets.*` slots](/reference/slots/sockets/) | [`sockets.users` &rarr;](/reference/slots/sockets/sockets.users/)


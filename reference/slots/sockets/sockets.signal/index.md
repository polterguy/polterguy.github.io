---
title: "[sockets.signal]"
description: "sockets.signal is a slot in the sockets namespace of Magic Cloud. Pushes a SignalR message to clients subscribed to the channel; use to broadcast events from server to browsers."
generated: true
llms: false
slot_json: "/reference/slots/sockets/sockets.signal/slot.json"
---

`sockets.signal` is a slot in the `sockets` namespace, in Hyperlambda, the language of Magic Cloud. Pushes a SignalR message to clients subscribed to the channel; use to broadcast events from server to browsers.

* **Value** (`socket-channel`), required: Socket channel to publish

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| `[args]` | lambda | yes | Payload serialized to JSON and sent with the socket message. |
| `[clients]` | string | no | Comma-separated connection IDs receiving the message. |
| `[groups]` | string | no | Comma-separated groups receiving the message. |
| `[roles]` | string | no | Comma-separated roles receiving the message. |
| `[users]` | string | no | Comma-separated users receiving the message. |

Guide: [How to use [sockets.signal]](/plugins/magic.lambda.sockets/#how-to-use-socketssignal)

### JSON declaration

This is the complete declaration of `sockets.signal`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "sockets.signal",
  "description": "Pushes a SignalR message to clients subscribed to the channel; use to broadcast events from server to browsers",
  "signature": {
    "input": {
      "kind": "socket-channel",
      "description": "Socket channel to publish",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "args": {
        "type": "lambda",
        "kind": "socket-args",
        "description": "Payload serialized to JSON and sent with the socket message",
        "required": true,
        "mode": "ValueOrExpression",
        "cardinality": "ExactlyOne",
        "role": "Payload",
        "evaluation": "UnwrapDescendants",
        "projection": "StructuredTree"
      },
      "roles": {
        "type": "string",
        "kind": "role",
        "description": "Comma-separated roles receiving the message",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      },
      "users": {
        "type": "string",
        "kind": "username",
        "description": "Comma-separated users receiving the message",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      },
      "groups": {
        "type": "string",
        "kind": "socket-group",
        "description": "Comma-separated groups receiving the message",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      },
      "clients": {
        "type": "string",
        "kind": "socket-connection-id",
        "description": "Comma-separated connection IDs receiving the message",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      }
    }
  }
}
```

</details>

---

[&larr; `sockets.connection.leave-group`](/reference/slots/sockets/sockets.connection.leave-group/) | [all `sockets.*` slots](/reference/slots/sockets/) | [`sockets.user.add-to-group` &rarr;](/reference/slots/sockets/sockets.user.add-to-group/)


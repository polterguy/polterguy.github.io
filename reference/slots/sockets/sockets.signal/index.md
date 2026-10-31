---
title: "[sockets.signal]"
description: "sockets.signal is a slot in the sockets namespace of Magic Cloud. Pushes a SignalR message to clients subscribed to the channel; use to broadcast events from server to browsers."
generated: true
llms: "guide"
slot_json: "/reference/slots/sockets/sockets.signal/slot.json"
---

`sockets.signal` is a slot in the `sockets` namespace, in Hyperlambda, the language of Magic Cloud. Pushes a SignalR message to clients subscribed to the channel; use to broadcast events from server to browsers.

* **Value** (`socket-channel`), required: Socket channel to publish

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[args]` | lambda | yes | Payload serialized to JSON and sent with the socket message. |
| `[roles]` | string | no | Comma-separated roles receiving the message. |
| `[users]` | string | no | Comma-separated users receiving the message. |
| `[groups]` | string | no | Comma-separated groups receiving the message. |
| `[clients]` | string | no | Comma-separated connection IDs receiving the message. |

Guide: [How to use [sockets.signal]](/plugins/magic.lambda.sockets/#arguments-to-socketssignal)

### Guide

<!-- guide -->
In addition to the above, you can explicitly publish SignalR events by signaling the **[sockets.signal]** slot,
which will automatically transform the specified children **[args]** nodes to JSON, and invoke the specified
method for all connections somehow subscribing to the specified method - Allowing you to filter according
to groups, users and roles if you wish. Below is an example.

```
sockets.signal:foo.bar
   roles:root, admin
   args
      howdy:world
```

The above will invoke the `foo.bar` method, passing in `{"howdy":"world"}` as a JSON string, but only users belonging
to the roles of either `admin` or `root` will be notified. Both the **[roles]** and the **[args]** arguments are optional.
To subscribe to the above invocation, you could use something such as the following in TypeScript.

```typescript
this.connection.on('foo.bar', (args: string) => {
  console.log(JSON.parse(args));
});
```

You can also signal a list of specified users, such as the following illustrates.

```
sockets.signal:foo.bar
   users:user1, user2, user3
   args
      howdy:world
```

In addition to that you can signal a list of specified groups, such as the following illustrates.

```
sockets.signal:foo.bar
   groups:group1, group2, group3
   args
      howdy:world
```

Finally, you can signal a list of specified client connections, such as the following illustrates.

```
sockets.signal:foo.bar
   clients:e6U2Zz6kqHDCEVyEX6v35w, 5uWWytAM8kJ2gfIL0fEw2A
   args
      howdy:world
```

The above will only signal the two specified client connections.

**Notice** - If you signal a group or a list of groups, you'll have to add your users to the group before
you do.
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.sockets](/plugins/magic.lambda.sockets/) plugin, which documents every slot it contains.

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


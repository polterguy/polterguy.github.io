---
title: magic.lambda.sockets slot reference
description: Every slot in magic.lambda.sockets with its value, arguments and return value, generated from the source code.
generated: true
---

_This page is generated from the `[Slot]` attributes in the source code of [magic.lambda.sockets](https://github.com/polterguy/magic/tree/master/plugins/magic.lambda.sockets). Do not edit it; improve the attribute instead. The hand-written guide is at [magic.lambda.sockets](/plugins/magic.lambda.sockets/)._

## [sockets.connection.enter-group]

Adds the current connection to a socket group.


## [sockets.connection.leave-group]

Removes the current connection from a socket group.


## [sockets.signal]

Pushes a SignalR message to clients subscribed to the channel; use to broadcast events from server to browsers.

* **Value** (`socket-channel`), required: Socket channel to publish

| Argument | Type | Required | Description |
|---|---|---|---|
| `[args]` | lambda | yes | Payload serialized to JSON and sent with the socket message |

Guide: [How to use [sockets.signal]](/plugins/magic.lambda.sockets/#how-to-use-socketssignal)

## [sockets.user.add-to-group]

Adds a user to a socket group.

* **Value** (`username`), required: Username to add to the socket group

## [sockets.user.remove-from-group]

Removes a user from a socket group.

* **Value** (`username`), required: Username to remove from the socket group

## [sockets.users]

Lists connected socket users, optionally filtered by username.

* **Returns**: Returns one child node per connected socket user matching the optional filter

| Argument | Type | Required | Description |
|---|---|---|---|
| `[offset]` | int | no | Number of matching users to skip |
| `[limit]` | int | no | Maximum number of users to return |

## [sockets.users.count]

Counts connected socket users, optionally filtered by username.

* **Returns**: Resolves to the number of connected socket users matching the optional filter


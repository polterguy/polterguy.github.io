---
title: sockets.* slots
description: The 7 slots named sockets.* in Magic Cloud and Hyperlambda, with their arguments and return values, generated from the running system.
generated: true
---

_Generated from the running system, see [how this reference is built](/reference/slots/). Do not edit this page._

## [sockets.connection.enter-group]

Adds the current connection to a socket group.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[group]` | string | yes | Socket group name. |

## [sockets.connection.leave-group]

Removes the current connection from a socket group.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[group]` | string | yes | Socket group name. |

## [sockets.signal]

Pushes a SignalR message to clients subscribed to the channel; use to broadcast events from server to browsers.

* **Value** (`socket-channel`), required: Socket channel to publish

| Argument | Type | Required | Description |
|---|---|---|---|
| `[args]` | lambda | yes | Payload serialized to JSON and sent with the socket message. |
| `[roles]` | string | no | Comma-separated roles receiving the message. |
| `[users]` | string | no | Comma-separated users receiving the message. |
| `[groups]` | string | no | Comma-separated groups receiving the message. |
| `[clients]` | string | no | Comma-separated connection IDs receiving the message. |

Guide: [How to use [sockets.signal]](/plugins/magic.lambda.sockets/#how-to-use-socketssignal)

## [sockets.user.add-to-group]

Adds a user to a socket group.

* **Value** (`username`), required: Username to add to the socket group

| Argument | Type | Required | Description |
|---|---|---|---|
| `[group]` | string | yes | Socket group name. |

## [sockets.user.remove-from-group]

Removes a user from a socket group.

* **Value** (`username`), required: Username to remove from the socket group

| Argument | Type | Required | Description |
|---|---|---|---|
| `[group]` | string | yes | Socket group name. |

## [sockets.users]

Lists connected socket users, optionally filtered by username.

* **Returns**: Returns one child node per connected socket user matching the optional filter

| Argument | Type | Required | Description |
|---|---|---|---|
| `[filter]` | string | no | Username filter. |
| `[offset]` | int | no | Number of matching users to skip. Default: `0`. |
| `[limit]` | int | no | Maximum number of users to return. Default: `10`. |

## [sockets.users.count]

Counts connected socket users, optionally filtered by username.

* **Returns**: Resolves to the number of connected socket users matching the optional filter

| Argument | Type | Required | Description |
|---|---|---|---|
| `[filter]` | string | no | Username filter. |


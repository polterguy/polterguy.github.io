---
title: server.* slots
description: The 1 slots named server.* in Magic Cloud and Hyperlambda, with their arguments and return values, generated from the running system.
generated: true
---

_Generated from the running system, see [how this reference is built](/reference/slots/). Do not edit this page._

## [server.ip]

Returns the server's local IP address (IPv4 by default); useful for logging or building absolute URLs.

* **Returns**: Resolves to the server IP address for the requested IP version

| Argument | Type | Required | Description |
|---|---|---|---|
| `[version]` | string | no | IP version to return, either ipv4 or ipv6. |


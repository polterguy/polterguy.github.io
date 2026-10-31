---
title: auth.* slots
description: The 7 slots named auth.* in Magic Cloud and Hyperlambda, with their arguments and return values, generated from the running system.
generated: true
---

_Generated from the running system, see [how this reference is built](/reference/slots/). Do not edit this page._

## [auth.ticket.create]

Issues a signed JWT carrying the supplied username, roles, and claims; typically returned after a successful login.

* **Returns**: Resolves to the created JWT ticket string

| Argument | Type | Required | Description |
|---|---|---|---|
| `[claims]` | lambda | no | Claims to put in the ticket. |
| `[claims]` / _any node name_ | string | no | Named map entry. Can be repeated. |
| `[duration]` | long | no | Relative expiration duration in minutes. |
| `[expires]` | DateTime | no | Absolute UTC expiration time. |
| `[roles]` | lambda | no | Roles to put in the ticket. |
| `[roles]` / _any node name_ | string | no | List item. Can be repeated. |
| `[username]` | string | yes | Username to put in the ticket. |

* **Constraint** (AtMostOneOf): Use either absolute [expires] or relative [duration] (`[expires]`, `[duration]`)

Guide: [How to use [auth.ticket.create]](/plugins/magic.lambda.auth/#how-to-use-authticketcreate)

## [auth.ticket.get]

Returns the current ticket username, roles, and claims.

* **Returns**: Resolves to the username in value and roles and claims as child nodes

Guide: [How to use [auth.ticket.get]](/plugins/magic.lambda.auth/#how-to-use-authticketget)

## [auth.ticket.in-role]

Returns true if the current ticket belongs to one of the specified roles.

* **Value** (`role`), required: Comma-separated roles to test for
* **Returns**: Returns true if the current ticket belongs to at least one of the comma-separated roles

Guide: [How to use [auth.ticket.in-role]](/plugins/magic.lambda.auth/#how-to-use-authticketin-role)

## [auth.ticket.refresh]

Issues a new JWT with an extended expiration based on the current ticket, so active users don't get logged out.

* **Returns**: Resolves to the refreshed JWT ticket string

| Argument | Type | Required | Description |
|---|---|---|---|
| `[duration]` | long | no | Relative expiration duration in minutes. |
| `[expires]` | DateTime | no | Absolute UTC expiration time. |

* **Constraint** (AtMostOneOf): Use either absolute [expires] or relative [duration] (`[expires]`, `[duration]`)

Guide: [How to use [auth.ticket.refresh]](/plugins/magic.lambda.auth/#how-to-use-authticketrefresh)

## [auth.ticket.verify]

Verifies that the current user is authenticated and optionally in one of the specified roles.

* **Value** (`role-list`), optional: Optional comma-separated roles to require

Guide: [How to use [auth.ticket.verify]](/plugins/magic.lambda.auth/#how-to-use-authticketverify)

## [auth.token.read]

Validates a JWT token and verifies that it contains one of the required roles.

* **Value** (`jwt`), required: JWT token to validate

| Argument | Type | Required | Description |
|---|---|---|---|
| `[roles]` | string | yes | Comma-separated roles required by the token. |

## [auth.token.verify]

Verifies an externally created JWT token from the required [token] child node, against one or more trusted [issuer]/[issuers] supplied by the caller.

* **Returns**: Returns token claims as child nodes such as [issuer], [email], and optional [name] and [nonce]

| Argument | Type | Required | Description |
|---|---|---|---|
| `[issuer]` | string | no | Trusted issuer the token's issuer must equal; meta data is never fetched from issuers not supplied by the caller. |
| `[issuers]` | lambda | no | Trusted issuers, the token's issuer must equal one of them; meta data is never fetched from issuers not supplied by the caller. |
| `[issuers]` / _any node name_ | string | no | List item. Can be repeated. |
| `[token]` | string | yes | External JWT token to verify. |

Guide: [How to use [auth.token.verify]](/plugins/magic.lambda.auth/#openid-connect-authtokenverify)


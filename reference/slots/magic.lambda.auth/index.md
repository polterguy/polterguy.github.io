---
title: magic.lambda.auth slot reference
description: Every slot in magic.lambda.auth with its value, arguments and return value, generated from the source code.
generated: true
---

_This page is generated from the `[Slot]` attributes in the source code of [magic.lambda.auth](https://github.com/polterguy/magic/tree/master/plugins/magic.lambda.auth). Do not edit it; improve the attribute instead. The hand-written guide is at [magic.lambda.auth](/plugins/magic.lambda.auth/)._

## [auth.jwks]

Returns a public JSON Web Key Set for the supplied [public-key] arguments, removing duplicates, allowing other systems to verify RS256 tokens created by [auth.ticket.create].

* **Returns**: Returns a [keys] node with one child per supplied key, having [kty], [use], [alg], [kid], [n] and [e]

| Argument | Type | Required | Description |
|---|---|---|---|
| `[public-key]` | string | yes | RSA public key as PEM, or DER as base64 or byte[], to include in the key set, repeat for multiple keys |

Guide: [How to use [auth.jwks]](/plugins/magic.lambda.auth/#rs256-signing-and-authjwks)

## [auth.ticket.create]

Issues a signed JWT carrying the supplied username, roles, and claims; typically returned after a successful login.

* **Returns**: Resolves to the created JWT ticket string

| Argument | Type | Required | Description |
|---|---|---|---|
| `[expires]` | DateTime | no | Absolute UTC expiration time |
| `[duration]` | long | no | Relative expiration duration in minutes |
| `[*]` |  | no | List item |

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
| `[expires]` | DateTime | no | Absolute UTC expiration time |
| `[duration]` | long | no | Relative expiration duration in minutes |

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
| `[roles]` | string | yes | Comma-separated roles required by the token |
| `[public-key]` | string | no | RSA public key as PEM, or DER as base64 or byte[], accepting only RS256 tokens signed by its private half instead of HS256 tokens signed with the auth secret |

## [auth.token.verify]

Verifies an externally created JWT token from the required [token] child node, against one or more trusted [issuer]/[issuers] supplied by the caller.

* **Returns**: Returns token claims as child nodes such as [issuer], [email], and optional [name] and [nonce]

| Argument | Type | Required | Description |
|---|---|---|---|
| `[token]` | string | yes | External JWT token to verify |
| `[issuer]` | string | no | Trusted issuer the token's issuer must equal; meta data is never fetched from issuers not supplied by the caller |
| `[issuers]` | list | no | Trusted issuers, the token's issuer must equal one of them; meta data is never fetched from issuers not supplied by the caller |
| `[audience]` | string | no | Audience the token must have been issued to, typically the OAuth client ID; not validated unless [audience] or [audiences] is supplied |
| `[audiences]` | list | no | Audiences the token must have been issued to, it must match one of them; not validated unless [audience] or [audiences] is supplied |

Guide: [How to use [auth.token.verify]](/plugins/magic.lambda.auth/#openid-connect-authtokenverify)


---
title: "[auth.ticket.create]"
description: "auth.ticket.create is a slot in the auth namespace of Magic Cloud. Issues a signed JWT carrying the supplied username, roles, and claims; typically returned after a successful login."
generated: true
llms: false
slot_json: "/reference/slots/auth/auth.ticket.create/slot.json"
---

`auth.ticket.create` is a slot in the `auth` namespace, in Hyperlambda, the language of Magic Cloud. Issues a signed JWT carrying the supplied username, roles, and claims; typically returned after a successful login.

* **Returns**: Resolves to the created JWT ticket string

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[username]` | string | yes | Username to put in the ticket. |
| `[roles]` | lambda | no | Roles to put in the ticket. |
| `[roles]` / _any node name_ | string | no | List item. Can be repeated. |
| `[claims]` | lambda | no | Claims to put in the ticket. |
| `[claims]` / _any node name_ | string | no | Named map entry. Can be repeated. |
| `[expires]` | DateTime | no | Absolute UTC expiration time. |
| `[duration]` | long | no | Relative expiration duration in minutes. |
| `[private-key]` | string | no | RSA private key as PEM, or DER as base64 or byte[], signing the ticket with RS256 instead of HS256 using the auth secret. |

### Constraints

* **AtMostOneOf**: Use either absolute [expires] or relative [duration] (`[expires]`, `[duration]`)

### Guide

[How to use `auth.ticket.create`](/plugins/magic.lambda.auth/auth.ticket.create/)

### JSON declaration

This is the complete declaration of `auth.ticket.create`, as the running system describes it. It is also published as [slot.json](slot.json).

<details class="slot-declaration slot-json" data-src="slot.json">
<summary>JSON declaration (loads when opened)</summary>
<noscript><p><a href="slot.json">Open the JSON declaration</a>.</p></noscript>
</details>

---

[&larr; `auth.jwks`](/reference/slots/auth/auth.jwks/) | [all `auth.*` slots](/reference/slots/auth/) | [`auth.ticket.get` &rarr;](/reference/slots/auth/auth.ticket.get/)


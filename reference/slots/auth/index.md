---
title: "auth.* slots"
description: "The 8 slots named auth.* in Magic Cloud and Hyperlambda, each with its own page."
generated: true
---

8 slots, each with its own page and JSON declaration. See [how this reference is built](/reference/slots/).

| Slot | Description |
|---|---|
| [`auth.jwks`](/reference/slots/auth/auth.jwks/) | Returns a public JSON Web Key Set for the supplied [public-key] arguments, removing duplicates, allowing other systems to verify RS256 tokens created by [auth.ticket.create]. |
| [`auth.ticket.create`](/reference/slots/auth/auth.ticket.create/) | Issues a signed JWT carrying the supplied username, roles, and claims; typically returned after a successful login. |
| [`auth.ticket.get`](/reference/slots/auth/auth.ticket.get/) | Returns the current ticket username, roles, and claims. |
| [`auth.ticket.in-role`](/reference/slots/auth/auth.ticket.in-role/) | Returns true if the current ticket belongs to one of the specified roles. |
| [`auth.ticket.refresh`](/reference/slots/auth/auth.ticket.refresh/) | Issues a new JWT with an extended expiration based on the current ticket, so active users don't get logged out. |
| [`auth.ticket.verify`](/reference/slots/auth/auth.ticket.verify/) | Verifies that the current user is authenticated and optionally in one of the specified roles. |
| [`auth.token.read`](/reference/slots/auth/auth.token.read/) | Validates a JWT token and verifies that it contains one of the required roles. |
| [`auth.token.verify`](/reference/slots/auth/auth.token.verify/) | Verifies an externally created JWT token from the required [token] child node, against one or more trusted [issuer]/[issuers] supplied by the caller. |


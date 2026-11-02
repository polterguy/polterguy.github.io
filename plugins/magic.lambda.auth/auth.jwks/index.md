---
title: "How to use [auth.jwks]"
description: "How to use [auth.jwks] - To allow other systems to verify your tokens, you can return a standard JWKS document from an endpoint of your own, by passing one or more public keys into [auth.jwks]."
generated: true
guide: true
---

The reference page of [`auth.jwks`](/reference/slots/auth/auth.jwks/) has its arguments, constraints and declaration.

To allow other systems to verify your tokens, you can return a standard JWKS document from an endpoint of your own,
by passing one or more public keys into **[auth.jwks]**.

```
auth.jwks
   public-key:x:@.public-key-app-1
   public-key:x:@.public-key-app-2
```

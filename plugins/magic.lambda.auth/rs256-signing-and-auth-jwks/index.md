---
title: "RS256 signing and [auth.jwks]"
description: "RS256 signing and [auth.jwks] - By default Magic signs JWT tokens with HS256, using the magic:auth:secret setting."
generated: true
---

This page is part of the [magic.lambda.auth](/plugins/magic.lambda.auth/) documentation.

By default Magic signs JWT tokens with HS256, using the `magic:auth:secret` setting. This means anybody who can verify
a token can also create one. If other systems need to verify your tokens, or you need different keys for different
apps, you can sign tokens with RS256 by passing an RSA private key of at least 2048 bits into **[auth.ticket.create]**.
Keys can be PEM encoded, or DER encoded as base64 or `byte[]`, which is what **[crypto.rsa.create-key]** returns.

Magic never reads these keys from configuration. You load them yourself, using whatever logic you want to, from a file,
a database, an environment variable, etc. This allows you to have any number of keys in one cloudlet, for instance one
per app.

```
// Your own logic loading the private key belonging to the app.
.private-key
set-value:x:-
   io.file.load:/etc/keys/my-app.private.pem

auth.ticket.create
   username:foo
   roles
      .:admin
   private-key:x:@.private-key
```

The token is signed with RS256, and its `kid` header is the RFC 7638 thumbprint of the public key. To verify such a
token you pass the public key into **[auth.token.read]**, at which point it ONLY accepts RS256 tokens signed by that
key pair, and refuses tokens signed with the auth secret, with another key, or with any other algorithm.

```
auth.token.read:x:@.token
   roles:admin
   public-key:x:@.public-key
```

To allow other systems to verify your tokens, you can return a standard JWKS document from an endpoint of your own,
by passing one or more public keys into **[auth.jwks]**.

```
auth.jwks
   public-key:x:@.public-key-app-1
   public-key:x:@.public-key-app-2
```

The above returns a **[keys]** node with one child per unique key, having **[kty]**, **[use]**, **[alg]**, **[kid]**,
**[n]** and **[e]**. If you pass in a private key, only its public half is returned. Any argument other than **[public-key]** throws, so pass a private key as the value of **[public-key]**. Notice the following.

* Without a **[private-key]** or **[public-key]** everything works exactly as before, using HS256 and the auth secret
* If you pass in **[private-key]** or **[public-key]** and it has no value, for instance because your expression found no key, the slot throws instead of falling back to the auth secret
* The JWT bearer middleware that authenticates HTTP requests is NOT changed, and only accepts HS256 tokens signed with the auth secret. An RS256 token is verified explicitly using **[auth.token.read]**
* **[auth.ticket.refresh]** refreshes HS256 tokens only, and **[auth.token.read]** only checks roles, it does not return the token's claims. RS256 tokens are intended to be verified by other systems using your JWKS
* Tokens carry no issuer or audience by default. If several apps share one key, add your own claims and check them
* Rotating a key is up to you. Publish both the old and the new public key in your JWKS while tokens signed by the old key are still valid

---

[all of magic.lambda.auth](/plugins/magic.lambda.auth/)

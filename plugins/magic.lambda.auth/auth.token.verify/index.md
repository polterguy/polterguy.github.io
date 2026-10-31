---
title: "How to use [auth.token.verify]"
description: "How to use [auth.token.verify] - This slot accepts an external token created by OpenID Connect providers, and verifies the token's authenticity, and throws an exception if the token is not valid."
generated: true
guide: true
---

The reference page of [`auth.token.verify`](/reference/slots/auth/auth.token.verify/) has its arguments, constraints and declaration.

This slot accepts an external token created by OpenID Connect providers, and verifies the token's authenticity, and throws an exception if the token is not valid. If the token is valid it will return the **[email]** claim and the **[name]** claim if existing, in addition to **[nonce]** if existing - But it will not return anything else. The slot requires the following argument.

* __[token]__ - Being the actual token as created by the OIDC provider.

Example usage.

```text
auth.token.verify
   token:SOME_JWT_TOKEN_HERE
```

The slot will download well known configurations automatically, in addition to signing keys, which it will use to verify the token. Notice, the slot will accept all issuers by default, but it will return the issuer as **[issuer]** allowing you to check in your code if you trust the issuer or not after having invoked the slot before you generate an application specific token to return to the client.

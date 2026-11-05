---
title: "[auth.jwks]"
description: "auth.jwks is a slot in the auth namespace of Magic Cloud. Returns a public JSON Web Key Set for the supplied [public-key] arguments, removing duplicates, allowing other systems to verify RS256 tokens created by [auth.ticket.create]."
generated: true
llms: false
slot_json: "/reference/slots/auth/auth.jwks/slot.json"
---

`auth.jwks` is a slot in the `auth` namespace, in Hyperlambda, the language of Magic Cloud. Returns a public JSON Web Key Set for the supplied [public-key] arguments, removing duplicates, allowing other systems to verify RS256 tokens created by [auth.ticket.create].

* **Returns**: Returns a [keys] node with one child per supplied key, having [kty], [use], [alg], [kid], [n] and [e]

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[public-key]` | string | yes | RSA public key as PEM, or DER as base64 or byte[], to include in the key set, repeat for multiple keys. Can be repeated. |

### Guide

[How to use `auth.jwks`](/plugins/magic.lambda.auth/auth.jwks/)

### JSON declaration

This is the complete declaration of `auth.jwks`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "auth.jwks",
  "description": "Returns a public JSON Web Key Set for the supplied [public-key] arguments, removing duplicates, allowing other systems to verify RS256 tokens created by [auth.ticket.create]",
  "signature": {
    "children": {
      "public-key": {
        "type": "string",
        "kind": "rsa-public-key",
        "description": "RSA public key as PEM, or DER as base64 or byte[], to include in the key set, repeat for multiple keys",
        "required": true,
        "mode": "ValueOrExpression",
        "cardinality": "OneOrMore",
        "role": "Option",
        "projection": "Value"
      }
    },
    "output": {
      "mode": "Lambda",
      "kind": "jwks,lambda-tree",
      "description": "Returns a [keys] node with one child per supplied key, having [kty], [use], [alg], [kid], [n] and [e]"
    }
  }
}
```

</details>

---

[all `auth.*` slots](/reference/slots/auth/) | [`auth.ticket.create` &rarr;](/reference/slots/auth/auth.ticket.create/)


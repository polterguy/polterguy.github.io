---
title: "[auth.token.verify]"
description: "auth.token.verify is a slot in the auth namespace of Magic Cloud. Verifies an externally created JWT token from the required [token] child node, against one or more trusted [issuer]/[issuers] supplied by the caller."
generated: true
llms: false
slot_json: "/reference/slots/auth/auth.token.verify/slot.json"
---

`auth.token.verify` is a slot in the `auth` namespace, in Hyperlambda, the language of Magic Cloud. Verifies an externally created JWT token from the required [token] child node, against one or more trusted [issuer]/[issuers] supplied by the caller.

* **Returns**: Returns token claims as child nodes such as [issuer], [email], and optional [name] and [nonce]

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[token]` | string | yes | External JWT token to verify. |
| `[issuer]` | string | no | Trusted issuer the token's issuer must equal; meta data is never fetched from issuers not supplied by the caller. |
| `[issuers]` | lambda | no | Trusted issuers, the token's issuer must equal one of them; meta data is never fetched from issuers not supplied by the caller. |
| `[issuers]` / _any node name_ | string | no | List item. Can be repeated. |

Guide: [How to use [auth.token.verify]](/plugins/magic.lambda.auth/#openid-connect-authtokenverify)

### JSON declaration

This is the complete declaration of `auth.token.verify`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "auth.token.verify",
  "description": "Verifies an externally created JWT token from the required [token] child node, against one or more trusted [issuer]/[issuers] supplied by the caller",
  "signature": {
    "children": {
      "token": {
        "type": "string",
        "kind": "jwt",
        "description": "External JWT token to verify",
        "required": true,
        "mode": "ValueOrExpression",
        "cardinality": "ExactlyOne",
        "role": "Option",
        "projection": "Value"
      },
      "issuer": {
        "type": "string",
        "description": "Trusted issuer the token's issuer must equal; meta data is never fetched from issuers not supplied by the caller",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      },
      "issuers": {
        "type": "lambda",
        "description": "Trusted issuers, the token's issuer must equal one of them; meta data is never fetched from issuers not supplied by the caller",
        "required": false,
        "mode": "StructuredArguments",
        "cardinality": "ZeroOrOne",
        "role": "StructuredObject",
        "projection": "Children",
        "children": {
          "*": {
            "type": "string",
            "description": "List item",
            "required": false,
            "mode": "ValueOrExpression",
            "cardinality": "ZeroOrMore",
            "role": "Option",
            "projection": "Value"
          }
        }
      }
    },
    "output": {
      "mode": "Lambda",
      "kind": "jwt-claims,text,lambda-tree",
      "description": "Returns token claims as child nodes such as [issuer], [email], and optional [name] and [nonce]"
    }
  }
}
```

</details>

---

[&larr; `auth.token.read`](/reference/slots/auth/auth.token.read/) | [all `auth.*` slots](/reference/slots/auth/)


---
title: "[auth.token.read]"
description: "auth.token.read is a slot in the auth namespace of Magic Cloud. Validates a JWT token and verifies that it contains one of the required roles."
generated: true
llms: false
slot_json: "/reference/slots/auth/auth.token.read/slot.json"
---

`auth.token.read` is a slot in the `auth` namespace, in Hyperlambda, the language of Magic Cloud. Validates a JWT token and verifies that it contains one of the required roles.

* **Value** (`jwt`), required: JWT token to validate

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[roles]` | string | yes | Comma-separated roles required by the token. |

### Guide

[How to use `auth.token.read`](/plugins/magic.lambda.auth/auth.token.read/)

### JSON declaration

This is the complete declaration of `auth.token.read`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "auth.token.read",
  "description": "Validates a JWT token and verifies that it contains one of the required roles",
  "signature": {
    "input": {
      "kind": "jwt",
      "description": "JWT token to validate",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "roles": {
        "type": "string",
        "kind": "role",
        "description": "Comma-separated roles required by the token",
        "required": true,
        "mode": "ValueOrExpression",
        "cardinality": "ExactlyOne",
        "role": "Option",
        "projection": "Value"
      }
    }
  }
}
```

</details>

---

[&larr; `auth.ticket.verify`](/reference/slots/auth/auth.ticket.verify/) | [all `auth.*` slots](/reference/slots/auth/) | [`auth.token.verify` &rarr;](/reference/slots/auth/auth.token.verify/)


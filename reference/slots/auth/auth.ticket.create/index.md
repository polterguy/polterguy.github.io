---
title: "[auth.ticket.create]"
description: "auth.ticket.create is a slot in the auth namespace of Magic Cloud. Issues a signed JWT carrying the supplied username, roles, and claims; typically returned after a successful login."
generated: true
llms: "guide"
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

### Constraints

* **AtMostOneOf**: Use either absolute [expires] or relative [duration] (`[expires]`, `[duration]`)

### Guide

<!-- guide -->
This slot creates a new JWT token for you, and accepts a username and optionally a list of roles. Below
is some example usage.

```
auth.ticket.create
   username:foo
   roles
      .:howdy
      .:world
```

Like all auth related slots, it only makes sense to invoke from within a context of having an authorised
user, such as an HTTP endpoint intended to be invoked by an authenticated user.
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.auth](/plugins/magic.lambda.auth/) plugin, which documents every slot it contains.
* Discussed in [RS256 signing and [auth.jwks]](/plugins/magic.lambda.auth/rs256-signing-and-auth-jwks/).

### JSON declaration

This is the complete declaration of `auth.ticket.create`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "auth.ticket.create",
  "description": "Issues a signed JWT carrying the supplied username, roles, and claims; typically returned after a successful login",
  "signature": {
    "children": {
      "username": {
        "type": "string",
        "kind": "username",
        "description": "Username to put in the ticket",
        "required": true,
        "mode": "ValueOrExpression",
        "cardinality": "ExactlyOne",
        "role": "Option",
        "projection": "Value"
      },
      "roles": {
        "type": "lambda",
        "kind": "role-list",
        "description": "Roles to put in the ticket",
        "required": false,
        "mode": "StructuredArguments",
        "cardinality": "ZeroOrOne",
        "role": "StructuredObject",
        "projection": "Children",
        "children": {
          "*": {
            "type": "string",
            "kind": "role",
            "description": "List item",
            "required": false,
            "mode": "ValueOrExpression",
            "cardinality": "ZeroOrMore",
            "role": "Option",
            "projection": "Value"
          }
        }
      },
      "claims": {
        "type": "lambda",
        "description": "Claims to put in the ticket",
        "required": false,
        "mode": "StructuredArguments",
        "cardinality": "ZeroOrOne",
        "role": "DynamicMap",
        "projection": "Children",
        "children": {
          "*": {
            "type": "string",
            "kind": "jwt-claim",
            "description": "Named map entry",
            "required": false,
            "mode": "ValueOrExpression",
            "cardinality": "ZeroOrMore",
            "role": "Option",
            "projection": "Value"
          }
        }
      },
      "expires": {
        "type": "DateTime",
        "description": "Absolute UTC expiration time",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      },
      "duration": {
        "type": "long",
        "description": "Relative expiration duration in minutes",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      }
    },
    "constraints": [
      {
        "description": "Use either absolute [expires] or relative [duration]",
        "values": [
          "expires",
          "duration"
        ],
        "kind": "AtMostOneOf"
      }
    ],
    "output": {
      "mode": "Value",
      "kind": "jwt,text",
      "description": "Resolves to the created JWT ticket string"
    }
  }
}
```

</details>

---

[all `auth.*` slots](/reference/slots/auth/) | [`auth.ticket.get` &rarr;](/reference/slots/auth/auth.ticket.get/)


---
title: "[auth.ticket.refresh]"
description: "auth.ticket.refresh is a slot in the auth namespace of Magic Cloud. Issues a new JWT with an extended expiration based on the current ticket, so active users don't get logged out."
generated: true
llms: false
slot_json: "/reference/slots/auth/auth.ticket.refresh/slot.json"
---

`auth.ticket.refresh` is a slot in the `auth` namespace, in Hyperlambda, the language of Magic Cloud. Issues a new JWT with an extended expiration based on the current ticket, so active users don't get logged out.

* **Returns**: Resolves to the refreshed JWT ticket string

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[expires]` | DateTime | no | Absolute UTC expiration time. |
| `[duration]` | long | no | Relative expiration duration in minutes. |

### Constraints

* **AtMostOneOf**: Use either absolute [expires] or relative [duration] (`[expires]`, `[duration]`)

Guide: [How to use [auth.ticket.refresh]](/plugins/magic.lambda.auth/#how-to-use-authticketrefresh)

### JSON declaration

This is the complete declaration of `auth.ticket.refresh`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "auth.ticket.refresh",
  "description": "Issues a new JWT with an extended expiration based on the current ticket, so active users don't get logged out",
  "signature": {
    "children": {
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
      "description": "Resolves to the refreshed JWT ticket string"
    }
  }
}
```

</details>

---

[&larr; `auth.ticket.in-role`](/reference/slots/auth/auth.ticket.in-role/) | [all `auth.*` slots](/reference/slots/auth/) | [`auth.ticket.verify` &rarr;](/reference/slots/auth/auth.ticket.verify/)


---
title: "[auth.ticket.verify]"
description: "auth.ticket.verify is a slot in the auth namespace of Magic Cloud. Verifies that the current user is authenticated and optionally in one of the specified roles."
generated: true
llms: false
slot_json: "/reference/slots/auth/auth.ticket.verify/slot.json"
---

`auth.ticket.verify` is a slot in the `auth` namespace, in Hyperlambda, the language of Magic Cloud. Verifies that the current user is authenticated and optionally in one of the specified roles.

* **Value** (`role-list`), optional: Optional comma-separated roles to require

### Guide

[How to use `auth.ticket.verify`](/plugins/magic.lambda.auth/auth.ticket.verify/)

### JSON declaration

This is the complete declaration of `auth.ticket.verify`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "auth.ticket.verify",
  "description": "Verifies that the current user is authenticated and optionally in one of the specified roles",
  "signature": {
    "input": {
      "kind": "role-list",
      "description": "Optional comma-separated roles to require",
      "required": false,
      "mode": "ValueOrExpression"
    }
  }
}
```

</details>

---

[&larr; `auth.ticket.refresh`](/reference/slots/auth/auth.ticket.refresh/) | [all `auth.*` slots](/reference/slots/auth/) | [`auth.token.read` &rarr;](/reference/slots/auth/auth.token.read/)


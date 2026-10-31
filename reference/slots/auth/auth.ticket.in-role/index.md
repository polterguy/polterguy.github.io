---
title: "[auth.ticket.in-role]"
description: "auth.ticket.in-role is a slot in the auth namespace of Magic Cloud. Returns true if the current ticket belongs to one of the specified roles."
generated: true
llms: "guide"
slot_json: "/reference/slots/auth/auth.ticket.in-role/slot.json"
---

`auth.ticket.in-role` is a slot in the `auth` namespace, in Hyperlambda, the language of Magic Cloud. Returns true if the current ticket belongs to one of the specified roles.

* **Value** (`role`), required: Comma-separated roles to test for
* **Returns**: Returns true if the current ticket belongs to at least one of the comma-separated roles

### Guide

<!-- guide -->
This slot verifies that the currently authenticated user belongs to one or more roles provided as
a comma separated list of names. Contrary to the **[auth.ticket.verify]** slot this slot will _not_
throw an exception if the user does not belong to one or more roles, but simply return false.
Below is example usage.

```
auth.ticket.in-role:root,admin,guest
```

Like all auth related slots, it only makes sense to invoke from within a context of having an authorised
user, such as an HTTP endpoint intended to be invoked by an authenticated user.
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.auth](/plugins/magic.lambda.auth/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `auth.ticket.in-role`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "auth.ticket.in-role",
  "description": "Returns true if the current ticket belongs to one of the specified roles",
  "signature": {
    "input": {
      "kind": "role",
      "description": "Comma-separated roles to test for",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "output": {
      "mode": "Value",
      "kind": "boolean",
      "description": "Returns true if the current ticket belongs to at least one of the comma-separated roles"
    }
  }
}
```

</details>

---

[&larr; `auth.ticket.get`](/reference/slots/auth/auth.ticket.get/) | [all `auth.*` slots](/reference/slots/auth/) | [`auth.ticket.refresh` &rarr;](/reference/slots/auth/auth.ticket.refresh/)


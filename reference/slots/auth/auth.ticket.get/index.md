---
title: "[auth.ticket.get]"
description: "auth.ticket.get is a slot in the auth namespace of Magic Cloud. Returns the current ticket username, roles, and claims."
generated: true
llms: "guide"
slot_json: "/reference/slots/auth/auth.ticket.get/slot.json"
---

`auth.ticket.get` is a slot in the `auth` namespace, in Hyperlambda, the language of Magic Cloud. Returns the current ticket username, roles, and claims.

* **Returns**: Resolves to the username in value and roles and claims as child nodes

### Guide

<!-- guide -->
This slot returns the currently authenticated user, its roles, and what claims the user has. Below is example
usage. The slot returns the username as the value of its invocation and the roles as a **[roles]** list.

```
auth.ticket.get
```

Like all auth related slots, it only makes sense to invoke from within a context of having an authorised
user, such as an HTTP endpoint intended to be invoked by an authenticated user.
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.auth](/plugins/magic.lambda.auth/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `auth.ticket.get`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "auth.ticket.get",
  "description": "Returns the current ticket username, roles, and claims",
  "signature": {
    "output": {
      "mode": "Both",
      "kind": "username,text",
      "description": "Resolves to the username in value and roles and claims as child nodes"
    }
  }
}
```

</details>

---

[&larr; `auth.ticket.create`](/reference/slots/auth/auth.ticket.create/) | [all `auth.*` slots](/reference/slots/auth/) | [`auth.ticket.in-role` &rarr;](/reference/slots/auth/auth.ticket.in-role/)


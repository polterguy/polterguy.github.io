---
title: "How to use [auth.ticket.create]"
description: "How to use [auth.ticket.create] - This slot creates a new JWT token for you, and accepts a username and optionally a list of roles."
generated: true
guide: true
---

This is the guide to [`auth.ticket.create`](/reference/slots/auth/auth.ticket.create/), whose reference page has its arguments, constraints and declaration.

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

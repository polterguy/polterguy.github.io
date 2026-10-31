---
title: "How to use [auth.ticket.get]"
description: "How to use [auth.ticket.get] - This slot returns the currently authenticated user, its roles, and what claims the user has."
generated: true
guide: true
---

The reference page of [`auth.ticket.get`](/reference/slots/auth/auth.ticket.get/) has its arguments, constraints and declaration.

This slot returns the currently authenticated user, its roles, and what claims the user has. Below is example
usage. The slot returns the username as the value of its invocation and the roles as a **[roles]** list.

```
auth.ticket.get
```

Like all auth related slots, it only makes sense to invoke from within a context of having an authorised
user, such as an HTTP endpoint intended to be invoked by an authenticated user.

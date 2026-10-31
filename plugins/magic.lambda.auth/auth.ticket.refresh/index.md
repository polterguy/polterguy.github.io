---
title: "How to use [auth.ticket.refresh]"
description: "How to use [auth.ticket.refresh] - This slot returns a new JWT token from an old existing (and valid) token."
generated: true
guide: true
---

The reference page of [`auth.ticket.refresh`](/reference/slots/auth/auth.ticket.refresh/) has its arguments, constraints and declaration.

This slot returns a new JWT token from an old existing (and valid) token. However, the new token will
have a new expiration date, further into the future, allowing you to create a timer that occasionally
invokes the server to create a new token, preventing the user from being logged out due to having his
or her JWT token becoming expired.

```
auth.ticket.refresh
```

Like all auth related slots, it only makes sense to invoke from within a context of having an authorised
user, such as an HTTP endpoint intended to be invoked by an authenticated user.

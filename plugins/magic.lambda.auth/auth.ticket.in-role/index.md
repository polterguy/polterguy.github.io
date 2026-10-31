---
title: "How to use [auth.ticket.in-role]"
description: "How to use [auth.ticket.in-role] - This slot verifies that the currently authenticated user belongs to one or more roles provided as a comma separated list of names."
generated: true
guide: true
---

This is the guide to [`auth.ticket.in-role`](/reference/slots/auth/auth.ticket.in-role/), whose reference page has its arguments, constraints and declaration.

This slot verifies that the currently authenticated user belongs to one or more roles provided as
a comma separated list of names. Contrary to the **[auth.ticket.verify]** slot this slot will _not_
throw an exception if the user does not belong to one or more roles, but simply return false.
Below is example usage.

```
auth.ticket.in-role:root,admin,guest
```

Like all auth related slots, it only makes sense to invoke from within a context of having an authorised
user, such as an HTTP endpoint intended to be invoked by an authenticated user.

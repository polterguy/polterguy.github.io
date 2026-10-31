---
title: "How to use [auth.ticket.verify]"
description: "How to use [auth.ticket.verify] - This slot verifies that the currently authenticated user belongs to one or more roles provided as a comma separated list of names."
generated: true
guide: true
---

This is the guide to [`auth.ticket.verify`](/reference/slots/auth/auth.ticket.verify/), whose reference page has its arguments, constraints and declaration.

This slot verifies that the currently authenticated user belongs to one or more roles provided as
a comma separated list of names. If the user does not belong to any of the specified roles, the
slot will throw an exception. Below is example usage.

```
auth.ticket.verify:root,admin,guest
```

Like all auth related slots, it only makes sense to invoke from within a context of having an authorised
user, such as an HTTP endpoint intended to be invoked by an authenticated user.

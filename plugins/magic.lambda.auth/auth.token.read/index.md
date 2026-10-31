---
title: "How to use [auth.token.read]"
description: "How to use [auth.token.read] - This slot validates a JWT token and verifies that it contains at least one of the roles in its [roles] argument, a comma separated list."
generated: true
guide: true
---

The reference page of [`auth.token.read`](/reference/slots/auth/auth.token.read/) has its arguments, constraints and declaration.

This slot validates a JWT token and verifies that it contains at least one of the roles in its **[roles]** argument, a comma separated list. Below is an example.

```
.token:YOUR_JWT_TOKEN_HERE
auth.token.read:x:@.token
   roles:admin, root
```

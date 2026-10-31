---
title: "How to use [magic.auth.ensure-role]"
description: "How to use [magic.auth.ensure-role] - This slot allows you to ensure that the specified role exists, and if not, create it."
guide: true
slots: ["magic.auth.ensure-role"]
---

This slot allows you to ensure that the specified role exists, and if not, create it. This is a useful slot when
you create your own Hyperlambda modules, and your module depends upon some role existing in the system. Typically
you'd invoke this slot from one of your module's startup files, since these are executed both during startup and
during installation of your module. Below is an example of usage.

```
signal:magic.auth.ensure-role
   role:foo-role
   description:This is the foo role
```

If you execute the above Hyperlambda and go to Users & Roles afterwards, you will see how you now
have a _"foo-role"_ in your system.

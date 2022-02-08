---
title: Administrating roles
description: Magic's authorisation system is based upon role based access, where you grant access to some parts of your system based upon roles, for then to associate users with these roles somehow.
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/og-auth.jpg"
---

# Administrating roles

This component allows you to manage and administrate roles in your system, and/or
create new roles, fine tuning access to your backend through a role based access system.
Below is a screenshot of the component.

![Roles in Magic](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/auth.jpg)

Notice, all access in Magic is based upon roles, implying all users belonging to the same role(s)
have access to the same parts of your backend. This makes it easier to provide access to specific parts
of your system(s), and/or also see which parts of your system specific users have access to. To create
a new role click the plus button in the top/right corner of the component.

## Internals

Magic does _not_ create _"access rights"_ associations for roles. Instead the system allows individual
endpoints to declare themselves which roles are allowed to invoke the endpoint. This is done by invoking
**[auth.ticket.verify]** in your Hyperlambda code, and pass in a comma separated list of roles that are
allowed to invoke the endpoint. Below is an example.

```
// Some Hyperlambda endpoint file.
auth.ticket.verify:root, admin
```

The above Hyperlambda code will throw an exception if the user invoking the code does not belong
to either the _"admin"_ role or the _"root"_ role. Importanly, the system does not validate that
these roles exists, only that the JWT token the client submits contains this role in its claims.
This reduces the number of touch points related to authorisation in Magic, for the cost of making
it slightly more difficult to see which endpoints each user, and/or role is allowed to invoke.
To see _"access rights"_ for a specific role, you'll have to use the _"Endpoints"_ menu item,
which will show you which roles are allowed to invoke your endpoints. Below is a screenshot
illustrating this.

![Authorisation in Hyperlambda endpoints](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/endpoints.jpg)

Above you can see how the _"Authorization"_ object for that particular endpoint has the value of _"root, admin"_
implying only root users and admin users are allowed to invoke it. If a user not belonging to any
of the previously mentioned roles invokes the endpoint, and exception will be thrown, and the rest
of your Hyperlambda file will not execute.

* [Back to middleware documentation](/documentation/magic/)
* [Back to main documentation](/documentation/)

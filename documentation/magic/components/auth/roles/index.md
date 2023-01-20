---
title: Administrating roles
description: Magic's authorisation system is based upon role based access, where you grant access to some parts of your system based upon roles, for then to associate users with these roles somehow.
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/og-auth.jpg"
---

# Administrating roles

The users and roles component allows you to manage and administrate roles in your system, and/or
create new roles, fine tuning access to your backend through a role based access system.

![Users in Magic](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/auth.jpg)

Notice, all access in Magic is based upon roles, implying all users belonging to the same role(s)
have access to the same parts of your backend. This makes it easier to provide access to specific parts
of your system(s), and/or also see which parts of your system specific users have access to. This is referred
to as RBAC or Role Based Access Control.

To create a new role choose _"Role management"_ and click the plus button in the top/right corner of the component.

## Internals

Magic does _not_ create _"access rights"_ associations for roles. Instead the system allows individual
endpoints to declare themselves which roles are allowed to invoke the endpoint. This is often referred to
as _"Inversion of Control"_ or IoC. This is done by invoking **[auth.ticket.verify]** from your Hyperlambda code,
and pass in a comma separated list of roles that are allowed to invoke the endpoint. Below is an example.

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
and click the endpoint in question, which will show you which roles are allowed to invoke your
endpoints.

![Authorisation in Hyperlambda endpoints](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/endpoints.jpg)

If a user not belonging to any of roles required to invoke the endpoint, an exception will be thrown, and the rest
of your Hyperlambda file will not execute. You can also retrieve the access rights associations
for all endpoints in the system from your own code by invoking the `magic/system/auth/endpoints`
endpoint. This endpoint does not require authentication or authorisation, but returns all
access rights associations for every single endpoint in your backend, allowing you to create
frontend authorisation guards, dynamically building your frontend UI, according to which
endpoints the user is legally allowed to invoke, which again of course is determined by
what role(s) the user belongs to. The return value from this endpoint will resemble the following.

```json
[
  {
    "path": "magic/foo/bar1",
    "verb": "get"
  },
  {
    "path": "magic/foo/bar2",
    "verb": "get",
    "auth": [
      "root",
      "admin"
    ]
  },
  {
    "path": "magic/foo/bar3",
    "verb": "post",
    "auth": [
      "*"
    ]
  }
]
```

In the above example the first endpoint can be invoked by anyone, including a user who is not authenticated
at all. While the second endpoint can only be invoked by _"admin"_ or _"root"_ users. The third endpoint
can be invoked by any user, but the user must be authenticated to invoke the endpoint. Notice, the `auth/endpoints`
endpoint caches its result on the server for 5 minutes, implying if you create new endpoints, and/or change
the roles requirements for an endpoint, you'll either have to wait 5 minutes before the changes takes effect,
or explicitly purge your server side cache.

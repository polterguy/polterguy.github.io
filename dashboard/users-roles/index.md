---
title: Users & Roles
description: Tired of creating authentication and authorisation code? Magic contains both of these constructs out of the box, allowing you to use Magic's existing HTTP endpoints to authenticate your users.
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/auth.jpg"
---

The Users & Roles component allows you to manage and administrate your users and roles in your system, and/or
create new users and roles. This component
is what allows you to control how others are accessing your system. You might for instance have 3 different roles
in your company, being c-level executives, managers and employers. Typically these 3 different roles should not
have access to do the same things, so you want to associate users belonging to these different roles to different
roles in Magic.

![Users and roles administration in Magic](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/auth.jpg)

## Magic's authentication and authorization internals

Magic is built upon [JWT](https://jwt.io) authentication and authorisation. This is a commonly used web standard, and allows
you to easily use its existing authentication and authorisation system in your own code. JWT implies JSON Web Token,
and is typically transmitted from your frontend to your backend as a _"Bearer"_ token in your _"Authorization"_ HTTP header.

Each user again belongs to one or more roles, and you assign access rights to parts of your system by declaring what access a
role has. This is referred to as RBAC security, and implies Role Based Access Control. This makes it easy for you to see
what access rights an individual user has by seeing what role(s) the user belongs to.

## Managing users and roles

The users component is divided up into two parts. One part allows you to manage your users, and the other
part allows you to manage your roles. You can create as many roles and users as you wish.

Users again have extra fields, which can be any information you wish - However, by default Magic will only
handle email and name, allowing you to associate a name and an email address with users you create in your
cloudlet.

## Users and roles internals

All access in Magic is based upon roles, implying all users belonging to the same role(s)
have access to the same parts of your backend. This makes it easier to provide access to specific parts
of your system(s), and/or also see which parts of your system specific users have access to. This is referred
to as RBAC or Role Based Access Control. To create a new role choose _"Role management"_ and click the plus
button in the top/right corner of the component.

Magic does _not_ create _"access rights"_ associations for roles. Instead the system allows individual
endpoints to declare themselves which roles are allowed to invoke the endpoint. This is often referred to
as _"Inversion of Control"_ or IoC. This is done by invoking **[auth.ticket.verify]** from your Hyperlambda code,
and pass in a comma separated list of roles that are allowed to invoke the endpoint.

```
// Some Hyperlambda endpoint file.
auth.ticket.verify:root, admin
```

The above will throw an exception if the user is not authenticated, or does not belong to either the admin
role or the root role.

## Consuming the auth component in your own apps

The authentication and authorisation system in Magic is very flexible, and allows you to consume it from
your own apps. The auth system is built as a _"half fabricated auth system"_, allowing you to implement it
any ways you see fit, to customise it according to your needs.

In the video below, I am creating a custom registration module in 15 minutes if you're interested in seeing
how to create your own custom auth module.

<iframe style="margin-left: auto; margin-right: auto; width: 560px; max-with: 100%; display: block;" width="560" height="315" src="https://www.youtube.com/embed/Ntunzh-DdaY" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

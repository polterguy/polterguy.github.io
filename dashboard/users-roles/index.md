---
title: Users & Roles
description: Documentation for Magic's User & Roles component, allowing you to use an RBAC-based authentication and authorisation mechanism for your own code.
header:
  image: /assets/images/wizard-helping-his-village.webp
---

The Users & Roles component allows you to manage and administrate users and roles in your system, and/or create new users and roles. This component is what allows you to control how others are accessing your system. You might for instance have 3 different roles in your company, being C-level executives, managers, and employers. Typically these 3 different roles should not have access to the same parts, so you want to associate users belonging to these different roles to different roles in Magic.

![Screenshot of how to create a new user in Magic](/images/auth.jpg)

## Managing users and roles

The users component is divided up into two parts. One part allows you to manage your users, and the other part allows you to manage your roles. You can create as many roles and users as you wish.

Users again have extra fields, which can be any information you wish - However, by default Magic will only handle email and name, allowing you to associate a name and an email address with users you create in your cloudlet.

## Authentication and authorization internals

Magic is built upon [JWT](https://jwt.io) authentication and authorisation. This is a commonly used web standard, and allows you to easily use its existing authentication and authorisation system in your own code. JWT implies JSON Web Token, and is typically transmitted from your frontend to your backend as a _"Bearer"_ token in your _"Authorization"_ HTTP header.

## Users and roles internals

All access in Magic is based upon roles, implying by default all users belonging to the same role(s) have access to the same parts of your backend. This makes it easier to provide access to specific parts of your system(s), and/or also see which parts of your system specific users have access to. This is referred to as RBAC or Role Based Access Control.

Magic does _not_ create _"access rights"_ associations for roles. Instead the system allows individual endpoints to declare themselves what roles are allowed to invoke the endpoint. This is done by invoking **[auth.ticket.verify]** from your Hyperlambda code, and pass in a comma separated list of roles that are allowed to invoke the endpoint. Below is how you would lock down an endpoints from being accessed by users not belonging to either the root role or the admin role.

```
// Some Hyperlambda endpoint file.
auth.ticket.verify:root, admin
```

The above will throw an exception if the user is not authenticated, or does not belong to either the admin role or the root role.

## Rolling your own auth

The authentication and authorisation system in Magic is very flexible, and allows you to consume it from your own apps. The auth system is built as a _"half fabricated auth system"_, allowing you to implement it any ways you see fit, to customise it according to your needs.

In the video below, I am creating a custom registration module in 15 minutes if you're interested in seeing how to create your own custom auth module.

<iframe style="margin-left: auto; margin-right: auto; width: 560px; max-with: 100%; display: block;" width="560" height="315" src="https://www.youtube.com/embed/Ntunzh-DdaY" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>


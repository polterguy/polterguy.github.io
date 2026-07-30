---
title: Users & Roles
description: Secure your own code with Magic's role-based access control (RBAC), managing users, roles, authentication, and authorisation from one component.
header:
  image: /assets/images/hero/users-roles.png
  og_image: /assets/images/hero/users-roles-og.png
  image_description: Users and roles
faq:
  - q: "What is the Users and roles component?"
    a: "A graphical user interface for managing your application's users and roles, built on role based access control (RBAC)."
  - q: "How does authentication work in Magic?"
    a: "Magic uses JWT (JSON Web Token) authentication, transmitted as a Bearer token in the Authorization HTTP header. Magic can also act as an OAuth server, and supports OIDC, letting users sign in through external identity providers such as Google or Microsoft."
  - q: "How do endpoints declare who can access them?"
    a: "Each endpoint declares its own access by invoking auth.ticket.verify with a comma separated list of roles. If the user is not authenticated or lacks the role, an exception is thrown."
  - q: "Can I build my own authentication on top of Magic?"
    a: "Yes. The auth system is deliberately built as a 'half fabricated' system you can extend and customise, for instance with your own registration flow."
---

The Users & Roles component allows you to manage and administrate users and roles in your system, and/or create new users and roles. This component is what allows you to control how others are accessing your system. You might for instance have 3 different roles in your company, being C-level executives, managers, and employees. Typically these 3 different roles should not have access to the same parts, so you want to associate users with these different roles in Magic.

![Screenshot of how to create a new user in Magic](/images/auth.jpg)

## Managing users and roles

The users component is divided up into two parts. One part allows you to manage your users, and the other part allows you to manage your roles. You can create as many roles and users as you wish.

Users again have extra fields, which can be any information you wish - However, by default Magic will only handle email and name, allowing you to associate a name and an email address with users you create in your cloudlet.

## Authentication and authorization internals

Magic is built upon [JWT](https://jwt.io) authentication and authorisation. This is a commonly used web standard, and allows you to easily use its existing authentication and authorisation system in your own code. JWT implies JSON Web Token, and is typically transmitted from your frontend to your backend as a _"Bearer"_ token in your _"Authorization"_ HTTP header.

In addition to its own username and password authentication, Magic can act as an OAuth server, and it can use OIDC (OpenID Connect) for authentication - allowing your users to sign in through an external identity provider such as Google, Microsoft, or any other OIDC-compliant provider. Regardless of how a user signs in - whether through Magic's own login, as an OAuth client, or through an OIDC identity provider - they are still mapped onto Magic's own internal roles, and access is still governed by the same internal RBAC-based system described below. This gives you the convenience of federated, standards-based sign-in, without giving up the fine-grained role-based control Magic provides over your endpoints.

![Screenshot of signing in to Magic through an external OIDC identity provider](/assets/images/oidc-login-magic.png)

## Users and roles internals

All access in Magic is based upon roles, implying by default all users belonging to the same role(s) have access to the same parts of your backend. This makes it easier to provide access to specific parts of your system(s), and/or also see which parts of your system specific users have access to. This is referred to as RBAC or Role Based Access Control.

![Screenshot of the Roles tab listing all roles with their descriptions](/assets/images/roles.jpeg)

Magic does _not_ create _"access rights"_ associations for roles. Instead the system allows individual endpoints to declare themselves what roles are allowed to invoke the endpoint. This is done by invoking **[auth.ticket.verify]** from your Hyperlambda code, and passing in a comma separated list of roles that are allowed to invoke the endpoint. Below is how you would lock down an endpoint from being accessed by users not belonging to either the root role or the admin role.

```
// Some Hyperlambda endpoint file.
auth.ticket.verify:root, admin
```

The above will throw an exception if the user is not authenticated, or does not belong to either the admin role or the root role.

## Rolling your own auth

The authentication and authorisation system in Magic is very flexible, and allows you to consume it from your own apps. The auth system is built as a _"half fabricated auth system"_, allowing you to implement it any way you see fit, to customise it according to your needs.

{% include faq.html %}

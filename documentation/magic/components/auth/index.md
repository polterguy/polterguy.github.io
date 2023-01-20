---
title: Authentication and authorisation
description: Tired of creating authentication and authorisation code? Magic contains both of these constructs out of the box, allowing you to use Magic's existing HTTP endpoints to authenticate your users.
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/og-auth.jpg"
---

# The Users and Roles component

The users and roles component allows you to manage and administrate your users and roles in your system, and/or
create new users and roles giving access to your backend somehow to your users and roles. This is the primary component you
would want to use for granting access to parts of Magic to other people.

![Users and roles administration in Magic](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/auth.jpg)

Magic is built upon [JWT](https://jwt.io) authentication and authorisation. This is a commonly used web standard, and allows
for you to easily use its existing authentication and authorisation system in your own code. JWT implies JSON Web Token,
and is typically transmitted from your frontend to your backend as a _"Bearer"_ token in your _"Authorization"_ HTTP header.

Each user again belongs to one or more roles, and you assign access rights to parts of your system by declaring what access a
role has. This is referred to as RBAC security, and implies Role Based Access Control. This makes it easy for you to see
what access rights an individual user has by seeing what role(s) the user belongs to.

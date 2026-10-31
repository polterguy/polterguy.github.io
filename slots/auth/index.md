---
title: Authentication and authorisation slots
description: Magic's dynamic slots for authentication and authorisation; authenticating users, changing passwords, creating users, and ensuring roles exist.
moved_anchors: {"magicauthauthenticate": "/slots/auth/magic.auth.authenticate/", "magicauthchange-password": "/slots/auth/magic.auth.change-password/", "magicauthcreate-user": "/slots/auth/magic.auth.create-user/", "magicauthensure-role": "/slots/auth/magic.auth.ensure-role/"}
---

## Authentication and authorisation related slots

These are slots related to authentication and authorisation, and allow you to authenticate, 
change password of users, and other things related to the _"auth"_ parts of the system. Notice, you would
rarely if ever use these slots directly, since the system contains several endpoints helping you out with
the consumption of these slots. However, to be complete, we've chosen to document these none the less.

* [`magic.auth.authenticate`](/slots/auth/magic.auth.authenticate/) - This slot authenticates a user towards your specific authentication and authorisation logic, which implies looking up the username in the magic.users database table, and ensuring the password is corre
* [`magic.auth.change-password`](/slots/auth/magic.auth.change-password/) - Allows a user to change his or her password.
* [`magic.auth.create-user`](/slots/auth/magic.auth.create-user/) - This slot allows you to create a new user in Magic, with the specified username/password combination, belonging to the specified role(s).
* [`magic.auth.ensure-role`](/slots/auth/magic.auth.ensure-role/) - This slot allows you to ensure that the specified role exists, and if not, create it.

---
title: "How to use [magic.auth.create-user]"
description: "How to use [magic.auth.create-user] - This slot allows you to create a new user in Magic, with the specified username/password combination, belonging to the specified role(s)."
guide: true
slots: ["magic.auth.create-user"]
---

This slot allows you to create a new user in Magic, with the specified username/password combination, belonging
to the specified role(s). Below is an example of usage.

```
signal:magic.auth.create-user
   username:foo
   password:bar
   roles
      .:guest
```

The above creates a new user called _"foo"_ with the password of _"bar"_ belonging to the _"guest"_ role. If you
execute the above Hyperlambda for then to go to your [Users & Roles](/dashboard/users-roles/) component item,
you will find this user. Notice, you might want to delete the user after having verified it exists.

In addition the slot handles the following optional arguments.

* __[is_hashed]__ - If true, the specified password is assumed to already be hashed
* __[extra]__ - Extra fields to associate with the user, such as name and email, as a list of type/value nodes

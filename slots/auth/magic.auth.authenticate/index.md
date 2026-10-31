---
title: "How to use [magic.auth.authenticate]"
description: "How to use [magic.auth.authenticate] - This slot authenticates a user towards your specific authentication and authorisation logic, which implies looking up the username in the magic.users database table, and ensuring..."
guide: true
slots: ["magic.auth.authenticate"]
---

This slot authenticates a user towards your specific authentication and authorisation logic, which implies
looking up the username in the `magic.users` database table, and ensuring the password is correct. If both
the username exists, and the password is correct, the slot will return a valid JWT token, allowing you to
use it as a token authorising you to act on behalf of the user, and/or return the JWT token to the client.
Below is an example assuming your root password is _"admin"_. Try to execute the following code with your
own root user's password to see how it works.

```
signal:magic.auth.authenticate
   username:root
   password:admin
```

In addition to **[username]** and **[password]** the slot handles the following optional arguments.

* __[password-check]__ - If false, the password is not verified - allowing middleware that has already verified the user through other means, such as OIDC, to create a token
* __[expires]__ - Optional explicit expiration date for the JWT token

The above would return something resembling the following.

```
signal
   ticket:eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.xxx
```

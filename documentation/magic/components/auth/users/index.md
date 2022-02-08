---
title: Administrating users
description: Magic allows you to easily create new users and grant these access to parts of the system you need for these to have access to. Combined with the registration component in Magic, this makes it very easy to manage and administrate your users.
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/og-auth.jpg"
---

# Administrating users

The users component allows you to manage and administrate users in your system, and/or
create new users, and grant access to your backend somehow. Below is a screenshot of the
component.

![Users in Magic](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/auth.jpg)

Notice, this component is especially interesting combined with the registration component, allowing others to
registers in your backend, for then to have a root-user/system-administrator grant access to the newly registered
user according to whatever role the new user should be associated with. To create a new user manually click the
plus button in the top/right corner of the component.

## Registering users

Magic allows anybody to easily register in your backend. By default the user will not have access to anything
before a _"root"_ user has granted access, and such registered users have to provide a valid email address
to register, but after the email is verified an existing root user can grant access to whatever he wants
the newly created user to be able to access. Below is a screenshot of how registering in Magic typically
looks like.

![Registering as a new user in Magic](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/og-registering.jpg)

Notice, to allow for registrations in Magic you should probably setup your SMTP configuration settings.
To accomplish this you can read [this article](/tutorials/registering/).

* [Back to middleware documentation](/documentation/magic/)
* [Back to main documentation](/documentation/)

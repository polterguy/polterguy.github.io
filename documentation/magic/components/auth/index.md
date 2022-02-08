---
title: Authentication and authorisation
description: Tired of creating authentication and authorisation code? Magic contains both of these constructs out of the box, allowing you to use Magic's existing HTTP endpoints to authenticate your users.
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/og-auth.jpg"
---

# Authentication and authorisation

This component allows you to manage and administrate your users and roles in your system, and/or
create new users giving them access to your backend somehow. This is the primary component you
would want to use for granting access to parts of Magic to other people. Below is a screenshot
of how it looks like.

![Authentication and authorisation in Magic](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/auth.jpg)

Magic is built upon JWT authentication and authorisation. This is a commonly used web standard, and allows
for you to easily use its existing authentication and authorisation system in your own code. To understand
how to achieve this, you can read the [following article](/tutorials/registering/) that explains in details
how to create your own custom registration forms wrapping Magic's existing auth system.

* [Administrating users](/documentation/magic/components/auth/users/)
* [Administrating roles](/documentation/magic/components/auth/roles/)
* [Registration tutorial](/tutorials/registering/)
* [Back to middleware documentation](/documentation/magic/)
* [Back to main documentation](/documentation/)

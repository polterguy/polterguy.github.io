---
title: Crudify your Magic database
description: When you have created your Magic database you need to generate HTTP web API endpoints wrapping your newly created database.
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/og-setup-crudify.jpg"
---

# Crudify your Magic database

When you have created your Magic database you need to generate HTTP CRUD web API endpoints wrapping your newly created database,
such that Magic can use it. Below is a screenshot of this process.

![CRUDify your Magic database](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/og-setup-crudify.jpg)

Unless you are absolute sure about what you are doing, you should _not_ change anything in this screen. The JSON payload
submitted to your backend in this process is a _"CRUD manifest"_ that tells Magic how to generate these endpoints, and if it's
not correctly applied, your Magic server will not work correctly. Click the next button in this screen to have Magic generate
these endpoints automatically for you.


* [Back to configuration](/documentation/magic/components/config/)
* [Back to middleware documentation](/documentation/magic/)
* [Back to main documentation](/documentation/)

---
title: Backend CRUD HTTP API generator
description: Magic's integrated HTTP API backend CRUD generator allows you to create web API endpoints wrapping any database you wish by simply clicking a button.
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/og-backend-crud.jpg"
---

# Backend crudifier component

This component allows you to automatically generate an HTTP CRUD web API wrapping your database. This
component is the heart of the Low-Code and Automation parts of Magic, and allows you to generate
an HTTP web API wrapping your database by literally clicking a button. Below is a screenshot of
the component.

![Backend CRUD generator](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/backend-crud.jpg)

To use the component you must first select a database. Then you can optionally configure the
CRUD process for individual tables, such as configuring what URL your CRUD API should use, whether or
not to turn on caching of HTTP GET endpoints, what authorisation requirements each endpoint should have,
etc. Below is a screenshot of how this would look like.

![Configuring CRUD endpoints](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/configuring-crud.jpg)

The backend CRUD generator creates 5 HTTP endpoints by default for each table, if it can. To understand
how it works, you can check out [this article](/tutorials/database-crud/).

* [Back to middleware documentation](/documentation/magic/)
* [Back to main documentation](/documentation/)

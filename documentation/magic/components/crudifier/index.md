---
title: Magic's CRUD generator
description: Magic allows you to automatically generate backend HTTP endpoints, both CRUD endpoints wrapping any database of your choosing, SQL based endpoints where you supply some arbitrary SQL, in addition to fully fledged frontends accessing your automatically generated backend.
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/og-backend-crud.jpg"
---

# Magic's backend CRUD generator

The crudifier component allows you to automatically generate code, either by wrapping your database
with HTTP CRUD endpoints, and/or create HTTP endpoints based upon SQL statements, and/or create
a frontend based upon your backend. This component allows you to select a database, click a button,
for then to have thousands of lines of code automatically generated for you, wrapping your database
with HTTP backend endpoints with all CRUD operations required to manipulate records and rows in
your database. In addition the component also allows you to generate web API endpoints based upon
SQL statements, and generate frontends based upon your backend code. Below is a screenshot of the
component.

![Backend CRUD generator](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/backend-crud.jpg)

Notice, the crudifier is actually 3 components, all of whom you can find the documentation for below.
You can use the crudifier directly from the dashboard as a separate component, and/or integrated through
Hyper IDE.

* [Backend crudifier](/documentation/magic/components/crudifier/backend/)
* [SQL crudifier](/documentation/magic/components/crudifier/sql/)
* [Frontend crudifier](/documentation/magic/components/crudifier/frontend/)
* [Back to middleware documentation](/documentation/magic/)
* [Back to main documentation](/documentation/)

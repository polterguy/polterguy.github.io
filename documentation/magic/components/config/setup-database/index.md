---
title: Create your Magic database
description: Before you can use Magic you need to create its database. Magic needs an internal database to function. This database is used for storing users, roles, tasks, log items, etc.
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/og-setup-database.jpg"
---

# Create your Magic database

Before you can use Magic, you need to create your Magic database. Magic needs an internal database to function correctly.
This database is used to store users, roles, scheduled tasks, log items, etc, and during the setup process Magic will ask
you for a valid connection string to a MySQL, PostgreSQL or SQL Server database where it will create this database.
Below is a screenshot of the component.

![Creating your Magic database](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/og-setup-database.jpg)

The database connection string you choose in this process will become your default database, so it's important that you _keep_
the `{database}` parts exactly as it is. Magic will substitute this part of your connection string with your database of choice
when you create database connections, implying if you change this part of your connection string Magic will not work correctly.

When Magic has created its database it will create a _"root_" user in this database using the password of your choice, and
secure your authentication module by saving your _"auth secret"_ into your _"appsettings.json"_ file. To ensure Magic is
secured correctly it is important that you keep your root user's password a secret, and create a strong password - In addition
to that you never share your _"auth secret"_ with anyone.


* [Back to configuration](/documentation/magic/components/config/)
* [Back to middleware documentation](/documentation/magic/)
* [Back to main documentation](/documentation/)

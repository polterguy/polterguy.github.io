---
title: Create your Magic database
description: Before you can use Magic you need to create its database. Magic needs an internal database to function. This database is used for storing users, roles, tasks, log items, etc.
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/og-setup-database.jpg"
---

# Create your Magic database

Before you can use Magic, you need to create your Magic database. Magic needs an internal database to function.
This database is used to store users, roles, scheduled tasks, log items, etc, and during the setup process Magic will ask
you for a valid connection string to a MySQL, PostgreSQL, SQLite, or SQL Server database where it will create this database.
Below is a screenshot of the component.

![Creating your Magic database](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/og-setup-database.jpg)

The database connection string you choose in this process will become your default database, so it's important that you _keep_
the `{database}` parts exactly as it is. Magic will substitute the `{database}` part of your connection string with your database
of choice when you create database connections, implying if you change this part of your connection string Magic will not
work correctly.

When Magic has created its database it will create a _"root_" user in this database using the password of your choice, and
secure your authentication module by saving your _"auth secret"_ into your _"appsettings.json"_ file. To ensure Magic is
secured correctly it is important that you keep your root user's password a secret, and create a strong password - In addition
to that you never share your _"auth secret"_ with anyone. If you are super paranoid, you can manually add characters to your
_"Auth secret"_ by typing random characters into it using your keyboard. A good auth secret should at least contain 80
random characters to provide sufficient entropy for the JWT authentication module.

The _"Default time zone"_ parts allows you to associate a default time zone with dates not explicitly declaring a time zone,
and simplifies consumption of your Magic backend, since it will automatically assume date objects are from the specified
time zone if no time zone information is available in your date object. Legal values for this is as follows.

* _"None"_ - No default time zone assumptions about your date objects
* _"UTC"_ - All date objects without an explicit time zone is assumed to be in UTC time zone
* _"Local"_ - All date objects without an explicit time zone is assumed to be in your server's local time zone

The _"reCAPTCHA"_ setting allows you to declare a default reCAPTCHA site-key and secret for your backend, allowing
you to implement reCAPTCHA validaton more easily on your server.

* [Back to configuration](/documentation/magic/components/config/)
* [Back to middleware documentation](/documentation/magic/)
* [Back to main documentation](/documentation/)

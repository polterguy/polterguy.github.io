---
title: Databases
description: Magic allows you to automatically generate unit tests, or integration tests. The assumptions component allows you to automatically run all such tests to sanity check your system's health.
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/assumptions.jpg"
---

The databases component allows you to manage your connection strings, in addition to your external
and internal databases. This is your goto component if you want to connect to an external database,
and it allows you to connect to any MySQL, PostgreSQL, SQL Server or MariaDB database. Provide it with
your connection string, give your connection string a name, and click connect.

![Assumptions](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/databases.jpg)

In addition to allowing you to connect to external databases, this is also the place you go to create
a new SQLite database.

## Adding a connection string

It is important that you exchange your catalogue name, or database name, with the text _"{database}"_.
This is because Magic needs to be able to dynamically connect to multiple catalogues or databases
in your database server.

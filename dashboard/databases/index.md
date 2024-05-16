---
title: Databases
description: Magic allows you to automatically generate unit tests, or integration tests. The assumptions component allows you to automatically run all such tests to sanity check your system's health.
og_image: "/images/assumptions.jpg"
header:
  image: /assets/images/wizard-asking-oracle-of-delphi.webp
---

The databases component allows you to manage your connection strings, in addition to your external and internal databases. This is your goto component if you want to connect to an external database. It allows you to connect to any MySQL, PostgreSQL, SQL Server, or MariaDB database. Provide it with your connection string, give your connection string a name, and click connect.

![Screenshot of the databases component](/images/databases.jpg)

In addition to allowing you to connect to external databases, this is also the place you go to create a new SQLite file-based database.

## Adding a connection string

It is important that you exchange your catalogue name, or database name, with the text _"{database}"_. This is because Magic needs to be able to dynamically connect to multiple catalogues or databases in your database server. Magic needs to be able to read system databases, in addition to connecting generically to any database in your system it's got access to. This is why it'll need the above `{database}` parts in its connection string.

If you're hosting your database in for instance Azure or AWS, you might also have to white list your cloudlet's IP address. You can get the IP address by [contacting AINIRO](mailto:team@ainiro.io) and ask us about it.

## Backup your SQLite databases

Every now and then, you should download a backup of your SQLite databases to make sure you've got a local backup if something goes wrong. We have global backups of our K8S volumes as a whole, but it might also be beneficial to have local backups in your own machine too.

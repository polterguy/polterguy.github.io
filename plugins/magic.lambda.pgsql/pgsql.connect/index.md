---
title: "How to use [pgsql.connect]"
description: "How to use [pgsql.connect] - This slot opens a connection to a PostgreSQL database, and evaluates its lambda object with that connection open."
generated: true
guide: true
---

The reference page of [`pgsql.connect`](/reference/slots/pgsql/pgsql.connect/) has its arguments, constraints and declaration.

This slot opens a connection to a PostgreSQL database, and evaluates its lambda object with that connection open. It works like **[data.connect]**, except it always uses PostgreSQL. You can pass in only the name of the database, which is substituted for the `{database}` part of the generic connection string in your _"appsettings.json"_ file, or a complete connection string. Below is an example.

```
pgsql.connect:sakila
   pgsql.select:select first_name, last_name from actor limit 5
```

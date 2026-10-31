---
title: "How to use [mssql.connect]"
description: "How to use [mssql.connect] - This slot opens a connection to a Microsoft SQL Server database, and evaluates its lambda object with that connection open."
generated: true
guide: true
---

The reference page of [`mssql.connect`](/reference/slots/mssql/mssql.connect/) has its arguments, constraints and declaration.

This slot opens a connection to a Microsoft SQL Server database, and evaluates its lambda object with that connection open. It works like **[data.connect]**, except it always uses Microsoft SQL Server. You can pass in only the name of the database, which is substituted for the `{database}` part of the generic connection string in your _"appsettings.json"_ file, or a complete connection string. Below is an example.

```
mssql.connect:sakila
   mssql.select:select first_name, last_name from actor limit 5
```

---
title: "How to use [log.info]"
description: "How to use [log.info] - By default, this project will log into your magic.logentries database/table, using either MySQL, PostgreSQL, Microsoft SQL Server or SQLite."
generated: true
guide: true
---

The reference page of [`log.info`](/reference/slots/log/log.info/) has its arguments, constraints and declaration.

By default, this project will log into your `magic.log_entries` database/table, using either MySQL, PostgreSQL,
Microsoft SQL Server or SQLite. This allows you to use SQL to generate statistics on top of your logs.
An example of creating a log entry can be found below.

```
log.info:Howdy world from magic.lambda.logging
```

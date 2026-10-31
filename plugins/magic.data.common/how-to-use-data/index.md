---
title: "How to use [data.*]"
description: "How to use [data.*] - All of the [data.xxx] slots are actually just polymorphistically evaluating your specialised adapter's slots, such as for instance [data.connect], that will invoke [mysql.connect] if this is your..."
generated: true
---

This page is part of the [magic.data.common](/plugins/magic.data.common/) documentation.

All of the **[data.xxx]** slots are actually just polymorphistically evaluating your specialised adapter's
slots, such as for instance **[\[data.connect\]](/reference/slots/data/data.connect/)**, that will invoke **[\[mysql.connect\]](/reference/slots/mysql/mysql.connect/)** if this is your default
database. However, all of these slots can also be given an explicit **[database-type]** argument, being for
instance _"mssql"_, allowing you to choose a database type explicitly as you invoke it.

If you don't provide an explicit **[database-type]** argument to these slots, the default database
type will be retrieved from your _"appsettings.json"_ file, from the `magic:databases:default` value,
and substitute the _"data"_ parts with the value found from your configuration setting, to invoke
your specialised implementation. For instance, if you're using MySQL as your default database type,
and you invoke for instance **[\[data.connect\]](/reference/slots/data/data.connect/)**, this will transform into an invocation to **[\[mysql.connect\]](/reference/slots/mysql/mysql.connect/)**,
allowing you to use generic database slot invocations, ignoring your database type, creating the correct
SQL dialect for you automagically.

The following CRUD slots are documented in their own sections below.

* __[\[data.create\]](/reference/slots/data/data.create/)__ - Inserts a new row into the current open database connection
* __[\[data.update\]](/reference/slots/data/data.update/)__ - Updates rows in the current open database connection, use **[where]** to constrain which rows are affected
* __[\[data.scan\]](/reference/slots/data/data.scan/)__ - Scans rows from the current open database connection

## Database transactions

Although you should be careful with database transactions, sometimes you _really_ need them. For those cases you
can use the following 3 slots to create, rollback, and/or commit transactions towards your underlying database.

* __[\[data.transaction.create\]](/reference/slots/data/data.transaction.create/)__ - Creates a new database transaction
* __[\[data.transaction.commit\]](/reference/slots/data/data.transaction.commit/)__ - Commits an existing open transaction
* __[\[data.transaction.rollback\]](/reference/slots/data/data.transaction.rollback/)__ - Roll back an existing open transaction

**Notice** - The default logic for a database transaction, is that unless it's _explicitly committed_
before leaving scope, it will roll back by default. Below is an example of a transaction that will
rollback, since it's not explicitly committed before leaving scope.

```
data.connect:sakila
   data.transaction.create
      data.execute:delete from film_actor

      /*
       * If you uncomment the line below the
       * transaction will be committed, resulting
       * in that everything from your film_actor
       * table will be deleted.
       */
      //data.transaction.commit

data.connect:sakila

   /*
    * Notice, this still returns 5462 items, since
    * transaction was implicitly rolled back above.
    */
   data.scalar:select count(*) from film_actor
```

A transaction typically follows your connection, implying to count items
after the transaction has been rolled back, we'll need a _new_ connection, as the
above example illustrates.

---

[all of magic.data.common](/plugins/magic.data.common/) | [Aggregate results &rarr;](/plugins/magic.data.common/aggregate-results/)

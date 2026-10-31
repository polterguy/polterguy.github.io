---
title: magic.data.common
moved_anchors: {"aggregate-results": "/plugins/magic.data.common/aggregate-results/", "aliasing-column-results": "/plugins/magic.data.common/aggregate-results/#aliasing-column-results", "comparison-operators": "/plugins/magic.data.common/comparison-operators/", "database-transactions": "/plugins/magic.data.common/how-to-use-data/#database-transactions", "differences-between-join-and-where": "/plugins/magic.data.common/differences-between-join-and-where/", "escaping-characters": "/plugins/magic.data.common/comparison-operators/#escaping-characters", "explicit-arguments-declarations-for-joins": "/plugins/magic.data.common/differences-between-join-and-where/#explicit-arguments-declarations-for-joins", "extension-comparison-operators": "/plugins/magic.data.common/comparison-operators/#extension-comparison-operators", "group-by": "/plugins/magic.data.common/namespacing-columns/#group-by", "how-to-use-data": "/plugins/magic.data.common/how-to-use-data/", "how-to-use-dataconnect": "/plugins/magic.data.common/data.connect/", "how-to-use-datacreate": "/plugins/magic.data.common/data.create/", "how-to-use-datadelete": "/plugins/magic.data.common/data.delete/", "how-to-use-dataexecute": "/plugins/magic.data.common/data.execute/", "how-to-use-datascalar": "/plugins/magic.data.common/data.scalar/", "how-to-use-dataselect": "/plugins/magic.data.common/data.select/", "how-to-use-dataupdate": "/plugins/magic.data.common/data.update/", "how-to-use-sqlcreate": "/plugins/magic.data.common/sql.create/", "how-to-use-sqldelete": "/plugins/magic.data.common/sql.delete/", "how-to-use-sqlread": "/plugins/magic.data.common/sql.read/", "how-to-use-sqlupdate": "/plugins/magic.data.common/sql.update/", "joins": "/plugins/magic.data.common/joins/", "magicdatacommon-and-meta-data": "/plugins/magic.data.common/comparison-operators/#magicdatacommon-and-meta-data", "namespacing-columns": "/plugins/magic.data.common/namespacing-columns/", "paging": "/plugins/magic.data.common/aggregate-results/#paging", "the-in-comparison-operator": "/plugins/magic.data.common/comparison-operators/#the-in-comparison-operator", "the-where-argument": "/plugins/magic.data.common/the-where-argument/"}
---

This project is the generic data adapter, that transform dynamically from a lambda node
structure into SQL, and polymorphistically invokes your specialised data adapter, resulting in SQL
statements executed towards your database type of choice. In addition, it contains helper slots to give
you more _"raw"_ database access, in addition to slots helping you to open database connections,
create transactions, execute SQL, etc.


## How to use [sql.*]

These slots never executes SQL towards your data adapter, but rather simply generates your SQL, and
returns the results of the SQL generation process back to you. They're mostly intended for debugging
purposes, and/or learning purposes, and can be interchanged with their **[data.xxx]** equivalent,
and/or their **[mysql.xxx]**/**[mssql.xxx]**/**[pgsql.xxx]** equivalent, etc. You can substitute
these slots with for instance **[data.xxx]** if you wish to actually execute some SQL towards your
database adapter of choice.


## How to use [sql.*] slots

All of these slots simply generates SQL for you, using the _generic_ SQL dialect syntax,
which might or might not work for your database adapter of choice. This allows you to create
SQL statements _without_ executing anything towards your database. This allows you to play
around with the syntax, to understand how it works, and see how some semantic graph object
results in an SQL statement before using it.
All of these slots have **[data.\*]** equivalent slots, which again polymorphistically
invokes your specialised data adapter's equivalent, and/or can be parametrised with a
database type - Which again resolves to the **[mysql.\*]** equivalent if you supply
_"mysql"_ as your **[database-type]**, and/or MySQL is your default database type
as configured in your _"appsettings.json"_ file.
Hence, the documentation for these slots is also the documentation for your **[data.\*]**
slots.


## SQL injection attacks

This project protects you automatically against SQL injection attacks, and protect values, and criteria, etc -
But you should _not_ allow any potentially insecure clients to dynamically declare which columns
to select, and/or field _names_ for your `where` clauses. It will only protect your _values_,
and _not_ table names or column names against SQL injection attacks.

The project does also _not_ verify that your SQL is possible to execute towards your database, such as verifying
that specified tables or columns actually exists. It does its best however, to verify that your Hyperlambda
is structured correctly, and that it will create somewhat valid SQL - But you should *not assume* the SQL
the project generates is valid, before you have tested it.


## Creating your own data adapter

If you wish to extend Magic to support a custom database type, you can do so using C# for instance.
This project contains 4 base classes, which you can inherit from to extend and implement your custom logic.

* `SqlCreateBuilder` - Helper class to generate insert SQL statements
* `SqlDeleteBuilder` - Helper class to generate delete SQL statements
* `SqlReadBuilder` - Helper class to generate select SQL statements
* `SqlUpdateBuilder` - Helper class to generate update SQL statements

If you create your own database implementation, you'll need to inherit from the above classes, and override
whatever parts of these classes that doesn't by default work as your database type needs it to work.
If you wish to do this, you would probably benefit from looking at one of the existing specialised
implementations, such as the MySQL, SQL Server or PostgreSQL specific implementations.


## Topics

* [How to use [data.*]](/plugins/magic.data.common/how-to-use-data/) - All of the [data.xxx] slots are actually just polymorphistically evaluating your specialised adapter's slots, such as for instance [data.connect], that will invoke [mysql.connect] if this is your defa
* [Aggregate results](/plugins/magic.data.common/aggregate-results/) - You can also create aggregate results, by simply adding your aggregate as your column, such as the following illustrates.
* [Joins](/plugins/magic.data.common/joins/) - The project supports joins by parametrizing your [sql.read] invocation with [join] arguments, beneath your [table] argument(s).
* [Differences between [join] and [where]](/plugins/magic.data.common/differences-between-join-and-where/) - There is one crucial semantic difference between a [join] condition and a [where] condition, which is that the library assumes a join is always between two columns, while a where always assume you're
* ['Namespacing' columns](/plugins/magic.data.common/namespacing-columns/) - When you're joining results from multiple tables, it's often required that you specify which table you want some resulting column to be fetched from, to avoid confusing your database as to which colum
* [The [where] argument](/plugins/magic.data.common/the-where-argument/) - This argument is common for [sql.update], [sql.delete], and [sql.read], in addition to that a [join] will also be logically parsed much the same way as a [where] argument.
* [Comparison operators](/plugins/magic.data.common/comparison-operators/) - The project supports the following comparison operators.

---
title: Database meta traversal slots
description: Magic's dynamic slots for database meta data; listing databases, tables, columns, foreign keys and indexes for MySQL, SQL Server, PostgreSQL and SQLite.
moved_anchors: {"magicdbmysqlcolumns": "/slots/database-meta/magic.db.mysql.columns/", "magicdbmysqldatabases": "/slots/database-meta/magic.db.mysql.databases/", "magicdbmysqlforeignkeys": "/slots/database-meta/magic.db.mysql.foreign_keys/", "magicdbmysqlindexes": "/slots/database-meta/magic.db.mysql.indexes/", "magicdbmysqltables": "/slots/database-meta/magic.db.mysql.tables/"}
---

## Database meta traversal

All the following slots are a part of the database meta system, and allow you to retrieve meta data about your
databases, such as database names, table names, columns names, and foreign keys for tables. These slots are heavily
relied upon by the CRUDifier, as it creates a Hyperlambda backend for you, in order to determine which arguments
your HTTP endpoints require, and how to validate these during HTTP invocations towards your backend.

All these have at least 4 versions, one for SQLite, one for MySQL, one for PostgreSQL, and a fourth for SQL Server,
and their only difference is that the MySQL versions use _"mysql"_ as its slot name, SQL Server uses _"mssql"_, PostgreSQL
uses _"pgsql"_ and SQLite uses _"sqlite"_. Besides from this, they're identical in regards to their APIs, which is
the point, since it allows for these slots to be used transparently, or _"polymorphistically"_ towards any underlying
database type. In the following section, we therefore document their MySQL version, implying you'll have to exchange
the _"mysql"_ parts to test these towards a different database type.

* [`magic.db.mysql.databases`](/slots/database-meta/magic.db.mysql.databases/) - This slot returns all databases the system has access to within the specified connection string.
* [`magic.db.mysql.tables`](/slots/database-meta/magic.db.mysql.tables/) - This slot returns all tables for the specified [connection-string]/[database] combination.
* [`magic.db.mysql.columns`](/slots/database-meta/magic.db.mysql.columns/) - This slot returns all columns for the specified [connection-string]/[database]/[table] combination.
* [`magic.db.mysql.foreign_keys`](/slots/database-meta/magic.db.mysql.foreign_keys/) - This slot returns all foreign keys for the specified [connection-string]/[database]/[table] combination.
* [`magic.db.mysql.indexes`](/slots/database-meta/magic.db.mysql.indexes/) - This slot returns all indexes for the specified [connection-string]/[database]/[table] combination.

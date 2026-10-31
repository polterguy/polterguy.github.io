---
title: magic.lambda.pgsql
moved_anchors: {"how-to-use-pgsqlconnect": "/plugins/magic.lambda.pgsql/pgsql.connect/", "how-to-use-pgsqlcreate": "/plugins/magic.lambda.pgsql/pgsql.create/", "how-to-use-pgsqldelete": "/plugins/magic.lambda.pgsql/pgsql.delete/", "how-to-use-pgsqlexecute": "/plugins/magic.lambda.pgsql/pgsql.execute/", "how-to-use-pgsqlread": "/plugins/magic.lambda.pgsql/pgsql.read/", "how-to-use-pgsqlscalar": "/plugins/magic.lambda.pgsql/pgsql.scalar/", "how-to-use-pgsqlselect": "/plugins/magic.lambda.pgsql/pgsql.select/", "how-to-use-pgsqltransactioncommit": "/plugins/magic.lambda.pgsql/pgsql.transaction.commit/", "how-to-use-pgsqltransactioncreate": "/plugins/magic.lambda.pgsql/pgsql.transaction.create/", "how-to-use-pgsqltransactionrollback": "/plugins/magic.lambda.pgsql/pgsql.transaction.rollback/", "how-to-use-pgsqlupdate": "/plugins/magic.lambda.pgsql/pgsql.update/"}
---

This is the PostgreSQL data adapter for Magic. This project allows you to provide a semantic lambda structure
to its slots, which in turn will dynamically create a PostgreSQL dialect SQL statement for you, for all basic
types of CRUD SQL statements. In addition, it provides slots to open a PostgreSQL database connection, and
such allows you to declare your own SQL statements to be executed towards a PostgreSQL database. Slots
this project contains are as follows.

* __[\[pgsql.connect\]](/plugins/magic.lambda.pgsql/pgsql.connect/)__ - Connects to a database
* __[\[pgsql.create\]](/plugins/magic.lambda.pgsql/pgsql.create/)__ - Creates a single record in the specified table
* __[\[pgsql.read\]](/plugins/magic.lambda.pgsql/pgsql.read/)__ - Reads multiple records from the specified table
* __[\[pgsql.update\]](/plugins/magic.lambda.pgsql/pgsql.update/)__ - Updates a single record in the specified table
* __[\[pgsql.delete\]](/plugins/magic.lambda.pgsql/pgsql.delete/)__ - Deletes a single record in the specified table
* __[\[pgsql.select\]](/plugins/magic.lambda.pgsql/pgsql.select/)__ - Executes an arbitrary SQL statement, and returns results of reader as lambda objects to caller
* __[\[pgsql.scalar\]](/plugins/magic.lambda.pgsql/pgsql.scalar/)__ - Executes an arbitrary SQL statement, and returns the result as a scalar value to caller
* __[\[pgsql.execute\]](/plugins/magic.lambda.pgsql/pgsql.execute/)__ - Executes an arbitrary SQL statement
* __[\[pgsql.transaction.create\]](/plugins/magic.lambda.pgsql/pgsql.transaction.create/)__ - Creates a new transaction
* __[\[pgsql.transaction.commit\]](/plugins/magic.lambda.pgsql/pgsql.transaction.commit/)__ - Explicitly commits an open transaction
* __[\[pgsql.transaction.rollback\]](/plugins/magic.lambda.pgsql/pgsql.transaction.rollback/)__ - Explicitly rolls back an open transaction
* __[.db-factory.connection.pgsql]__ - Creates a PostgreSQL connection factory (private C# slot)

**Notice** - If you use any of the CRUD slots from above, the whole idea is that you can polymorphistically
use the same lambda object, towards any of the underlying database types, and the correct specific syntax
for your particular database vendor's SQL syntax will be automatically generated. This allows you to
transparently use the same lambda object, towards any of the database types Magic supports, without having to
change it in any ways.

All of the slots in this project are documented in the documentation for the _"magic.data.common"_ project.
If you replace the **[data.xxx]** or **[sql.xxx]** slots with **[pgsql.xxx]**, you will use the PgSQL specific
slots, instead of the generic, and/or polymorphistic slots.
Hence, please refer to the documentation for _"magic.data.common"_ to see the complete documentation for this
project. If you need for instance documentation about the **[pgsql.connect]** slot you should look for the
documentation for **[data.connect]**, since it's more or less the exact same documentation.

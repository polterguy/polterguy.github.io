---
title: magic.lambda.sqlite
moved_anchors: {"how-to-use-sqlitebackup": "/reference/slots/sqlite/sqlite.backup/#guide", "how-to-use-sqliteload-extension": "/reference/slots/sqlite/sqlite.load-extension/#guide"}
---

This is the SQLite data adapter for Magic. This project allows you to provide a semantic lambda structure
to its slots, which in turn will dynamically create a SQLite dialect SQL statement for you, for all basic
types of CRUD SQL statements. In addition, it provides slots to open a SQLite database connection, and
such allows you to declare your own SQL statements to be executed towards a SQLite database. Slots
this project contains are as follows.

* __[\[sqlite.connect\]](/reference/slots/sqlite/sqlite.connect/)__ - Connects to a database
* __[\[sqlite.create\]](/reference/slots/sqlite/sqlite.create/)__ - Creates a single record in the specified table
* __[\[sqlite.read\]](/reference/slots/sqlite/sqlite.read/)__ - Reads multiple records from the specified table
* __[\[sqlite.update\]](/reference/slots/sqlite/sqlite.update/)__ - Updates a single record in the specified table
* __[\[sqlite.delete\]](/reference/slots/sqlite/sqlite.delete/)__ - Deletes a single record in the specified table
* __[\[sqlite.select\]](/reference/slots/sqlite/sqlite.select/)__ - Executes an arbitrary SQL statement, and returns results of reader as lambda objects to caller
* __[\[sqlite.scalar\]](/reference/slots/sqlite/sqlite.scalar/)__ - Executes an arbitrary SQL statement, and returns the result as a scalar value to caller
* __[\[sqlite.execute\]](/reference/slots/sqlite/sqlite.execute/)__ - Executes an arbitrary SQL statement
* __[\[sqlite.transaction.create\]](/reference/slots/sqlite/sqlite.transaction.create/)__ - Creates a new transaction
* __[\[sqlite.transaction.commit\]](/reference/slots/sqlite/sqlite.transaction.commit/)__ - Explicitly commits an open transaction
* __[\[sqlite.transaction.rollback\]](/reference/slots/sqlite/sqlite.transaction.rollback/)__ - Explicitly rolls back an open transaction
* __[\[sqlite.connections.flush\]](/reference/slots/sqlite/sqlite.connections.flush/)__ - Flushed cached schemas and connection pools
* __[\[sqlite.backup\]](/reference/slots/sqlite/sqlite.backup/)__ - Creates a backup of the currently active database
* __[\[sqlite.load-extension\]](/reference/slots/sqlite/sqlite.load-extension/)__ - Loads a SQLite extension into the current connection from child-node arguments
* __[.db-factory.connection.sqlite]__ - Creates a SQLite connection factory (private C# slot)

**Notice** - If you use any of the CRUD slots from above, the whole idea is that you can polymorphistically
use the same lambda object, towards any of the underlying database types, and the correct specific syntax
for your particular database vendor's SQL syntax will be automatically generated. This allows you to
transparently use the same lambda object, towards any of the database types Magic supports, without having to
change it in any ways.

All of the slots in this project are documented in the documentation for the _"magic.data.common"_ project.
If you replace the **[data.xxx]** or **[sql.xxx]** slots with **[sqlite.xxx]**, you will use the sqlite specific
slots, instead of the generic, and/or polymorphistic slots.
Hence, please refer to the documentation for _"magic.data.common"_ to see the complete documentation for this
project. If you need for instance documentation about the **[\[sqlite.connect\]](/reference/slots/sqlite/sqlite.connect/)** slot you should look for the
documentation for **[\[data.connect\]](/reference/slots/data/data.connect/)**, since it's more or less the exact same documentation.

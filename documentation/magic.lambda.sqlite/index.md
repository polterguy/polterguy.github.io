
# magic.lambda.sqlite

This is the SQLite data adapter for Magic. This project allows you to provide a semantic lambda structure
to its slots, which in turn will dynamically create a SQLite dialect SQL statement for you, for all basic
types of CRUD SQL statements. In addition, it provides slots to open a SQLite database connection, and
such allows you to declare your own SQL statements to be executed towards a SQLite database. Slots
this project contains are as follows.

* __[sqlite.connect]__ - Connects to a database
* __[sqlite.create]__ - Creates a single record in the specified table
* __[sqlite.read]__ - Reads multiple records from the specified table
* __[sqlite.update]__ - Updates a single record in the specified table
* __[sqlite.delete]__ - Deletes a single record in the specified table
* __[sqlite.select]__ - Executes an arbitrary SQL statement, and returns results of reader as lambda objects to caller
* __[sqlite.scalar]__ - Executes an arbitrary SQL statement, and returns the result as a scalar value to caller
* __[sqlite.execute]__ - Executes an aribitrary SQL statement
* __[sqlite.transaction.create]__ - Creates a new transaction
* __[sqlite.transaction.commit]__ - Explicitly commits an open transaction
* __[sqlite.transaction.rollback]__ - Explicitly rolls back an open transaction
* __[sqlite.connections.flush]__ - Flushed cached schemas and connection pools

**Notice** - If you use any of the CRUD slots from above, the whole idea is that you can polymorphistically
use the same lambda object, towards any of the underlaying database types, and the correct specific syntax
for your particular database vendor's SQL syntax will be automatically generated. This allows you to
transparently use the same lambda object, towards any of the database types Magic supports, without having to
change it in any ways.

All of the slots in this project are documented in the documentation for the _"magic.data.common"_ project.
If you replace the **[data.xxx]** or **[sql.xxx]** slots with **[sqlite.xxx]**, you will use the sqlite specific
slots, instead of the generic, and/or polymorphistic slots.
Hence, please refer to the documentation for _"magic.data.common"_ to see the complete documentation for this
project. If you need for instance documentation about the **[sqlite.connect]** slot you should look for the
documentation for **[data.connect]**, since it's more or less the exact same documentation.

## Project website for magic.lambda.sqlite

The source code for this repository can be found at [github.com/polterguy/magic.lambda.sqlite](https://github.com/polterguy/magic.lambda.sqlite), and you can provide feedback, provide bug reports, etc at the same place.

- ![Build status](https://github.com/polterguy/magic.lambda.sqlite/actions/workflows/build.yaml/badge.svg)
- [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.sqlite&metric=alert_status)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.sqlite)
- [![Bugs](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.sqlite&metric=bugs)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.sqlite)
- [![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.sqlite&metric=code_smells)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.sqlite)
- [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.sqlite&metric=coverage)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.sqlite)
- [![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.sqlite&metric=duplicated_lines_density)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.sqlite)
- [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.sqlite&metric=ncloc)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.sqlite)
- [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.sqlite&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.sqlite)
- [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.sqlite&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.sqlite)
- [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.sqlite&metric=security_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.sqlite)
- [![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.sqlite&metric=sqale_index)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.sqlite)
- [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.sqlite&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.sqlite)

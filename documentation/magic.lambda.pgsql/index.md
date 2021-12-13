
# Magic Lambda for PostgreSQL

This is the PostreSQL data adapter for Magic. This project allows you to provide a semantic lambda structure
to its slots, which in turn will dynamically create a PgSQL dialect SQL statement for you, for all basic
types of CRUD SQL statements. In addition, it provides slots to open a PgSQL database connection, and
such allows you to declare your own SQL statements to be executed towards a PostgreSQL database. Slots
this project contains are as follows.

* __[pgsql.connect]__ - Connects to a database
* __[pgsql.create]__ - Creates a single record in the specified table
* __[pgsql.read]__ - Reads multiple records from the specified table
* __[pgsql.update]__ - Updates a single record in the specified table
* __[pgsql.delete]__ - Deletes a single record in the specified table
* __[pgsql.select]__ - Executes an arbitrary SQL statement, and returns results of reader as lambda object to caller
* __[pgsql.scalar]__ - Executes an arbitrary SQL statement, and returns the result as a scalar value to caller
* __[pgsql.execute]__ - Executes an aribitrary SQL statement
* __[pgsql.transaction.create]__ - Creates a new transaction
* __[pgsql.transaction.commit]__ - Explicitly commits an open transaction
* __[pgsql.transaction.rollback]__ - Explicitly rolls back an open transaction

**Notice** - If you use any of the CRUD slots from above, the whole idea is that you can polymorphistically
use the same lambda object, towards any of the underlaying database types, and the correct specific syntax
for your particular database vendor's SQL syntax will be automatically generated. This allows you to
transparently use the same lambda object, towards any of the database types Magic supports, without having to
change it in any ways.

All of the slots in this project are documented in the documentation for the _"magic.data.common"_ project.
If you replace the **[data.xxx]** or **[sql.xxx]** slots with **[pgsql.xxx]**, you will use the PgSQL specific
slots, instead of the generic, and/or polymorphistic slots.

Hence, please refer to the documentation for _"magic.data.common"_ to read the documentation for this
project.

## Project website

The source code for this repository can be found at [github.com/polterguy/magic.lambda.mysql](https://github.com/polterguy/magic.lambda.mysql), and you can provide feedback, provide bug reports, etc at the same place.

## Quality gates

- ![Build status](https://github.com/polterguy/magic.lambda.mysql/actions/workflows/build.yaml/badge.svg)
- [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.mysql&metric=alert_status)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.mysql)
- [![Bugs](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.mysql&metric=bugs)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.mysql)
- [![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.mysql&metric=code_smells)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.mysql)
- [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.mysql&metric=coverage)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.mysql)
- [![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.mysql&metric=duplicated_lines_density)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.mysql)
- [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.mysql&metric=ncloc)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.mysql)
- [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.mysql&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.mysql)
- [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.mysql&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.mysql)
- [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.mysql&metric=security_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.mysql)
- [![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.mysql&metric=sqale_index)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.mysql)
- [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.mysql&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.mysql)

## License

This project is the copyright(c) 2020-2021 of Thomas Hansen thomas@servergardens.com, and is licensed under the terms
of the LGPL version 3, as published by the Free Software Foundation. See the enclosed LICENSE file for details.

* [Magic Documentation](https://polterguy.github.io/)

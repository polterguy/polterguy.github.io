
# magic.lambda.mysql - Using MySQL and MariaDB from Hyperlambda

The magic.lambda.mysql project is Hyperlambda's MySQL data adapter. This project allows you to provide a semantic
lambda structure to its slots, which in turn will dynamically create a MySQL dialect SQL statement for you, for
all basic types of CRUD SQL statements. In addition, it provides slots to open a MySQL database connection, and
such allows you to declare your own SQL statements to be executed towards a MySQL database. Slots
this project contains are as follows.

* __[mysql.connect]__ - Connects to a database
* __[mysql.create]__ - Creates a single record in the specified table
* __[mysql.read]__ - Reads multiple records from the specified table
* __[mysql.update]__ - Updates a single record in the specified table
* __[mysql.delete]__ - Deletes a single record in the specified table
* __[mysql.select]__ - Executes an arbitrary SQL statement, and returns results of reader as lambda objects to caller
* __[mysql.scalar]__ - Executes an arbitrary SQL statement, and returns the result as a scalar value to caller
* __[mysql.execute]__ - Executes an aribitrary SQL statement
* __[mysql.transaction.create]__ - Creates a new transaction
* __[mysql.transaction.commit]__ - Explicitly commits an open transaction
* __[mysql.transaction.rollback]__ - Explicitly rolls back an open transaction

**Notice** - If you use any of the CRUD slots from above, the whole idea is that you can polymorphistically
use the same lambda object, towards any of the underlaying database types, and the correct specific syntax
for your particular database vendor's SQL syntax will be automatically generated. This allows you to
transparently use the same lambda object, towards any of the database types Magic supports, without having to
change it in any ways.

All of the slots in this project are documented in the documentation for the _"magic.data.common"_ project.
If you replace the **[data.xxx]** or **[sql.xxx]** slots with **[mysql.xxx]**, you will use the MySQL specific
slots, instead of the generic, and/or polymorphistic slots.
Hence, please refer to the documentation for _"magic.data.common"_ to see the complete documentation for this
project. If you need for instance documentation about the **[mysql.connect]** slot you should look for the
documentation for **[data.connect]**, since it's more or less the exact same documentation.

## Project website for magic.lambda.mysql

The source code for this repository can be found at [github.com/polterguy/magic.lambda.mysql](https://github.com/polterguy/magic.lambda.mysql), and you can provide feedback, provide bug reports, etc at the same place.

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

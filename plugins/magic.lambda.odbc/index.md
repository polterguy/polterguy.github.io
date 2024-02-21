# magic.lambda.odbc

This is the ODBC data adapter for Magic. This project provides slots to open an ODBC database
connection, and allows you to execute your own SQL statements towards an open ODBC connection. Slots
this project contains are as follows.

* __[odbc.connect]__ - Connects to a database
* __[odbc.select]__ - Executes an arbitrary SQL statement, and returns results of reader as lambda objects to caller
* __[odbc.scalar]__ - Executes an arbitrary SQL statement, and returns the result as a scalar value to caller
* __[odbc.execute]__ - Executes an aribitrary SQL statement
* __[odbc.transaction.create]__ - Creates a new transaction
* __[odbc.transaction.commit]__ - Explicitly commits an open transaction
* __[odbc.transaction.rollback]__ - Explicitly rolls back an open transaction

All of the slots in this project are documented in the documentation for the _"magic.data.common"_ project.
If you replace the **[data.xxx]** or **[sql.xxx]** slots with **[odbc.xxx]**, you will use the ODBC specific
slots, instead of the generic, and/or polymorphistic slots.
Hence, please refer to the documentation for _"magic.data.common"_ to see the complete documentation for this
project. If you need for instance documentation about the **[odbc.connect]** slot you should look for the
documentation for **[data.connect]**, since it's more or less the exact same documentation.

## ODBC data adapter drivers

Notice, Magic does _not_ install any ODBC drivers for your specific database type during installation. Hence,
depending upon which database type you want to use, you're going to have to manually make sure you install
the driver for it yourself, by adding the NuGet package for your particular database type and manually building
the _"backend.csproj"_ file yourself, using for instance the DotNet CLI. The reasons for this is because there
exists literally hundreds of different databases out there having specific ODBC data adapter drivers, and
installing all of these would be impossible for us to do.

## Magic's GitHub project page

Magic is 100% Open Source and you can find the primary project GitHub page [here](https://github.com/polterguy/magic).

## Project website for magic.lambda.odbc

The source code for this repository can be found at [github.com/polterguy/magic.lambda.odbc](https://github.com/polterguy/magic.lambda.odbc), and you can provide feedback, provide bug reports, etc at the same place.

- ![Build status](https://github.com/polterguy/magic.lambda.odbc/actions/workflows/build.yaml/badge.svg)
- [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.odbc&metric=alert_status)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.odbc)
- [![Bugs](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.odbc&metric=bugs)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.odbc)
- [![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.odbc&metric=code_smells)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.odbc)
- [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.odbc&metric=coverage)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.odbc)
- [![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.odbc&metric=duplicated_lines_density)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.odbc)
- [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.odbc&metric=ncloc)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.odbc)
- [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.odbc&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.odbc)
- [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.odbc&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.odbc)
- [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.odbc&metric=security_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.odbc)
- [![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.odbc&metric=sqale_index)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.odbc)
- [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.odbc&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.odbc)

## Copyright and maintenance

The projects is copyright Thomas Hansen 2023 - 2024, and professionally maintained by [AINIRO.IO](https://ainiro.io).

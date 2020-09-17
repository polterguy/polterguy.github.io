
# Magic Lambda MS SQL

These are the MS SQL Server data adapters for Magic. They allow you to provide a semantic
lambda strucutre to its slots, which in turn will dynamically create a MS SQL dialectic SQL statement for you, for all basic
types of SQL statements. In addition, it provides slots to open a MS SQL database connection, and such, to allow you to
declare your own SQL statements, to be executed towards a MS SQL database. Slots this project encapsulates are as follows.

* __[mssql.connect]__ - Connects to a database, either taking an entire connection string, or a reference to a configuration connection string
* __[mssql.create]__ - Creates a single redorc in the specified table
* __[mssql.delete]__ - Deletes a single record in the specified table
* __[mssql.read]__ - Reads multiple records from the specified table
* __[mssql.update]__ - Updates a single record in the specified table
* __[mssql.select]__ - Executes an arbitrary SQL statement, and returns results of reader as lambda object to caller
* __[mssql.scalar]__ - Executes an arbitrary SQL statement, and returns the result as a scalar value to caller
* __[mssql.execute]__ - Executes an aribitrary SQL statement
* __[mssql.execute-batch]__ - Executes a _"batch"_ of SQL statements, where each statement is separated by the word _"GO"_
* __[mssql.transaction.create]__ - Creates a new transaction, that will be explicitly rolled back as execution leaves scope, unless __[mssql.transaction.commit]__ is explicitly called before leaving scope
* __[mssql.transaction.commit]__ - Explicitly commits an open transaction
* __[mssql.transaction.rollback]__ - Explicitly rolls back an open transaction

Most of the above slots also have async (wait.) overloads.

**Notice** - If you use any of the CRUD slots from above, the whole idea is that you can polymorphistically use the
same lambda object, towards any of the underlaying database types, and the correct specific syntax for your particular
database vendor's SQL syntax will be automatically generated.
This allows you to transparently use the same lambda object, towards any of the supported database types, without
having to change it in any ways.

## [mssql.create], [mssql.read], [mssql.update] and [mssql.delete]

All of these slots have the _exact same syntax_ for all supported data adapters, which you can read about in the
magic.data.common section of the documentation. Just make sure you start out your CRUD slot invocations with
`mssql.` instead of `sql.` to use
them towards a Microsoft SQL Server database. You will also need to open a database connection before you invoke
these slots, unless you're only interested in generating its specific SQL command text, and not actually execute
the SQL.

**Important!** You should prefer these CRUD slots, since they completely abstract away your underlaying
database vendor's specific SQL syntax, overriding the SQL generation, such that you don't create yourself
a lockin towards a single database vendor, and their specific SQL syntax in any ways.

In addition, these slots can be semantically traversed, allowing you to for instance find all files
that somehow retrieves data from some specific table, by introspecting your Hyperlambda files, etc.
These slots are _extremely_ powerful in nature, once you've gotten used to their nature.

## [mssql.connect]

This slot will open a database connection for you. You can pass in a complete connection string (not recommended),
or only the database name if you wish. If you pass in only the database name, the generic connection string for MS SQL
from your _"appsettings.json"_ file will be used, substituting its `{database}` parts with the database of your choice.

Inside of this, which actually is a lambda **[eval]** invocation, you can use any of the other slots, requiring
an existing and open database connection to function. You can see an example below.

```
mssql.connect:northwind
   mssql.read
      table:customers
```

## [mssql.select]

This slot allows you to pass in any arbitrary SQL you wish, and it will evaluate to a `DataReader`, and return
all records as a lambda object. You can find an example below.

```
mssql.connect:sakila
   mssql.select:select top 10 first_name, last_name from customers
```

Assuming you have the _"northwind"_ database from Microsoft installed in your database, the above
Hyperlambda will return the first 10 customers from your database.

**Notice** - This slot requires MS SQL syntax type of SQL, and will not in any ways transpile towards your specific underlaying
database type. If you can, you should rather use **[mssql.read]** for instance, to avoid tying yourself down to a
specific database vendor's SQL dialect.

## [mssql.scalar]

This slot is similar to the above select slot, but will only return one value, as the value of its node after
execution, and is typically used for aggregate results. You can see an example below.

```
mssql.connect:northwind
   mssql.scalar:select count(*) from customers
```

After execution, your result will resemble the following.

```
mssql.connect
   mssql.scalar:long:100
```

## [mssql.execute]

This slot should be used if you don't expect any type of result at all, such as in for instance delete or update
invocations, where you don't care about the result of the operation. You can find an example below.

```
mssql.connect:northwind

   // Notice, will throw! (hopefully!)
   mssql.scalar:delete from non_existing_table
```

## Database transactions

Although you should be careful with database transactions, sometimes you _really_ need them. For those cases you
can use the following 3 slots to create, rollback, and/or commit transactions towards your underlaying database.

* __[mssql.transaction.create]__ - Creates a new database transaction
* __[mssql.transaction.commit]__ - Commits an existing open transaction
* __[mssql.transaction.rollback]__ - Rolls back an existing open transaction

**Notice** - The default logic for a database transaction, is that unless it's _explicitly committed_
before leaving scope, it will roll back by default. Below is an example of a transaction that will
rollback, since it's not explicitly commited before leaving scope.

```
mssql.connect:northwind
   mssql.transaction.create
      mssql.execute:delete from customers

      /*
       * If you uncomment the line below, by removing the initial
       * "." (DON'T!) - Then the transaction will be COMMITTED.
       */
      .mssql.transaction.commit

mssql.connect:northwind

   /*
    * Notice, this still returns items, since
    * transaction was implicitly rolled back above.
    */
   mssql.scalar:select count(*) from customers
```

**Notice** - A transaction will follow your connection, implying to count items
after transaction has been rolled back, we'll need a _new_ connection, as the
above example illustrates.

## Quality gates

- [![Build status](https://travis-ci.com/polterguy/documentation/magic.lambda.mssql.svg?master)](https://travis-ci.com/polterguy/documentation/magic.lambda.mssql)
- [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.mssql&metric=alert_status)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.mssql)
- [![Bugs](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.mssql&metric=bugs)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.mssql)
- [![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.mssql&metric=code_smells)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.mssql)
- [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.mssql&metric=coverage)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.mssql)
- [![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.mssql&metric=duplicated_lines_density)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.mssql)
- [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.mssql&metric=ncloc)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.mssql)
- [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.mssql&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.mssql)
- [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.mssql&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.mssql)
- [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.mssql&metric=security_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.mssql)
- [![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.mssql&metric=sqale_index)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.mssql)
- [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.mssql&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.mssql)

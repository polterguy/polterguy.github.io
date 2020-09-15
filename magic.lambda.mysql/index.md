
# Magic Lambda MySQL

This is the MySQL data adapter for [Magic](https://github.com/polterguy/magic). This project allows you to provide a semantic
lambda structure to its slots, which in turn will dynamically create a MySQL dialect SQL statement for you, for all basic
types of CRUD SQL statements. In addition, it provides slots to open a MySQL database connection, and such, to allow you to
declare your own SQL statements, to be executed towards a MySQL database. Slots this project contains are as follows.

* __[mysql.connect]__ - Connects to a database, either taking an entire connection string, or a reference to a configuration connection string.
* __[mysql.create]__ - Creates a single record in the specified table.
* __[mysql.read]__ - Reads multiple records from the specified table.
* __[mysql.update]__ - Updates a single record in the specified table.
* __[mysql.delete]__ - Deletes a single record in the specified table.
* __[mysql.select]__ - Executes an arbitrary SQL statement, and returns results of reader as lambda object to caller.
* __[mysql.scalar]__ - Executes an arbitrary SQL statement, and returns the result as a scalar value to caller.
* __[mysql.execute]__ - Executes an aribitrary SQL statement.
* __[mysql.transaction.create]__ - Creates a new transaction, that will be explicitly rolled back as execution leaves scope, unless __[mysql.transaction.commit]__ is explicitly called before leaving scope.
* __[mysql.transaction.commit]__ - Explicitly commits an open transaction.
* __[mysql.transaction.rollback]__ - Explicitly rolls back an open transaction.

Most of the above slots also have async (wait.) overloads.

**Notice** - If you use any of the CRUD slots from above, the whole idea is that you can polymorphistically use the
same lambda object, towards any of the underlaying database types, and the correct specific syntax for your particular
database vendor's SQL syntax will be automatically generated.

This allows you to transparently use the same lambda object, towards any of the supported database types, without
having to change it in any ways.

## [mysql.create], [mysql.read], [mysql.update] and [mysql.delete]

All of these slots have the _exact same syntax_ for all supported data adapters, which you can read about in the
link below. Just make sure you start out your CRUD slot invocations with `mysql.` instead of `sql.` to use
them towards a MySQL database. You will also need to open a database connection before you invoke these slots,
unless you're only interested in generating its specific SQL command text, and not actually execute the SQL.

* [Magic Data Common](https://github.com/polterguy/magic.data.common)

**Important!** You should prefer these CRUD slots, since they completely abstract away your underlaying
database vendor's specific SQL syntax, overriding the SQL generation, such that you don't create yourself
a lockin towards a single database vendor, and their specific SQL syntax in any ways.

In addition, these slots can be semantically traversed, allowing you to for instance find all files
that somehow retrieves data from some specific table, by introspecting your Hyperlambda files, etc.
These slots are _extremely_ powerful in nature, once you've gotten used to their nature.

## [mysql.connect]

This slot will open a database connection for you. You can pass in a complete connection string (not recommended),
or only the database name if you wish. If you pass in only the database name, the generic connection string for MySQL
from your _"appsettings.json"_ file will be used, substituting its `{database}` parts with the database of your choice.

Inside of this, which actually is a lambda **[eval]** invocation, you can use any of the other slots, requiring
an existing and open database connection to function. You can see an example below.

```
mysql.connect:sakila
   mysql.read
      table:actor
```

## [mysql.select]

This slot allows you to pass in any arbitrary SQL you wish, and it will evaluate to a `DataReader`, and return
all records as a lambda object. You can find an example below.

```
mysql.connect:sakila
   mysql.select:select first_name, last_name from actor limit 5
```

Assuming you have the _"sakila"_ database from Oracle installed in your database, the results of the above
will end up looking like the following.

```
mysql.connect
   mysql.select
      ""
         first_name:PENELOPE
         last_name:GUINESS
      ""
         first_name:NICK
         last_name:WAHLBERG
      ""
         first_name:ED
         last_name:CHASE
      ""
         first_name:JENNIFER
         last_name:DAVIS
      ""
         first_name:JOHNNY
         last_name:LOLLOBRIGIDA
```

Notice, this slot requires MySQL syntax type of SQL, and will not in any ways transpile towards your specific underlaying
database type. If you can, you should rather use **[mysql.read]** for instance, to avoid tying yourself down to a
specific database vendor's SQL dialect.

## [mysql.scalar]

This slot is similar to the above select slot, but will only return one value, as the value of its node after
execution, and is typically used for aggregate results. You can see an example below.

```
mysql.connect:sakila
   mysql.scalar:select count(*) from actor
```

After execution, your result will resemble the following.

```
mysql.connect
   mysql.scalar:long:200
```

## [mysql.execute]

This slot should be used if you don't expect any type of result at all, such as in for instance delete or update
invocations, where you don't care about the result of the operation. You can find an example below.

```
mysql.connect:sakila

   // Notice, will throw! (hopefully!)
   mysql.scalar:delete from `non-existing-table`
```

## Database transactions

Although you should be careful with database transactions, sometimes you _really_ need them. For those cases you
can use the following 3 slots to create, rollback, and/or commit transactions towards your underlaying database.

* __[mysql.transaction.create]__ - Creates a new database transaction
* __[mysql.transaction.commit]__ - Commits an existing open transaction
* __[mysql.transaction.rollback]__ - Rolls back an existing open transaction

**Notice** - The default logic for a database transaction, is that unless it's _explicitly committed_
before leaving scope, it will roll back by default. Below is an example of a transaction that will
rollback, since it's not explicitly commited before leaving scope.

```
mysql.connect:sakila
   mysql.transaction.create
      mysql.execute:delete from film_actor

      /*
       * If you uncomment the line below, by removing the initial
       * "." (DON'T!) - Then the transaction will be COMMITTED.
       */
      .mysql.transaction.commit

mysql.connect:sakila

   /*
    * Notice, this still returns 5462 items, since
    * transaction was implicitly rolled back above.
    */
   mysql.scalar:select count(*) from film_actor
```

**Notice** - A transaction will follow your connection, implying to count items
after transaction has been rolled back, we'll need a _new_ connection, as the
above example illustrates.

## Quality gates

- [![Build status](https://travis-ci.com/polterguy/magic.lambda.mysql.svg?master)](https://travis-ci.com/polterguy/magic.lambda.mysql)
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

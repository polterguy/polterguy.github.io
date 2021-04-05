
# Magic Data Common

This is the generic data adapter, that transform dynamically from a lambda node structure into SQL, and
polymorphistically invokes your specialised data adapter, resulting in SQL statements executed towards
your database type of choice. In addition, it contains helper slots to give you more _"raw"_ database
access, and also slots to help you open database connections, create transactions, execute SQL, etc.

## [sql.xxx] slots

These slots never executes SQL towards your data adapter, but rather simply generates your SQL, and
returns the results of the SQL generation process back to you. They're mostly intended for debugging
purposes, and/or learning purposes, and can be interchanged with their **[data.xxx]** equivalent,
and/or their **[mysql.xxx]**/**[mssql.xxx]** equivalent, etc. In this documentation we will mostly
be using these slots, but you can substitute our usage of these slots with for instance **[data.xxx]**
if you wish to actually execute some SQL towards your database adapter of choice.

## [data.xxx] slots

All of the **[data.xxx]** slots are actually just polymorphistically evaluating your specialised adapter's
slots, such as for instance **[data.connect]**, that will invoke **[mysql.connect]** if this is your default
database. However, all of these lots can also be given an explicit **[database-type]** argument, being for
instance _"mssql"_, allowing you to choose a database type explicitly as you invoke it.

If you don't provide an explicit **[database-type]** argument to these slots, the default database
type will be retrieved from your _"appsettings.json"_ file, from the `magic:databases:default` value,
and substitute the _"data"_ parts with the value found from your configuration setting, to invoke
your specialised implementation. For instance, if you're using MySQL as your default database type,
and you invoke for instance **[data.connect]**, this will transform into an invocation to **[mysql.connect]**,
allowing you to use generic database slot invocations, ignoring your database type, and to some extent
its SQL dialect.

### [data.connect]

This slot will open a database connection for you. You can pass in a complete connection string (not recommended),
or only the database name if you wish. If you pass in only the database name, the generic connection string for your
database type of choice from your _"appsettings.json"_ file will be used, substituting its `{database}` parts
with the database of your choice.

Inside of this slot, which actually is a lambda **[eval]** invocation, you can use any of the other slots, requiring
an existing and open database connection to function. You can see an example below.

```
data.connect:sakila
   data.read
      table:actor
```

**Notice**, since the **[data.connect]** slot actually takes a lambda object, you can also add any amount
of other lambda invocations inside of the lambda object supplied to the slot - Allowing you to for instance
create loops, conditional executions, etc - *Inside* of your invocation to **[data.connect]**. This is also
true for all other slots taking a lambda object, such as for instance **[data.transaction.create]**, etc.

### [data.select]

This slot allows you to pass in any arbitrary SQL you wish, and evaluate it to a `DataReader`, and return
all records as a lambda object. You can find an example below.

```
data.connect:sakila
   data.select:select first_name, last_name from actor limit 5
```

Assuming you have the _"sakila"_ database from Oracle installed in your database, and your default
database type is MySQL - The result of the above will end up looking like the following.

```
data.connect
   data.select
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

Notice, this slot requires SQL resembling your specialised database type of dialect, and will
not in any ways transpile the SQL towards your specific underlaying database type of SQL dialect.
If you can, you should rather use **[data.read]**, to avoid lockin towards a specific database
vendor's SQL dialect.

You can also select multiple result sets if you have batch type of SQL statements, containing
multiple SQL statements, and you want to return the result of all SQL statements you're executing.
You do this by providing a **[multiple-result-sets]** argument and set its value to boolean true.
If you do this, the slot will return an array of arrays, one outer array for each result set
your SQL generates.

### [data.scalar]

This slot is similar to the **[data.select]** slot, but will only return one value, as the
value of its node after execution, and is typically used for aggregate results. You can see
an example below.

```
data.connect:sakila
   data.scalar:select count(*) from actor
```

After execution, your result will resemble the following.

```
data.connect
   data.scalar:long:200
```

Yet again you should prefer the **[data.xxx]** slots if you can.

### [data.execute]

This slot should be used if you don't expect any type of result at all, such as in for instance
delete or update invocations, where you don't care about the result of the operation. You can
find an example below.

```
data.connect:sakila

   // Notice, will throw! (hopefully!)
   data.scalar:delete from non_existing_table
```

Yet again, prefer **[data.delete]** if you can.

### Database transactions

Although you should be careful with database transactions, sometimes you _really_ need them. For those cases you
can use the following 3 slots to create, rollback, and/or commit transactions towards your underlaying database.

* __[data.transaction.create]__ - Creates a new database transaction
* __[data.transaction.commit]__ - Commits an existing open transaction
* __[data.transaction.rollback]__ - Rolls back an existing open transaction

**Notice** - The default logic for a database transaction, is that unless it's _explicitly committed_
before leaving scope, it will roll back by default. Below is an example of a transaction that will
rollback, since it's not explicitly commited before leaving scope.

```
data.connect:sakila
   data.transaction.create
      data.execute:delete from film_actor

      /*
       * If you uncomment the line below the
       * transaction will be committed, resulting
       * in that everything from your film_actor
       * table will be deleted.
       */
      //data.transaction.commit

data.connect:sakila

   /*
    * Notice, this still returns 5462 items, since
    * transaction was implicitly rolled back above.
    */
   data.scalar:select count(*) from film_actor
```

**Notice** - A transaction will follow your connection, implying to count items
after the transaction has been rolled back, we'll need a _new_ connection, as the
above example illustrates.

## [sql.xxx] slots

All of these slots simply generates SQL for you, using the _generic_ SQL dialect syntax,
which might or might not work for your database adapter of choice. This allows you to create
SQL statements _without_ executing anything towards your database. This allows you to play
around with the syntax, to understand how it works, and see how some semantic graph object
results in an SQL statement before using it.

All of these slots have **[data.xxx]** equivalent slots, which again polymorphistically
invokes your specialised data adapter's equivalent, and/or can be parametrised with a
database type - Which again resolves to the **[mysql.xxx]** equivalent if you supply
_"mysql"_ as your **[database-type]**, and/or MySQL is your default database type
as configured in your _"appsettings.json"_ file.

Hence, the documentation for these slots is also the documentation for your **[data.xxx]**
slots.

### [sql.create]

This slot will generate the SQL necessary to insert a record into a database for you. Besides the table
argument, this slot can only be given one argument, which is __[values]__. Below is an example of usage.

```
sql.create
   table:table1
   values
      field1:howdy
      field2:world
```

Notice, to avoid SQL injection attacks, this slot will always return parameters expected to be passed in
from any potentially malicious clients as SQL parameters - Hence, the complete returned value of the
above Hyperlambda will be as follows.

```
sql.create:insert into 'table1' ('field1', 'field2') values (@0, @1)
   @0:howdy
   @1:world
```

The basic idea is that everything that might be dynamically injected into your data access layer,
should be consumed as `SqlParameters`, or something equivalent, to prevent SQL injection attacks
towards your database. This is true for all arguments passed in as data for all slots in the project.
The slot will in its specialized implementations return the ID of the inserted record if possible.

### [sql.read]

This slot requires only one mandatory argument, being your table name. The slot creates a select
SQL statement for you. An example can be found below.

```
sql.read
   table:foo
```

The above will result in the following SQL returned to you. **Notice**, if you're using the special implementations,
such as e.g. **[data.read]**, and/or **[mssql.read]** - The returned SQL might vary, according to your dialect. But the
results of executing the SQL will be the same.

```
select * from 'foo' limit 25
```

You can optionally supply the following arguments to this slot.

* __[columns]__ - Columns to select
* __[order]__ - Which column to order the results by
* __[direction]__ - Which direction to order your columns
* __[limit]__ - How many records to return, default is 25. Set this value to -1 to avoid having the parser inject it
* __[offset]__ - Offset of where to start returning records
* __[where]__ - Where condition
* __[join]__ - Join condition
* __[group]__ - Group by declaration

For instance, to select only the _"field1"_ column and the _"field2"_ column from _"table1"_,
and ordering descending by _"field3"_ - You can use something resembling the following.

```
sql.read
   table:table1
   order:field3
   direction:desc
   columns
      field1
      field2
```

This will result in the following SQL returned.

```
select 'field1','field2' from 'table1' order by 'field3' desc limit 25
```

**Notice** - The **[direction]** argument can _only_ be either _"asc"_ or _"desc"_, implying ascending or descending.

You can also supply multiple ordering columns, by separating them by _","_. See an example below, which also specifies
what table to use while ordering your results.

```
sql.read
   table:table1
   order:table1.field1, table1.field2
```

The above will result in the following SQL.

```
select * from 'table1' order by 'table1'.'field1','table1'.'field2' limit 25
```

#### Aggregate results

You can also create aggregate results, by simply adding your aggregate as your column, such as the
following illustrates. The reasons why this works, is because if the SQL generator finds a paranthesis in your
column declaration, it will simply ignore parsing that column altogether, and directly inject it into the
resulting SQL's columns declaration.

```
sql.read
   table:table1
   limit:-1
   columns
      count(*)
```

The above will result in the following SQL.

```
select count(*) from 'table1'
```

**Notice**, by setting **[limit]** to _"-1"_, like we do above, we avoid adding the limit parts to our SQL. Unless
you explicitly specify a limit, the default value will always be 25, to avoid accidentally exhausting your database,
and/or web server, by selecting all records from a table with millions of records.

#### Paging

To page your **[sql.read]** results, use **[limit]** and **[offset]**, such as the following illustrates.
Notice, even though we use _"limit"_ and _"offset"_ - The correct syntax will be applied for your database type,
depending upon which database type you're using - Implying for Microsoft SQL Server, it will inject MS SQL dialect,
and not MySQL dialect. But the syntax for your lambda object still remains the same, making it simpler to create
SQL dialect valid for your specific database type.

```
sql.read
   table:table1
   offset:5
   limit:10
```

The above will return the following SQL `select * from 'table1' limit 10 offset 5`. If you run the above lambda
towards Microsoft SQL server, SQL syntax specific for MS SQL will be generated.

#### Aliasing column results

You can also extract columns with an alias, _"renaming"_ the column in its result, such as the following illustrates.

```
sql.read
   table:table1
   columns
      table1.foo1
         as:howdy
      table1.foo2
         as:world
```

The above Hyperlambda will result in the following SQL.

```
select 'table1'.'foo1' as 'howdy','table1'.'foo2' as 'world' from 'table1' limit 25
```

Effectively resulting in that you'll have two columns returned after executing the above SQL, which
are `howdy` and `world`. Combining this with the join features from this project, allows you to create
any type of tabular _"projections"_ you wish.

#### Joins

The project supports joins by parametrizing your **[sql.read]** invocation with **[join]** arguments, beneath your
**[table]** argument. You can _only_ add **[join]** beneath **[table]** for **[sql.read]** invocations though.
If you have created the Sakila example database from Oracle, and you're using MySQL as your default database type,
you can execute the following MySQL join SQL statement to see a fairly complex recursive join.

```
data.connect:sakila
   data.read
      columns
         title
         description
         last_name
         first_name
      table:film
         join:film_actor
            type:inner
            on
               and
                  film.film_id:film_actor.film_id
            join:actor
               type:inner
               on
                  and
                     film_actor.actor_id:actor.actor_id
```

**Notice** - The above lambda assumes you've got Oracle's Sakila database in your MySQL instance. If you only wish to see
its resulting SQL, add the **[generate]** argument to the above root invocation, and set its value to _"true"_.

All specialised slots, dynamically building and executing some SQL towards your database, supports
the **[generate]** argument, allowing you to easily _"debug"_ your SQL statements, and see what they actually do.

```
select `film`.`title`, `film`.`description`, `actor`.`last_name`, `actor`.`first_name` from `film`
   inner join `film_actor` on `film`.`film_id` = `film_actor`.`film_id`
      inner join `actor` on `film_actor`.`actor_id` = `actor`.`actor_id`
   limit 25
```

You can recursively join as many levels as you wish, in addition to also supplying multiple join conditions for
the same join. An example of the latter can be found below.

```
sql.read
   limit:-1
   table:table1
      join:table2
         on
            and
               fk1:pk1
               fk2:pk2
```

The above lambda will result in the following SQL being generated.

```
select * from 'table1'
   inner join 'table2' on 'table1'.'fk1' = 'table2'.'pk1' and
      'table1'.'fk2' = 'table2'.'pk2'
```

**Notice** - Joining tables works exactly the same way as using a **[where]** argument, allowing you
to supply an operator for your join, such as we illustrate below, where we're using the `!=` operator,
instead of the (default) equality comparison. See the **[where]** criteria for details about comparison
operators.

```
sql.read
   limit:-1
   table:table1
      join:table2
         type:inner
         on
            and
               fk1.neq:pk1
```

The above results in the following SQL.

```
select * from 'table1' inner join 'table2' on 'table1'.'fk1' != 'table2'.'pk1'
```

The **[type]** argument to your **[join]** arguments, can be _"inner"_, _"full"_, _"left"_ or _"right"_,
resulting in the equivalent type of join for your SQL.

#### 'Namespacing' columns

When you're joining results from multiple tables, it's often required that you specify which table you want some resulting
column to be fetched from, to avoid confusing your database as to which column you want to extract, in cases where the
same column exists in multiple tables. For such cases, you can simply refer to your table first, and then the column
from that table, and separate your entities by a `.`. You can see an example of this below.

```
data.connect:sakila
   data.read
      columns

         /*
          * Prefixing result columns with table names.
          */
         film.title
         film.description
         actor.last_name
         actor.first_name

      table:film
         join:film_actor
            type:inner
            on
               and
                  film.film_id:film_actor.film_id
            join:actor
               type:inner
               on
                  and
                     film_actor.actor_id:actor.actor_id
```

The above will result in the following SQL, if you append the **[generate]** argument, and set its value to _"true"_.

```
select
   `film`.`title`,
   `film`.`description`,
   `actor`.`last_name`,
   `actor`.`first_name`
   from `film`
      inner join `film_actor` on `film`.`film_id` = `film_actor`.`film_id`
         inner join `actor` on `film_actor`.`actor_id` = `actor`.`actor_id`
   limit 25
```

**Notice** - Spacing is not applied to the actual generated SQL result, but have been applied to some of the SQL
examples in this documentation, to make the SQL more readable.

#### Group by

You can also provide a **[group]** argument to your lambda, resulting in a _"group by"_ statement injected
into the resulting SQL. Below is an example.

```
sql.read
   table:table1
   limit:-1
   columns
      col1
      count(*)
         as:count
   group
      col1
```

The above will result in the following SQL.

```
select col1, count(*) as count from 'table1' group by 'col1'
```

You can supply multiple group by columns, in addition to _"namespacing"_ your columns with your table names,
such as we illustrate below.

```
sql.read
   table:table1
   limit:-1
   columns
      count(*)
   group
      table1.foo1
      table1.foo2
```

The above of course results in the following SQL.

```
select count(*) from 'table1' group by 'table1'.'foo1','table1'.'foo2'
```

You can of course combine your **[group]** arguments with **[where]** arguments, and **[join]** arguments,
allowing you to create complex aggregate results, statistics, joining multiple tables, etc.

### [sql.update]

This slot allows you to update one or more records, in a specified **[table]**. Just like create, it requires
one mandatory argument, being **[values]**, implying columns/values you wish to update. This slot also takes
an optional **[where]** argument, which is described further down on this page. Its simplest version can be
imagined such as follows.

```
sql.update
   table:table1
   values
      field1:howdy
```

The above of course will result in the following.

```
sql.update:update 'table1' set 'field1' = @v0
   @v0:howdy
```

**Notice**, if you don't apply a **[where]** argument, then *all* records in your table will
be updated - Which is highly unlikely what your intentions are. Hence, make sure you apply a
**[where]** argument as you invoke this slot.

### [sql.delete]

This slot is for deleting records. Its **[where]** argument is applied in a similar fashion as the where
argument to **[sql.select]** and **[sql.update]**. You can find an example below.

```
sql.delete
   table:table1
   where
      and
         field1:value1
         field2:value2
```

The above will produce the following results.

```
sql.delete:delete from 'table1' where 'field1' = @0 and 'field2' = @1
   @0:value1
   @1:value2
```

### The [where] argument

This argument is common for both **[sql.update]**, **[sql.delete]** and **[sql.read]**, in addition
to that a **[join]** will also be logically parsed much the same way as a **[where]** argument. The where
argument follows a recursive structure, allowing you to supply multiple layers of `where` criteria,
being applied recursively, using some sort of comparison operator, applied to all conditions in the
same level. Its most basic usage is as follows.

```
sql.read
   table:table1
   limit:-1
   where
      and
         field1:howdy
```

The above would result in the following result.

```
sql.read:select * from 'table1' where 'field1' = @0
   @0:howdy
```

To apply multiple **[and]** criteria, you can simply add them consecutively as follows.

```
sql.read
   table:table1
   limit:-1
   where
      and
         field1:howdy
         field2:world
```

The above resulting in the following.

```
sql.read:select * from 'table1' where 'field1' = @0 and 'field2' = @1
   @0:howdy
   @1:world
```

If you exchange the above **[and]** with **[or]**, the system will use the `or` operator to
separate your arguments, such as the following illustrates.

```
sql.read
   table:table1
   limit:-1
   where
      or
         field1:howdy
         field2:world
```

The above results in the following result.

```
sql.read:select * from 'table1' where 'field1' = @0 or 'field2' = @1
    @0:howdy
    @1:world
```

You can also nest operators, producing paranthesis, creating complex conditions, such as the following
illustrates.

```
sql.read
   table:table1
   limit:-1
   where
      or
         field1:howdy
         and
            field2:world
            field3:dudes
```

Which of course results in the following result.

```
sql.read:select * from 'table1' where 'field1' = @0 or ('field2' = @1 and 'field3' = @2)
   @0:howdy
   @1:world
   @2:dudes
```

**Notice**, the parent of a list of criteria is deciding which logical operator to separate your conditions
with, contrary to traditional languages, where you separate your conditions with the logical operator, and
explicitly add paranthesis to group your levels. This might seem a little bit backwards in the beginning,
but this is a general rule with everything in Hyperlambda, and after a while will feel more natural than
the alternative. The reasons for this is to allow for semantically traverse your lambda objects, allowing
the computer to logically understand what it does more easily - Among other things.

#### Comparison operators

The project supports the following comparison operators.

* `eq` - Equality comparison, equivalent to `=`
* `neq` - Not equality comparison, equivalent to `!=`
* `mt` - More than comparison, equivalent to `>`
* `lt` - Less than comparison, equivalent to `<`
* `lteq` - Less than or equal comparison, equivalent to `<=`
* `mteq` - More than or equal comparison, equivalent to `>=`
* `like` - Like comparison, equivalent to SQL's `like` comparison
* `in` - Special comparison operator, since it requires a _list_ of values, generating an _"in"_ SQL condition

Everywhere you need to compare one field with another, such as in **[where]** or **[join]**
arguments, you can append a comparison operator to your left hand side column, such as the following
illustrates.

```
sql.read
   table:foo
   where
      and
         field1.neq:xxx
```

The above will produce the following SQL.

```
select * from 'foo' where 'field1' != @0
```

Notice the above **[field1.neq]**, which is substituted by the SQL generator to become a `!=` comparison operator
on the `field1` column versus the `xxx` argument. The comparison operator is *always* expected to be the
last parts of your _"LHS"_ (Left Hand Side) parts of your criteria - Implying the *value* of the node.

#### The [in] comparison operator

This operator is special, in that it doesn't require the caller to supply _one_ value, but rather a _list_ of values,
from where the column you compare towards must have a value matching at least _one_ of these values. An example can
be found below.

```
sql.read
   table:table1
   where
      and
         table1.field1.in
            :long:5
            :long:7
            :long:9
```

The above will generate the following SQL, in addition to returning 3 parameters to the caller.

```
select * from 'table1' where 'table1'.'field1' in (@0,@1,@2) limit 25
```

#### Escaping character

If you by some freak accident happen to have a column in one of your tables that is name for instance `neq`,
you can escape your column name, by prepending a `\` to it. See an example below.

```
sql.read
   table:table1
   where
      and
         table1.\neq:foo
```

Notice how the `\` character above results in the following SQL.

```
select * from 'table1' where 'table1'.'neq' = @0 limit 25
```

As you can see, the `\neq` is interpreted as a column name, and not a `neq` operator.

You can also escape columns entirely, if you for instance have a column that contains a `.` in its name,
such as we illustrate below.

```
sql.read
   table:table1
   where
      and
         \table1.foo:bar
```

Notice how the above lambda will interpret the `table1.foo` parts as a column name, and not as
column _"foo"_ on _"table1"_. You can see the resulting SQL below.

```
select * from 'table1' where 'table1.foo' = @0 limit 25
```

#### Extension comparison operators

You can also extend the existing comparison operators with your own, such as for instance having `ltmt`
resulting in `<>`. To do this, you'll have to register your comparison operator using the static
`AddComparisonOperator` method on the `SqlWhereBuilder` class. Below is an example.

```csharp
SqlWhereBuilder.AddComparisonOperator("ltmt", (builder, args, colNode, escapeChar) => {
    builder.Append(" <> ");
    SqlWhereBuilder.AppendArgs(args, colNode, builder, escapeChar);
});
```

The above will give you access to use `ltmt` as a comparison operator, resolving to `<>` in your SQL.

### Meta data

One of the really nice things about the semantic approach to generating SQL, is that it
allows you to retrieve meta data from your Hyperlambda snippets, asking questions such as for instance
_"find all files that somehow selects columns from the 'xxx' table"_ - And for that matter, even
dynamically change the table name, using refactoring and replacement concepts. Once you've crossed
the initial step into _meta data traversal_ in Hyperlambda, things like this, which is impossible
to achieve in traditional programming languages, becomes a commodity with Hyperlambda.

> Hyperlambda understands Hyperlambda

## SQL injection attacks

The project protects you automatically against SQL injection attacks, and protect values, and criteria, etc.
But you should _not_ allow any potentially insecure clients to dynamically declare which columns
to select, and/or field _names_ for your `where` clauses. It will only protect your _values_,
and _not_ table names or column names against SQL injection attacks.

The project does *not* verify that your SQL is possible to execute towards your database, such as verifying
that specified tables or columns actually exists. It does its best however, to verify that your Hyperlambda
is structured correctly, and that it will create valid SQL - But you should *not assume* the SQL the project
generates is valid, before you have tested it.

## Creating your own data adapter

If you wish to extend Magic to support a custom database type, you can do so using C# for instance.
This project contains 4 base classes, which you can inherit from to extend and implement your custom logic.

* `SqlCreateBuilder` - Helper class to generate insert SQL statements.
* `SqlDeleteBuilder` - Helper class to generate delete SQL statements.
* `SqlReadBuilder` - Helper class to generate select SQL statements.
* `SqlUpdateBuilder` - Helper class to generate update SQL statements.

If you create your own database implementation, you'll need to inherit from the above classes, and override
whatever parts of these classes that doesn't by default work as your database type needs it to work.
If you wish to do this, you would probably benefit from looking at one of the existing specialised
implementations, such as the MySQL or SQL Server specific implementation.

## Quality gates

- [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.data.common&metric=alert_status)](https://sonarcloud.io/dashboard?id=polterguy_magic.data.common)
- [![Bugs](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.data.common&metric=bugs)](https://sonarcloud.io/dashboard?id=polterguy_magic.data.common)
- [![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.data.common&metric=code_smells)](https://sonarcloud.io/dashboard?id=polterguy_magic.data.common)
- [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.data.common&metric=coverage)](https://sonarcloud.io/dashboard?id=polterguy_magic.data.common)
- [![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.data.common&metric=duplicated_lines_density)](https://sonarcloud.io/dashboard?id=polterguy_magic.data.common)
- [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.data.common&metric=ncloc)](https://sonarcloud.io/dashboard?id=polterguy_magic.data.common)
- [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.data.common&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.data.common)
- [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.data.common&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.data.common)
- [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.data.common&metric=security_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.data.common)
- [![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.data.common&metric=sqale_index)](https://sonarcloud.io/dashboard?id=polterguy_magic.data.common)
- [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.data.common&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=polterguy_magic.data.common)

## License

This project is the copyright(c) 2020-2021 of Thomas Hansen thomas@servergardens.com, and is licensed under the terms
of the LGPL version 3, as published by the Free Software Foundation. See the enclosed LICENSE file for details.

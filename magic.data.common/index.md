
# Magic Data Common

[![Build status](https://travis-ci.com/polterguy/magic.data.common.svg?master)](https://travis-ci.com/polterguy/magic.data.common)

This is the generic data adapter, that transform dynamically from a lambda node structure, into SQL, intended
to be executed towards your specific database implementation. If you wish to extend Magic to support a custom
database type, this is the project you'd want to extend from, to make sure you keep the exact same structure as
you create your lambda objects, intended to be converted into SQL, and executed towards some database
type. The project contains 4 base classes, which you should inherit from and extend to implement your custom logic.

* `SqlCreateBuilder` - Helper class to generate insert SQL statements.
* `SqlDeleteBuilder` - Helper class to generate delete SQL statements.
* `SqlReadBuilder` - Helper class to generate select SQL statements.
* `SqlUpdateBuilder` - Helper class to generate update SQL statements.

If you create your own database implementation, you'll need to inherit from the above classes, and override
whatever parts of these classes that doesn't by default work as your database type needs it to work.

Although the project is _not_ intended to be used directly, but rather through its special implementation,
such as the [MySQL](https://github.com/polterguy/magic.lambda.mysql) or [MS SQL](https://github.com/polterguy/magic.lambda.mssql)
adapters - You _can_ consume the project directly, and it does provide slots
for working directly with the generic adapter - Although, it will never actually execute the SQL,
but only allow you to dynamically parse a lambda object, producing generic SQL and parameters in
the process for you. The project contains the following slots.

* __[sql.create]__ - Creates an insert SQL for you, using the generic syntax for SQL
* __[sql.read]__ - Creates a select SQL for you, using the generic syntax for SQL
* __[sql.update]__ - Creates an update SQL for you, using the generic syntax for SQL
* __[sql.delete]__ - Creates a delete SQL for you, using the generic syntax for SQL

All of the above slots require you to pass in **[table]** as a mandatory argument, declaring which
table you intend to create your SQL towards. You can only supply _one_ table, but you can create joins on that
single table, allowing you to create left, right, inner and full joins, extracting data from multiple tables in
a single SQL.

## Project's intentions

This project will _never_ solve _all_ your SQL problems, and it's probably impossible to abstract away
all differences between all different database providers - But its intentions are to make it possible to
generically declare a lambda object for 80% of your use cases, which you can then later decide which database
to execute towards.

This is true due to that all generic examples in this page, can exchange their invocation to **[sql.read]**
for instance, with your specific database adapter, such as **[mysql.read]** or **[mssql.read]**, and have
it work perfectly across multiple database providers, assuming your tables and columns exists in the database
type you provide.

This allows you to polymorphistically create a lambda structure, for 80% of your cases, that you can execute
towards any database type - Completely de-coupling your database vendor's specific dialect, from your 
application's DAL, or _"Database Access Layer"_, and have this project, combined with its specialized
implementations, take care of automatically generating the dialect your particular database type requires.

## SQL injection attacks

The project protects you automatically against SQL injection attacks, and protect values, and criteria, etc.
But you should _not_ allow any potentially insecure clients to dynamically declare which columns
to select, and/or field _names_ for your `where` clauses. It will only protect your _values_,
and _not_ table names or column names against SQL injection attacks. Also, the project does not verify that
the SQL is possible to execute towards your database, such as verifying that specified tables or columns
actually exists on the database you're trying to execute your SQL towards. It does its best however, to verify
that the syntax of your SQL, is to some extent legally structured, and is valid SQL.

## [sql.create]

This slot will generate the SQL necessary to insert a record into a database for you. It can only be given
one argument, which is __[values]__. Below is an example of usage.

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

The basica idea is that everything that might be dynamically injected into your data access layer,
should be consumed as `SqlParameters`, or something equivalent, to prevent SQL injection attacks
towards your database. This is true for all arguments passed in as data for all slots in the project.

## [sql.read]

This slot requires only one mandatory argument, being your table name. The slot creates a select
SQL statement for you. An example can be found below.

```
sql.read
   table:foo
```

The above will result in the following SQL returned to you. **Notice**, if you're using the special implementations,
such as e.g. **[mysql.read]** or **[mssql.read]** - The returned SQL might vary, according to your dialect. But the
results of executing the SQL will be the same.

```
select * from 'foo' limit 25
```

You can optionally supply the following arguments to this slot.

* __[columns]__ - Columns to select.
* __[order]__ - Which column to order the results by.
* __[direction]__ - Which direction to order your columns.
* __[limit]__ - How many records to return, default is 25. Set this value to -1 to avoid having the parser inject it.
* __[offset]__ - Offset of where to start returning records.
* __[where]__ - Where condition. Described further down, since it's common for all slots that supports `where` conditions.

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

### Aggregate results

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

### Paging

To page your **[sql.read]** results, use **[limit]** and **[offset]**, such as the following illustrates.
Notice, even though we use _"limit"_ and _"offset"_ - The correct syntax will be applied for your database type,
depending upon which database type you're using - Implying for Microsoft SQL Server, it will inject MS SQL dialect,
and not MySQL dialect. But the syntax for your lambda object still remains the same, making it simpler to create
SQL syntax valid for your specific database type.

The whole intention with the project, is to provide a uniform common syntax, for creating SQL, that can be executed
towards any database type.

```
sql.read
   table:table1
   offset:5
   limit:10
```

The above will return the following SQL `select * from 'table1' limit 10 offset 5`. If you run the above lambda
towards Microsoft SQL server, SQL specific for MS SQL will be generated.

### Aliasing column results

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

Effectively resulting in that you'll have two columns returned after executing the above SQL, which are `howdy` and `world`.
Combining this with the join features from this project, allows you to create any type of tabular _"projections"_ you wish.

### Joins

The project supports joins by parametrizing your **[sql.read]** invocation with **[join]** arguments, beneath your
**[table]** argument. You can _only_ add **[join]** beneath **[table]** for **[sql.read]** invocations though.
If you have created the Sakila example database from Oracle, you can execute the following MySQL join SQL statement
to see a recursive join.

```
mysql.connect:sakila
   mysql.read
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

The above will result in the following SQL, which you can verify yourself, by parametrizing your **[mysql.read]** invocation
with a **[generate]** argument, and set its value to boolean _"true"_ to see its MySQL SQL syntax.

```
select `film`.`title`, `film`.`description`, `actor`.`last_name`, `actor`.`first_name` from `film`
   inner join `film_actor` on `film`.`film_id` = `film_actor`.`film_id`
      inner join `actor` on `film_actor`.`actor_id` = `actor`.`actor_id`
   limit 25
```

**Explanation** - The above first selects `title` and `description` from the `film` table, for then to join on `film_id`
towards `film_actor`, and then finally joining from `film_actor` towards the `actor` table, and extracting also
the `last_name` and `first_name` from the `actor` table, using `inner join` for both join operations. As you can see
above, you can recursively join as many levels as you wish, in addition to also supplying multiple join conditions for
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
to supply an operator for your join, such as we illustrate below, where we're using the _"!="_ operator,
instead of the (default) equality comparison. See the **[where]** criteria for details about operators.

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

Resulting in the following SQL.

```
select * from 'table1' inner join 'table2' on 'table1'.'fk1' != 'table2'.'pk1'
```

The **[type]** argument to your **[join]** arguments, can be _"inner"_, _"full"_, _"left"_ or _"right"_.

### Group by

You can also provide a **[group]** argument to your lambda, resulting in a _"group by"_ statement injected
into the resulting SQL. Below is an example.

```
sql.read
   table:table1
   limit:-1
   columns
      count(*)
   group
      foo1
```

The above will result in the following SQL.

```
select count(*) from 'table1' group by 'foo1'
```

You can supply multiple group by columns, in addition to _"namespacing"_ your columns, with your table names,
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

See more about _"namespacing"_ columns below.

### 'Namespacing' columns

When you're joining results from multiple tables, it's often required that you specify which table you want some resulting
column to be fetched from, to avoid confusing your database as to which column you want to extract, in cases where the
same column exists in multiple tables. For such cases, you can simply refer to your table first, and then the column
from that table, and separate your entities by a _"."_. You can see an example of this below.

```
mysql.connect:sakila
   mysql.read
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

## [sql.update]

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

## [sql.delete]

This slot works similar to the **[sql.select]** slot, except (ofc) it doesn't allow for **[join]**, and is for
deleting records. But its **[where]** argument is applied in a similar fashion. You can find an example below.

```
sql.delete
   table:table1
   where
      and
         field1:value1
         field2:value2
```

The above of course will produce the following results.

```
sql.delete:delete from 'table1' where 'field1' = @0 and 'field2' = @1
   @0:value1
   @1:value2
```

## The [where] argument

This argument is common for both **[sql.update]**, **[sql.delete]** and **[sql.read]**, in addition
to that a **[join]** will also be logically parsed much the same way as a **[where]** argument. The where
argument follows a recursive structure, allowing you to supply multiple layers of `where` criteria,
being applied recursively, using some sort of grouping operator. Its most basic usage is as follows.

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
with, contrary to traditional languages, where you separate your conditions with the logical operator.
This might seem a little bit backwards in the beginning, but this is a general rule with everything in
Hyperlambda, and after a while will feel more natural than the alternatives.

### Comparison operators

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
         field1.neq:field2
```

The above will produce the following SQL.

```
select * from 'foo' where 'field1' != 'field2'
```

Notice the above **[field1.neq]**, which is substituted by the SQL generator to become a `!=` comparison operator
on the `field1` column versus the `field2` column.

#### The [in] comparison operator

This operator is special, in that it doesn't require the caller to supply _one_ value, but rather a _list_ of values,
from where the column you compare towards, must have a value matching at least _one_ of these values. An example can
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

#### Extension comparison operators

You can also extend the existing comparison operators with your own, such as for instance having `ltmt`
implying `<>`. To do this, you'll have to register your comparison operator using the static `AddComparisonOperator`
method on the `SqlWhereBuilder` class. Below is an example.

```csharp
SqlWhereBuilder.AddComparisonOperator("ltmt", (builder, args, colNode, escapeChar) => {
    builder.Append(" <> ");
    SqlWhereBuilder.AppendArgs(args, colNode, builder, escapeChar);
});
```

The above will give you access to use `ltmt` as a comparison operator, resolving to `<>` in your SQL.

### Escaping character

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

You can also escape column entirely, if you for instance have a column that contains a `.` in its name,
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

* [Main documentation](https://polterguy.github.io/)

## Quality gates

- [![Build status](https://travis-ci.com/polterguy/magic.data.common.svg?master)](https://travis-ci.com/polterguy/magic.data.common)
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

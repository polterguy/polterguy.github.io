# Hyperlambda CRUD database endpoints

A 15 minute read, making you understand how to create CRUD
HTTP endpoints wrapping your database using Hyperlambda. In case you
didn't finish the [Hyperlambda Hello World tutorial](/tutorials/hyperlambda-hello-world),
you would probably benefit from reading it before going through with this one.

Hyperlambda supports 2 database types: Microsoft SQL Server and MySQL - But adding support
for another database, is probably easy for a seasoned C# developer. In
our previous tutorial, we executed a select SQL statement, and returned
the results back to the client as JSON. In case you don't remember how
we did this, here is some example code doing such a thing.

**Filename - "/modules/tutorials/read-data.get.hl"**

```
mysql.connect:sakila
   mysql.select:select * from actor limit 10
   return:x:-/*
```

If you want to control the columns returned, simply add them up as columns into your SQL.

## Semantic SQL

However, there exists an even better method, that we refer to as the _"semantic SQL generator"_.
This approach completely abstract away the underlaying database vendor,
and allows you to semantically declare which columns are returned - In addition to your
where clause, order clause, and paging. And what's even better, is that it transparently
generates the correct SQL towards any of your existing Magic database adapters, allowing
you to use the same structure for querying SQL Server as you would use to query MySQL.

This approach arguably reduces your database type down to a _"configurable property"_
in your end application, allowing you to use any database type, with the exact same code.
Below is an example resulting in the same SQL as the above Hyperlambda, except
this time we use the _"semantic structure"_, instead of providing _"raw"_ SQL.

```
mysql.connect:sakila
   mysql.read
      table:actor
      limit:10
   return:x:-/*
```

Notice how the above doesn't explicitly provide any SQL, but as it's being
executed towards your database adapter, its result becomes the same as the
handcoded SQL version above. You can also restrict what columns you wish to
return, such as the following illustrates.

```
mysql.connect:sakila
   mysql.read
      table:actor
      limit:10
      columns
         first_name
         last_name
   return:x:-/*
```

The above of course, will only return the _"first_name"_ and _"last_name"_
columns form your _"actor"_ table. The following _"semantic SQL"_ slots
exists for CRUD operations towards your database.

* __[mysql.create]__ - Creates (inserts) a new record into your database
* __[mysql.read]__ - Reads (selects) records from your database
* __[mysql.update]__ - Updates records in your database
* __[mysql.delete]__ - Deletes records from your database

All of the above slots have **[mssql.]** versions for Microsoft SQL Server.
If you want to follow this tutorial towards a Microsoft SQL Server database
instead of a MySQL database, just replace _"mysql"_ with _"mssql"_, and
everything should work the same, assuming you use some columns and
tables that actually exists in your SQL Server database.

## Creating CRUD HTTP endpoints

With the above in mind, let's create all 4 CRUD operations towards our
MySQL Sakila _"actor"_ table. First create a new folder
called _"/modules/data-crud/"_ and put the 4 following files into your
newly created folder.

**actor.post.hl**

```
.arguments
   first_name:string
   last_name:string
mysql.connect:sakila
   add:x:./*/mysql.create/*/values
      get-nodes:x:@.arguments/*
   mysql.create
      table:actor
      values
   unwrap:x:+/*
   return
      id:x:@mysql.create
```

**actor.get.hl**

```
.arguments
   limit:long
   offset:long
mysql.connect:sakila
   add:x:./*/mysql.read
      get-nodes:x:@.arguments/*
   mysql.read
      table:actor
      columns
         actor_id
         first_name
         last_name
         last_update
   return:x:-/*
```

**actor.put.hl**

```
.arguments
   actor_id:long
   first_name:string
   last_name:string
validators.mandatory:x:@.arguments/*/actor_id
mysql.connect:sakila
   add:x:./*/mysql.update/*/values
      get-nodes:x:@.arguments/*/first_name
      get-nodes:x:@.arguments/*/last_name
   mysql.update
      table:actor
      values
      where
         and
            actor_id:x:@.arguments/*/actor_id
```

**actor.delete.hl**

```
.arguments
   actor_id:long
validators.mandatory:x:@.arguments/*/actor_id
mysql.connect:sakila
   mysql.delete
      table:actor
      where
         and
            actor_id:x:@.arguments/*/actor_id
```

Exactly 50 lines of code, and we have all 4 CRUD operations towards one of our
database tables, with the read endpoint being able to page and limit its
result set. Not too bad for 50 lines of code if you ask me.

**Notice** - If you automatically CRUDify your database tables, the Hyperlambda
generator creates its endpoint files more or less like we manually created
them above, except of course it does it in 1 second automatically.
You can also add authorization to your endpoints just as easily as we
did in the previous _"hello world"_ tutorial, by adding the **[auth.ticket.verify]**
slot to your endpoint(s).

Now go to your _"Endpoints"_ menu item in your Magic Dashboard, and play around
with your endpoints as you see fit. If you can't find your endpoints, you can
add _"data-crud"_ as a filter. Try to create some few items, edit some
items, delete a couple of items, and read items. The association between
CRUD operations and endpoint verbs in the above code, is as follows.

* `POST` - Create one item
* `GET` - Read items
* `PUT` - Update one item
* `DELETE` - Delete one item

We could of course easily change the above code, to for instance accepting
multiple items in its _"update"_ endpoint, and/or _"delete"_ endpoint, etc -
But first, let's have a look at the **[where]** condition above, which is
common for all 3 slots above, minus the **[mysql.create]** slot.

## The [where] argument

The above **[where]** condition can be injected into the following 3 slots.

* __[mysql.read]__
* __[mysql.update]__
* __[mysql.delete]__

The create slot cannot be given a where condition, but all 3 other slots can,
and the syntax is of course the _exact same syntax_ for SQL Server, as it is
for MySQL. The result of the **[where]** argument above, obviously results
in an SQL _"where"_ condition, allowing you to restrict which items
the SQL should end up reading/changing/deleting. The first thing you'll need
to understand about the where condition, is that its boolean operator is its
outer most argument. This implies that if I create something such as the
following Hyperlambda.

```
where
   and
      foo.eq:some value
      bar.mteq:int:5
```

This would result in something equivalent to the following SQL being generated.

```
where foo = 'some value' and bar >= 5
```

**Notice** - All values will be added as SQL parameters, making it
impossible to inject malicious SQL into your database. Also try to
understand the relationship between the **[foo.eq]** parts, the
**[bar.mteq]** parts, and how this results in two different comparison operators
being generated for the fields. **[x.mteq]** basically means _"x more than or equals"_,
while **[x.eq]** implies _"x equals"_. If no comparison operator is specified,
equality (.eq) is assumed.

You can create any amount of complexity in your where statements as you wish.
This is done by recursively applying more and more **[and]** or **[or]** conditions,
such as the following illustrates.

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

The above would result in SQL resembling the following.

```
select * from 'table1' where 'field1' = @0 or ('field2' = @1 and 'field3' = @2)
```

Notice the relationship between the inner most `and` statement, and the paranthesis
generated in your SQL above. Each boolean operator added to your **[where]** beyond
its first, will create a new _"scope"_, adding paranthesis to your resulting SQL.
Also notice how by setting **[limit]** to _"-1"_, we can completely avoid
having the default limit of 25 applied to our end result.

By intelligently combining our **[where]** node with input arguments
to our endpoint, and by applying input arguments to our SQL slot invocation,
we can restrict which items are updated/deleted/selected, etc.
The SQL generator has a lot of other features, such as joining multiple
tables, changing the comparison operator, grouping by column(s), selecting
aggregate results, etc. Check out [magic.data.common](/documentation/magic.data.common)'s
reference documentation for more information about how to build
semantic SQL.

## Validators

As you are creating database CRUD endpoints, you will rapidly find
yourself in a situation where you need validators, such as
we illustrate above, in the `PUT` and `DELETE` endpoints. Remember
this guy ...?

```
validators.mandatory:x:@.arguments/*/actor_id
```

It basically ensures that our Hyperlambda file throws an exception,
unless an **[actor_id]** argument is supplied. Without this line of
code, we could in theory have some malicious client invoking our
endpoints, and for instance updating or deleting _every single item_
in our database - Which would probably be a bad thing ...

* [Read more about validators here](/documentation/magic.lambda.validators)

## Raw SQL access

If the above _"semantic slots"_ doesn't serve you, Magic and Hyperlambda
also provides _"raw access"_ to SQL, allowing you to execute any arbitrary
SQL, towards any of your database types. To use these lots you'd probably
want to check out your database specific adapter, but a list of its MySQL
versions can be found below.

* __[mysql.execute]__ - Wraps the `DbCommand.ExecuteNonQuery` method
* __[mysql.scalar]__ - Wraps the `DbCommand.ExecuteScalar` method
* __[mysql.select]__ - Wraps the `DbCommand.ExecuteReader` method

For the record, if you can, you _should_ use the CRUD operations instead
of the above _raw_ SQL slots - Since this allows you to transparently
support _any_ database type that Magic supports, This prevents _"lockin"_
of your application, allowing you to change database vendor as you see
fit. Even if this is not something _you_ care about, your _customers_
might care about it, since a lot of companies have
_"corporate database vendors"_, and don't even allow for purchasing
products that somehow doesn't support their particular database type.

In addition the database adapters in Magic also gives you transaction
support, creating, committing, and rolling back database transactions,
and lots of additional features. Please refer to your specific database
adapter for more information about these slots.

* [Read about the MySQL adapter here](/documentation/magic.lambda.mysql)
* [Read about the SQL Server adapter here](/documentation/magic.lambda.mssql)

And that's it for now. Hopefully I didn't snatch more than 10 minues
of your time :)

* [Continue to sending emails](/tutorials/send-email)

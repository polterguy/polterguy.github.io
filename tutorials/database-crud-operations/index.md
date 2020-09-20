# Hyperlambda CRUD operations

CRUD is at the core of everything relating to your database. It
implies **C**reate, **R**ead, **U**pdate and **D**elete, and these
are the 4 axioms that all database manipulation evolves around.
Notice, if you prefer to watch video tutorials, here’s a video
where I walk you through everything.

<div style="position:relative; padding-bottom:56.25%; padding-top:30px; height:0; overflow:hidden;margin-top:4rem;margin-bottom:4rem;">
<iframe width="560" height="315" style="position:absolute; top:0; left:0; width:100%; height:100%;" src="https://www.youtube.com/embed/fK3g_Aecx8Y" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

Hyperlambda supports 2 database types: Microsoft SQL Server and MySQL. In
our previous tutorial, we executed a select SQL statement, and returned
the results back to the client as JSON. Below is Hyperlambda illustrating
roughly how we did this.

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
where condition, ordering, and paging. And it transparently
generates the correct SQL towards any of your existing database adapters, allowing
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
result set.
Now go to your _"Endpoints"_ menu item in your Magic Dashboard, and play around
with your endpoints as you see fit. If you can't find your endpoints, you can
add _"data-crud"_ as a filter. Try to create some few items, edit some
items, delete a couple of items, and read items. The association between
CRUD operations and endpoint verbs in the above code, is as follows.

* `POST` - Create one item
* `GET` - Read items
* `PUT` - Update one item
* `DELETE` - Delete one item

**Notice** - If you automatically CRUDify your database tables, the Hyperlambda
generator creates its endpoint files more or less like we manually created
them above, except of course it does it in 1 second automatically.
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
in our database. Combining
validators with explicit **[.arguments]** declarations, and making
sure your arguments are declared with the correct type, ensures that
no malicious data can be sent into your endpoints. [Read more about validators here](/documentation/magic.lambda.validators)

## Raw SQL

If the above _"semantic slots"_ doesn't serve you, Magic and Hyperlambda
also allows you to supply _"raw SQL"_, allowing you to execute any arbitrary
SQL, towards any of your database types. To use these lots you'd probably
want to check out your database specific adapter, but a list of its MySQL
versions can be found below.

* __[mysql.execute]__ - Wraps the `DbCommand.ExecuteNonQuery` method
* __[mysql.scalar]__ - Wraps the `DbCommand.ExecuteScalar` method
* __[mysql.select]__ - Wraps the `DbCommand.ExecuteReader` method

For the record, if you can, you _should_ use the CRUD operations instead
of the above _raw_ SQL slots, since this allows you to transparently
support _any_ database type that Magic supports. This prevents _"lockin"_
of your application, allowing you to change database vendor as you see
fit. Even if this is not something _you_ care about, your _customers_
might care about it, since a lot of companies have
_"corporate database vendors"_, and don't even allow for purchasing
products that somehow doesn't support their particular database type.

In addition some database adapters in Magic also gives you transaction
support, creating, committing, and rolling back database transactions,
and lots of additional features. Please refer to your specific database
adapter for more information about these slots.

* [Continue to sending emails](/tutorials/send-email)

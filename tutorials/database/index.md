# Using Hyperlambda to perform CRUD operations towards your database

In case you didn't finish the [Hyperlambda Hello World tutorial](/hyperlambda-hello-world),
you would probably benefit from reading it before going through with this one. Anyways,
lets get started.

Hyperlambda supports 2 database types, Microsoft SQL Server and MySQL - But adding support
for another database type, is probably easy for a seasoned C# developer. As we saw in
the previous tutorial, we could easily execute any arbitrary select SQL, and return the
results of the DataReader back to the client, transforming it to JSON in the process.
In case you don't remember how we did this, the code can be found below.

```
mysql.connect:sakila
   mysql.select:select * from actor limit 10
   return:x:-/*
```

If you want to restrict the columns returned, simply add them up as columns into your SQL.
However, there exists an even better way, which we refer to as _"semantic SQL generating"_.
This approach completely abstract away the underlaying database vendor,
and allows you to semantically declare which columns are returned - In addition to your
where clause, order clause, and paging. And what's even better, is that it transparently
works towards any of your existing Magic database adapters, allowing you to use the
same structure for querying SQL Server as you would use to query MySQL - Assuming you
have the relevant tables and columns in some database in your database type.
This approach arguably reduces your database type down to a _"configurable property"_
in your end application. Below is an example resulting in the exact same SQL as the
above Hyperlambda, except it's using the _"semantic structure"_, instead of raw SQL.

```
mysql.connect:sakila
   mysql.read
      table:actor
      limit:10
   return:x:-/*
```

Notice how the above doesn't explicitly provide any SQL, but as it's being
executed towards your database adapter, its result becomes the same as the
first handcoded SQL version. You can also restrict what columns you wish to
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
columns form your _"actor"_ table. The following slots exists for all CRUD
operations towards your database.

* __[mysql.create]__ - Creates (inserts) a new record into your database
* __[mysql.read]__ - Reads records from your database
* __[mysql.update]__ - Updates records in your database
* __[mysql.delete]__ - Deletes records from your database

All of the above slots have **[mssql.]** versions for Microsoft SQL Server.
If you want to follow this tutorial towards a Microsoft SQL Server database
instead of a MySQL database, then just replace _"mysql"_ with _"mssql"_, and
everything should work the same way, assuming you use some columns and
tables that actually exists in your SQL Server database - And that you
connect to an existing SQL Server database in your instance.

## Creating CRUD HTTP endpoints

Let's create all 4 CRUD operations towards our MySQL Sakila _"actor"_ table.
Create a new folder called _"/modules/data-crud/"_ and put the 4 following
files into your folder.

**actor.post.hl**

```
.arguments
   first_name
   last_name
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
   actor_id
   first_name
   last_name
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
            actor_id.eq:x:@.arguments/*/actor_id
```

**actor.delete.hl**

```
.arguments
   actor_id
validators.mandatory:x:@.arguments/*/actor_id
mysql.connect:sakila
   mysql.delete
      table:actor
      where
         and
            actor_id.eq:x:@.arguments/*/actor_id
```

Exactly 50 lines of code, and we have all 4 CRUD operations towards one of our
database tables, with the read endpoint being able to page and limit its
result set. Not too bad for 50 lines of code if you ask me.

And in fact, if you automatically CRUDify your database tables, the Hyperlambda
generator creates its endpoint files more or less like we manually created
above, except of course it does it in 1 second. And you can add authorization
to your endpoints just as easily as we did in the previous _"hello world"_
tutorial.

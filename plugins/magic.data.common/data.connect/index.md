---
title: "How to use [data.connect]"
description: "How to use [data.connect] - This slot will open a database connection for you."
generated: true
guide: true
---

This is the guide to [`data.connect`](/reference/slots/data/data.connect/), whose reference page has its arguments, constraints and declaration.

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

Since the **[data.connect]** slot actually takes a lambda object, you can also add any amount
of other lambda invocations inside of the lambda object supplied to the slot, allowing you to for instance
create loops, conditional executions, etc, _inside_ of your invocation to **[data.connect]**. This is also
true for all other slots taking a lambda object, such as for instance **[data.transaction.create]**.
Inside your lambda object, an invocation towards your database such as e.g. **[data.read]**, will be
using this database connection, as long as the type of database is matching. The database connection will
be kept open, and implicitly used, for the entirety of the lambda object. If you need another database
connection inside of your lambda object, you'll need to nest **[data.connect]** invocations.
You can also explicitly choose which connection string to use as you open a connection, by separating the
connection string and the database name by a `|` symbol, and wrapping your entire value inside
of brackets. If you have a connection string in your _"appsettings.json"_ file named for instance _"foo"_,
and this connection string points to a server instance having a database named _"bar"_, you could open
a connection to this database using something resembling the following.

```
data.connect:[foo|bar]
```

This is why your connection strings should contain the `{database}` as a generic argument, since the slot
substitutes the `{database}` parts dynamically as you create new connections. Below is an example of such
a connection string configuration setting.

```
"generic": "Server=localhost\\SQLEXPRESS;Database={database};Trusted_Connection=True;"
```

---
title: "How to use [sql.create]"
description: "How to use [sql.create] - This slot will generate the SQL necessary to insert a record into a database for you."
generated: true
guide: true
---

The reference page of [`sql.create`](/reference/slots/sql/sql.create/) has its arguments, constraints and declaration.

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
The slot will in its specialized implementations return the ID of the inserted record if possible,
unless you explicitly parametrize it with a **[return-id]** argument and set its value to boolean
`false`.

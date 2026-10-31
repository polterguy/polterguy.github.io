---
title: "How to use [data.select]"
description: "How to use [data.select] - This slot allows you to pass in any arbitrary SQL you wish, and evaluate it to a DataReader, and return all records as a lambda object."
generated: true
guide: true
---

This is the guide to [`data.select`](/reference/slots/data/data.select/), whose reference page has its arguments, constraints and declaration.

This slot allows you to pass in any arbitrary SQL you wish, and evaluate it to a `DataReader`, and return
all records as a lambda object. You can find an example below.

```
data.connect:sakila
   data.select:select first_name, last_name from actor limit 5
```

Assuming you have the _"sakila"_ database from Oracle installed in your database, and your default
database type is MySQL, the result of the above will end up looking like the following.

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

This slot requires SQL resembling your specialised database type of dialect, and will
not in any ways transpile the SQL towards your specific underlying database type's SQL dialect.
If you can, you should rather use **[data.read]**, to avoid lockin towards a specific database
vendor's SQL dialect.
You can also select multiple result sets if you have batch type of SQL statements, containing
multiple SQL statements, and you want to return the result of all SQL statements you're executing.
You do this by providing a **[multiple-result-sets]** argument and set its value to boolean true.
If you do this, the slot will return an array of arrays, one outer array for each result set
your SQL generates. Below is an example.

```sql
data.select:"select * from table1; select * from table2;"
   multiple-result-sets:bool:true
```

Which would result in something resembling the following.

```
   data.select
      ""
         ""
            field1:foo1
            field2:bar1
         ""
            field1:foo2
            field2:bar2
      ""
         ""
            field1:foo1
            field2:bar1
         ""
            field1:foo2
            field2:bar2
```

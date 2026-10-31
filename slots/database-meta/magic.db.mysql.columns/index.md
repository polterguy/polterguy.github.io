---
title: "How to use [magic.db.mysql.columns]"
description: "How to use [magic.db.mysql.columns] - This slot returns all columns for the specified [connection-string]/[database]/[table] combination."
guide: true
slots: ["magic.db.mysql.columns"]
---

This slot returns all columns for the specified **[connection-string]**/**[database]**/**[table]** combination. Below
is example usage.

```
signal:magic.db.mysql.columns
   connection-string:generic
   database:magic
   table:users_roles
```

The above would return all columns in your _"users\_roles"_ table, resulting in something resembling the
following.

```
signal
   ""
      name:role
      db:varchar(45)
      nullable:bool:false
      primary:bool:true
      automatic:bool:false
      hl:string
   ""
      name:user
      db:varchar(256)
      nullable:bool:false
      primary:bool:true
      automatic:bool:false
      hl:string
```

The fields imply the following.

* __[name]__ - Name of column
* __[db]__ - Database type for column
* __[nullable]__ - If true column accepts null values
* __[primary]__ - If true column is a part of the primary key for the table
* __[automatic]__ - If true column has a default value
* __[hl]__ - Hyperlambda type mapping for the column

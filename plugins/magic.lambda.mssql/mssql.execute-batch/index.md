---
title: "How to use [mssql.execute-batch]"
description: "How to use [mssql.execute-batch] - Executes a batch SQL script, such as a schema creation script, on the SQL Server connection opened by [mssql.connect]."
generated: true
guide: true
---

The reference page of [`mssql.execute-batch`](/reference/slots/mssql/mssql.execute-batch/) has its arguments, constraints and declaration.

Executes a batch SQL script, such as a schema creation script, on the SQL Server connection opened by **[mssql.connect]**.
SQL Server cannot execute scripts containing `GO` separators as one single command, so this slot splits the script
on every line consisting only of `GO` (case insensitive), and executes each part as its own command. This is the
difference between this slot and **[mssql.execute]**, which executes its SQL as one single command.

* __[value]__ - The batch SQL script to execute. Can be a constant or an expression.

After execution the slot's value is `null`, and it has one child per executed batch, each containing a
**[Records affected]** node.

This slot executes a script made of several batches against the open connection. A line containing only `GO` separates one batch from the next, which is what SQL Server tools do, and each batch is executed on its own. The slot adds one child node per batch, telling how many records the batch affected. Below is an example.

```
mssql.connect:sakila
   mssql.execute-batch:@"update actor set last_name = 'Smith' where actor_id = 1
GO
update actor set last_name = 'Jones' where actor_id = 2"

// The result of the above looks like the following.
mssql.execute-batch
   ""
      Records affected:int:1
   ""
      Records affected:int:1
```

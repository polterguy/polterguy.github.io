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

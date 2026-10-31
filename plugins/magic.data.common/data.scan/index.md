---
title: "How to use [data.scan]"
description: "How to use [data.scan] - This slot scans rows from your database, using the current open connection created by [data.connect]."
generated: true
guide: true
---

The reference page of [`data.scan`](/reference/slots/data/data.scan/) has its arguments, constraints and declaration.

This slot scans rows from your database, using the current open connection created by **[data.connect]**.
It takes the same arguments as **[data.read]** and **[sql.read]**, and returns the matching rows as children nodes.
It returns all columns unless you supply **[columns]**, and limits the result to 25 rows unless you supply **[limit]**.

* __[table]__ - Name of the table to scan. Mandatory, the slot throws if it is missing
* __[columns]__ - Columns to select
* __[where]__ - Where condition
* __[order]__ - Which column(s) to order the results by
* __[limit]__ - How many records to return, default is 25. Set this value to -1 to avoid having the parser inject its default value
* __[offset]__ - Offset of where to start returning records
* __[group]__ - Group by declaration
* __[distinct]__ - Removes duplicate rows from the result when true
* __[database-type]__ - Database adapter to use instead of your default database type
* __[generate]__ - If true, only generates the SQL and its parameters instead of executing it, default is false

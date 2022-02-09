---
title: A web based SQL workbench
description: The web based SQL 'workbench' allows you to execute any SQL, see the result immediately, in addition to storing your frequently used SQL snippets for later.
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/og-sql-component.jpg"
---

# A web based SQL workbench

The SQL component allows you to execute any SQL towards your database of choice. This component also
allows you to export the result of some SQL to a CSV file, in addition to saving frequently used
SQL statements by using its _"Load"_ and _"Save"_ buttons. Out of the box Magic also comes with
a whole range of example SQL snippets, implying the SQL component in Magic is also a nice place
to start out if you want to teach yourself SQL. Below is a screenshot of how loading an SQL
snippet would look like in your SQL component.

![Loading SQL snippets](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/sql-editor.jpg)

The SQL component also provides you with syntax highlighting, in addition to autocomplete on
tables and columns that can be shown by clicking CTRL+SPACE or FN+CONTROL+SPACE on a Mac. Below
is a screenshot of how it would look like if you toggle autocomplete. Notice, it only shows you tables
and columns within your currently selected database. If you don't find the tables you're looking for,
make sure you have selected the correct database.

![SQL autocomplete](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/sql-autocomplete.jpg)

Notice, the _"Safe mode"_ checkbox prevents you from selecting more than 200 rows from your database.
If you need to select more rows you must click this checkbox _off_. However, if you return thousands of records
in this component, your server might become unresponsive, and/or you may end up exhausting your
server's memory. You can save your frequently used SQL statements as _"snippets"_ here similarly to
how you can save frequently used Hyperlambda in your _"Evaluator"_ component.

**Notice** - If you have some SQL Server script that creates a database, and/or contains _"go"_ keywords,
you'll need to turn on _"Batch mode"_ to have Magic understand your SQL. If you click the _"Load"_ button
you will also find several example _"create database"_ types of scripts, for each database type Magic supports.
This allows you to create some database in your database type of choice, and play around with for instance
the _"Crudifier"_ to generate web APIs automatically.

* [Back to middleware documentation](/documentation/magic/)
* [Back to main documentation](/documentation/)

---
title: A web based SQL workbench
description: The web based SQL 'workbench' allows you to execute any SQL, see the result immediately, in addition to storing your frequently used SQL snippets for later.
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/og-sql-component.jpg"
---

# The SQL Studio component

SQL Studio allows you to execute any arbitrary SQL towards your database of choice. This component also
allows you to export the result of some SQL to a CSV file, in addition to saving frequently used
SQL statements by using its _"Snippets"_ and _"Save"_ buttons. Out of the box Magic also comes with
a whole range of example SQL snippets, implying the SQL component in Magic is also a nice place
to start out if you want to teach yourself SQL. To access the SQL editor in SQL Studio open up
SQL Studio and click _"SQL view"_.

![SQL Studio SQL view](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/sql-editor.jpg)

SQL Studio also provides you with syntax highlighting, in addition to autocomplete on
tables and columns that can be shown by clicking CTRL+SPACE on Windows or FN+CONTROL+SPACE on a Mac.
Notice, it only shows you tables and columns within your currently selected database. If you don't find the
tables you're looking for, make sure you have selected the correct database.

![SQL autocomplete](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/sql-autocomplete.jpg)

The _"Safe mode"_ checkbox above prevents you from selecting more than 200 rows from your database.
If you need to select more rows you must click this checkbox _off_. However, if you return thousands of records
in this component, your server might become unresponsive, and/or you may end up exhausting your
server's memory. You can save your frequently used SQL statements as _"snippets"_ here similarly to
how you can save frequently used Hyperlambda in your _"Hyperlambda Playground"_ component.

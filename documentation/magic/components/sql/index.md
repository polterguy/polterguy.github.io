---
title: Magic's integrated SQL workbench
description: Magic contains an integrated SQL workbench component, allowing you to execute any arbitrary SQL, for then to immediately see its result.
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/og-sql-component.jpg"
---

# Magic's integrated SQL workbench

The SQL component allows you to execute any SQL towards your database of choice. This component also
allows you to export the result of some SQL to a CSV file, in addition to saving frequently used
SQL statements by using its _"Load"_ and _"Save"_ buttons. Out of the box Magic also comes with
a whole range of example SQL snippets, implying the SQL component in Magic is also a nice place
to start out if you want to teach yourself SQL. Below is a screenshot of how loading an SQL
snippet would look like in your SQL component.

![Loading SQL snippets](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/sql-editor.jpg)

The SQL component also provides you with syntax highlighting, in addition to autocomplete on
tables and columns that can be shown by clicking CTRL+SPACE or FN+CONTROL+SPACE on a Mac. Below
is a screenshot of how it would look like if you toggle autocomplete.

![SQL autocomplete](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/sql-autocomplete.jpg)

Notice, the _"Safe mode"_ checkbox prevents you from selecting more than 200 rows from your database.
If you need to select more rows you must click this checkbox _off_. However, if you return thousands of records
in this component, your server might become unresponsive, and/or you may end up exhausting your
server's memory. You can save your frequently used SQL statements as _"snippets"_ here similarly to
how you can save frequently used Hyperlambda in your _"Evaluator"_ component.


* [Back to middleware documentation](/documentation/magic/)
* [Back to main documentation](/documentation/)

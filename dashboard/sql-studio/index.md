---
title: SQL Studio
description: The web based SQL 'workbench' allows you to execute any SQL, see the result immediately, in addition to storing your frequently used SQL snippets for later.
header:
  image: /assets/images/hero/sql-studio.png
  og_image: /assets/images/hero/sql-studio-og.png
  image_description: SQL Studio
---

SQL Studio allows you to visually design your database, and also execute any SQL towards your database of choice.
SQL Studio also allows you to export the result of some SQL to a CSV file, in addition to saving frequently used
SQL statements by using the _"Snippets"_ and _"Save"_ buttons.

If you install one of the SQLite database
plugins using [the plugins component](/dashboard/plugins/), you also typically get a lot
of example SQL statements - Implying SQL Studio is also a nice place to start out if you
want to teach yourself SQL. To access the SQL editor open up SQL Studio and click the _"SQL"_ tab.

![Screenshot of SQL Studio in SQL view to execute SQL with syntax highlighting and autocomplete](/images/sql-editor.jpg)

## Create and design your database visually

You can also use SQL Studio to visually create and design your database. This is a graphical user interface, where you don't need to write any SQL DDL to create your database structure. SQL Studio's database designer allows you to create new tables, add fields to your tables, and create foreign keys referencing other tables as you wish.

![Screenshot of SQL Studio and its design view allowing you to visually design your databases](/images/sql-designer.jpg)

## SQL Studio features

The _"Safe mode"_ slider prevents you from selecting more than 200 records from your database in one go. If you need to select more records you must turn this slider _off_. However, if you return thousands of records with some SQL statement, your server might become unresponsive, and/or you may end up exhausting your server's memory or your client's memory.

When you execute SQL, you can run your entire statement, or highlight part of it in the code editor and execute only the selected portion. If you have a selection, only the selected SQL is executed - which is handy when your editor contains several statements and you only want to run one of them.

You can save your frequently used SQL statements as _"snippets"_ similarly to how you can save frequently used Hyperlambda in the [Hyperlambda Playground](/dashboard/hyperlambda-playground/) component. This allows you to store frequently used SQL snippets for later, creating a library of snippets you can tap into as you need to execute the same SQL again.

SQL Studio also provides you with autocomplete on both your tables and columns. This typically works best if you write SQL statements where your tables are aliased, and you write the alias of your table, followed by a dot (.), for then to trigger autocomplete. To launch autocomplete click FN+CONTROL+SPACE on a Mac, or CTRL+SPACE on Windows.

In addition, you can import SQL statements from your local development machine by clicking the _"Import"_ button, which will bring up a browse for file dialogue, allowing you to import some SQL file from your local machine into the SQL editor surface of SQL Studio.

## SQL Studio and Machine Learning

SQL Studio integrates with the machine learning and AI parts of Magic. This allows you to ask SQL related questions, such as; _"Create an SQLite DDL for me that creates a users and roles table, where each user is referencing a role with a foreign key"_.

The AI features of SQL Studio don't always produce perfect code, but it is built on top of OpenAI's APIs, so it should be good enough to give you at least an approximation of what you want to achieve. Notice, you need an API key with OpenAI to have these parts of SQL Studio work.

If you use the AI chat interface in SQL Studio you can ask the AI to create, and/or modify your code, and such have _"conversations"_ with the AI about your code.

## SQL Studio designer features

The SQL Studio database designer allows you to do the following things.

* Create new tables
* Create new fields
* Create new foreign keys
* Export one table's DDL
* Export all tables' DDL
* Import a CSV file as a new table
* Flush the server-side schema cache

SQL Studio doesn't give you every single feature of SQL DDL, but it's good enough to provide you with 90% of what you need as you are designing your database schema. When you create a new foreign key for instance, it will ask you if you want to allow for null values in your foreign keys, and if you want to turn on cascading deletes - But it will not ask you if you want to set to null upon deletions.

### Importing a CSV file

The designer can also create a table directly from a CSV file. Click the _"Import .csv"_ button, choose a CSV file from your local machine, and Magic creates a new table named after the file, with one column for each column in your CSV file. It automatically picks a numeric or text type for each column based on its values, adds an automatically incrementing primary key, and then imports every row from your file. The import runs in the background, so you'll be notified once it completes - just reload the page afterwards to see your new table in the designer.

### Flushing the server-side cache

For performance, Magic caches your database schema on the server. If your schema changes outside the designer - for instance when you import a CSV file, or when an AI agent creates a table over the [MCP server](/tutorials/how-to-connect-the-mcp-server/) - click the _"Flush cache"_ button to clear this cached schema. Doing so reloads the page, so the designer reflects the current state of your database.

SQL Studio's designer works transparently towards all database types, implying you can use it to create databases for MySQL, PostgreSQL, SQLite, MariaDB, and SQL Server. However, what types of fields you can create differs between database types.

## How to create a database using SQL Studio

You cannot actually create a database with SQL Studio. This needs to be done using the [Databases menu item](/dashboard/databases/) below the _"Create"_ section. However, once you have created a database, you can use SQL Studio to create tables in it, and modify these as you see fit.

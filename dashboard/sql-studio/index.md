---
title: SQL Studio
description: The web based SQL 'workbench' allows you to execute any SQL, see the result immediately, in addition to storing your frequently used SQL snippets for later.
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/sql-editor.jpg"
header:
  image: /assets/images/wizard-creating-sql-statements.png
---

SQL Studio allows you to visually design your database, and also execute any SQL towards your database of choice.
SQL Studio also allows you to export the result of some SQL to a CSV file, in addition to saving frequently used
SQL statements by using the _"Snippets"_ and _"Save"_ buttons.

If you install one of the SQLite database
plugins using [the plugins component](/dashboard/plugins/), you also typically get a lot
of example SQL statements - Implying SQL Studio is also a nice place to start out if you
want to teach yourself SQL. To access the SQL editor open up SQL Studio and click _"SQL view"_.

![SQL Studio SQL view](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/sql-editor.jpg)

## Create and design your database visually

You can also use SQL Studio to visually create and design your database. This is a graphical user interface, where
you don't need to write any SQL DDL to create your database structure. SQL Studio's database designer
allows you to create new tables, add fields to your tables, and create foreign keys referencing other tables
as you wish. In addition SQL Studio's designer also allows you to create _"link tables"_, automatically
encapsulating a many to many relationship between two tables.

![SQL Studio design view](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/sql-designer.jpg)

## SQL Studio features

The _"Safe mode"_ slider prevents you from selecting more than 200 records from your database in one go.
If you need to select more records you must turn this slider _off_. However, if you return thousands of records
with some SQL statement, your server might become unresponsive, and/or you may end up exhausting your
server's memory.

You can save your frequently used SQL statements as _"snippets"_ similarly to how you can save frequently
used Hyperlambda in the [Hyperlambda Playground](/dashboard/hyperlambda-playground/) component.
This allows you to store frequently used SQL snippets for later, creating a library of snippets you
can tap into later as you need to execute the same SQL later.

SQL Studio also provides you with autocomplete on both your tables and columns. This typically
works best of you write SQL statements where your tables are aliased, and you write the alias of your table,
followed by a dot (.), for then to trigger autocomplete. To launch autocomplete click FN+CONTROL+SPACE
on a Mac, or CTRL+SPACE on Windows.

In addition, you can import SQL statements from your local development machine by clicking the _"Import"_
button, which will bring up a browse for file dialogue, allowing you to import some SQL file from your local
machine into the SQL editor surface of SQL Studio.

## SQL Studio and Machine Learning

SQL Studio integrates with the machine learning and AI parts of Magic. This allows you to ask SQL related
questions, such as; _"Create an SQLite DDL for me that creates a users and roles table, where each user is
referencing a role with a foreign key"_.

The AI features of SQL Studio doesn't always produce perfect code, but it is built
on top of OpenAI's APIs, so it should be good enough to give you at least an approximation
of what you want to achieve. Notice, you need an API key with OpenAI to have these parts of SQL Studio work.

If you use the AI chat interface in SQL Studio you can ask the AI to create, and/or modify your code, and
such have _"conversations"_ with the AI about your code.

## SQL Studio designer features

The SQL Studio database designer allows you to do the following things.

* Create new tables
* Create new fields
* Create new foreign keys
* Create many to many link tables automatically
* Export one table's DDL
* Export all tables' DDL
* Automatically create migration scripts

SQL Studio doesn't give you every single feature of SQL DDL, but it's good enough to provide you
with 90% of what you need as you are designing your database schema. When you create a new foreign key for instance,
it will ask you if you want to allow for null values in your foreign keys, and if you wants to turn on cascading
deletes - But it will not ask you if you want to set to null upon deletions.

For a walkthrough of SQL Studio's most important features you can watch the [following YouTube video](https://www.youtube.com/watch?v=xQYwPFEOTAI).

<iframe width="560" height="315" src="https://www.youtube.com/embed/xQYwPFEOTAI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

### Exporting your DDL to a module

When you are exporting your table(s)' DDL, you can also optionally export your DDL to a _"module"_. This is
useful if you are creating plugins or similar functionality using Magic, since it will automatically wire
up everything required to automatically create your database if it doesn't exist on whatever cloudlet you
install your module on - In addition to sequentially executing all migrate scripts associated with your module.

This implies that if you create a reusable module or plugin, once your plugin is installed, it will automatically
create its database, and execute all SQL migration scripts as it is installed or updated.

SQL Studio's designer works transparently towards all database types, implying you can use it to create
databases for MySQL, PostgreSQL, SQLite, MariaDB, and SQL Server. However, what types of fields you can create
differs between database types.

![Export your database DDL to module](/assets/images/export-database-ddl.jpeg)

## Auto migrations

If you turn on _"Auto migrate"_ by clicking the triple dots icon in design view, and turn on auto migrate,
SQL Studio will ask you if you want to apply auto migration as you change your database DDL. This functionality
will automatically create the required files to apply automatic migration as you're editing your database.

![Auto migrate your database DDL](/assets/images/auto-migrate-database.jpeg)

This is useful if you're editing a reusable module you want to install on other cloudlets somehow, since if
the module is (re)-installed it will run through each of your migration scripts, and automatically change your
database structure.

## How to create a database using SQL Studio

You cannot actually create a database with SQL Studio. This needs to be done using the [Databases menu
item](/dashboard/databases/) below the _"Create"_ section. However, once you have created a database, you can
use SQL Studio to create tables in it, and modify it as you need.

---
title: Databases
description: The databases component allows you to manage your connection strings, connect to external databases, and create new SQLite databases in Magic.
header:
  image: /assets/images/hero/databases.png
  og_image: /assets/images/hero/databases-og.png
  image_description: The Databases component
faq:
  - q: "What is the Databases component?"
    a: "The place to manage your connection strings and databases. Connect to any external MySQL, PostgreSQL, SQL Server or MariaDB database, or create file based SQLite databases with a single click - no server required."
  - q: "Why must my connection string contain {database}?"
    a: "Magic needs to dynamically connect to multiple catalogues on your database server, so you exchange the database name in your connection string with the text {database}."
  - q: "Can an AI create my database?"
    a: "Yes. Connect your cloudlet to an AI agent such as Claude over the MCP server, describe the database you want in plain English, and the orchestrating LLM creates the SQLite database and its schema for you."
  - q: "Should I backup my SQLite databases?"
    a: "Yes. Download a backup of your SQLite databases every now and then, so you have a local copy if something goes wrong."
---

The databases component allows you to manage your connection strings, in addition to your external and internal databases. This is your goto component if you want to connect to an external database. It allows you to connect to any MySQL, PostgreSQL, SQL Server, or MariaDB database. Provide it with your connection string, give your connection string a name, and click connect.

![Screenshot of the databases component](/images/databases.jpg)

In addition to allowing you to connect to external databases, this is also the place you go to create a new SQLite file-based database.

## Creating and designing SQLite databases

Besides connecting to external databases, you can create your own file-based SQLite databases directly from this component — no server or connection string required. Just give your database a name, and Magic creates it for you.

Once created, you can design your database visually in [SQL Studio](/dashboard/sql-studio/), adding tables, columns, and foreign keys through a graphical designer without writing any DDL by hand. You can of course also execute SQL against your database directly if you prefer.

You can even let an AI do it for you. If you connect your cloudlet to an AI agent such as Claude over the [MCP server](/tutorials/how-to-connect-the-mcp-server/), you can describe the database you want in plain English, and have the orchestrating LLM create the SQLite database and its schema for you.

## Adding a connection string

It is important that you exchange your catalogue name, or database name, with the text _"{database}"_. This is because Magic needs to be able to dynamically connect to multiple catalogues or databases in your database server. Magic needs to be able to read system databases, in addition to connecting generically to any database in your system it's got access to. This is why it'll need the above `{database}` parts in its connection string.

If you're hosting your database in for instance Azure or AWS, you might also have to white list your cloudlet's IP address.

## Backup your SQLite databases

Every now and then, you should download a backup of your SQLite databases to make sure you've got a local backup if something goes wrong. We have global backups of our K8S volumes as a whole, but it might also be beneficial to have local backups in your own machine too.

{% include faq.html %}

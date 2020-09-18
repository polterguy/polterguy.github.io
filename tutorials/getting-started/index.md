# Getting started with Magic

A 5 minute read, with 5 simple steps, teaching you how to get started with Magic.
When you're done following this tutorial, you'll have something resembling
the following.

![Example Magic application](https://servergardens.files.wordpress.com/2020/01/magic-datagrid.png)

## Prerequisites

1. [Download Visual Studio](https://visualstudio.microsoft.com/downloads/) or [VS Code](https://code.visualstudio.com/download) + [DotNet CLI](https://dotnet.microsoft.com/download)
2. [Install NodeJS](https://nodejs.org/en/download/)
3. [Install Angular](https://angular.io/cli)
4. [Install MySQL](https://dev.mysql.com/downloads/mysql/) or [Microsoft SQL Server Developer Edition](https://www.microsoft.com/en-us/sql-server/sql-server-downloads)
5. Download Magic from the link above

## 1. Start Magic

1. Open _"magic.sln"_ file in Visual Studio and click F5. If you're using a Mac, open a terminal window in its backend folder, and type `dotnet run`
2. Open a command prompt/terminal in the frontend folder, and type `npm link`
3. After npm link is done, type `ng serve` in the frontend folder
4. Go to [localhost:4200](https://localhost:4200) with your browser
5. Login with root/root

## 2. Setup Magic

In order to get Magic to work, you'll have to create an authentication
and authorization database. Magic will do this automatically for you,
assuming you have some database installed somewhere - But you will have
to give it a valid connection string to your database, in addition to
choosing a _"root"_ password.

![Setup Magic](https://servergardens.files.wordpress.com/2020/09/setup-magic.png)

**Notice** - It's important that you keep the `{database}` parts of your
connection string as is. This is because Magic will substitute this
with whatever database catalogue you want to query as you open a
database connection later. You also need to choose the correct
_database type_ - Implying MySQL or Microsoft SQL Server, depending
upon what database type you want to use Magic with.

Click _"Save"_, and Magic will spend some few seconds configuring.

## 3. Crudify your auth database

Click the _"Crudify"_ menu item, and choose the _"magic"_ database.
Select all tables, and click the _"Crudify all"_ button. After a
couple of seconds, Magic have created CRUD HTTP endpoints necessary
to administrate your users and roles. At this point, you can already
visit the _"Users"_ and _"Roles"_ menu items, and create new users
or roles as you see fit. You now have a 100% perfectly
working, and highly secure, authentication and authorization
backend.

![Crudify your Magic database](https://servergardens.files.wordpress.com/2020/09/crudify-magic-database.png)

## 4. Crudify your first custom database

**Notice** - At this point you'll need a database. Below are links
to example database for MySQL and SQL Server. Make sure you download
the correct database schema, according to what database type you have
installed.

* [MySQL Sakila database](https://downloads.mysql.com/docs/sakila-db.zip)
* [Bike Store example SQL Server database](https://cdn.sqlservertutorial.net/wp-content/uploads/SQL-Server-Sample-Database.zip)

Run the create database script(s) through _"MySQL Workbench"_ or
_"SQL Server Management Studio"_. If you haven't already installed
these components, you might want to install them at this point.
They will make it simpler to administrate your database(s).
When you have created your database, or maybe you already had an
existing database from before, you can create CRUD endpoint
wrapping your database of choice.

Go back to the _"Crudify"_ menu item, but this time choose another
database, for instance Sakila or Bike Store. Then choose _"All tables"_
in the _"Select table"_ dropdown, and click _"Crudify all"_. After
a couple of seconds, you'll have CRUD HTTP endpoints wrapping every
single table in your database.

## 5. Generate your frontend

Go to _"Endpoints"_, give your application a name, and
choose a template. You can optionally supply a file comment
header for your file at this point. Click the _"Generate"_
button, and after a couple of seconds, you'll get a zip file.

Unzip the zip file Magic gave you, open a terminal/command
prompt, go to the folder where the zip file was unzipped,
and type `npm link`. When npm link is done, type the
following into the same terminal window.

```
ng serve --port 4201
```

This time you'll have to choose a different port, since
port 4200 is already busy serving your Magic Dashboard.
When ng serve is done transpiling your Angular project,
[open localhost:4201](https://localhost:4201), and login with
your root username and password.

* [Continue to Hyperlambda Hello World](/tutorials/hyperlambda-hello-world)

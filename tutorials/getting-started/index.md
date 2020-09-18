# Getting started with Magic

## Prerequisites

1. [Visual Studio](https://visualstudio.microsoft.com/downloads/) or [VS Code](https://code.visualstudio.com/download) + [DotNet CLI](https://dotnet.microsoft.com/download)
2. [NodeJS](https://nodejs.org/en/download/)
3. [Angular](https://angular.io/cli)
4. [MySQL](https://dev.mysql.com/downloads/mysql/) or [Microsoft SQL Server](https://www.microsoft.com/en-us/sql-server/sql-server-downloads)
5. Download Magic from the link above

<div style="position:relative; padding-bottom:56.25%; padding-top:30px; height:0; overflow:hidden;margin-top:4rem;margin-bottom:4rem;">
<iframe width="560" height="315" style="position:absolute; top:0; left:0; width:100%; height:100%;" src="https://www.youtube.com/embed/9ZXs4Nb4QVo" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## 1. Start Magic

1. Open _"magic.sln"_ file in Visual Studio and click F5. If you're using a Mac, open a terminal window in its backend folder, and type `dotnet run`
2. Open a command prompt/terminal in the frontend folder, and type `npm link`
3. After npm link is done, type `ng serve` in the frontend folder
4. Go to [localhost:4200](https://localhost:4200) with your browser
5. Login with root/root

## 2. Setup Magic

To setup Magic, you'll have to create an authentication
and authorization database. Magic will do this automatically for you,
assuming you have MySQL or SQL Server somewhere, but you will have
to give it a valid connection string, in addition to choosing
a _"root"_ password.

**Notice** - It's important that you keep the `{database}` parts of your
connection string as is. This is because Magic will substitute this
with whatever database catalogue you want to query as you open a
database connection later. You also need to choose the correct
_database type_ - Implying MySQL or Microsoft SQL Server, depending
upon what database type you want to use Magic with.

![Setup Magic](https://servergardens.files.wordpress.com/2020/09/setup-magic.png)

Click _"Save"_, and Magic will spend some few seconds configuring.

## 3. Crudify your auth database

Click the _"Crudify"_ menu item, and choose the _"magic"_ database.
Select all tables, and click the _"Crudify all"_ button. After a
couple of seconds, Magic have created CRUD HTTP endpoints necessary
to administrate your users and roles. At this point, you can already
visit the _"Users"_ and _"Roles"_ menu items, and create new users
or roles as you see fit.

![Crudify your Magic database](https://servergardens.files.wordpress.com/2020/09/crudify-magic-database.png)

## 4. Crudify your first custom database

**Notice** - At this point you'll need a database. Below are links
to example database for MySQL and SQL Server. Make sure you download
the correct database schema, according to what database type you have
installed, or use any of your existing databases.

Go to the _"Crudify"_ menu item, but this time choose another
database, for instance Sakila or Bike Store. Then choose _"All tables"_
in the _"Select table"_ dropdown, and click _"Crudify all"_. After
a couple of seconds, you'll have CRUD HTTP endpoints wrapping every
single table in your database.

### 4.5 - No existing database?

Download one of these free database scripts for SQL Server or MySQL.

* [MySQL Sakila database](https://downloads.mysql.com/docs/sakila-db.zip)
* [Bike Store example SQL Server database](https://cdn.sqlservertutorial.net/wp-content/uploads/SQL-Server-Sample-Database.zip)

Run the above create database script through _"MySQL Workbench"_ or
_"SQL Server Management Studio"_.

## 5. Generate your frontend

Go to _"Endpoints"_, give your application a name, and
choose a template. Click the _"Generate"_
button, and after a couple of seconds, you'll get a zip file.
Unzip the file Magic gave you, open a terminal/command
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

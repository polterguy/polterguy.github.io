# Getting started with Magic

## Prerequisites

1. [Visual Studio](https://visualstudio.microsoft.com/downloads/) or [VS Code](https://code.visualstudio.com/download) + [DotNet CLI and SDK](https://dotnet.microsoft.com/download)
2. [NodeJS](https://nodejs.org/en/download/)
3. [Angular](https://angular.io/cli)
4. [MySQL](https://dev.mysql.com/downloads/mysql/) or [Microsoft SQL Server](https://www.microsoft.com/en-us/sql-server/sql-server-downloads)
5. Download Magic from the link above

## 1. Start Magic

1. Open the _"magic.sln"_ file in Visual Studio and click F5. If you're using VS Code, open a terminal window, go to the `backend` folder, and type `dotnet run`
2. Open a terminal window in the `frontend` folder and run `npm link`
3. After npm link is done run `ng serve`
4. Go to [localhost:4200](http://localhost:4200) with your browser
5. Login with root/root

## 2. Setup Magic

To setup Magic, you'll have to create an authentication
and authorization database. Magic will do this automatically for you,
but you will have to give it a valid connection string, in addition
to choosing a _"root"_ password. At this point you'll need either MySQL
or SQL Server installed somewhere.

**Notice** - It's important that you keep the `{database}` parts of your
connection string as is. This is because Magic will substitute this
with whatever database catalogue you want to query as you open a
database connection later. You also need to choose the correct
_database type_ - Implying MySQL or Microsoft SQL Server, depending
upon what database type you want to use Magic with.
Click _"Save"_, and Magic will spend some few seconds configuring.

## 4. Crudify your database

Select your database, then click _"Crudify all tables"_.
After a couple of seconds, you'll have CRUD HTTP endpoints
wrapping every single table in your database.

## 5. Generate your frontend

Choose the _"Frontend"_ tab, select a template, give your app
a name, select modules to crudify, and click _"Generate"_.
After a couple of seconds, you'll get a zip file.
Unzip the file Magic gave you, open a terminal
window, go to the folder where the zip file was unzipped,
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

Magic generates 100% perfectly valid Angular code for you,
obeying all TS lint standards, easily modified by you to
serve your specialized needs. If you need further help with
individual menu items, you can find context sensitive help
on each menu item, by clicking the question mark in the top
right corner of your dashboard.

**Notice** - Unless you have obtained a valid license for Magic,
it will stop working after 2 days. You can
[obtain a license here](https://servergardens.com/buy/).

* [Continue to Hyperlambda Hello World](/tutorials/hyperlambda-hello-world)

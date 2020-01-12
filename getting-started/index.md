# Getting started

To get started with Magic you'll need the following installed.

1. [MySQL](https://dev.mysql.com/downloads/mysql/) or [Microsoft SQL Server](https://www.microsoft.com/en-us/sql-server/sql-server-downloads).
2. [Visual Studio Code](https://code.visualstudio.com/download), or Visual Studio if you're on Windows
3. [NodeJS](https://nodejs.org/en/download/) - To serve the frontend/dashboard
4. [Angular](https://cli.angular.io), which is installed using `npm install -g @angular/cli` after installing NodeJS
5. [DotNet CLI](https://dotnet.microsoft.com/learn/dotnet/hello-world-tutorial/install) - Unless you're using Visual Studio on Windows

Then download Magic, unzip it, and follow the instructions in the following video.

<div style="margin-left: auto; margin-right: auto; width: 560px;">
<iframe width="560" height="315" src="https://www.youtube.com/embed/qPn5tfGfhR4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## List of what to do

1. Open Visual Studio Code in your magic folder
2. Open one terminal window and go to `magic.backend`
3. Run `dotnet run` in the magic.backend terminal
4. Open another terminal window and go to `frontend`
5. Run `npm install` in this terminal
6. When npm install from above is done, run `ng serve` in the frontend terminal
7. Open your browser and point it to [http://localhost:4200](http://localhost:4200)

## Creating your CRUD Web APIs

1. Login with _"root/root"_ as your username/password
2. Run through the _"Setup"_ wizard
3. Click the _"Crudify"_ menu item
4. Choose your database and your table
5. Click the _"Crudify"_ button

When you have created your first CRUD endpoints, you can click the _"Endpoints"_ menu item, and try out your
newly created HTTP REST endpoints.

**Notice** - If you want to use the default authentication and authorisation system that comes out of the
box with Magic, you will have to _"Crudify"_ your _"magic\_auth"_ database.

## Creating your Angular frontend

After having created your backend, you can click the _"Endpoints"_ menu in the Magic dashboard, go to the
bottom of this page, give your application a name, and click _"Generate"_. After some few seconds, a zip file
with your Angular frontend code will be downloaded to your client. You can also decide which endpoints you
wish to generate Angular code for by clicking the checkboxes before you click _"Generate"_. However, Magic
will _"intelligently"_ generate your Angular code, according to which endpoints you choose during generation.

## The scaffolded Angular code

The generated Angular code will be highly modular in its structure, and one router link for each of your
HTTP REST GET endpoints will be automatically created for you - In addition a menu link will be created
for each GET endpoint. Magic will also create one Angular component for each of these endpoints. This
allows you to immediately start editing this code, to change your UI according to how you want it to look
like. You might for instance want to use DateTime pickers for your date fields, or textareas for some of
your string fields from your database. This is easily done by changing the generated Angular code.

The generated code is created according to all Angular _"best practices"_, and it is highly componentised
and modular in nature. This makes it a perfect starting point for learning Angular, with existing code,
wrapping your entire database.

[Custom SQL](/custom-sql)

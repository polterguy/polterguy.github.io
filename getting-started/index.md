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

## Creating your first CRUD Web API

1. Login with _"root/root"_ as your username/password
2. Run through the _"Setup"_ wizard
3. Click the _"Crudify"_ menu item
4. Choose your database and your table
5. Click the _"Crudify"_ button

When you have created your first CRUD endpoints, you can click the _"Endpoints"_ menu item, and try out your
newly created HTTP REST endpoints.

[Custom SQL](/custom-sql)


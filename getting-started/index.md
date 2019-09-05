# Getting started

To get started with Magic you'll need the following installed.

1. [MySQL](https://dev.mysql.com/downloads/mysql/) - Future versions will support MSSQL
2. [Visual Studio Code](https://code.visualstudio.com/download), or Visual Studio if you're on Windows
3. [NodeJS](https://nodejs.org/en/download/) - To serve the frontend/dashboard
4. [Angular](https://cli.angular.io), which is installed using `npm install -g @angular/cli`
5. [DotNet CLI](https://dotnet.microsoft.com/learn/dotnet/hello-world-tutorial/install) - Unless you're using Visual Studio on Windows

Then download Magic, unzip it, and follow the instructions in the following video.

<div style="margin-left: auto; margin-right: auto; width: 560px;">
<iframe width="560" height="315" src="https://www.youtube.com/embed/Lpqco0BgYYY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## List of what to do

1. Open Visual Studio Code in your magic folder
2. Edit your `appsettings.json` file, and modify your MySQL connection string
3. Open one terminal window and go to `magic.backend`
4. Run `dotnet run` in the magic.backend terminal
5. Open another terminal window and go to `frontend`
6. Run `npm install` in this terminal
7. When npm install from above is done, run `ng serve` in the frontend terminal

If you're using the full version of Visual Studio, you might have to edit your `environment.ts` file and change
its `apiURL` to become `http://localhost:55246/api/` and its `apiDomain`to be `localhost:55246`.


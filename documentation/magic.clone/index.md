
# Cloning Magic locally

This recipe helps you clone Magic locally, and assumes you've got VS Code, NodeJS, Angular CLI, and the .Net SDK
version 6 or higher. You can also use Visual Studio instead of VS Code if you're on Windows, at which point
you only need to open the _"magic.sln"_ file. When you've made sure you've got all of these parts, clone
this repository locally using the following.

```bash
git clone https://github.com/polterguy/magic.clone.git
```

Then run the _"clone.sh"_ file, and wait until it's done.

```bash
./clone.sh
```

You now have everything needed to run and debug Magic locally within your _"src/"_ folder. Whenever you need to
pull the repositories again simply execute _"pull.sh"_ again. To debug, and/or run Magic, type the following
in a terminal.

```bash
cd src

# This requires having VS Code locally installed and in your path
code ./
```

Then open _two_ terminal windows in VS Code and type the following into the first.

```bash
cd magic
cd backend
dotnet run --project dev_backend.csproj
```

Type the following into the second terminal window.

```bash
cd magic
cd frontend
npm install
ng serve
```

When `ng serve` and `dotnet run` is done, you can visit [localhost:4200](https://localhost:4200) in your
browser, and you should be set. Notice, you will need a database to configure Magic. Below are recipies
for how to accomplish this if you don't have a database accessible already somewhere.
To debug, make sure you've got the OmniSharp C# debugger plugin installed in VSCode, click F5 while in VS Code, 
and set breakpoints where you wish to debug Magic locally on your development machine. This is configured through
the `.vscode/launch.json` and `.vscode/tasks.json` files. If you started Magic first with `dotnet run` you have to
stop that process before you start debugging Magic.

## Docker database images

This project also contains _"docker-compose.yml"_ files for SQL Server, PostreSQL, and MySQL, allowing you
to locally start a database instance using Docker. These files can be found within the _"db"_ folder,
that contains one folder for each database type, allowing you to test Magic with any of these databases
locally. To start for instance SQL Server, execute the following from a terminal.

```bash
cd db
cd mssql
docker-compose up
```

The connection strings for each database type can be found below.

* __SQL Server__ - Server=localhost;Initial Catalog={database};User=sa;Password=Your_password123;
* __MySQL__ - Server=localhost;Database={database};Uid=root;Pwd=ThisIsNotAGoodPassword;SslMode=Preferred;Old Guids=true;Port=54321;
* __PostgreSQL__ - User ID=postgres;Password=ThisIsNotAGoodPassword;Host=localhost;Database={database}; Port=54321;

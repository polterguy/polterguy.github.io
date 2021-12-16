
# Magic Clone - Develop Magic locally

This recipe assumes you've got VS Code, MySQL, PostgreSQL or SQL Server accessible somewhere, NodeJS,
Angular, and the .Net SDK version 6 or higher. You can also use Visual Studio instead of VS Code if
you're on Windows, at which point you only need to open the _"magic.sln"_ file. When you've made sure
you've got all of these parts, clone this repository locally using the following.

```
git clone https://github.com/polterguy/magic.clone.git
```

Then run the _"clone.sh"_ file, and wait until it's done - At which point you will find everything
needed to run and debug Magic locally within your _"src/"_ folder. Whenever you need to pull the
repositories again simply execute _"pull.sh"_. To debug, and/or run Magic, type the following in a terminal.

```bash
cd src

// This requires having VS Code locally installed and in your path
code ./
```

Then open _two_ terminal windows and type the following into the first.

```bash
cd magic
cd backend
dotnet run --project dev_backend.csproj
```

Type the following into the second terminal window.

```bash
cd magic
cd frontend
npm link
ng serve
```

When `ng serve` and `dotnet run` is done, you can visit [localhost:4200](https://localhost:4200) in your
browser, and you should be set.

To debug, make sure you've got the OmniSharp C# debugger plugin installed in VSCode, click F5 while in VS Code, 
and you can set breakpoints, and/or debug Magic locally on your development machine. This is configured through
the `.vscode/launch.json` and `.vscode/tasks.json` files.

## Build status of all projects

Below you can find the build status of all projects in their respective master branches, and the links to the
GitHub project pages of all projects.

* ![Build status](https://github.com/polterguy/magic/actions/workflows/codeql-analysis.yml/badge.svg) - [Magic](https://github.com/polterguy/magic)
* ![Build status](https://github.com/polterguy/magic.data.common/actions/workflows/build.yaml/badge.svg) - [magic.data.common](https://github.com/polterguy/magic.data.common)
* ![Build status](https://github.com/polterguy/magic.endpoint/actions/workflows/build.yaml/badge.svg) - [magic.endpoint](https://github.com/polterguy/magic.endpoint)
* ![Build status](https://github.com/polterguy/magic.lambda/actions/workflows/build.yaml/badge.svg) - [magic.lambda](https://github.com/polterguy/magic.lambda)
* ![Build status](https://github.com/polterguy/magic.lambda.ad-auth/actions/workflows/build.yaml/badge.svg) - [magic.lambda.ad-auth](https://github.com/polterguy/magic.lambda.ad-auth)
* ![Build status](https://github.com/polterguy/magic.lambda.auth/actions/workflows/build.yaml/badge.svg) - [magic.lambda.auth](https://github.com/polterguy/magic.lambda.auth)
* ![Build status](https://github.com/polterguy/magic.lambda.caching/actions/workflows/build.yaml/badge.svg) - [magic.lambda.caching](https://github.com/polterguy/magic.lambda.caching)
* ![Build status](https://github.com/polterguy/magic.lambda.config/actions/workflows/build.yaml/badge.svg) - [magic.lambda.config](https://github.com/polterguy/magic.lambda.config)
* ![Build status](https://github.com/polterguy/magic.lambda.crypto/actions/workflows/build.yaml/badge.svg) - [magic.lambda.crypto](https://github.com/polterguy/magic.lambda.crypto)
* ![Build status](https://github.com/polterguy/magic.lambda.csv/actions/workflows/build.yaml/badge.svg) - [magic.lambda.csv](https://github.com/polterguy/magic.lambda.csv)
* ![Build status](https://github.com/polterguy/magic.lambda.dates/actions/workflows/build.yaml/badge.svg) - [magic.lambda.dates](https://github.com/polterguy/magic.lambda.dates)
* ![Build status](https://github.com/polterguy/magic.lambda.guid/actions/workflows/build.yaml/badge.svg) - [magic.lambda.guid](https://github.com/polterguy/magic.lambda.guid)
* ![Build status](https://github.com/polterguy/magic.lambda.html/actions/workflows/build.yaml/badge.svg) - [magic.lambda.html](https://github.com/polterguy/magic.lambda.html)
* ![Build status](https://github.com/polterguy/magic.lambda.http/actions/workflows/build.yaml/badge.svg) - [magic.lambda.http](https://github.com/polterguy/magic.lambda.http)
* ![Build status](https://github.com/polterguy/magic.lambda.hyperlambda/actions/workflows/build.yaml/badge.svg) - [magic.lambda.hyperlambda](https://github.com/polterguy/magic.lambda.hyperlambda)
* ![Build status](https://github.com/polterguy/magic.lambda.image/actions/workflows/build.yaml/badge.svg) - [magic.lambda.image](https://github.com/polterguy/magic.lambda.image)
* ![Build status](https://github.com/polterguy/magic.lambda.io/actions/workflows/build.yaml/badge.svg) - [magic.lambda.io](https://github.com/polterguy/magic.lambda.io)
* ![Build status](https://github.com/polterguy/magic.lambda.json/actions/workflows/build.yaml/badge.svg) - [magic.lambda.json](https://github.com/polterguy/magic.lambda.json)
* ![Build status](https://github.com/polterguy/magic.lambda.logging/actions/workflows/build.yaml/badge.svg) - [magic.lambda.logging](https://github.com/polterguy/magic.lambda.logging)
* ![Build status](https://github.com/polterguy/magic.lambda.mail/actions/workflows/build.yaml/badge.svg) - [magic.lambda.mail](https://github.com/polterguy/magic.lambda.mail)
* ![Build status](https://github.com/polterguy/magic.lambda.math/actions/workflows/build.yaml/badge.svg) - [magic.lambda.math](https://github.com/polterguy/magic.lambda.math)
* ![Build status](https://github.com/polterguy/magic.lambda.mime/actions/workflows/build.yaml/badge.svg) - [magic.lambda.mime](https://github.com/polterguy/magic.lambda.mime)
* ![Build status](https://github.com/polterguy/magic.lambda.mssql/actions/workflows/build.yaml/badge.svg) - [magic.lambda.mssql](https://github.com/polterguy/magic.lambda.mssql)
* ![Build status](https://github.com/polterguy/magic.lambda.mysql/actions/workflows/build.yaml/badge.svg) - [magic.lambda.mysql](https://github.com/polterguy/magic.lambda.mysql)
* ![Build status](https://github.com/polterguy/magic.lambda.pgsql/actions/workflows/build.yaml/badge.svg) - [magic.lambda.pgsql](https://github.com/polterguy/magic.lambda.pgsql)
* ![Build status](https://github.com/polterguy/magic.lambda.scheduler/actions/workflows/build.yaml/badge.svg) - [magic.lambda.scheduler](https://github.com/polterguy/magic.lambda.scheduler)
* ![Build status](https://github.com/polterguy/magic.lambda.slots/actions/workflows/build.yaml/badge.svg) - [magic.lambda.slots](https://github.com/polterguy/magic.lambda.slots)
* ![Build status](https://github.com/polterguy/magic.lambda.sockets/actions/workflows/build.yaml/badge.svg) - [magic.lambda.sockets](https://github.com/polterguy/magic.lambda.sockets)
* ![Build status](https://github.com/polterguy/magic.lambda.strings/actions/workflows/build.yaml/badge.svg) - [magic.lambda.strings](https://github.com/polterguy/magic.lambda.strings)
* ![Build status](https://github.com/polterguy/magic.lambda.system/actions/workflows/build.yaml/badge.svg) - [magic.lambda.system](https://github.com/polterguy/magic.lambda.system)
* ![Build status](https://github.com/polterguy/magic.lambda.validators/actions/workflows/build.yaml/badge.svg) - [magic.lambda.validators](https://github.com/polterguy/magic.lambda.validators)
* ![Build status](https://github.com/polterguy/magic.library/actions/workflows/build.yaml/badge.svg) - [magic.library](https://github.com/polterguy/magic.library)
* ![Build status](https://github.com/polterguy/magic.signals/actions/workflows/build.yaml/badge.svg) - [magic.signals](https://github.com/polterguy/magic.signals)
* ![Build status](https://github.com/polterguy/magic.node/actions/workflows/build.yaml/badge.svg) - [magic.node](https://github.com/polterguy/magic.node)

## Summing up

This project helps you clone Magic, and all of its satellite projects, making it easier for you to debug and develop
Magic locally.

* [Magic Documentation](https://polterguy.github.io/)


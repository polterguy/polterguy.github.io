---
title: Getting Started with Magic and Hyperlambda
description: This tutorial gets you started with Magic and Hyperlambda, helping you install it locally, using either Docker or the source code directly, for then to walk you through how to automatically generate your HTTP API backend wrapping your SQL database.
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/og-getting-started.jpg"
---

# Getting started with Magic and Hyperlambda

The absolute easiest way to get started with Magic is to signup at [Aista website](https://aista.com), for then
to create a _"cloudlet"_. This gives you CDN, security out of the box, a pre configured backend,
etc. If you create a cloudlet at Aista.com, you can [skip to the next tutorial](/tutorials/database-crud/).
If you intend to run Magic locally, you should probably follow this article hands on.

* How to setup Magic locally in your own development environment using Docker or the code
* How to update Magic
* How to clone Magic's code
* How to get support for Magic

The easiest way to get started locally is to [download the docker-compose file from the primary Aista website](https://github.com/polterguy/magic/releases/download/v15.3.0/docker-compose.yml), assuming you have [Docker](https://www.docker.com/products/docker-desktop) installed, and then execute the following in a terminal window where you saved the file.

```
docker compose up
```

When your docker containers have started, open your browser and go to [http://localhost:5555](http://localhost:5555),
use the default connection string for SQLite, choose a root password, type in your name and email address, and Magic
should work out of the box without any hassle. If you want to test Magic's CRUD automation capabilities, you can
download the Sakila SQLite plugin that creates a database for you to play with. You can use Magic with SQL Server,
MySQL, MariaDB or PostgreSQL if you don't want to use SQLite.

* [Using Magic with Microsoft SQL Server](/tutorials/sql-server/)
* [Using Magic with PostgreSQL](/tutorials/postgresql/)
* [Using Magic with MySQL or MariaDB](/tutorials/mysql/)

## Download the code

If you can't use Docker, you can also configure your development environment locally on your
development machine using the code directly. If so you will first of all need the following components.

1. [Visual Studio](https://visualstudio.microsoft.com/downloads/) or [VS Code](https://code.visualstudio.com/download) + [DotNet CLI and SDK](https://dotnet.microsoft.com/download)
2. [NodeJS](https://nodejs.org/en/download/)
3. [Angular](https://angular.io/cli)
4. [Download Magic Cloud's source code](https://github.com/polterguy/magic) from GitHub

## Updating Magic

If you're using the docker images, updating Magic is fairly easy, and only requires you to stop Magic
for some few seconds, update the core, and restart your docker containers again. Below is the entire
recipe. Execute the following terminal commands one at the time. Make sure you execute the following
in _the same folder_ as where your main Magic _"docker-compose.yml"_ file is.

```
docker-compose down
docker pull aistamagic/magic-frontend
docker pull aistamagic/magic-backend
docker-compose up
```

## Cloning Magic

Magic is not one project, it's actually 40+ projects, implying if you clone only Magic,
you'll only get some few hundreds lines of C# code, while most of its actual code exists in one
of the 40+ satellite projects. Hence, to clone Magic to for instance maintain it, or look at its
code, you'll have to follow [the recipe provided in the magic.clone project](/documentation/magic.clone/).

## Support

If you have a support request of private nature, you can send us an
email at [info@aista.com](mailto:info@aista.com). If you want to submit a
feature request or a bug report, you can do such through the project's
[GitHub Issues](https://github.com/polterguy/magic/issues).

* Continue with [Automatically generate a CRUD Web API](/tutorials/database-crud/)

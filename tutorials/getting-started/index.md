---
title: Getting Started with Magic and Hyperlambda
description: This tutorial walks you through the process of getting started with Magic and Hyperlambda, helping you install it locally, using either Docker or the source code directly. It guides you through downloading, installation, and all the way until you've crudified your first database.
---

# Getting started with Magic and Hyperlambda

In this tutorial we will cover the following parts of Magic and Hyperlambda.

* How to setup Magic locally in your own development environment using Docker or the code
* How to deploy Magic to your own VPS
* How to update Magic
* How to clone Magic's code
* How to get support for Magic

The easiest way to get started is to [download the docker-compose file](https://github.com/polterguy/magic/releases/download/v10.0.4/docker-compose.yml), assuming you have [Docker](https://www.docker.com/products/docker-desktop)
installed, and then execute the following in a terminal window where you saved the file.

```
docker-compose up
```

When your docker containers have started, open your browser and go to [http://localhost:5555](http://localhost:5555),
and use the default connection string for MySQL, choose a root password, crudify your Magic database,
type your name and email address when you generate a key pair, and Magic should work out of the box without
any hassle. If you want to test Magic's CRUD automation capabilities, there's a _"sakila"_ SQL script that you
can execute in the _"SQL"_ menu item to create an example database. In the video below I am illustrating this process.

<div class="video">
<iframe width="560" height="315" style="position:absolute; top:0; left:0; width:100%; height:100%;" src="https://www.youtube.com/embed/ldy-idQO_jA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

If you want to use Magic with Microsoft SQL Server or PostgreSQL you can find recipes for this below.

* [Using Magic with Microsoft SQL Server](/tutorials/sql-server/)
* [Using Magic with PostgreSQL](/tutorials/postgresql/)
* [Using Magic with MySQL](/tutorials/mysql/)

## Download the code

If you can't use Docker, you can also configure your development environment locally on your
development machine using the code directly. If so you will first of all need the following components.

1. [Visual Studio](https://visualstudio.microsoft.com/downloads/) or [VS Code](https://code.visualstudio.com/download) + [DotNet CLI and SDK](https://dotnet.microsoft.com/download)
2. [NodeJS](https://nodejs.org/en/download/)
3. [Angular](https://angular.io/cli)
4. [MySQL](https://dev.mysql.com/downloads/mysql/) or [Microsoft SQL Server](https://www.microsoft.com/en-us/sql-server/sql-server-downloads)
5. [Magic Cloud](https://github.com/polterguy/magic/releases)

In the video below I go through the manual setup process.

<div class="video">
<iframe width="560" height="315" style="position:absolute; top:0; left:0; width:100%; height:100%;" src="https://www.youtube.com/embed/H7RH4lrISGw" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Deploy Magic

To deploy Magic into production you can follow [this recipe](/documentation/magic.deploy/), which
guides you through setting up your VPS server to host Magic.

## Updating Magic

If you're using the docker images, updating Magic is fairly easy, and only requires you to stop Magic
for some few seconds, update the core, and restart your docker containers again. Below is the entire
recipe. Execute the following terminal commands one at the time. Make sure you execute the following
in _the same folder_ as where your main Magic _"docker-compose.yml"_ file is.

```
docker-compose down
docker pull servergardens/magic-frontend
docker pull servergardens/magic-backend
docker-compose up
```

## Cloning Magic

Magic is not one project, it's actually 35+ projects, implying if you clone only Magic,
you'll only get some few hundreds lines of code, while most of its actual code exists in one
of the 35+ satellite projects. Hence, to clone Magic, to for instance maintain it, look at its
code etc, you'll have to follow [this recipe](/documentation/magic.clone/).

## Support

If you have a support request of private nature, you can send us an
email at [th@aista.com](mailto:th@aista.com). If you want to submit a
feature request or a bug report, you can do such through the project's
[GitHub Issues](https://github.com/polterguy/magic/issues).

* Continue with [Automatically generate a CRUD Web API](/tutorials/database-crud/)

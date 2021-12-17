
# Getting started with Magic

There are multiple ways to use Magic, depending upon whether or not you just want to try it out locally
on your development machine, use the Docker images to more rapidly getting up to speed, deploy it
to your production server, or clone its source code locally to view and debugs its source code.
In this section we'll walk you through all of these different methods to get started with Magic.

## Using Docker

The easiest way to get started is to [download the docker-compose.yml file](https://github.com/polterguy/magic/releases/download/v10.0.4/docker-compose.yml), assuming you have [Docker](https://www.docker.com/products/docker-desktop)
installed, and then execute the following in a terminal window where you saved the file. This is the
exact same process for both Windows, Mac, and Linux.

```
docker-compose up
```

When your Docker containers have started, open your browser and go to [http://localhost:5555](http://localhost:5555),
and use the default configuration settings for MySQL, choose a root password, crudify your Magic database,
type your name and email address when you generate a key pair, and Magic should work out of the box without
any hassle. If you want to test Magic's CRUD automation capabilities, there's a _"sakila"_ SQL script that you
can execute in the _"SQL"_ menu item to create an example database. In the video below I am illustrating this process.

<div style="position:relative; padding-bottom:56.25%; padding-top:30px; height:0; overflow:hidden;margin-top:4rem;margin-bottom:4rem;">
<iframe width="560" height="315" style="position:absolute; top:0; left:0; width:100%; height:100%;" src="https://www.youtube.com/embed/ldy-idQO_jA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

**Notice** - If you want to use SQL Server instead of MySQL you can follow [this recipe](/tutorials/sql-server/).

## Download the code

If you don't want to use Docker, you can also configure your development environment locally on your
development machine using the code directly. If so you will first of all need the following components.

1. [Visual Studio](https://visualstudio.microsoft.com/downloads/) or [VS Code](https://code.visualstudio.com/download) + [DotNet CLI and SDK](https://dotnet.microsoft.com/download)
2. [NodeJS](https://nodejs.org/en/download/)
3. [Angular](https://angular.io/cli)
4. [MySQL](https://dev.mysql.com/downloads/mysql/) or [Microsoft SQL Server](https://www.microsoft.com/en-us/sql-server/sql-server-downloads)

In the video below I go through the manual setup process.

<div style="position:relative; padding-bottom:56.25%; padding-top:30px; height:0; overflow:hidden;margin-top:4rem;margin-bottom:4rem;">
<iframe width="560" height="315" style="position:absolute; top:0; left:0; width:100%; height:100%;" src="https://www.youtube.com/embed/H7RH4lrISGw" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Deploy Magic

The easiest method to deploy Magic into production, is to follow [this recipe](/documentation/magic.deploy/), which
guides you through setting up your VPS server to host Magic. Notice, if this is too complex for you,
[we do provide this as a service](https://servergardens.com) for a fee.

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

**Notice** - As of version 9.9.1 the development version of the docker images will store your
custom modules as you tear down your docker containers, but it will _not_ store your _"appsettings.json"_
file. The deployment version above however will also keep your _"appsettings.json"_ file, in addition
to your custom modules - Implying updating Magic both in your local development environment, and
in your production environment should be fairly straight forward - Except in your local development
environment, you'll need to re-configure Magic after tearing down and updating your containers.

## Cloning Magic

Magic is not one project, it's actually more than 30 projects, implying if you clone only Magic,
you'll only get some few hundreds lines of code, while most of its actual code exists in any
of the 30+ satellite projects. Hence, to clone Magic, to for instance maintain it, look at its
code, etc you'll have to follow [this recipe](/documentation/magic.clone/).

## Support

If you have a support request of private nature, you can send us an
email at [thomas@servergardens.com](mailto:thomas@servergardens.com). If you want to submit a
feature request or a bug report, you can do such through the project's
[GitHub Issues](https://github.com/polterguy/magic/issues).

## License

Magic is 100% Open Source and free to use, also in proprietary and closed source applications.
The only exception is if you improve the frontend dashboard, or improve one of its plugins,
at which point you must make your improvements publicly available for others to use.

## Go Pro

[ServerGardens.Com](https://servergardens.com) provides a whole range of professional services
based upon Magic. Check out our website for details.

* [Documentation](/documentation/)

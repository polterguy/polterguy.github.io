
# Using Magic with SQL Server

This tutorial walks you through how to use Magic with SQL Server instead of MySQL.
In the following video I am walking you through the whole process.

<div style="position:relative; padding-bottom:56.25%; padding-top:30px; height:0; overflow:hidden;margin-top:4rem;margin-bottom:4rem;">
<iframe width="560" height="315" style="position:absolute; top:0; left:0; width:100%; height:100%;" src="https://www.youtube.com/embed/iRc5Y8xw6VM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

The default _"docker-compose.yml"_ file for Magic will create a MySQL Docker container. If you instead
want to use SQL Server, you'll need a slightly modified _"docker-compose.yml"_ file. Below is a complete
docker-compose file, except it spawns up a SQL Server database instance image, and not a MySQL image.

```
version: "3.3"

services:

  db:
    image: mcr.microsoft.com/mssql/server
    environment:
        SA_PASSWORD: Your_password123
        ACCEPT_EULA: Y

  backend:
    image: servergardens/magic-backend:latest
    depends_on:
      - db
    restart: always
    ports:
      - "4444:4444"
    volumes:
      - modules:/magic/files/modules

  frontend:
    image: servergardens/magic-frontend:latest
    depends_on:
      - backend
    restart: always
    ports:
      - "5555:80"

volumes:
  modules:
```

If you create a file named _"docker-compose.yml"_ and save it to any directory on your machine with the
above content, for then to run the following command in that _same directory_, this should start an SQL
Server instance on your machine. Notice, this should work transparently on both Windows, Linux, and OS X.

```
docker-compose up
```

**Notice** - If you already have the default _"docker-compose.yml"_ file's containers running, you'll have
to _stop_ these containers, since the above file uses the same ports on your host operating system as the MySQL
file does. To do this, go to the folder where you have your MySQL _"docker-compose.yml"_ file using a
terminal window and type `docker-compose down`.

## Configuring Magic

When you configure Magic, you'll need to choose the _"mssql"_ database type. Afterwards you'll need to
paste the following into its connection string settings.

```
Server=db;Database={database};User=sa;Password=Your_password123;
```

**Notice** - When just playing around on your local development machine, the password is not really that
important, since Docker will _not_ expose your SQL Server instance outside of the virtualised Docker network.
So the above password, although obviously not good enough for a real world production environment,
would be more than enough to secure your development machine.

The rest of the process is similar to the MySQL equivalent, and implies crudifying your backend, creating
a key pair, and running the assumptions. Just remember to type your name and email address into the
identity and email textboxes as Magic asks you for this.

**Notice** - You also obviously need to have [Docker](https://www.docker.com/products/docker-desktop)
installed on your development machine.

## Magic Docker internals

The above _"docker-compose.yml"_ file creates 3 containers.

* The Magic Dashboard
* The Magic Backend
* A Microsoft SQL Server instance

The Magic dashboard and backend are images I maintain and update every time I create a release of Magic.
If you want to update these in the future as I create new releases, all you need to do is to write
`docker pull servergardens/magic-frontend:latest` and `docker pull servergardens/magic-backend:latest`
in _any_ terminal window. This works since Docker uses a local _"repository of images"_ on your host machine.

To stop the containers you need to go to the same folder you saved your _"docker-compose.yml"_
file in, and type `docker-compose down`.

## Wrapping up

In this micro-tutorial we used Docker to configure Magic to use Microsoft SQL Server instead of MySQL.
To create a more resilient production ready environment, you'd probably benefit from reading more about
Docker by finding tutorials related to this online.

* [Documentation](/documentation/)

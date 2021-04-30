
# Using Magic with SQL Server

This tutorial walks you through how to use Magic with an SQL Server instance instead of the default MySQL
instance. If you don't care about SQL Server, there are no reasons for you to read this article.

The default _"docker-compose.yml"_ file for Magic will create a MySQL Docker container. If you instead
want to use SQL Server, you'll need to slightly modify your docker-compose file. Below is a complete
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

  frontend:
    image: servergardens/magic-frontend:latest
    depends_on:
      - backend
    restart: always
    ports:
      - "5555:80"
```

If you create a file named _"docker-compose.yml"_ and save it to any directory on your machine with the
above content, for then to run the following command in that _same directory_, this should start an SQL
Server instance on your machine. Notice, this should work on both Windows, Linux and Mac OS X. I have tried it only on
Mac though, but this should not make a difference.

```
docker-compose up -d
```

**Notice** - If you already have the default _"docker-compose.yml"_ file's containers running, you'll have
to _stop_ these containers, since the above file uses the same ports on your host operating system as that
file does. To do this, go to the folder where you have your MySQL _"docker-compose.yml"_ file using a terminal
window and type `docker-compose down`.

When your Docker images are up running, you can visit [localhost:5555](http://localhost:5555) and you should
come to the Magic Dashboard. Login with _"root/root"_ and configure Magic as you see fit.

## Magic Docker internals

The above _"docker-compose.yml"_ file creates 3 containers.

* The Magic Dashboard
* The Magic Backend
* A Microsoft SQL Server instance

The Magic dashboard and backend are images I maintain and update every time I create a release of Magic.
If you want to update these in the future as I create new releases, all you need to do is to write
`docker pull servergardens/magic-frontend:latest` and `docker pull servergardens/magic-backend:latest`
in any terminal window.

To stop the containers you need to go to the same folder you saved your _"docker-compose.yml"_
file in, and type `docker-compose down`.

**Notice** - If you stop your containers this will destroy your databases, since the above file does not add
any `volumes` for your SQL Server database catalogues. However, if all you want to do is to play around
with Magic locally this shouldn't matter too much. If you want to modify the above file to persist
your database catalogues, you can probably easily achieve this by searching for _"sql server volumes persist databases"_
or something similar.

## Configuring Magic

When you configure Magic, you'll need to choose the _"mssql"_ database type. Afterwards you'll need to
paste the following into its connection string settings.

```
Server=db;Database={database};User=sa;Password=Your_password123;
```

**Notice**** - When just playing around on your local development machine, the password is not really that
important, since Docker will _not_ expose your SQL Server instance outside of the virtualized Docker network.
So the above password, although obviously not good enough for a real world production environment,
would be more than enough to secure your development machine.

The rest of the process is similar to the MySQL equivalent, and implies crudifying your backend, creating
a key pair, and running the assumptions. Just remember to type your name and email address into the
identity and email textboxes as Magic asks you for these parts.

**Notice** - You also obviously need to have [Docker](https://www.docker.com/products/docker-desktop)
installed on your development machine.

## Creating your own app

Notice, if you create _other_ apps needing to access the Magic backend, you'll have to expose the Magic
backend to your host operating system. To understand this process search for _"Docker expose port to host operating system"_.
It basically implies adding one single entry to the above docker-compose file.

## Wrapping up

In this micro-tutorial we used Docker to configure Magic to use Microsoft SQL Server instead of MySQL.
To create a more reciliant production ready environment, you'd probably benefit from reading more about
Docker by finding tutorials related to Docker online.

* [Documentation](/documentation/)

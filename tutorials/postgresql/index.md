
# Using Magic with PostgreSQL

The default _"docker-compose.yml"_ file for Magic will create a MySQL Docker container. If you instead
want to use Postgres, you'll need a slightly modified _"docker-compose.yml"_ file. Below is a complete
docker-compose file, except it spawns up a PostgreSQL database image and not a MySQL image.

```yaml
version: "3.3"

services:

  db:
    image: postgres:9.3
    restart: always
    environment:
      - POSTGRES_PASSWORD=ThisIsNotAGoodPassword

  backend:
    image: servergardens/magic-backend:latest
    depends_on:
      - db
    restart: always
    ports:
      - "4444:4444"
    volumes:
      - etc_magic_folder_pg:/magic/files/etc
      - modules_magic_folder_pg:/magic/files/modules
      - config_magic_folder_pg:/magic/config

  frontend:
    image: servergardens/magic-frontend:latest
    depends_on:
      - backend
    restart: always
    ports:
      - "5555:80"

volumes:
  etc_magic_folder_pg:
  modules_magic_folder_pg:
  config_magic_folder_pg:
```

If you create a file named _"docker-compose.yml"_ and save it to any directory on your machine with the
above content, for then to run the following command in that _same directory_, this will start a 
Postgres instance on your machine. Notice, this should work transparently on both Windows, Linux, and OS X.

```
docker-compose up
```

## Configuring Magic

When you configure Magic, you'll need to choose the _"pgsql"_ database type. Afterwards you'll need to
paste the following into its connection string settings.

```
User ID=postgres;Password=ThisIsNotAGoodPassword;Host=db;Database={database};
```

The rest of the process is similar to the MySQL equivalent, and implies crudifying your backend, creating
a key pair, and running the assumptions.

**Notice** - You also obviously need to have [Docker](https://www.docker.com/products/docker-desktop)
installed on your development machine.

## Wrapping up

In this micro-tutorial we used Docker to configure Magic to use PostgreSQL instead of MySQL.
To create a more resilient production ready environment, you'd probably benefit from reading more about
Docker by finding tutorials related to this online.

* [Documentation](/documentation/)

---
title: Using Magic with Microsoft SQL Server
description: In this article you will setup Magic using Docker and SQL Server. The article guides you through everything you need to know, starting out with a docker-compose.yml file for getting Magic up running, using SQL Server as your backend database.
---

# Using Magic with SQL Server

The default _"docker-compose.yml"_ file for Magic will create a MySQL Docker container. If you instead
want to use SQL Server, you'll need a slightly modified _"docker-compose.yml"_ file. Below is a complete
docker-compose file, except it spawns up a SQL Server database instance image, and not a MySQL image.

```yaml
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
      - etc_magic_folder_ms:/magic/files/etc
      - modules_magic_folder_ms:/magic/files/modules
      - config_magic_folder_ms:/magic/config

  frontend:
    image: servergardens/magic-frontend:latest
    depends_on:
      - backend
    restart: always
    ports:
      - "5555:80"

volumes:
  etc_magic_folder_ms:
  modules_magic_folder_ms:
  config_magic_folder_ms:
```

If you create a file named _"docker-compose.yml"_ and save it to any directory on your machine with the
above content, for then to run the following command in that _same directory_, this will start an SQL
Server instance on your machine.

```
docker-compose up
```

## Configuring Magic

When you configure Magic, you'll need to choose the _"mssql"_ database type. Afterwards you'll need to
paste the following into its connection string settings and choose a root password.

```
Server=db;Initial Catalog={database};User=sa;Password=Your_password123;
```

The rest of the process is similar to the MySQL equivalent, and implies crudifying your backend, creating
a key pair, and running the assumptions. You also need to
have [Docker](https://www.docker.com/products/docker-desktop) installed on your development machine.

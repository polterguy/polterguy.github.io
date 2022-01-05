---
title: Using Magic with MySQL
description: In this article you will setup Magic using Docker and MySQL. The article guides you through everything you need to know, starting out with a docker-compose.yml file for getting Magic up running, using MySQL as your backend database.
---

# Using Magic with MySQL

For reference purposes, and to be complete in our documentation, we've provided this guide of how to
get started with Magic using MySQL - Even though MySQL is the database type in the default starter
guide. Below is a complete docker-compose file, that spawns up a MySQL image in addition to the Magic
backend and frontend.

```yaml
version: "3.3"

services:

  db:
    image: mysql
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: ThisIsNotAGoodPassword

  backend:
    image: servergardens/magic-backend:latest
    depends_on:
      - db
    restart: always
    ports:
      - "4444:4444"
    volumes:
      - etc_magic_folder_my:/magic/files/etc
      - modules_magic_folder_my:/magic/files/modules
      - config_magic_folder_my:/magic/config

  frontend:
    image: servergardens/magic-frontend:latest
    depends_on:
      - backend
    restart: always
    ports:
      - "5555:80"

volumes:
  etc_magic_folder_my:
  modules_magic_folder_my:
  config_magic_folder_my:
```

If you create a file named _"docker-compose.yml"_ and save it to any directory on your machine with the
above content, for then to run the following command in that _same directory_, this will start a MySQL
instance on your machine.

```
docker-compose up
```

## Configuring Magic

When you configure Magic, you'll need to choose the _"mysql"_ database type. Afterwards you'll need to
paste the following into its connection string settings.

```
Server=db;Database={database};Uid=root;Pwd=ThisIsNotAGoodPassword;SslMode=Preferred;Old Guids=true;
```

You also need to have [Docker](https://www.docker.com/products/docker-desktop)
installed on your development machine.

* [Continue with reference documentation](/documentation/)

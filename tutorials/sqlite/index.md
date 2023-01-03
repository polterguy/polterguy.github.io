---
title: Using Magic with SQLite
description: In this article you will setup Magic using Docker and SQLite. The article guides you through everything you need to know, starting out with a docker-compose.yml file for getting Magic up running, using SQLite as your backend database.
---

# Using Magic with SQLite

In this tutorial we will cover the following parts of Magic and Hyperlambda.

* How to use Magic with SQLite

The default _"docker-compose.yml"_ file for Magic will create a MySQL Docker container. If you instead
want to use SQLite, you'll need a slightly modified _"docker-compose.yml"_ file. Below is a complete
docker-compose file, except it doesn't create a MySQL docker container at all. This is because SQLite
allows you to simply use your file system as your _"connection string"_ and connect directly to a file,
making it significantly easier to use since there's no network configuration, or explicit requirement
to even have a database server installed at all.

```yaml
version: "3.3"

services:

  backend:
    image: aistamagic/magic-backend:latest
    depends_on:
      - db
    restart: always
    ports:
      - "4444:4444"
    volumes:
      - etc_magic_folder_sqlite:/magic/files/etc
      - modules_magic_folder_sqlite:/magic/files/modules
      - config_magic_folder_sqlite:/magic/config

  frontend:
    image: aistamagic/magic-frontend:latest
    depends_on:
      - backend
    restart: always
    ports:
      - "5555:80"

volumes:
  etc_magic_folder_sqlite:
  modules_magic_folder_sqlite:
  config_magic_folder_sqlite:
```

If you create a file named _"docker-compose.yml"_ and save it to any directory on your machine with the
above content, for then to run the following command in that _same directory_, this will start Magic
for you _without_ any database servers at all, allowing you to use SQLite's integrated file system adapter.

```
docker-compose up
```

## Configuring Magic

When you configure Magic, you'll need to choose the _"sqlite"_ database type. Afterwards you'll need to
_keep the existing connection string as is_.

The rest of the process is similar to the MySQL equivalent, and implies crudifying your backend, creating
a key pair, and running the assumptions. You also need to
have [Docker](https://www.docker.com/products/docker-desktop) installed on your development machine.

Notice, since SQLite is based upon the file system, this implies that in order to create a new database,
you'll need to create an empty _"xxx.db"_ file inside your _"/data/"_ folder. To see your _"/data/"_ folder
make sure you enable for _"System files"_ in Hyper IDE, select the data folder, and create for instance
a new empty file called _"sakila.db"_. Then go to the SQL menu item, purge your server-side cache, for then
to load up the _"sakila"_ script that's been ported to SQLite that you can find by clicking the _"Load"_
button. Make sure you select your newly created _"sakila"_ database before you execute the script.

* Continue with [Using Magic with PostgreSQL](/tutorials/postgresql/)

---
title: SQL endpoints
description: Magic's built-in SQL endpoints, executing SQL, retrieving database meta data, and managing SQL snippet files.
header:
  image: /assets/images/hero/endpoints-top.webp
  og_image: /assets/images/hero/endpoints-top-og.png
  image_description: SQL endpoints
---

## SQL related endpoints

These endpoints allow you to retrieve meta data about your databases, and/or connection strings, in addition
to execute SQL towards a specific database, etc. These endpoints are the foundation for the _"SQL"_ menu item
in the Magic dashboard.

### GET magic/system/sql/connection-strings

This endpoint returns all database connection strings existing in the backend, being of type **[databaseType]**,
where the type can be one of 'mysql', 'mssql', 'pgsql' or 'sqlite'. The endpoint can only be invoked by a root user.

This endpoint is not intended for you to consume in your own code.

### GET magic/system/sql/databases

This endpoint returns meta data associated with the specified **[databaseType]** and **[connectionString]**
combination, such as all databases, all tables within each database, all columns, and any foreign keys existing
between columns. The endpoint can only be invoked by a root user. The endpoint requires the following query
argument(s).

* __[databaseType]__ - Type of database, one of 'mysql', 'mssql', 'pgsql', or 'sqlite'
* __[connectionString]__ - Name of connection string such as for instance _"generic"_

Notice, the endpoint is fairly expensive to execute, and therefore its result is cached on the server with
the key of _"magic.sql.databases.xxx.yyy"_ where _"xxx"_ is the database type and _"yyy"_ is the connection
string name.

This endpoint is not intended for you to consume in your own code.

### GET magic/system/sql/default-database-type

This endpoint returns your default database type, in addition to all databases types the system currently
supports. An example of invoking the endpoint can be found below.

```
{
  "options": [
    "mssql",
    "mysql",
    "pgsql"
  ],
  "default": "mysql"
}
```

The above result implies that MySQL is the default database type, while the system still has support for both
'mssql' and 'pgsql' in addition to 'mysql'. The endpoint can only be invoked by a root user.

This endpoint is not intended for you to consume in your own code.

### POST magic/system/sql/evaluate

This endpoint allows you to evaluate the specified SQL towards your database. The endpoint requires the
following payload.

```
{
  "databaseType": "sqlite",
  "database": "magic",
  "sql": "select * from roles",
  "safeMode": true,
  "batch": false
}
```

The above arguments imply the following.

* __[databaseType]__ - Type of database to execute your SQL towards, either 'mysql', 'pgsql', 'mssql' or 'sqlite'
* __[database]__ - Name of database to execute your SQL towards _and_ connection string to use. E.g. `[generic|mysql]`
* __[sql]__ - Actual SQL to execute
* __[safeMode]__ - If true only the first 200 records will be returned, to avoid exhausting your server for huge responses
* __[batch]__ - If true, will execute the SQL as a _"batch"_ SQL statement. Only relevant for SQL Server when executing scripts containing the _"go"_ keyword

The endpoint can only be invoked by a root user.

This endpoint is not intended for you to consume in your own code.

### GET magic/system/sql/list-files

This endpoint lists all SQL files associated with the specified **[databaseType]** query parameter. These are
template files, stored by the user or distributed by the system by default. The endpoint can only be invoked
by a root user. The endpoint requires the following query argument(s).

* __[databaseType]__ - Type of database, one of 'mysql', 'mssql', 'pgsql' or 'sqlite'.

### PUT magic/system/sql/save-file

This endpoint saves a template SQL snippet file in your backend, and requires the following payload.

```
{
  "databaseType": "foo",
  "filename": "foo",
  "content": "foo"
}
```

The above arguments imply the following.

* __[databaseType]__ - Type of database, e.g. 'mysql', 'pgsql' or 'mssql'
* __[filename]__ - Filename of where to save the SQL file
* __[content]__ - Actual SQL content of your file

Your SQL snippet files are saved in your backend inside of your _"/etc/xxx/templates/"_ folder, where _"xxx"_
is your database type such as for instance 'pgsql', 'mysql' or 'mssql'.

This endpoint is not intended for you to consume in your own code.

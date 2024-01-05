---
title: Endpoints
description: Documentation for the most important endpoints you can find in Magic's middleware
og_image: https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/backend-crud.jpg
---

Magic contains a whole range of endpoints, or _"middleware"_ parts, that the system itself
relies upon to function. You can play around with these endpoints by using the [Endpoints](/dashboard/endpoints/)
component and ensure you show your system endpoints.
Most of these endpoints are for internal use through the Magic dashboard, and should as a general
rule of thumb _not_ be consumed directly by you - But some of these endpoints are useful for your own projects.

![Endpoints](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/endpoints.jpg)

Notice, all endpoints that requires authorization of some sort assumes a valid JWT token is transmitted
in the `Authorization` HTTP header as a _"Bearer"_ type of token, and if not, the user will not be
allowed to invoke the endpoint, and an HTTP status code of 401 will be returned. To retrieve a JWT token
use the `magic/system/auth/authenticate` endpoint.

## Authentication and authorisation endpoints

These are the endpoints related to the authentication and authorisation parts of Magic. You can find
their Hyperlambda files in the _"/system/auth/"_ folder. These endpoints are typically useful for you
as you implement your own authentication logic in your own code, and most of these endpoints
are intended for you to consume yourself as you see fit.

### GET magic/system/auth/authenticate

This endpoint allows you to authenticate towards your Magic backend with a username and password
combination. It's mostly a thin layer on top of your **[magic.auth.authenticate]** slot.
**[magic.auth.authenticate]** requires two query arguments being as follows.

* __[username]__ - Username of user wanting to authenticate
* __[password]__ - Password of user wanting to authenticate

The endpoint can be invoked by anyone, and does not have any authorisation requirements. The endpoint
will return a JWT token you can use for consecutive requests towards your backend, authorising you
to invoke endpoints your user is authorised to invoke.

Magic relies upon the JWT tokens
being transmitted as _"Bearer"_ tokens in the _"Authorization"_ HTTP header, implying you'll have to
ensure the resulting JWT token from invoking the above endpoint is attached to consecutive HTTP requests.
This endpoint can be invoked by anyone, including non-authenticated clients.
This endpoints is intended for you to consume from your own code.

### PUT magic/system/auth/change-password

This endpoint allows an existing user to change his or her password. It can only change the password of
the currently authenticated user, and takes the new password as the following payload.

```
{
  "password": "new-password"
}
```

This endpoint can be invoked by anyone as long as they have authenticated towards your backend previously.
This endpoints is intended for you to consume from your own code.

### GET magic/system/auth/endpoints

This endpoint returns the authorisation requirements for all endpoints in the system. It does not require
any arguments. It returns one item for each Hyperlambda endpoint in the system, with its associated verb,
and a list of roles the user must belong to in order to invoke the endpoint, if the endpoint requires
authorisation.

The endpoint can be invoked by anyone, and does not have any authorisation requirements.
This endpoint caches its result for 5 minutes, implying changes done to the authorisation
requirements of your endpoints will not be accessible for clients before 5 minutes after your changes have
been applied, unless you explicitly delete the cache item for the endpoint.
This endpoints is intended for you to consume from your own code.

### GET magic/system/auth/refresh-ticket

This endpoint allows an already authenticated user to retrieve a new JWT token with an expiration date
further into the future. The idea of the endpoint is to allow for an authenticated user to non-stop
constantly invoke this endpoint some few minutes before his existing JWT token expires, to retrieve
a new JWT token, preventing the user from being thrown out of the backend as his or her existing token
expires.

The endpoint does not take any arguments, but can only be invoked by an already authenticated
user, implying you'll need to pass in your JWT token to it in the Authorization HTTP header as a
_"Bearer"_ token or the endpoint will return _"Access denied"_.
This endpoints is intended for you to consume from your own code.

### GET magic/system/auth/verify-ticket

This endpoint allows a frontend to verify an existing JWT token, and it will return _"success"_ if
the JWT token is valid and can be used in consecutive invocations requiring authorisation somehow.
The endpoint can be invoked by any user as long as the user is authenticated.

The endpoint does not
require any arguments, but can only be invoked by an already authenticated user, implying you'll need
to pass in your JWT token to it in the Authorization HTTP header as a _"Bearer"_ token. If the JWT
token is not valid the endpoint will return a 401 status code with _"Access denied"_ as its message.
This endpoints is intended for you to consume from your own code.

## Plugins endpoints

These are endpoints related to the [Plugins](/dashboard/plugins/) component somehow, allowing you to install
new plugins. The Plugins component is a micro service _"App Store"_ for your
Magic cloudlet, allowing your Magic server to install backend modules on the fly, resulting
in having some backend micro service installed into your backend, without interrupting normal
usage. None of these endpoints are really intended to be consumed by your own code, but only
for internal usage by Magic itself.

### GET magic/system/bazar/app-manifests

This endpoint returns a list of plugin apps that have been installed in your backend. Each item will
contain a date of installation, the username of the user who installed the app, the name and version
of the app, etc. Below is an example of what the endpoint might
return if you only have one plugin item installed. The endpoint can only be invoked by a root user and
it requires no arguments.

```
[
  {
    "name": "Babel Fish",
    "version": "v1.0.0",
    "module_name": "babelfish",
    "installed_by": "root",
    "installed": "2022-01-31T06:03:01.669Z"
  }
]
```

This endpoint is not intended for you to consume in your own code.

### POST magic/system/bazar/install-plugin

This endpoint downloads a plugin item as a zip file from the specified URL, and unzips the file into the backend,
for the to install the plugin by executing its startup files. The endpoint can only be invoked by a root user
and requires the following payload.

```
{
  "url": "https://some-bazar.com/download?app=some-app.zip",
  "name": "some-module"
}
```

The plugin will be downloaded from the specified URL and assumed to be a zip file. The zip file
will then be unzipped into your _"modules"_ folder as the specified _"name"_. Notice, any
previously installed plugins with the same name will be automatically deleted and uninstalled.

## Cache related endpoints

These are the endpoints related to your server side cache, and allows you to delete a single
cache item on the server. Internally Magic is using server-side cache sparsingly for some
expensive operations, such as retrieving meta data from your database. Sometimes you need to
manually purge your cache, and/or delete individual cache items on your server, to re-retrieve
data invalidating your cache in the process. This section provides
information about such operations for such scenarios.

These endpoints are not intended to be consumed in your own code, but only
for internal usage by Magic itself.

### DELETE magic/system/cache/delete

This endpoint requires an **[id]** as a query parameter, and will delete the associated server side
cache item. It can only be invoked by a root user. The endpoint requires the following argument(s).

* __[id]__ - Mandatory id of cache item to evict

This endpoint is not intended for you to consume in your own code.

## Configuration related endpoints

These endpoints are related to configuration of your system, and allows you to read and modify
configuration settings as you see fit. These endpoints are typically not intended for being used
directly by your code, but for the most parts only used during initialisation of your Magic server,
and/or as you change configuration settings in Magic.
None of these endpoints are intended to be consumed in your own code, but only
for internal usage by Magic itself.

### GET magic/system/config/load

This endpoint loads your configuration settings and returns it to the caller. The endpoint
can only be invoked by a root user and does not require any arguments.

This endpoint is not intended for you to consume in your own code.

### POST magic/system/config/save

This endpoint allows you to save your configuration settings. The specified paylod will
in its entirety overwrite your existing _"appsettings.json"_ file. The endpoint
can only be invoked by a root user.

The endpoint can accept any type of JSON payload,
however whatever you supply to the endpoint will in its entirety be persisted in
your backend as your _"appsettings.json"_ file, implying if you supply bogus data,
your backend will no longer function correctly.
This endpoint is not intended for you to consume in your own code.

### GET magic/system/config/status

This endpoint returns the setup status of your system, implying if the system has been correctly
initialised. The endpoint requires no argument. If this endpoint does _not_ return true, the
frontend dashboard will guide you through the process of finishing the configuration process before
allowing you to gain access to other parts of your Magic server. The endpoint can only be invoked
by a root user. This endpoint is not intended for you to consume in your own code.

### POST magic/system/config/setup

This endpoint will setup Magic, and should only be used initially as you install Magic, and should
never be invoked afterwards, unless you need to reset your root user's password. This endpoint is
being used as you setup your Magic cloudlet initially, and creates a root user, in addition to creating
a JWT secret, etc.

## CRUD related endpoints

These endpoints allows you to among other things generate CRUD HTTP backend modules, and is at the heart of
the [Endpoint Generator](/dashboard/endpoint-generator/). In addition these endpoints allows you to generate
SQL based HTTP endpoints. These endpoints are not intended for being directly
invoked by your code, but rather from the Magic dashboard as it is creating backend endpoints for you.

## Backend CRUD operations

This section describes the parts that generates backend HTTP endpoints for you, typically wrapping a database
table with CRUD operations.

### POST magic/system/crudifier/crudify

This endpoint creates one CRUD HTTP endpoint for you, wrapping the specified database table
with the specified HTTP verb/CRUD-operation. The endpoint requires the following payload.

```
{
  "verbose": true,
  "join": true,
  "databaseType": "xxx",
  "moduleName": "xxx",
  "database": "xxx",
  "table": "xxx",
  "moduleUrl": "xxx",
  "returnId": true,
  "template": "xxx",
  "verb": "xxx",
  "auth": "xxx",
  "log": "xxx",
  "overwrite": true,
  "validators": "xxx",
  "cache": 42,
  "publicCache": true,
  "cqrs": true,
  "cqrsAuthorisation": "xxx",
  "cqrsAuthorisationValues": "xxx",
  "args": "*",
  "conditions": "*"
}
```

The above fields implies the following.

* __[verbose]__ - If true more query parameter types will be generated for your GET/read endpoint
* __[join]__ - If true, joins will be automatically applied for the endpoint
* __[databaseType]__ - Type of database, such as for instance 'pgsql', 'mssql', or 'mysql'
* __[moduleName]__ - The root URL of your endpoint
* __[database]__ - Name of database, and connection string, e.g. `[generic|sakila]`
* __[table]__ - Name of table to wrap
* __[moduleUrl]__ - Secondary part of your CRUD endpoint's URL
* __[returnId]__ - Only relevant for POST/create endpoints, but if true will return the ID of the newly created item
* __[template]__ - Full relative path of the template to use, e.g. '/system/crudifier/templates/crud.template.get.hl'
* __[verb]__ - HTTP verb to wrap, either 'delete', 'get', 'post' or 'put'
* __[auth]__ - Comma separated list of roles allowed to invoke endpoint
* __[log]__ - Log entry to write upon invocation of endpoint
* __[overwrite]__ - If true will overwrite existing file. If false the invocation will throw an exception if the endpoint file already exists
* __[validators]__ - Hyperlambda code being validators for endpoint
* __[cache]__ - Number of seconds the GET endpoint should be cached (HTTP cache). Only relevant for GET endpoints
* __[publicCache]__ - Whether or not the cache will be public cache, implying possible to cache by proxies. Only relevant if above is non-zero
* __[cqrs]__ - If true will publish SignalR/socket messages upon invocation of endpoint
* __[cqrsAuthorisation]__ - Type of authorisation for SignalR messages published. Legal values are 'inherited', 'roles', 'groups', 'users' or 'none'
* __[cqrsAuthorisationValues]__ - If the above is supplied, these are the comma separated values defining their values. For instance, if you're using _"roles"_ as the above value, this is a comma separated value declaring which roles will be notified when subscribing to the message
* __[args]__ - These are arguments to the endpoint, implying a list of **[columns]** and a list of **[primary]** keys. Primary keys are only relevant for PUT and DELETE endpoints, but columns is a list of objects with _"name"_ and _"type"_ values.
* __[conditions]__ - This is a list of optional query parameters and are only relevant to GET endpoints. If specified it completely overrides the existing query parameters generated automatically by Magic.

The CRUD endpoints to HTTP verb mappings this endpoint generates are as follows.

* __Create__ - HTTP POST verb
* __Read__ - HTTP GET verb
* __Read(count)__ - HTTP GET verb with `-count` postfix in URL
* __Update__ - HTTP PUT verb
* __Delete__ - HTTP DELETE verb

This endpoint can only be invoked by a root user. This endpoint is to be considered obsolete and will probably
change in a future version of Magic.
This endpoint is not intended for you to consume in your own code.

### POST magic/system/crudifier/custom-sql

This endpoint creates an SQL based HTTP endpoint for you. It's similar to the above endpoint, but much simpler
in syntax. It requires the following payload.

```
{
  "databaseType": "xxx",
  "authorization": "xxx",
  "moduleName": "xxx",
  "database": "xxx",
  "arguments": "xxx",
  "verb": "xxx",
  "endpointName": "xxx",
  "sql": "xxx",
  "overwrite": true,
  "isList": true
}
```

The arguments implies the following.

* __[databaseType]__ - Database type your SQL is wrapping. E.g. 'mysql', 'pgsql' or 'mssql'
* __[authorization]__ - Comma separated list of roles allowed to invoke the endpoint
* __[moduleName]__ - Primary URL of endpoint
* __[database]__ - Name of database, and connection string, e.g. `[generic|sakila]`
* __[arguments]__ - Hyperlambda declaratiun of arguments endpoint can handle. E.g. `filter:string`.
* __[verb]__ - HTTP verb endpoint wraps. This can be any of 'get', 'post', 'put', 'delete', and 'patch'
* __[endpointName]__ - Secondary URL for endpoint
* __[sql]__ - Actual SQL executed as endpoint is executing
* __[overwrite]__ - If true invocation will overwrite any existing file, otherwise the invocation will throw an exception if the endpoint file already exists
* __[isList]__ - If true, the endpoint will return an array of objects - Otherwise it will return the first object only.

The endpoint can only be invoked by a root user.
This endpoint is not intended for you to consume in your own code.

### GET magic/system/diagnostics/system-information

This endpoint returns system related information to the caller, such as Magic backend version, number of
tasks, 10 last log items, etc. The endpoint is the foundation for the KPIs displayed in your dashboard.
The endpoint does not require any arguments. The endpoint can only be invoked by a root user.

This endpoint is not intended for you to consume in your own code.

## File system related endpoints

These endpoints are related to the file system somehow and allows you to upload and download files,
create and delete folders, etc. These endpoints are arguably the foundation of Hyper IDE,
allowing you to edit your files on your server. Most of these endpoints can only be invoked by a root user, and
you would typically not consume these endpoints yourself directly from your own code.

### GET magic/system/file-system/download-folder

This endpoint allows the caller to download the specified folder from the backend as a ZIP file. The
endpoint can only be invoked by a root account, and requires the caller to specify **[folder]** being
an existing folder in the Magic backend. The endpoint requires the following query argument(s).

* __[folder]__ - Relative path of which folder to zip and download to the client

This endpoint is not intended for you to consume in your own code.

### DELETE magic/system/file-system/file

This endpoints deletes the specified **[file]** in the backend. The endpoint can only be invoked by a
root user. The endpoint requires the following query argument(s).

* __[file]__ - Full relative path of which file to delete

This endpoint is not intended for you to consume in your own code.

### GET magic/system/file-system/file

This endpoint returns the specified **[file]** to the caller. The endpoint can only be invoked by
a root user. The endpoint requires the following query argument(s).

* __[file]__ - Full relative path of file to download

This endpoint is not intended for you to consume in your own code.

### PUT magic/system/file-system/file

This endpoint creates or updates an existing file on the server. The endpoint requires its payload
as `multipart/form-data`, where **[folder]** becomes the folder of where to save the file,
and the attached **[file]** becomes the file to save, assuming the file has a name specified
as a part of its MIME entity as its Content-Disposition header's `filename`. The endpoint
can only be invoked by a root user.

This endpoint is not intended for you to consume in your own code.

### DELETE magic/system/file-system/folder

This endpoint deletes the specified **[folder]** in your backend. The endpoint can only be
invoked by a root user. The endpoint requires the following query argument(s).

* __[folder]__ - Full relative path of folder to delete

This endpoint is not intended for you to consume in your own code.

### PUT magic/system/file-system/folder

This endpoint creates a new folder in your backend given the specified payload.

```
{
  "folder": "/foo/bar/"
}
```

The endpoint can only be invoked by a root user.

This endpoint is not intended for you to consume in your own code.

### GET magic/system/file-system/list-folders-recursively

This endpoint lists all folders recursively starting from the specified **[folder]** argument.
The endpoint can only be invoked by a root user. The endpoint requires the following query
argument(s).

* __[folder]__ - Root folder of where to start listing folders. Will return all folders existing within this folder to caller

This endpoint is not intended for you to consume in your own code.

### GET magic/system/file-system/list-files-recursively

This endpoint returns all files recursively from within the specified **[folder]** folder.
The endpoint can only be invoked by a root user. The endpoint requires the following query
argument(s).

* __[folder]__ - Root folder of where to start listing files. Will return all files existing within this folder to caller

This endpoint is not intended for you to consume in your own code.

### GET magic/system/file-system/list-files

This endpoint lists all files within the specified **[folder]** folder, optionally containing
the specified **[filter]** criteria. The endpoint can only be invoked by a root user. The endpoint
requires the following argument(s).

* __[folder]__ - Folder to list files within
* __[filter]__ - Optional filter criteria filenames must contain in order to be considered a match

This endpoint is not intended for you to consume in your own code.

### GET magic/system/file-system/list-folders

This endpoint lists all folders within the specified **[folder]** folder. The endpoint
can only be invoked by a root user. The endpoint requires the following argument(s).

* __[folder]__ - Folder to list folder within

This endpoint is not intended for you to consume in your own code.

### POST magic/system/file-system/rename

This endpoint renames a file or a folder. It requires the following payload.

```
{
  "oldName": "xxx",
  "newName": "yyy"
}
```

Notice, the endpoint can rename both files or folders, but can only be invoked by a root user.
The **[oldName]** is the _full path_ of the file's or folder's _current_ name. The **[newName]**
is its new full name or path.

This endpoint is not intended for you to consume in your own code.

### PUT magic/system/file-system/unzip

This endpoint unzips the specified **[file]** ZIP file in place. The endpoint requires the
following payload.

```
{
  "file": "/foo/bar.zip"
}
```

The endpoint can only be invoked by a root user.

This endpoint is not intended for you to consume in your own code.

## PUT magic/system/file-system/install-module

This endpoint uploads a zip file assumed to be a module, and installs it in your backend.

The endpoint can only be invoked by a root user, and is not intended for you to consume in your own code.

## Log related endpoints

These are log related endpoints, allowing you to retrieve information related to your log.
Your log items are persisted in your `log_entries` Magic database table.

### GET magic/system/log/count

This endpoint counts the total number of log items in your backend. The endpoint can only be invoked by
a root user.

This endpoint is not intended for you to consume in your own code.

### GET magic/system/log/get

This endpoint returns the specified **[id]** log item, including its meta data. The endpoint can
only be invoked by a root user. The endpoint requires the following query argument(s).

* __[id]__ - Id of log item to retrieve

This endpoint is not intended for you to consume in your own code.

### GET magic/system/log/list

This endpoint returns log items from your backend, and can optionally allow you to page with the
following query parameters.

* __[from]__ - Id of an existing log item from where items will be returned _"from"_, not including
* __[max]__ - Maximum number of log items to return

This endpoint is not intended for you to consume in your own code.

### POST magic/system/log/log-loc

This endpoint allows you to log lines of code generated by either some sort of frontend scaffolding
process, or CRUD backend process. The endpoint can only be invoked by a root user, and requires
the following payload.

```
{
  "loc": 42,
  "type": "backend|frontend",
  "name": "Name of module/frontend"
}
```

The above arguments implies the following.

* __[loc]__ - Number of lines of code generated
* __[type]__ - Either `backend` or `frontend`
* __[name]__ - Name of module or frontend that was generated

This endpoint is not intended for you to consume in your own code.

### POST magic/system/log/log

This endpoint allows you to log some arbitrary log item, and takes the following payload.

```
{
  "type": "foo",
  "content": "foo",
  "meta": {
    "foo1": "bar1",
    "foo2": "bar2",
    "foo3": "bar3"
  }
}
```

The above arguments implies the following.

* __[type]__ - Type of log entry to create, one of 'debug', 'info', 'error' or 'fatal'
* __[content]__ - Content description for your log item
* __[meta]__ - Key/value pair of additional _"meta information"_ associated with log item

The endpoint can be invoked by _any_ user but requires the user to be authenticated towards the backend
and transmit his JWT token in the `Authorization` HTTP header as a _"Bearer"_ token.

This endpoints is intended for you to consume from your own code.

## SQL related endpoints

These endpoints allows you to retrieve meta data about your databases, and/or connection strings, in addition
to execute SQL towards a specific database, etc. These endpoints are the foundation for the _"SQL"_ menu item
in the Magic dashboard.

### GET magic/system/sql/connection-strings

This endpoint returns all database connection strings existing in the backend, being of type **[databaseType]**,
where the type can be one of 'mysql', 'mssql' or 'pgsql'. The endpoint can only be invoked by a root user.

This endpoint is not intended for you to consume in your own code.

### GET magic/system/sql/databases

This endpoint returns meta data associated with the specified **[databaseType]** and **[connectionString]**
combination, such as all databases, all tables within each database, all columns, and any foreign keys existing
between columns. The endpoint can only be invoked by a root user. The endpoint requires the following query
argument(s).

* __[databaseType]__ - Type of database, one of 'mysql', 'mssql', or 'pgsql'
* __[connectionString]__ - Name of connection string such as for instance _"generic"_

Notice, the endpoint is fairly expensive to execute, and therefor its result is cached on the server with
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
'mssql' and 'pgsql" in addition to 'mysql'. The endpoint can only be invoked by a root user.

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

The above arguments implies the following.

* __[databaseType]__ - Type of database to execute your SQL towards, either 'mysql', 'pgsql' or 'mssql'
* __[database]__ - Name of database to execute your SQL towards _and_ connection string to use. E.g. `[generic|mysql]`
* __[sql]__ - Actual SQL to execute
* __[safeMode]__ - If true only the first 200 records will be returned, to avoid exhausting your server for huge responses
* __[batch]__ - If true, will execute the SQL as a _"batch"_ SQL statement. Only relevant for SQL Server when executing scripts containing the _"go"_ keyword

The endpoint can only be invoked by a root user.

This endpoint is not intended for you to consume in your own code.

### GET magic/system/sql/list-files

This endpoint lists all SQL files associated with the specified **[databaseType]** query parameter. These are
template files, stored by the user or distributed by the system by default. The endpoint can only be invoked
by a root user. The endpoint requires no argument(s).

### PUT magic/system/sql/save-file

This endpoint saves a template SQL snippet file in your backend, and requires the following payload.

```
{
  "databaseType": "foo",
  "filename": "foo",
  "content": "foo"
}
```

The above arguments implies the following.

* __[databaseType]__ - Type of database, e.g. 'mysql', 'pgsql' or 'mssql'
* __[filename]__ - Filename of where to save the SQL file
* __[content]__ - Actual SQL content of your file

Your SQL snippet files are saved in your backend inside of your _"/etc/xxx/templates/"_ folder, where _"xxx"_
is your database type such as for instance 'pgsql', 'mysql' or 'mssql'.

This endpoint is not intended for you to consume in your own code.

## Task related endpoints

These are endpoints related to administrating tasks, and/or due dates for executing tasks. To understand the
task scheduler and how it works please refer to the [Task Manager](/dashboard/task-manager/).

### GET magic/system/tasks/list

This endpoint returns a list of all your tasks, optionally matching the specified query parameters.

* __[offset]__ - Offset of where to start returning tasks
* __[limit]__ - Maximum number of tasks to return
* __[filter]__ - Filter parameter the task must match

All the above arguments are optional, and the endpoint can only be invoked by a root user.
This endpoint is not intended for you to consume in your own code.

### GET magic/system/tasks/get

This endpoint returns the declaration for the specified **[name]** task, where name is the ID or name
of your task. This endpoint can only be invoked by a root user, and it requires the following query argument(s).

* __[name]__ - Name or id of task to return

This endpoint is not intended for you to consume in your own code.

### GET magic/system/tasks/count

Returns the number of tasks in your system, optionally matching the specified **[filter]** filtering argument.
This endpoint can only be invoked by a root user. The endpoint requires the following argument(s).

* __[filter]__ - Optional filter criteria that must be found in the task's description or id for the task to be considered a match

This endpoint is not intended for you to consume in your own code.

### POST magic/system/tasks/create

This endpoint creates a new task in your backend. The endpoints requires the following payload.

```
{
  "id": "foo",
  "description": "foo",
  "hyperlambda": "foo"
}
```

The above arguments implies the following.

* __[id]__ - ID or name of task. Must be unique and non-existing
* __[description]__ - Humanly readable description of your task. Optional
* __[hyperlambda]__ - Actual Hyperlambda to be associated with your task

This endpoint can only be invoked by a root user.
This endpoint is not intended for you to consume in your own code.

### POST magic/system/tasks/update

This endpoint updates an existing task, and requires the following payload.

```
{
  "id": "foo",
  "description": "foo",
  "hyperlambda": "foo"
}
```

The above arguments are the same as when creating a new task and implies the following.

* __[id]__ - The id or name of the task you want to update
* __[description]__ - The new description of the task
* __[hyperlambda]__ - The new Hyperlambda associated with your task

This endpoint is not intended for you to consume in your own code.

### DELETE magic/system/tasks/delete

This endpoint deletes a previously persisted task with the specified **[id]**. This endpoint
can only be invoked by a root user. The endpoint requires the following query argument(s).

* __[id]__ - Id of task to delete

This endpoint is not intended for you to consume in your own code.

### POST magic/system/tasks/due/add

This endpoints adds a due date, or a repetition pattern, to a previously persisted task. It requires
the following payload.

```
{
  "id": "foo",
  "due": "2022-01-31T11:16:09.492Z",
  "repeats": "foo"
}
```

The above arguments implies the following.

* __[id]__ - ID or name of task you want to associate your schedule with
* __[due]__ - A date and time for when you want to execute the task. Mutually exclusive with the **[repeats]** argument
* __[repeats]__ - A repetition value for the task. Mutually exclusive with the **[due]** argument

To understand how the **[repetition]** works see the documentation
for [magic.lambda.scheduler](/documentation/magic.lambda.scheduler/). This endpoint can only be invoked by a root user.

This endpoint is not intended for you to consume in your own code.

### DELETE magic/system/tasks/due/delete

This endpoint deletes the specified **[id]** due/repeats instance in your backend. This endpoint can
only be invoked by a root user. The endpoint requires the following query argument(s).

* __[id]__ - Id of due date object to delete

This endpoint is not intended for you to consume in your own code.

## Misc endpoints

These are endpoints not belonging to a particular category of endpoints, but still a part of the Magic
middleware, and used by the frontend dashboard somehow.

### GET magic/system/endpoints/list

This endpoint returns all endpoints in the system, their meta data such as description, input arguments,
and resulting response if possible. The endpoint can only be invoked by a root user. The endpoints requires
no argument(s).

This endpoint is not intended for you to consume in your own code.

### GET magic/system/endpoints/openapi

This endpoints returns an OpenAPI (Swagger) specification. Optionally pass in `system` as true if you want
to retrieve system endpoints, or optionally apply a `filter` which is a partial path endpoints must match
to be returned.

This endpoint is intended for you to consume in your own code and it does not require authentication.

### POST magic/system/evaluator/evaluate

This endpoint executes the specified Hyperlambda and returns the result of the invocation back to caller.
The endpoint can only be invoked by a root user and takes the following payload.

```
{
  "hyperlambda": "/* ... Some Hyperlambda here ... */"
}
```

This endpoint is not intended for you to consume in your own code.

### GET magic/system/evaluator/vocabulary

This endpoint returns the Hyperlambda vocabulary from the backend, implying which Hyperlambda slots
exists on the server. The endpoint can only be invoked by a root user.

This endpoint is not intended for you to consume in your own code.

### GET magic/system/misc/gibberish

This endpoint returns cryptographically secured random characters to the caller, optionally
taking **[min]** and **[max]** as query parameters, being the minimum length and maximum length
of the returned _"gibberish"_. With gibberish we imply CSRNG characters. This endpoint can
be invoked by anyone and optionally handles the following argument(s).

* __[min]__ - Minimum length of gibberish returned
* __[max]__ - Maximum length of gibberish returned

This endpoints is intended for you to consume from your own code.

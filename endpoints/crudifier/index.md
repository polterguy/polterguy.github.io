---
title: CRUD generator endpoints
description: Magic's built-in crudifier endpoints, generating CRUD and SQL based HTTP endpoints wrapping your database.
header:
  image: /assets/images/hero/endpoints-top.webp
  og_image: /assets/images/hero/endpoints-top-og.png
  image_description: CRUD generator endpoints
---

## CRUD related endpoints

These endpoints allow you to among other things generate CRUD HTTP backend modules, and are at the heart of
the [Endpoint Generator](/dashboard/endpoint-generator/). In addition these endpoints allow you to generate
SQL based HTTP endpoints. These endpoints are not intended for being directly
invoked by your code, but rather from the Magic dashboard as it is creating backend endpoints for you.

## Backend CRUD operations

This section describes the parts that generate backend HTTP endpoints for you, typically wrapping a database
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

The above fields imply the following.

* __[verbose]__ - If true more query parameter types will be generated for your GET/read endpoint
* __[paging]__ - If true, paging query parameters (limit and offset) are generated for your GET/read endpoint
* __[sorting]__ - If true, sorting query parameters (order and direction) are generated for your GET/read endpoint
* __[distinct]__ - If true, an additional distinct GET endpoint is generated for the table
* __[aggregate]__ - If true, an additional aggregate GET endpoint is generated for the table
* __[search]__ - If true, an additional keyword density search GET endpoint is generated for the table
* __[captcha]__ - If specified, requires a Magic CAPTCHA token with at least this value to invoke the endpoint
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
  "overwrite": true
}
```

The arguments imply the following.

* __[databaseType]__ - Database type your SQL is wrapping. E.g. 'mysql', 'pgsql' or 'mssql'
* __[authorization]__ - Comma separated list of roles allowed to invoke the endpoint
* __[moduleName]__ - Primary URL of endpoint
* __[database]__ - Name of database, and connection string, e.g. `[generic|sakila]`
* __[arguments]__ - Hyperlambda declaration of arguments endpoint can handle. E.g. `filter:string`.
* __[verb]__ - HTTP verb endpoint wraps. This can be any of 'get', 'post', 'put', 'delete', and 'patch'
* __[endpointName]__ - Secondary URL for endpoint
* __[sql]__ - Actual SQL executed as endpoint is executing
* __[overwrite]__ - If true invocation will overwrite any existing file, otherwise the invocation will throw an exception if the endpoint file already exists

The endpoint can only be invoked by a root user.
This endpoint is not intended for you to consume in your own code.

---
title: Middleware Endpoints
description: A reference to the most important built-in HTTP endpoints in Magic's middleware, covering files, authentication, and system operations.
header:
  image: /assets/images/hero/endpoints-top.png
  og_image: /assets/images/hero/endpoints-top-og.png
  image_description: Middleware Endpoints
---

Magic contains a whole range of endpoints, or _"middleware"_ parts, that the system itself relies upon to function. You can play around with these endpoints by using the [Endpoints](/dashboard/endpoints/) component and ensure you show your system endpoints. Most of these endpoints are for internal use through the Magic dashboard, and should as a general rule of thumb _not_ be consumed directly by you - But some of these endpoints are useful for your own projects.

![Screenshot of the Endpoints component](/images/endpoints.jpg)

Notice, all endpoints that require authorization of some sort assume a valid JWT token is transmitted in the `Authorization` HTTP header as a _"Bearer"_ type of token, and if not, the user will not be allowed to invoke the endpoint, and an HTTP status code of 401 will be returned. To retrieve a JWT token use the `magic/system/auth/authenticate` endpoint. When you use the Endpoint component, it will automatically associate your existing JWT token with your invocations.

Endpoints marked as _"not intended for you to consume in your own code"_ exist for the dashboard itself, and may change between versions of Magic - while endpoints explicitly marked as intended for your own consumption are stable, and safe to build upon.

## Endpoint reference

The reference documentation is organised by concept. Each page below documents every endpoint within its category; its URL, HTTP verb, arguments, authorisation requirements, and whether the endpoint is intended for your own consumption.

* [Authentication and authorisation endpoints](/endpoints/auth/) - Authenticating, changing passwords, refreshing and verifying JWT tokens
* [Plugins endpoints](/endpoints/plugins/) - Listing installed plugins and installing new ones
* [Cache endpoints](/endpoints/cache/) - Deleting server-side cache items
* [Configuration endpoints](/endpoints/configuration/) - Loading and saving your configuration, and initial setup
* [CRUD generator endpoints](/endpoints/crudifier/) - Generating CRUD and SQL based HTTP endpoints
* [File system endpoints](/endpoints/files/) - Uploading, downloading, listing, renaming and deleting files and folders
* [Log endpoints](/endpoints/log/) - Listing, counting and creating log items
* [SQL endpoints](/endpoints/sql/) - Executing SQL, database meta data, and SQL snippet files
* [Task endpoints](/endpoints/tasks/) - Creating, scheduling and administering background tasks
* [Misc endpoints](/endpoints/misc/) - Endpoint meta data, OpenAPI specifications, Hyperlambda evaluation, and diagnostics

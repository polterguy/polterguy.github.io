
# Magic middleware documentation

This is the documentation for Magic itself, implying the _"middleware"_ found in Magic's core.
Due to the extremely modularised architecture Magic is built upon, these parts are actually surprisingly
small in the larger context, but still contains everything that wires up Magic, and the backend of modules
such as Hyper IDE and the CRUDifier. This part documents the middleware, the file system's structure,
the slots in the middleware parts of Magic, and the endpoints you can find there.

## File structure

There are 5 primary folders in Magic, these are as follows.

* etc
* misc
* modules
* system
* temp

The _"modules"_ folder and the _"system"_ folders are the only folders that allows for resolving Hyperlambda
endpoints, while the other folders are for helper files, and/or uploaded files. If you use the docker images
of Magic, Magic will automatically update the following folders as you pull the Docker images from Docker hub.

* misc
* system

This implies that you _should not_ edit files in these folders, since if you do, your changes might vanish
the next time you update Magic. You should also not store your own files in these folders, since your files
might disappear the next time you update Magic. The only folder where it's safe to store your own files
and folders within are as follows.

* __etc__ - For dynamic files, uploads and downloads, etc
* __modules__ - For your own custom Hyperlambda modules
* __temp__ - For temporary files. Notice this folder might be emptied occassionally automatically

The two remaining folders; _"misc"_ and _"system"_ should be kept for Magic's internals, and not tampered
with in any ways. If in doubt, most folders in Magic has README files you can open to see the purpose
of a specific folder, and/or its files - And in fact, becoming acquinted with Magic's file and folder 
structure is probably a smart investment, since everything in Magic is based upon _"conventions"_, implying
folders have semantic value of some sort. As a general rule of thumb the only folders you should modify
and add files to are as follows.

* __modules__ - All your Hyperlambda code should in general end up here
* __etc__ - Everything else such as uploaded files etc should end up here

## Initialisation

When you start Magic for the first time, the system might need to initialise itself, which implies doing 3
things.

* Create a magic database, insert a root user into it, and initialise the authentication secret
* CRUDify the magic database
* Create a cryptography key pair for your server

These 3 steps is what you're going through as you initially install Magic, either locally, or on
a VPS of your chosing. The first step requires you to have a database of some sort somewhere, where
Magic can create its internal `magic` database. Magic will use this database for authenticating users,
logging, persisting tasks, etc.
The second step implies generating CRUD HTTP backend endpoints wrapping this database, to allow
you to interact with it through a client of some sort. The 3rd step is required to create a
public and private server key pair. This key is used for cryptographically secured lambda
invocations, but also in other parts of the system.

After you have followed the above process, you can see that inside your _"modules"_ folder there
exists Hyperlambda endpoint files wrapping your entire magic database into CRUD HTTP endpoints.
These files were created in the second step of the above process, and is required to have Magic
functioning properly. Below you can see a screenshot of how the folder structure looks like in
Magic through Hyper IDE.

![Magic folder structure](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/folder-structure.jpg)

The _"exceptions.hl"_ file at the root of your folder structure is the default exception handler
that will be used if no module creates its own exception handler logic to override the default handler.

## Endpoints

Magic contains a whole range of endpoints, or _"middleware"_ parts, that the system itself
relies upon to function. You can play around with these endpoints by using the _"Endpoints"_
menu item in your dashboard, ensure you show your system endpoints, while filtering on _"magic/system"_.
Most of these endpoints are for internal use through the Magic dashboard, and should as a general
rule of thumb _not_ be consumed directly by you - But some of these endpoints are useful for things such
as implementing authentication and authorisation in your own frontend as you consume Magic.

Notice, all endpoints that requires authorization of some sort assumes a valid JWT token is transmitted
in the `Authorization` HTTP header as a _"Bearer"_ type of token, and if not, the user will not be
allowed to invoke the endpoint, and an HTTP status code of 401 will be returned. To retrieve a JWT token
use the `magic/system/auth/authenticate` endpoint documented further down in this document.

### Authentication and authorisation endpoints

These are the endpoints related to the authentication and authorisation parts of Magic. You can find
their Hyperlambda files in the _"/system/auth/"_ folder. These endpoints are typically useful for you
as you implement your own authentication logic in your own code, and most of these endpoints
are intended for you to consume in your own frontend clients.

#### GET magic/system/auth/authenticate

This endpoint allows you to authenticate towards your Magic backend with a username and password
combination. It's mostly a thin layer on top of your **[magic.auth.authenticate]** slot that you
can read about further down in this document. It requires two query arguments being as follows.

* __[username]__ - Username of user wanting to authenticate
* __[password]__ - Password of user wanting to authenticate

The endpoint can be invoked by anyone, and does not have any authorisation requirements. The endpoint
will return a JWT token you can use for consecutive requests towards your backend, authorising you
to invoke endpoints your user is authorised to invoking. Notice, Magic relies upon the JWT tokens
being transmitted as _"Bearer"_ tokens in the _"Authorization"_ HTTP header, implying you'll have to
ensure the resulting JWT token from invoking the above endpoint is attached to your HTTP requests as
such in later requests. This endpoint can be invoked by anyone, including non-authenticated clients.

#### GET magic/system/auth/auto-auth

This endpoint always returns _"off"_ unless you've configured Magic to use automatic LDAP authentication
by following [this recipe](/tutorials/auth-internals/). The idea with this endpoint is to use the frontend
to check if automatic authentication has been turned on, and if so, simply invoking the authenticate
endpoint directly without any username or password combination, which works only if you've enabled
LDAP authentication, and your frontend is deployed on a local domain where LDAP credentials are
transmitted to the backend. The endpoint does not require any arguments. The endpoint can be invoked by
anyone, and does not have any authorisation requirements. The endpoint does not require any arguments.

Notice, this endpoint is considered obsolete and might be removed in future versions of Magic.

#### PUT magic/system/auth/change-password

This endpoint allows an existing user to change his or her password. It can only change the password of
the currently authenticated user, and takes the new password as the following payload. This endpoint
can be invoked by anyone as long as you have authenticated towards your backend previously. This endpoint
can also be invoked with a _"change password"_ type of JWT token, generated by the backend if the caller
forgot his or her password, and requested to change his or her password somehow.

```json
{
  "password": "new-password"
}
```

#### GET magic/system/auth/endpoints

This endpoint returns the authorisation requirements for all endpoints in the system. It does not take
arguments. It returns one item for each Hyperlambda endpoint in the system, with its associated verb,
and a list of roles the user must belong to in order to invoke the endpoint. The endpoint can be invoked
by anyone, and does not have any authorisation requirements. Notice, this endpoint caches its result for
5 minutes, implying changes done to the authorisation requirements of your endpoints will not be accessible
for clients before 5 minutes after your changes have been applied.

#### GET magic/system/auth/impersonate

This endpoint allows you to generate a JWT token on behalf of another user, by providing a username allowing
you to impersonate the other user in the system. The endpoint requires the following argument(s).

* __[username]__ - Username of user to impersonate

This endpoint can only be invoked by a root user. This endpoint is useful when debugging user related
errors, and/or supporting/helping users who for some reasons needs help, allowing you to use the
system within the context of the user you impersonate.

#### GET magic/system/auth/reset-password

This endpoint allows you to generate a reset password JWT token on behalf of another user, by providing a
username, returning a _"reset password"_ JWT token that can _only_ be used to reset the user's password.
The endpoint requires the following argument(s).

* __[username]__ - Username of user to generate token for

This endpoint can only be invoked by a root user. However there exists another endpoint you can see further
down in this document allowing a user to have Magic send him a _"forgot password email"_.

#### PUT magic/system/auth/imprison

This endpoint allows you to _"imprison"_ a user in your system. When a user is imprisoned, the user cannot
login to the system for as long as the user is _"imprisoned"_. This endpoint can only be invoked by a root user,
and the endpoint relies upon scheduled tasks to release users imprisoned, so the endpoint will not function
correctly unless scheduled tasks are enabled in the system. The endpoint takes the following JSON payload.

```json
{
  "username": "user-to-imprison",
  "releaseDate": "2022-01-31T05:44:52.439Z"
}
```

The release date is the date when the user should be released from his _"imprisonment"_. This endpoint
is considered obsolete and might be removed in a future version of Magic.

#### GET magic/system/auth/refresh-ticket

This endpoint allows an already authenticated user to retrieve a new JWT token with an expiration date
further into the future. The idea of the endpoint is to allow for an authenticated user to non-stop
constantly invoke this endpoint some few minutes before his existing JWT token expires, to retrieve
a new JWT token, preventing the user from being thrown out of the backend as his or her existing token
expires. The endpoint does not take any arguments, but can only be invoked by an already authenticated
user, implying you'll need to pass in your JWT token to it in the Authorization HTTP header as a
_"Bearer"_ token or the endpoint will return _"Access denied"_.

#### POST magic/system/auth/register

This endpoint allows a user to register in your backend, which implies creating a new user. The endpoint
requires the username to be a valid email address. If you want users to confirm their email address as they
register, you'll have to configure your SMTP settings. Configuring your SMTP settings can be done by reading
the [following parts](/documentation/magic.lambda.mail/). In addition you need to provide a `frontendUrl`
to the endpoint that will be used by the email template as a _"confirm email address link"_
is sent to the user to dynamically create a link the user must click to confirm his or her email address. The
endpoint requires the payload below to be transmitted by the client. Notice, the `frontendUrl`
is only used if the system has been configured with an SMTP server, resulting in that the endpoint
invocation tries to send the registered user an email to have the user confirm his or her email address.
If you don't care about having users confirm their email address, and/or haven't configured SMTP
settings, you don't have to supply the `frontendUrl` argument.

When a user registers using this endpoint, a new user will be created, but the user will be added to
the _"unconfirmed"_ role, resulting in that the user have no access to any parts of the system at
all before his or her email address has been confirmed. When his or her email address is confirmed,
the _"unconfirmed"_ user/role association is deleted, and the user is added to the _"guest"_ role. The guest
role still doesn't have access to much of the system, so if the user is to gain access to more of the
system, this must be manually added by a root user after the user has confirmed his or her email address.

```json
{
  "username": "john@doe.com",
  "password": "some-password",
  "frontendUrl": "https://your-frontend-url.com",
  "template": "/some/path/to-some-email-template.html",
  "subject": "Subject line of registration email"
}
```

The above arguments implies the following.

* __[username]__ - Username for user, implying user's email address
* __[password]__ - Password user wants to use on site
* __[frontendUrl]__ - The URL to the frontend responsible for validating the user's email address. Optional, and if not given will not send user a _"confirm email address"_ email
* __[template]__ - The full relative path to an email template used to send user a verify email address link. Optional, and if not given will default to _"/system/auth/email-templates/register.html"_
* __[subject]__ - Subject line of welcome email. Optional, and if not supplied the default value of _"Thank you for registering with Aista Magic Cloud"_ will be used

This endpoint does not require the caller to be authenticated and can be invoked by anyone. If you have
configured the system to send _"confirm email address"_ emails, the URL transmitted to the user to confirm
his or her email address will resemble the following, except the query parameters will be URL encoded of
course.

```
https://your-frontend-url.com?
token=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855&
username=john@doe.com&
url=https://your-backend-url.com
```

The above arguments in the URL sent to the user's email address implies the following.

* __[token]__ - A cryptographically secure token that must be supplied to the `verify-email` endpoint as the user confirms his or her email address. Notice, this is _not_ a JWT token but rather a cryptographic hash based upon the user's email address and the auth secret from your _"appsettings.json"_ file. Hence this token can only be used to verify the user's email address, and not to authorise the user in any ways
* __[username]__ - The username of the user that also needs to be submitted to the `verify-email` endpoint as the user confirms his or her email address
* __[url]__ - The root URL for your backend, implying the backend to use as you invoke the `verify-email` endpoint

This endpoint allows you to create a frontend page somewhere where you accept the above `token` query parameter,
the `username` query parameter, and the `url` query parameter, for then to invoke the `verify-email`
endpoint found below to verify the user's email address, passing in the `token` value found in your query
parameters above as the `token` argument to the `verify-email` endpoint. Notice, Magic's dashboard will
correctly handle these URL arguments if you supply the root-URL/domain to your Magic dashboard as your
`frontendUrl` when invoking the endpoint. The endpoints can return one of the following values if it
successfully executes.

* __confirm-email-address-email-sent__ - This implies the user was successfully sent a _"verify email address"_ email
* __already-registered__ - This implies the user has already registered at the site
* __success__ - This implies the user was successfully registered, but no verify email address email was sent

You can override the email template used to send user a _"verify email address"_ email. The default email template
used can be found at `/system/auth/email-templates/register.html`. However, if you create your own email
template you'll have to make sure you _keep_ the dynamically substituted `url` parts in your own custom template.
See how the `href` parameter for the default email template is constructed to understand how this works.

#### POST magic/system/auth/verify-email

This endpoint allows a registered user to verify his or her email address, and is typically occurring
after a user has registered and the system has sent the user an email to confirm his or her email address.
The endpoint does not require authorisation, but takes the following payload.

```json
{
  "username": "john@doe.com",
  "token": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
}
```

Notice, the above `token` must be the same token generated by Magic as the user registered, and sent
to the user on email.

#### POST magic/system/auth/send-reset-password-link

This endpoint sends a _"reset password email"_ to a registered user. Like the register endpoint, the
endpoint requires a `frontendUrl` field, in addition to of course a username. The
username must be an email address. This endpoint requires that you have configured Magic's SMTP settings
such that it can send an email to the user allowing him or her to reset the password. Below is an
example payload.

```json
{
  "username": "john@doe.com",
  "frontendUrl": "https://your-frontend-url.com",
  "template": "/some/path/to-some-email-template.html",
  "subject": "Subject line of change password email"
}
```

The above arguments implies the following.

* __[username]__ - Username/email address for user requesting a new password for
* __[frontendUrl]__ - The URL of the frontend where you want to allow the user to change his or her password
* __[template]__ - The email template used to send the user the _"forgot password"_ email. Optional, and if not specified will default to _"/system/auth/email-templates/reset-password.html"_
* __[subject]__ - Subject line of email to send. Optional, and if not supplied will default to _"Change your password at Aista Magic Cloud"_

The endpoint does not require the caller to be authenticated and can be invoked by anyone.

#### GET magic/system/auth/verify-ticket

This endpoint allows a frontend to verify an existing JWT token, and it will return _"success"_ if
the JWT token is valid and can be used in consecutive invocations requiring authorisation somehow.
The endpoint can be invoked by any user as long as the user is authenticated. The endpoint does not
take any arguments, but can only be invoked by an already authenticated user, implying you'll need
to pass in your JWT token to it in the Authorization HTTP header as a _"Bearer"_ token. If the JWT
token is not valid the endpoint will return a 401 status code with _"Access denied"_ as its message.

### Bazar endpoints

These are endpoints related to the Bazar somehow, allowing you to install new Bazar modules, and check
which Bazar modules have already been installed. The Bazar is a micro service _"AppStore"_ for your
Magic server, allowing your Magic server to install backend modules on the fly, resulting
in having some backend micro service installed into your backend, without interrupting normal
usage.

**Notice** - None of these endpoints are really intended to be consumed in your own code, but only
for internal usage by Magic itself.

#### GET magic/system/bazar/app-manifests

This endpoint returns a list of Bazar apps that have been installed in your backend. Each item will
contain a date of installation, the username of the user who installed the app, the name and version
of the app, etc. Most importantly each Bazar manifest item will also contain a _"token"_, which is
typically required as the app is to be updated. Below is an example of what the endpoint might
return if it only has one Bazar item installed. The endpoint can only be invoked by a root user and
it requires no arguments.

```json
[
  {
    "name": "Babel Fish",
    "version": "v1.0.0",
    "token": "3b65f514-2e30-4ca2-bdcf-96a2d2727bc1",
    "module_name": "babelfish",
    "installed_by": "root",
    "installed": "2022-01-31T06:03:01.669Z"
  }
]
```

#### GET magic/system/bazar/can-install

This endpoint requires a Magic version number, such as _"v10.0.15"_, and returns either _"SUCCESS"_ or _"ERROR"_,
depending upon whether or not the current version of Magic is above or beneath the specified version number.
It is typically used to verify that a Bazar app can be installed, to verify the Magic version is high enough
for the Bazar item to be successfully installed. The endpoint can only be invoked by a root user. The endpoint
requires the following argument(s).

* __[required_magic_version]__ - Minimum version of Magic requried

This endpoint is considered obsolete and might be removed in a future version of Magic.

#### POST magic/system/bazar/download-from-bazar

This endpoint downloads a Bazar item as a ZIP file from the specified URL, and unzips the file into the backend.
The endpoint can only be invoked by a root user and requires the following payload.

```json
{
  "url": "https://some-bazar.com/download?app=some-app.zip",
  "name": "some-module"
}
```

The Bazar item will be downloaded from the specified URL and assumed to be a ZIP file. The ZIP file
will then be unzipped, and unzipped into your _"modules"_ folder as the specified _"name"_. Notice, any
previously installed modules with the same name will be automatically deleted, and the endpoint will _not_
install the module, but only unzip it and create its folder structure. To install the module after it has
been unzipped make sure you invoke the `/system/file-system/install` endpoint.

Notice, this endpoint is considered obsolete and will be changed in a future version of Magic.

#### POST magic/system/bazar/download-from-url

This endpoint downloads a file from its specified __[url]__ and saves it to the specified __[folder]__
in your backend. The endpoint can only be invoked by a root user, and requires the following payload.

```json
{
  "folder": "foo",
  "url": "foo"
}
```

The above arguments implies the following.

* __[folder]__ - The folder in your backend you want to save the file
* __[url]__ - The URL to download the file from

The __[url]__ field needs to be a valid URL returning a file, with the `Content-Disposition` HTTP
header correctly applied, since the `Content-Disposition` header's _"filename"_ value becomes
the name of the file on your server.

### Cache related endpoints

These are the endpoints related to your server side cache, and allows you to query your cache, purge
your cache entirely, or delete a single cache item on the server. Internally Magic is using
server-side cache sparsingly for some expensive operations, such as retrieving meta data from your
database. Sometimes you need to manually purge your cache, and/or delete individual cache items
on your server, to re-retrieve data invalidating your cache in the process. This section provides
information about such operations for such scenarios.

**Notice** - None of these endpoints are really intended to be consumed in your own code, but only
for internal usage by Magic itself.

#### DELETE magic/system/cache/delete-cache-item

This endpoint requires an **[id]** as a query parameter, and will delete the associated server side
cache item. It can only be invoked by a root user. The endpoint requires the following argument(s).

* __[id]__ - Mandatory id of cache item to evict

#### DELETE magic/system/cache/empty-cache

This endpoint completely empties your server side cache, optionally taking a _"filter"_ query
parameter, which if specified will ensure only cache items _starting_ with the specified filter
key will be deleted. The endpoint can only be invoked by a root user. The endpoint requires the
following argument(s).

* __[filter]__ - Optional filter declaring _"namespace"_ of cache items to evict

This endpoint is obsolete and will be changed in a future version of Magic.

#### GET magic/system/cache/list-cache-count

This endpoint returns the number of cache items in total on your server, optionally starting out
with the _"filter"_ query parameter as their key. The endpoint can only be invoked by a root user.
The endpoint requires the following argument(s).

* __[filter]__ - Optional filter declaring _"namespace"_ of cache items to count

This endpoint is obsolete and will be changed in a future version of Magic.

#### GET magic/system/cache/list-cache

This endpoint returns the number of cache items on your server, optionally allowing you to page
with the following query parameters.

* __[limit]__ - Maximum number of items to return
* __[offset]__ - Offset of where to start returning items
* __[filter]__ - Filter key cache items must start with in order to be considered a hit

The endpoint can only be invoked by a root user. This endpoint is obsolete and will be changed in
a future version of Magic.

### Configuration related endpoints

These endpoints are related to configuration of your system, and allows you to read and modify
configuration settings as you see fit. These endpoints are typically not intended for being used
directly by your code, but for the most parts only used during initialisation of your Magic server,
and/or as you change configuration settings in Magic.

**Notice** - None of these endpoints are really intended to be consumed in your own code, but only
for internal usage by Magic itself.

#### GET magic/system/config/load

This endpoint loads your configuration settings and returns it to the caller. The endpoint
can only be invoked by a root user.

#### POST magic/system/config/save

This endpoint allows you to save your configuration settings. The specified paylod will
in its entirety overwrite your existing _"appsettings.json"_ file. The endpoint
can only be invoked by a root user.

#### GET magic/system/config/status

This endpoint returns the setup status of your system, implying if the system has been correctly
initialised. The endpoint requires no argument. The response object will resemble the following.

```json
{
  "config_done": true,
  "magic_crudified": true,
  "server_keypair": true
}
```

The fields in the above payload implies the following.

* __[config_done]__ - If true the primary configuration process of your server has been done, implying Magic has created a magic database, and changed your _"appsettings.json"_ file, applying a valid connection string to an existing database, and an auth secret
* __[magic_crudified]__ - If true your magic database has been CRUDified
* __[server_keypair]__ - If true the server has a cryptography key pair

If any of the above fields does _not_ return true, the frontend dashboard will guide you through the process
of finishing the configuration process before allowing you to gain access to other parts of your Magic server.
The endpoint can only be invoked by a root user.

#### POST magic/system/config/setup

This endpoint sets up your system, and requires the following payload.

```json
{
  "password": "yyy",
  "settings": "*"
}
```

The above fields implies the following.

* __[password]__ - The root user's password
* __[settings]__ - The initial value for your _"appsettings.json"_ file. This is the entire JSON content of your _"appsettings.json"_ file, and will be sanity checked on the server to some extent before saved and applied

The endpoint can only be invoked by a root user, and will setup Magic to use the specified connection string found
in your __[settings]__ field, verify the database server exists and can be connected to, create the `magic` database
if not existing from before, and create a root user account in the `users` table for you with the specified __[password]__.
The endpoint can only be invoked _once_ and will throw an exception if the system has previously been setup - Which Magic
determines by checking the `auth:secret` value of your existing _"appsettings.json"_ file, and if it's not the default
value of _"THIS-IS-NOT-A-GOOD-SECRET-PLEASE-CHANGE-IT"_, Magic will assume it's been previously setup and throw an exception.
If the `magic` database already exists in your database server, it will only run its migration scripts, and replace
the existing root user's password with whatever you provided as a payload to the endpoint invocation.

**Notice** - If you for some reasons needs to reconfigure Magic, you can manually change its `magic:auth:secret` value
to _"THIS-IS-NOT-A-GOOD-SECRET-PLEASE-CHANGE-IT"_ to force it to guide you through the configuration process again as you
log out and login again.

#### GET magic/system/config/version-compare

This endpoint requires two version numbers and return -1, 0 or 1 depending upon which of the two versions
comes before the other one. It's useful for validating the backend is at least at some specific version number
or higher, before for instance installing modules and such requiring a specific version. The versions it expects
to perform this comparison must be in the form of `vn.n.n`, e.g. _"v10.14.33"_. Refer to the **[version]** slot
further down in this document to understand how a Magic version provides semantic meaning with its version entities.
The query parameters the endpoint requires are as follows.

* __[version_1]__ - Left hand side comparison argument
* __[version_2]__ - Right hand side comparison argument

If __[version_1]__ is lower than __[version_2]__ the endpoint will return -1. If the versions are the same
the endpoint will return 0, if __[version_1]__ is higher it will return 1.

### CRUD related endpoints

These endpoints allows you to among other things generate CRUD HTTP backend modules, and is at the heart of
the _"CRUDifier"_ in Magic. In addition these endpoints allows you to generate SQL based HTTP endpoints,
and/or frontends using a template of some sort. Most of these endpoints are not intended for being directly
invoked by your code, but rather from the Magic dashboard as it is creating HTTP backend endpoints for you,
and/or frontends based upon your backend.

### Backend CRUD operations

This section describes the parts that generates backend HTTP endpoints for you, typically wrapping a database
table with CRUD operations.

#### POST magic/system/crudifier/crudify

This endpoint creates one CRUD HTTP backend endpoint for you, wrapping the specified database table
with the specified HTTP verb/CRUD-operation. The endpoint requires the following payload.

```json
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

#### POST magic/system/crudifier/custom-sql

This endpoint creates an SQL based HTTP backend endpoint for you. It's similar to the above endpoint, but much simpler
in syntax. It requires the following payload.

```json
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

### Frontend generator

This part describes the frontend generator allowing you to create some sort of frontend, wrapping
your previously created backend endpoints.

#### GET magic/system/crudifier/templates

This endpoint returns all frontend templates the system can use for generating frontends. It requires no arguments,
but can only be invoked by a root user. This is used to allow the user to select a frontend template as he or she
wants to generate a frontend of some sort.

#### GET magic/system/crudifier/template

This endpoint returns Markdown describing the specified template with a humanly understandable description, implying
it returns the README.md file associated with the template specified as the **[name]** query parameter. As the user is
selecting a template, typically displaying the result of invoking this endpoint makes sense, since it allows the user
to understand what the template does for him or her. The endpoint can only be invoked by a root user. The endpoint
requires the following query argument(s).

* __[name]__ - Name of template to return Markdown for

#### GET magic/system/crudifier/template-args

This endpoint returns the additional custom arguments the specified frontend template can handle. It requires one
query parameter being **[name]** of template you wish to retrieve arguments for. The return value of invocations to this
endpoint becomes the **[args]** collection for invocations to the above endpoint. The endpoint can only be invoked by a
root user. The endpoint requires the following query argument(s).

* __[name]__ - Name of template to return template arguments for

#### POST magic/system/crudifier/generate-frontend

This endpoint generates a frontend based upon a template, and either puts the result into a local folder on
the server, or returns as a ZIP file download to the client. The endpoint requires the following payload.

```json
{
  "templateName": "xxx",
  "apiUrl": "xxx",
  "frontendUrl": "xxx",
  "email": "xxx",
  "name": "xxx",
  "copyright": "xxx",
  "endpoints": "*",
  "deployLocally": true,
  "args": "*"
}
```

The above arguments implies the following.

* __[templateName]__ - Name of template to use. This must be one of the folders found inside of your _"/misc/templates/"_ folder, _minus_ the _"common"_ folder, which is common for all templates
* __[apiUrl]__ - The API URL the frontend will use
* __[frontendUrl]__ - The URL you intend to deploy the frontend to, which will be used in the _"docker-compose.yml"_ file that is automatically generated
* __[email]__ - Email address of person administrating the SSL certificate for the frontend. Typically your email address.
* __[name]__ - Name of frontend. Typically the name of your app.
* __[copyright]__ - Copyright notice put into each source file where such can be put, implying TypeScript files, JavaScript files, CSS files, etc - But not HTML files.
* __[endpoints]__ - Endpoints declaration
* __[deployLocally]__ - If true will deploy your frontend locally within _"/etc/frontends/"_, otherwise invocation will return a ZIP file to the client
* __[args]__ - Optional argument collection for your template. These are different depending upon which template you use. You can use the _"template-args"_ endpoint to retrieve which arguments, and/or different values each template accepts

The endpoint can only be invoked by a root user.

### Cryptography related endpoints

These are endpoints related to cryptography somehow, implying among other things the cryptographically secured
HTTP lambda implementation. To understand this feature [read the following article](/tutorials/crypto-lambda-http/)
that describes them from a high level perspective. However, the basic foundation for this feature is to allow
for cryptographically signing a Hyperlambda payload, for then to transmit the payload to another Magic server,
for then to have that Magic server _securely_ execute the specified Hyperlambda, without risking compromising
the server in any ways. In addition this section also describes how to associate a user with a cryptography
key pair, allowing users to sign in with zero username/password requirements, etc.

#### PUT magic/system/crypto/associate-user

Associates a specified public cryptography key with a specified user. The endpoints requires the following
payload.

```json
{
  "keyId": 42,
  "username": "foo"
}
```

The **[keyId]** is the ID of the public cryptography key, and the **[username]** is the username of the
user you want to associate with the public key. Invoking this endpoint allows the specified user to authenticate
towards the backend using a _"cryptography challenge"_, implying zero username/password, allowing the user
to authenticate using his private cryptography key instead, by giving the client a _"cryptography challenge"_
the client is assumed to be able to cryptographically sign using his or her own private key.

#### PUT magic/system/crypto/deassociate-user

The opposite of the above endpoint, allowing a root user to de-associate a user with the specified public
key. Payload to endpoint is as follows.

```json
{
  "keyId": 42
}
```

Whatever users are associated with the above public key will be de-associated with their existing key association,
and no longer be able to use cryptography challenges to authenticate towards the backend.

#### GET magic/system/crypto/challenge

Returns a new cryptography challenge to the client, allowing him to use it to cryptographically sign the
specified challenge, submit the cryptographically signed result to another endpoint, to generate a JWT token
that authorises the client on behalf of the user associated with the public key. The challenge is is valid
for 300 seconds, implying the client needs to be able to cryptographically sign the result, and submit the
cryptographically signed result to the coupled endpoint within 5 minutes to be able to authenticate as the
user associated with his cryptography key. The endpoint can be invoked by anyone, and does not require
any argument(s).

#### POST magic/system/crypto/challenge

Coupled with the above endpoint, this endpoint allows the user to use his private cryptography key to
authenticate towards the backend without having to supply his or her username/password combination.
After having cryptographically signed the challenge returned from the above endpoint, the user can submit
the signed challenge to this endpoint, resulting in a JWT token being returned, allowing the user to
invoke endpoints afterwards within the context of the user associated with the cryptography key pair.

If the invocation to this endpoint is successful, a valid JWT token will be returned, allowing the
client to use this JWT token to invoke other endpoints authorised as the user associated with the
public cryptography key on the server using the JWT token. The endpoint requires the following
payload.

```json
{
  "challenge": "cryptographically-signed-challenge"
}
```

The above argument implies the following.

* __[challenge]__ - Cryptographically signed result from the GET counterpart endpoint in base64 encoded format

#### PATCH magic/system/crypto/eval-id

Executes a cryptographically secured lambda invocation.
See [cryptographically secured lambda invocations](/tutorials/crypto-lambda-http/) to understand what this
implies. The payload is assumed to be binary in the form of `application/octet-stream`, assumed to be
a cryptographically signed Hyperlambda snippet, and only after the signature has been confirmed to belong
to a public key in the database being enabled and allowed to create such HTTP invocations, the Hyperlambda
will be executed within the **[whitelist]** declaration associated with the key the payload was
signed with.

#### POST magic/system/crypto/generate-keypair

This endpoint generates a new server cryptography key pair, both its public key and its private key, and
takes a backup of the old key, making the newly generated key the default server key. The endpoint requires
the following payload.

```json
{
  "strength": 4096,
  "seed": "qwertyuiop",
  "subject": "John Doe",
  "email": "john@doe.com",
  "domain": "https://johndoe.com"
}
```

The above arguments implies the following.

* __[strength]__ - Key bit strength, typically 1024, 2048, 4096 or 8192. Notice, anything below 2048 is _not_ considered secure, but to be safe you should only use at least 4096 in your production environment
* __[seed]__ - Random text gibberish used to seed the CSRNG implementation
* __[subject]__ - The subject owning the cryptography key pair, typically the full name of the individual whom the key is created for
* __[email]__ - Email address where the above subject can be reached
* __[domain]__ - Domain associated with the key pair. When creating a new server key pair, this is typically your backend's domain prefixed by `https://`

#### GET magic/system/crypto/get-fingerprint

This endpoint returns the fingerprint for the specified public key. The public key must be base64 encoded
DER format. The endpoint requires one query parameter being its **[key]**, which is the key the invocation
will return the fingerprint for. The endpoint can only be invoked by a root user and it requires the following
argument(s).

* __[key]__ - Public key to generate a fingerprint from

#### POST magic/system/crypto/import

This endpoint allows _any_ user to import his or her public key to the backend. By default the key
will _not_ be enabled, but disabled, and needs to be enabled by an administrator before it can be
used to create cryptographically secured lambda invocations. The payload for the endpoint is as
follows.

```json
{
  "subject": "xxx",
  "email": "xxx",
  "domain": "xxx",
  "content": "xxx"
}
```

The above arguments implies the following.

* __[subject]__ - Subject owning public key, typically the full name of a single person, e.g. _"John Doe"_
* __[email]__ - Email associated with the public key
* __[domain]__ - Domain associated with the public key, e.g. `https://foo.com`
* __[content]__ - Actual public key in BASE64 encoded DER format

Notice, currently Magic only supports RSA keys base64 encoded in DER format.

#### GET magic/system/crypto/public-key-raw

Returns the server's public key as base64 encoded DER format. This endpoint can be invoked by anyone, allowing
others to import your server's public key into their own database. The endpoint requires no arguments.

#### GET magic/system/crypto/public-key

This endpoint is similar to the above endpoint, but instead of returning the public key of your server
in raw base64 encoded DER format, it returns the following response.

```json
{
  "fingerprint": "d090-3322-fcfa-c064-27e3-fd45-d5bc-1035-5c3f-13c8-7c53-1d03-ecb7-ad71-2ea2-cce1",
  "publicKey": "MIIBIjANBgkq... snip ...3QIDAQAB",
  "keyFormat": "base64/DER",
  "fingerprintFormat": "SHA256-fingerprint",
  "keyType": "RSA"
}
```

The above fields implies the following.

* __[fingerprint]__ - Fingerprint associated with key
* __[publicKey]__ - The base64 encoded DER format of the key. The key's actual content
* __[keyFormat]__ - If the key has been encoded differently than base64/DER this will have a different value
* __[fingerprintFormat]__ - Format of the fingerprint returned
* __[keyType]__ - Type of key. Magic only supports RSA keys currently

This endpoint can be invoked by anyone and does not require authentication. The endpoint requires no argument(s).

#### GET magic/system/crypto/user-association

This endpoint returns the username associated with the specified public cryptography key ID. The endpoint
can only be invoked by a root account, and requires **[keyId]** as a query parameter, being the ID of the
public key as taken from the `crypto_keys` table from your magic database. The endpoint requires the
following query arguments(s).

* __[keyId]__ - Id of public key as persisted into your _"crypto_keys"_ database table

### Diagnostic endpoints

These endpoints are diagnostic endpoints, allowing you to diagnose your backend, and/or run
assumptions to sanity check your current installation. An assumption is a high level integration
test specifically created to verify that some HTTP endpoint returns what is _"assumed"_ given
a specific payload of some sort. Notice, assumptions can also be manually ceated as lambda objects,
to execute arbitrary Hyperlambda code, throwing exceptions if assumptions are incorrect.

#### GET magic/system/diagnostics/assumption-test-description

This endpoint returns the description associated with the specified **[test_file]** assumption.
The endpoint can only be invoked by a root user. The endpoint requires the following query argument(s).

* __[test_file]__ - The full relative path of the assumption file to return the description for

#### POST magic/system/diagnostics/create-test

This endpoint creates a new assumption test. The endpoint can only be invoked by a root user
and requires the following payload.

```json
{
  "filename": "foo",
  "verb": "foo",
  "url": "foo",
  "status": 42,
  "description": "foo",
  "payload": "foo",
  "response": "foo",
  "produces": "foo"
}
```

The above arguments implies the following.

* __[filename]__ - Filename for assumption
* __[verb]__ - HTTP verb assumption should use
* __[url]__ - URL assumption will invoke
* __[status]__ - Assumed status code for invoking above URL
* __[description]__ - Description for your assumption
* __[payload]__ - JSON payload to transmit to above endpoint. Only relevant for POST or PUT endpoints
* __[produces]__ - Assumed Content-Type above URL produces when given the specified payload
* __[response]__ - Assumed response after invoking above URL. Optional, and if not specified will not create assumptions about result besides the status code

#### GET magic/system/diagnostics/execute-test

This endpoint executes the specified assumption test, given through its **[root_url]** and **[test_file]**
query parameters. The endpoint can only be invoked by a root user. The endpoint requires the following
query argument(s).

* __[root_url]__ - The root URL of where to invoke the assumption towards. Typically the domain parts of your backend
* __[test_file]__ - The full relative path of the test file to execute

#### GET magic/system/diagnostics/system-information

This endpoint returns system related information to the caller, such as Magic backend version, number of
tasks, log items count, etc. The endpoint can only be invoked by a root user. The endpoint does not
require any arguments. The endpoint can only be invoked by a root user.

### File system related endpoints

These endpoints are related to the file system somehow and allows you to upload and download files,
create and delete folders, etc in your Magic backend. These endpoints are arguably the foundation of Hyper IDE,
allowing you to edit your files on your server. Most of these endpoints can only be invoked by a root user, and
you would typically not consume these endpoints yourself directly from your own frontends.

#### GET magic/system/file-system/download-folder

This endpoint allows the caller to download the specified folder from the backend as a ZIP file. The
endpoint can only be invoked by a root account, and requires the caller to specify **[folder]** being
an existing folder in the Magic backend. The endpoint requires the following query argument(s).

* __[folder]__ - Full relative path of which folder to ZIP and download to the client

#### DELETE magic/system/file-system/file

This endpoints deletes the specified **[file]** in the backend. The endpoint can only be invoked by a
root user. The endpoint requires the following query argument(s).

* __[file]__ - Full relative path of which file to delete

#### GET magic/system/file-system/file

This endpoint returns the specified **[file]** to the caller. The endpoint can only be invoked by
a root user. The endpoint requires the following query argument(s).

* __[file]__ - Full relative path of file to download

#### PUT magic/system/file-system/file

This endpoint creates or updates an existing file on the server. The endpoint requires its payload
as `multipart/form-data`, where **[folder]** becomes the folder of where to save the file,
and the attached **[file]** becomes the file to save, assuming the file has a name specified
as a part of its MIME entity as its Content-Disposition header's `filename`. The endpoint
can only be invoked by a root user.

#### DELETE magic/system/file-system/folder

This endpoint deletes the specified **[folder]** in your backend. The endpoint can only be
invoked by a root user. The endpoint requires the following query argument(s).

* __[folder]__ - Full relative path of folder to delete

#### PUT magic/system/file-system/folder

This endpoint creates a new folder in your backend given the specified payload.

```json
{
  "folder": "/foo/bar/"
}
```

The endpoint can only be invoked by a root user.

#### PUT magic/system/file-system/install

This endpoint installs a new module already assumed to be unzipped somehow inside your modules
folder, by recursively executing all files found beneath _"magic.startup"_ folders within
your module's primary folder, and/or within folders directly within the main folder of
your module's folder. The endpoint requires the following payload.

```json
{
  "folder": "/modules/bar/",
  "app_version": "v15.0.11",
  "name": "bar",
  "token": "xyz"
}
```

The above arguments implies the following.

* __[folder]__ - Full path of folder where module exists
* __[app_version]__ - Version of module currently installed, e.g. _"v10.0.26"_
* __[name]__ - Name of app in humanly readable form
* __[token]__ - Token needed to update the module form the Bazar

The endpoint can only be invoked by a root user.

#### GET magic/system/file-system/list-folders-recursively

This endpoint lists all folders recursively starting from the specified **[folder]** argument.
The endpoint can only be invoked by a root user. The endpoint requires the following query
argument(s).

* __[folder]__ - Root folder of where to start listing folders. Will return all folders existing within this folder to caller

#### GET magic/system/file-system/list-files-recursively

This endpoint returns all files recursively from within the specified **[folder]** folder.
The endpoint can only be invoked by a root user. The endpoint requires the following query
argument(s).

* __[folder]__ - Root folder of where to start listing files. Will return all files existing within this folder to caller

#### GET magic/system/file-system/list-files

This endpoint lists all files within the specified **[folder]** folder, optionally containing
the specified **[filter]** criteria. The endpoint can only be invoked by a root user. The endpoint
requires the following argument(s).

* __[folder]__ - Folder to list files within
* __[filter]__ - Optional filter criteria filenames must contain in order to be considered a match

#### GET magic/system/file-system/list-folders

This endpoint lists all folders within the specified **[folder]** folder. The endpoint
can only be invoked by a root user. The endpoint requires the following argument(s).

* __[folder]__ - Folder to list folder within

#### POST magic/system/file-system/rename

This endpoint renames a file or a folder. It requires the following payload.

```json
{
  "oldName": "xxx",
  "newName": "yyy"
}
```

Notice, the endpoint can rename both files or folders, but can only be invoked by a root user.
The **[oldName]** is the _full path_ of the file's or folder's _current_ name. The **[newName]**
is its new full name or path.

#### PUT magic/system/file-system/unzip

This endpoint unzips the specified **[file]** ZIP file in place. The endpoint requires the
following payload.

```json
{
  "file": "/foo/bar.zip"
}
```

The endpoint can only be invoked by a root user.

### Log related endpoints

These are log related endpoints, allowing you to retrieve information related to your log. By default
your log items are persisted in the magic database table called `log_entries`, but there exists
alternative log service implementations allowing you to among other things persist log entries
into a NoSQL/CQL based database of your choice, such as ScyllaDB or Cassandra. What features
the log has varies from which service is used for persisting log items.

#### GET magic/system/log/count-items

This endpoint counts the total number of log items in your backend. The endpoint can only be invoked by
a root user.

#### GET magic/system/log/log-item

This endpoint returns the specified **[id]** log item, including its meta data. The endpoint can
only be invoked by a root user. The endpoint requires the following query argument(s).

* __[id]__ - Id of log item to retrieve

#### GET magic/system/log/log-items

This endpoint returns log items from your backend, and can optionally allow you to page with the
following query parameters.

* __[from]__ - Id of an existing log item from where items will be returned _"from"_, not including
* __[max]__ - Maximum number of log items to return

#### POST magic/system/log/log-loc

This endpoint allows you to log lines of code generated by either some sort of frontend scaffolding
process, or CRUD backend process. The endpoint can only be invoked by a root user, and requires
the following payload.

```json
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

#### POST magic/system/log/log

This endpoint allows you to log some arbitrary log item, and takes the following payload.

```json
{
  "type": "foo",
  "content": "foo"
}
```

The above arguments implies the following.

* __[type]__ - Type of log entry to create, one of 'debug', 'info', 'error' or 'fatal'
* __[content]__ - Content description for your log item

The endpoint can be invoked by _any_ user but requires the user to be authenticated towards the backend
and transmit his JWT token in the `Authorization` HTTP header as a _"Bearer"_ token.

### SQL related endpoints

These endpoints allows you to retrieve meta data about your databases, and/or connection strings, in addition
to execute SQL towards a specific database, etc. These endpoints are the foundation for the _"SQL"_ menu item
in the Magic dashboard.

#### GET magic/system/sql/connection-strings

This endpoint returns all database connection strings existing in the backend, being of type **[databaseType]**,
where the type can be one of 'mysql', 'mssql' or 'pgsql'. The endpoint can only be invoked by a root user.

#### GET magic/system/sql/databases

This endpoint returns meta data associated with the specified **[databaseType]** and **[connectionString]**
combination, such as all databases, all tables within each database, all columns, and any foreign keys existing
between columns. The endpoint can only be invoked by a root user. The endpoint requires the following query
argument(s).

* __[databaseType]__ - Type of database, one of 'mysql', 'mssql', or 'pgsql'
* __[connectionString]__ - Name of connection string such as for instance _"generic"_

Notice, the endpoint is fairly expensive to execute, and therefor its result is cached on the server with
the key of _"magic.sql.databases.xxx.yyy"_ where _"xxx"_ is the database type and _"yyy"_ is the connection
string name.

#### GET magic/system/sql/default-database-type

This endpoint returns your default database type, in addition to all databases types the system currently
supports. An example of invoking the endpoint can be found below.

```json
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

#### POST magic/system/sql/evaluate

This endpoint allows you to evaluate the specified SQL towards your database. The endpoint requires the
following payload.

```json
{
  "databaseType": "foo",
  "database": "foo",
  "sql": "foo",
  "safeMode": true,
  "batch": true
}
```

The above arguments implies the following.

* __[databaseType]__ - Type of database to execute your SQL towards, either 'mysql', 'pgsql' or 'mssql'
* __[database]__ - Name of database to execute your SQL towards _and_ connection string to use. E.g. `[generic|mysql]`
* __[sql]__ - Actual SQL to execute
* __[safeMode]__ - If true only the first 200 records will be returned, to avoid exhausting your server for huge responses
* __[batch]__ - If true, will execute the SQL as a _"batch"_ SQL statement. Only relevant for SQL Server when executing scripts containing the _"go"_ keyword

The endpoint can only be invoked by a root user.

#### GET magic/system/sql/list-files

This endpoint lists all SQL files associated with the specified **[databaseType]** query parameter. These are
template files, stored by the user or distributed by the system by default. The endpoint can only be invoked
by a root user. The endpoint requires no argument(s).

#### PUT magic/system/sql/save-file

This endpoint saves a template SQL snippet file in your backend, and requires the following payload.

```json
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

### Task related endpoints

These are endpoints related to administrating tasks, and/or due dates for executing tasks. To understand the
task scheduler and how it works please refer to the [following article](/tutorials/task-scheduler/).

#### POST magic/system/tasks/add-due

This endpoints adds a due date, or a repetition pattern, to a previously persisted task. It requires
the following payload.

```json
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

#### GET magic/system/tasks/count-tasks

Returns the number of tasks in your system, optionally matching the specified **[query]** filtering argument.
This endpoint can only be invoked by a root user. The endpoint requires the following argument(s).

* __[query]__ - Optional filter criteria that must be found in the task's description or id for the task to be considered a match

Notice, this endpoint should be considered obsolete and might change in a future version.

#### POST magic/system/tasks/create-task

This endpoint creates a new task in your backend. The endpoints requires the following payload.

```json
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

#### DELETE magic/system/tasks/delete-due

This endpoint deletes the specified **[id]** due/repeats instance in your backend. This endpoint can
only be invoked by a root user. The endpoint requires the following query argument(s).

* __[id]__ - Id of due date object to delete

#### DELETE magic/system/tasks/delete-task

This endpoint deletes a previously persisted task with the specified **[id]**. This endpoint
can only be invoked by a root user. The endpoint requires the following query argument(s).

* __[id]__ - Id of task to delete

#### GET magic/system/tasks/get-task

This endpoint returns the declaration for the specified **[name]** task, where name is the ID or name
of your task. This endpoint can only be invoked by a root user, and it requires the following query argument(s).

* __[name]__ - Name or id of task to return

Notice, this endpoint should be considered obsolete and will change in a future version of Magic.

#### GET magic/system/tasks/list-tasks

This endpoint returns a list of all your tasks, optionally matching the specified query parameters.

* __[offset]__ - Offset of where to start returning tasks
* __[limit]__ - Maximum number of tasks to return
* __[query]__ - Filter parameter the task must match

All the above arguments are optional, and the endpoint can only be invoked by a root user.
Notice, this endpoint should be considered obsolete and might change in a future version of Magic.

#### POST magic/system/tasks/update-task

This endpoint updates an existing task, and requires the following payload.

```json
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

### Terminal related endpoints

These are terminal related endpoints, and/or socket connection points. Magic has support for subscribing
to web socket messages using SignalR, in addition to executing Hyperlambda files over the same socket
connection. This part of the documentation describes the endpoints related to such socket operations
in regards to the integrated _"Terminal"_ component. The terminal component again allows for executing
terminal or bash commands in your backend, and see the result of the command in your frontend.

#### SOCKET magic/system/terminal/command

This socket URL allows you to transmit a command to a previously opened terminal instance on your
server. The socket endpoints can only be invoked by a root user. The endpoints requires the following
payload.

```json
{
  "cmd": "cd",
  "channel": "xyz"
}
```

The **[cmd]** above is a terminal or bash command, such as `ls` or `mkdir` - While the **[channel]** above
is the name of a previously created channel in your backend. To create a unique channel you can use the `gibberish`
endpoint. This endpoint can only be invoked by a root user.

#### SOCKET magic/system/terminal/start

This socket URL allows you to create a new terminal instance on your server, allowing you to transmit
bash command over. The socket endpoint requires the following payload.

```json
{
  "channel": "foo",
  "folder": "/modules/"
}
```

The above **[channel]** becomes a unique reference for future commands transmitted to your server,
while the **[folder]** becomes the initial default folder from where to run your terminal within on
your server. This endpoint can only be invoked by a root user.

#### SOCKET magic/system/terminal/stop

This socket URL allows you to stop a previously created terminal instance on your server. It requires
the following payload.

```json
{
  "channel": "foo"
}
```

The above **[channel]** is a channel previously created using the start socket endpoint. This endpoint
can only be invoked by a root user.

### Misc endpoints

These are endpoints not belonging to a particular category of endpoints, but still a part of the Magic
middleware, and used by the frontend dashboard somehow.

#### GET magic/system/emails/email

This endpoint returns the email address and full name of the root user. The endpoint can only be invoked
by a root user.

#### GET magic/system/endpoints/assumptions

This endpoint returns all assumptions associated with the specified **[verb]** **[endpoint]**
combination. This endpoint can only be invoked by a root user. The endpoint requires the following
query argument(s).

* __[verb]__ - HTTP verb of endpoint
* __[endpoint]__ - Relative URL of endpoint

#### GET magic/system/endpoints/endpoints

This endpoint returns all endpoints in the system, their meta data such as description, input arguments,
and resulting response if possible. The endpoint can only be invoked by a root user. The endpoints requires
no argument(s).

#### POST magic/system/evaluator/evaluate

This endpoint executes the specified Hyperlambda and returns the result of the invocation back to caller.
The endpoint can only be invoked by a root user and takes the following payload.

```json
{
  "hyperlambda": "/* ... Some Hyperlambda here ... */"
}
```

#### GET magic/system/evaluator/vocabulary

This endpoint returns the Hyperlambda vocabulary from the backend, implying which Hyperlambda slots
exists on the server. The endpoint can only be invoked by a root user.

#### GET magic/system/ide/macro

This endpoint returns a Hyper IDE macro definition to caller, allowing the caller to see which
arguments the macro can handle, and other meta data associated with the macro. Typically the
macro will return something resembling the following.

```json
{
  "name": "Creates a download file endpoint",
  "description": "Macro for Hyper IDE that creates Markdown documentation for a module's endpoints, and stores the documentation in an ENDPOINTS.md file at root of the module's folder.",
  "arguments": [
    {
      "name": "module",
      "type": "string",
      "description": "Name of module to create a 'download file endpoint' for",
      "mandatory": true
    }
  ]
}
```

The endpoint can only be invoked by a root user.

#### POST magic/system/ide/execute-macro

This endpoint executes the specified Hyper IDE macro with the specified arguments. The endpoint
requires the following payload.

```json
{
  "macro": "/full-path-of-macro.hl",
  "args": "*"
}
```

The **[macro]** is the _full_ filename of the macro to execute, while the **[args]** depends upon
the macro itself, and differs according to what macro is being executed. See the above endpoint for
how to retrieve arguments related to a specific macro. The endpoint can only be invoked by a root user.

#### GET magic/system/images/generate-qr

This endpoint generates a QR code, and returns to the caller as Content-Type of `image/png`.
The endpoint can be invoked by _anyone_ and does not require authentication to be invoked. The
endpoint requires the following query parameters.

* __[content]__ - Content of QR code. Can be a URL or anything really
* __[size]__ - Number of pixels per _"pixel"_ in the QR code. Effectively becomes the size of the QR code

#### GET magic/system/misc/gibberish

This endpoint returns cryptographically secured random characters to the caller, optionally
taking **[min]** and **[max]** as query parameters, being the minimum length and maximum length
of the returned _"gibberish"_. With gibberish we imply CSRNG characters. This endpoint can
be invoked by anyone and requries the following argument(s).

* __[min]__ - Minimum length of gibberish returned
* __[max]__ - Maximum length of gibberish returned

#### POST magic/system/sockets/send-socket-message

This endpoint allows you to publish a socket message. The endpoint requires the following
payload.

```json
{
  "client": "foo",
  "roles": "foo",
  "groups": "foo",
  "name": "foo",
  "message": "*"
}
```

The endpoint can only be invoked by a root user. The above arguments implies the following.

* __[client]__ - A comma separated list of clients to whom the message will be transmitted to. Optional
* __[roles]__ - A comma separated list of roles to whom the message will be transmitted to. Optional
* __[groups]__ - A comma separated list of groups to whom the message will be transmitted to. Optional
* __[name]__ - The name of the message to publish
* __[message]__ - Any JSON data that will become the published message

#### GET magic/system/sockets/socket-users-count

Returns number of currently connected socket users, having subscribed to one or more messages from
the backend. The endpoint optionally takes a **[filter]** query parameter, allowing you to filter
users returned by it. The endpoint can only be invoked by a root user. The endpoint requires the following
argument(s).

* __[filter]__ - Optional filtering criteria the socket connection must contain to be considered a match

#### GET magic/system/sockets/socket-users

Returns the currently connected socket users form the backend, optionally matching the optional **[filter]**
argument. The endpoint can only be invoked by a root user. The endpoint requires the following argument(s).

* __[filter]__ - Optional filtering criteria the socket connection must contain to be considered a match

## Static slots

These slots are C# slots the core itself exposes.

* __[version]__ - Returns the current version of the Magic backend
* __[version.compare]__ - Compares two versions

The **[version]** slot returns the current version of Magic. Below is an example.

```
version
```

The above would result in something resembling the following.

```
version:v10.0.21
```

The first integer number is the major version number, the second number the secondary version number, and the
third the minor version number. When you depend upon a feature in your own Hyperlambda that was released in
a specific version of Magic, you typically don't want to check if the current version is exactly the version
you need to use to use your functionality, but rather if the current version is more than or equal to the
version you need in order to run your code. For such scenarios you have the **[version.compare]** slot.
This slot takes two version numbers, and compares them, returning which version is the highest. Below is
an example.

```
version.compare
   .:v10.0.22
   .:v10.0.21
```

The above will return the integer 1, implying the second argument comes _before_ the first argument,
similar to how a string compare method invocation would work in C#. To provide you with a use case,
imagine you create a Hyperlambda module that needs at least version 10.0.18 to function correctly,
since it relies upon features that was released in that particular version. For this case you can
use code resembling the following.

```
version
if
   mte
      version.compare
         get-value:x:@version
         .:v10.0.18
      .:int:0
   .lambda

      // Version is 10.0.18 or higher.
else

   // Version is too small for us.
   throw:You need to update your Magic version to use this module
```

If the above Hyperlambda does not throw an exception, you can assume the current version is version 10.0.18 or
higher, and you can probably safely rely upon features released in that version to exist in the current version.

## Dynamic slots

Magic also creates the following dynamic slots during startup. Notice, most of these slots are there exclusively
to make sure the middleware of Magic works correctly, and are _not_ intended to be used directly by you
in your own Hyperlambda code, unless explicitly stated otherwise, and/or you're extending Magic or replacing
parts of its core with your own custom logic.

* __[magic.auth.authenticate]__ - Authenticates a user and returns a JWT token
* __[magic.auth.change-password]__ - Allows a user to reset his or her password with a _"reset-password"_ JWT token, _or_ an existing valid token wrapping the user
* __[magic.auth.create-user]__ - Creates a new user in Magic
* __[magic.auth.ensure-role]__ - Ensures the specified role exists, and if not, creates it
* __[magic.crypto.get-public-key]__ - Returns a registered public key and its associated meta data
* __[magic.crypto.get-server-private-key]__ - Returns your server's private cryptography key
* __[magic.crypto.get-server-public-key]__ - Returns your server's public cryptography key
* __[magic.crypto.http.eval]__ - Cryptographically secured invokes an HTTP lambda invocation
* __[magic.crypto.http.has-invoked]__ - Returns true if the specified request has been executed before
* __[magic.crypto.http.persist-invocation]__ - Persists a cryptographically secured lambda invocation
* __[magic.crypto.import-key]__ - Imports a public cryptography key into your key database
* __[magic.db.mysql.databases]__ - Returns all databases for a specified connection string
* __[magic.db.mysql.tables]__ - Returns all tables for the specified connection-string/database combination
* __[magic.db.mysql.columns]__ - Returns all columns for a specified connection-string/database/table combination
* __[magic.db.mysql.foreign_keys]__ - Returns all foreign keys for a specified connection-string/database/table combination
* __[magic.db.mssql.databases]__ - See the MySQL equivalent above
* __[magic.db.mssql.tables]__ - See the MySQL equivalent above
* __[magic.db.mssql.columns]__ - See the MySQL equivalent above
* __[magic.db.mssql.foreign_keys]__ - See the MySQL equivalent above
* __[magic.db.pgsql.databases]__ - See the MySQL equivalent above
* __[magic.db.pgsql.tables]__ - See the MySQL equivalent above
* __[magic.db.pgsql.columns]__ - See the MySQL equivalent above
* __[magic.db.pgsql.foreign_keys]__ - See the MySQL equivalent above
* __[magic.emails.send]__ - Sends a _"braided"_ email
* __[magic.google.translate]__ - Translates something using Google Translate
* __[magic.io.file.load-recursively]__ - Loads all files from within some folder recursively
* __[magic.modules.ensure-database]__ - Ensures some database exists by executing its create database SQL file
* __[magic.modules.install-module]__ - Installs a module in your system
* __[transformers.hash-password]__ - Hashes a specified password in place

## Authentication and authorisation related slots

These are slots related to authentication and authorisation, and allows you to authenticate, impersonate,
change password of users, and other parts related to the _"auth"_ parts of the system. Notice, you would
rarely if ever use these slots directly, since the system contains several endpoints helping you out with
the consumption of this logic. However, to be complete, we've chosen to document these none the less.

### [magic.auth.authenticate]

This slot authenticates a user towards your specific authentication and authorisation logic, which implies
looking up the username in the `magic.users` database table, and ensuring the password is correct. If both
the username exists, and the password is correct, the slot will return a valid JWT token, allowing you to
use it as a token authorising you to act on behalf of the user, and/or return the JWT token to the client.
Below is an example assuming your root password is _"admin"_. Try to execute the following code with your
own root user's password to see how it works.

```
signal:magic.auth.authenticate
   username:root
   password:admin
```

The above would return something resembling the following.

```
signal
   ticket:eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.xxx
```

Notice, the authentication and authorisation logic in Magic is extendible, and allows you to use for
instance LDAP or Windows SSO authentication. To understand how to apply this refer
to [this documentation](/tutorials/auth-internals/). The slot can also be given two optional arguments.

* __[check-password]__ - Boolean value declaring whether or not password should be checked or not. Defaults to true.
* __[reset-password]__ - Boolean value declaring whether or not a _"reset password"_ JWT token should be generated or not. Defaults to false.

If you invoke the slot with the **[check-password]** argument being boolean false, you do _not_ need to supply
a password, and in fact the password will simply be ignored if you do. This allows you to _"impersonate"_ a user
without knowing the user's password. Below is an example.

```
signal:magic.auth.authenticate
   username:root
   check-password:bool:false
```

If you execute the above Hyperlambda, you will see the slot succeeds, and returns a valid JWT token for your
root user, even though you did not supply a password to it. This obviously has security consequences, and you
should _never_ in any ways what so ever expose this slot invocation to a user whom is not already authenticated
as _"root"_ in your backend. However, for a root user, it allows for _"impersonating"_ another user, to for
instance debug, and/or view sites, within the context of another user, by creating a JWT token wrapping some
other user, and use this as if the root user was that other user - Which is useful sometimes for helping users
whom are stuck with something and need help, and/or debug issues related to specific users in your backend.
The `magic/system/auth/generate-token` endpoint is using this slot to generate JWT token allowing you to
impersonate users in your backend.

The **[reset-password]** argument generates a _"reset password"_ token, that can _only_ be used to reset
a user's password, and is typically quite useful for _"reset password forms"_ that users can use to reset
their own passwords, by sending a reset password link to the user's registered email address, etc. Notice,
this argument must be accompanied by a **[check-password]** argument being set to `false`. Below is an
example of usage.

```
signal:magic.auth.authenticate
   username:root
   check-password:bool:false
   reset-password:bool:true
```

The above will result in a valid JWT token - However, if you run the token through for instance [JWT.io](https://jwt.io),
you will notice the user _only_ belongs to the _"reset-password"_ role, in addition to that it contains a hashed version
of the user's existing password. This role is an extremely restricted role and can _only_ be used to change the
user's password by invoking the **[magic.auth.change-password]** slot, which is done by
the `magic/system/auth/change-password` endpoint. The reason why the old password is sent in hashed format, is to
prevent the same reset password JWT token from being used _twice_, which would obviously be a security concern.
Notice, _only_ use the **[rest-password]** logic for functions that for instance sends a reset password link
on email to the user's registered email address, or something similar, to prevent malicious users from high jacking
other user accounts.

Magic contains endpoints wrapping all of the above slots, so you would typically never need to manually
use these slots yourself, unless you're building your own custom authentication system on top of Magic.

### [magic.auth.change-password]

Allows a user to change his or her password. This slot requires the user to be already authenticated and having a valid
JWT token. An example of changing your own password to _"admin2"_ can be found below.

```
signal:magic.auth.change-password
   password:admin2
```

If you invoke the above Hyperlambda, and log out from Magic, you'll need to use _"admin2"_ as your password to
authenticate again. Notice, this slot will evaluate within the context of the _"current user"_, implying the only
person who can change his or her password is the user currently being authenticated. To allow for having a user
whom have forgotten his or her password to change his or her password, see the **[magic.auth.authenticate]** slot above, 
and specifically the **[reset-password]** argument, allowing you to generate a _"reset password"_ type of JWT token
that you can send to the registered user in for instance an email or something, to allow for users to reset their
passwords when they have forgotten their current passwords.

Yet again, Magic contains helper endpoints for these types of operations, and you would probably never want to
directly invoke the slots yourself, but rather use the helper endpoints from your own frontend if you wish to
use this type of functionality. See the endpoints section further down in this document for details.

### [magic.auth.create-user]

This slot allows you to create a new user in Magic, with the specified username/password combination, belonging
to the specified role(s). Below is an example of usage.

```
signal:magic.auth.create-user
   username:foo
   password:bar
   roles
      .:guest
```

The above creates a new user called _"foo"_ with the password of _"bar"_ belonging to the _"guest"_ role. If you
execute the above Hyperlambda for then to go to your _"Auth"_ menu item, you will find this user. Notice, you might
want to delete the user after having verified it exists.

### [magic.auth.ensure-role]

This slot allows you to ensure that the specified role exists, and if not, create it. This is a useful slot when
you create your own Hyperlambda modules, and your module depends upon some role existing in the system. Typically
you'd invoke this slot from one of your module's startup files, since these are executed both during startup and
during installation of your module. Below is an example of usage.

```
signal:magic.auth.ensure-role
   role:foo-role
   description:This is the foo role
```

If you execute the above Hyperlambda and open up your _"Auth"_ menu item afterwards, you will see how you now
have a _"foo-role"_ in your system.

## Cryptography related slots

These slots are related to cryptography usage in your system, and most of these are specifically related to
cryptographically secured lambda invocations, allowing you to transmit and execute Hyperlambda from your
server to some other server, having your Hyperlambda securely executed on the destination server. Yet again
you would rarely if ever consume (most of) these slots directly yourself, but rather use them indirectly.
To understand cryptographically secured lambda invocations you can refer to [this part](/tutorials/crypto-lambda-http/)
of our documentation.

### [magic.crypto.get-public-key]

This slot returns a registered public key from your public cryptography key database, in addition to its domain, vocabulary
access right, etc. Below is an example of usage. Notice, you'll have to change the **[fingerprint]** of the invocation below
to a key that actually exists in your system, which you can do by opening up your _"Crypto"_ menu item and for instance
copy and paste the fingerprint of your own server's key.

```
signal:magic.crypto.get-public-key
   fingerprint:d090-3322-fcfa-c064-27e3-fd45-d5bc-1035-5c3f-13c8-7c53-1d03-ecb7-ad71-2ea2-cce1
```

The above would result in something resembling the following.

```
signal
   vocabulary
      add
      return
      get-nodes
      vocabulary
      slots.vocabulary
   id:int:3
   public_key:MIIBIjANBxyz
   domain:"http://localhost:5000"
   email:th@aista.com
   enabled:bool:true
```

To understand the structure and purpose of the above properties of a public key refer
to [the following documentation](/tutorials/crypto-lambda-http/).

### [magic.crypto.get-server-private-key]

This slot returns your server's private cryptography key, allowing you to use it for cryptography operations,
such as for instance encrypting or signing some package intended for being sent to some recipient. Below is
example usage.

```
signal:magic.crypto.get-server-private-key
```

The above wold return something resembling the following.

```
signal
   private-key:MIIEvAIBxyz....rwKw==
   fingerprint:d090-3322-fcfa-c064-27e3-fd45-d5bc-1035-5c3f-13c8-7c53-1d03-ecb7-ad71-2ea2-cce1
```

Notice, your server's private key needs to _stay private_, and you should be _very_ careful with it, since among
other things it allows others to impersonate your server's root account, and also execute arbitrary Hyperlambda
on your server. To understand the structure and purpose of your server's private key refer
to [the following documentation](/tutorials/crypto-lambda-http/).

### [magic.crypto.get-server-public-key]

This slot returns your server's public key, and contrary to the private key, this key should preferably be
shared with as many recipients as possible, since it among other things allows others to encrypt data transmitted
to your server, and/or verify that data originates from your server, and not some malicious _"main in the middle"_.
Example usage can be found below.

```
signal:magic.crypto.get-server-public-key
```

The above wold result in something resembling the following.

```
signal
   key:MIIBIjANBxyz.....
   fingerprint:d090-3322-fcfa-c064-27e3-fd45-d5bc-1035-5c3f-13c8-7c53-1d03-ecb7-ad71-2ea2-cce1
```

To understand the structure and purpose of your server's public key refer
to [the following documentation](/tutorials/crypto-lambda-http/).

### [magic.crypto.http.eval]

This slots allows you to cryptographically secured transmit Hyperlambda from your server to another Magic server, and have
your Hyperlambda securely executed on the server of your choice, assuming the other party have given you
the rights to execute your Hyperlambda object. Example usage can be found below.

```
guid.new
unwrap:x:+/**/.request-id
signal:magic.crypto.http.eval
   url:"http://localhost:5000/magic/system/crypto/eval-id"
   .lambda
      .request-id:x:@guid.new
      vocabulary
      slots.vocabulary
      add:x:./*/return
         get-nodes:x:@vocabulary/*
         get-nodes:x:@slots.vocabulary/*
      return
```

The above would result in something resembling the following.

```
signal:int:200
   headers
      Date:"Sun, 30 Jan 2022 07:48:36 GMT"
      Server:Kestrel
      Content-Length:351
      Content-Type:application/octet-stream
   content:@":return
:slots.vocabulary
:get-nodes
:vocabulary
:add
"
```

To understand the structure and purpose of the above Hyperlambda refer
to [the following documentation](/tutorials/crypto-lambda-http/).

### [magic.crypto.http.has-invoked]

This slot allows you to determine if a cryptographically secured lambda invocation has been executed before. It
requires a **[request-id]** only, and returns true or false depending upon whether or not a receipt of the request
has been persisted into your `magic.crypto_invocations` database table. The purpose of the slot is to avoid
_"replay attacks"_ of cryptographically secured lambda invocations. To understand the structure and purpose of
the above slot refer to [the following documentation](/tutorials/crypto-lambda-http/).

### [magic.crypto.http.persist-invocation]

This slot persists a cryptographically secured lambda invocation, resulting in a receipt, preventing the same
payload to be persisted twice. As most of the other related slots, it's not intended to be directly consumed,
but rather indirectly used by the other cryptographic slots that allows you to execute lambda objects
that are cryptographically signed. But it takes the following arguments.

* __[request-id]__ - The request ID of the invocation
* __[crypto-key]__ - ID of public cryptography key used to verify the signature of the payload
* __[request]__ - The request Hyperlambda
* __[request-raw]__ - The raw request, implying the Hyperlambda and the payload's signature
* __[response]__ - The response returned to the client after execution

### [magic.crypto.import-key]

This slot allows you to import a public cryptography key into your key database. It requires the following arguments.

* __[content]__ - The actual content
* __[enabled]__ - Whether or not the key should be enabled. The default is false.
* __[subject]__ - Subject of public key, typically the full name of its owner
* __[email]__ - Email address associated with the subject
* __[domain]__ - Domain associated with the subject

By default this inserts a new key and associates it with the following slots.

* __[add]__
* __[return]__
* __[get-nodes]__
* __[vocabulary]__
* __[slots.vocabulary]__

## Database meta traversal

All the following slots are a part of the database meta system, and allows you to retrieve meta data about your
databases, such as database names, table names, columns names, and foreign keys for tables. These slots are heavily
relied upon by the CRUDifier, as it creates a Hyperlambda backend for you, in order to determine which arguments
your HTTP endpoints requires, and how to validate these during HTTP invocations towards your backend.

All these have at least 3 versions, one for MySQL, one for PostgreSQL, and a third for SQL Server, and their only
difference is that the MySQL versions use _"mysql"_ as its slot name, SQL Server uses _"mssql"_ and PostgreSQL
uses _"pgsql"_. Besides from this, they're identical in regards to their APIs, which is the point, since it
allows for these slots to be used transparently, or _"polymorphistically"_ towards any underlaying database
type. In the following section, we therefor document their MySQL version, implying you'll have to exchange
the _"mysql"_ parts to test these towards a different database type.

### [magic.db.mysql.databases]

This slot returns all databases the system has access to within the specified connection string. Example
usage can be found below.

```
signal:magic.db.mysql.databases
   connection-string:generic
```

The above would result in a list of databases resembling the following.

```
signal
   ""
      db:information_schema
   ""
      db:magic
   ""
      db:mysql
   ""
      db:performance_schema
   ""
      db:sys
```

### [magic.db.mysql.tables]

This slot returns all tables for the specified **[connection-string]**/**[database]** combination. Below
is example usage.

```
signal:magic.db.mysql.tables
   connection-string:generic
   database:magic
```

The above would return all tables in your _"magic"_ database, resulting in something resembling the
following.

```
signal
   ""
      table:crypto_invocations
   ""
      table:crypto_keys
   ""
      table:log_entries
   ""
      table:magic_version
   ""
      table:roles
   ""
      table:task_due
   ""
      table:tasks
   ""
      table:users
   ""
      table:users_crypto_keys
   ""
      table:users_roles
```

### [magic.db.mysql.columns]

This slot returns all columns for the specified **[connection-string]**/**[database]**/**[table]** combination. Below
is example usage.

```
signal:magic.db.mysql.columns
   connection-string:generic
   database:magic
   table:users_roles
```

The above would return all columns in your _"users\_roles"_ table, resulting in something resembling the
following.

```
signal
   ""
      name:role
      db:varchar(45)
      nullable:bool:false
      primary:bool:true
      automatic:bool:false
      hl:string
   ""
      name:user
      db:varchar(256)
      nullable:bool:false
      primary:bool:true
      automatic:bool:false
      hl:string
```

The fields implies the following.

* __[name]__ - Name of column
* __[db]__ - Database type for column
* __[nullable]__ - If true column accepts null values
* __[primary]__ - If true column is a part of the primary key for the table
* __[automatic]__ - If true column has a default value
* __[hl]__ - Hyperlambda type mapping for the column

### [magic.db.mysql.foreign_keys]

This slot returns all foreign keys for the specified **[connection-string]**/**[database]**/**[table]** combination.
Below is example usage.

```
signal:magic.db.mysql.foreign_keys
   connection-string:generic
   database:magic
   table:users_roles
```

The above would return all foreign keys in your _"users\_roles"_ table, resulting in something resembling the
following.

```
signal
   ""
      column:role
      foreign_table:roles
      foreign_column:name
   ""
      column:user
      foreign_table:users
      foreign_column:username
```

In the above result we can see how the _"role"_ column in the _"users_roles"_ table for instance has a foreign
key declaration pointing towards the _"name"_ column in the _"roles"_ table, and similarly for the _"user"_
column pointing towards the _"users"_ table's _"username"_ column. The resulting values implies the following.

* __[column]__ - Name of column in table you're querying
* __[foreign_table]__ - Name of table the column is referencing
* __[foreign_column]__ - Name of column in _foreign_ table the column is referencing

## Misc slots

These are slots that don't belong to a specific category solving some problem related to your applications.

### [magic.emails.send]

This slot allows you to send a templated email, where the email's content can be found in a template file in
your file system, allowing you to provide substitution values that are _"braided"_ into the email before it's being
sent. The slot takes the following arguments.

* __[subject]__ - The subject line for your email
* __[template-file]__ - The full path of the template file to use for the body of the email
* __[substitutes]__ - A key/value collection of substitutions
* __[mime-type]__ - MIME type of your email. Typically either _"text/plain"_ or _"text/html"_
* __[email]__ - Which email address to send your email to
* __[name]__ - The name of the recipient of the email
* __[attachments]__ - List of entities/attachments to add to the email

Notice, this slot requires you to have configured your SMTP settings. To see how to do this refer
to the [magic.lambda.mail](/documentation/magic.lambda.mail/) project. The **[substitutes]** arguments
is a key/value collection matching &#123;&#123;key&#125;&#125; values in your template, replacing the content by the
value of your key. If you've got a template such as the following.

> Hello &#123;&#123;name&#125;&#125;, ...

You can invoke it with the following Hyperlambda.

```
signal:magic.emails.send
   substitutes
      name:John Doe
```

The above will substitute the &#123;&#123;key&#125;&#125; parts in your template with _"John Doe"_.
The **[attachments]** argument is a list of additional MIME entities as **[entity]** objects. Refer
to [magic.lambda.mime](/documentation/magic.lambda.mime/) to understand how these can be created and parametrised.
If you specify at least one such additional **[attachments]** object, the email will be sent as a _"multipart/mixed"_
entity. The **[template-file]** argument is assumed to be the path of an email template file in your system,
that can be either HTML or plain text. If you have an HTML file you need to set the **[mime-type]** argument
to `text/html` - Otherwise you should set this argument to `text/plain`.

### [magic.google.translate]

This slot allows you to translate something using Google Translate, and it requires the following arguments.

* __[text]__ - Text piece to translate
* __[src-lang]__ - Source language to translate _from_
* __[dest-lang]__ - Destination language to translate _to_

Below is example usage.

```
signal:magic.google.translate
   text:This is some piece of text that will be translated into Arabic
   src-lang:en
   dest-lang:ar
```

The above will result in the following after executing it.

```
signal:هذا جزء من النص سيتم ترجمته إلى اللغة العربية
```

The slots requires the two character ISO code for its source and destination language arguments. You can
lookup this online if you wish.

### [magic.io.file.load-recursively]

This slot loads _all_ files recursively within the specified folder, and returns their filenames _and_ their
content. The following example Hyperlambda illustrates its usage.

```
signal:magic.io.file.load-recursively
   .:/modules/
```

The above will result in something resembling the following. Notice, the result below has been _significantly_ snippet.

```
signal
   :/modules/README.md
      :"\n# Your modules folder\n\nThis ... snip ...\n"
   :/modules/magic/crypto_invocations-count.get.hl
      :@"..."
```

As you can see above the result is an array of filenames, where each filename has one child node, being the actual
content of the file. The slot is used when for instance a frontend application is being generated based upon a
template - In addition when you download a folder or something similar.

### [magic.modules.ensure-database]

This slot ensures that a module's database exists by invoking its associated create database SQL file. The
slot requires the following arguments.

* __[module]__ - Name of module
* __[database]__ - Name of database to check for

The slot basically checks to see if the specified **[database]** database exists, and if not, attempts
to find its associated _"xxx.yyy.sql"_ script within its folder, where _"xxx"_ is the module name and
_"yyy"_ is the default database type. The slot will also automatically execute any migration scripts
associated with the module. Notice, the _"Ensure database"_ macro in _"Hyper IDE"_ automatically takes
care of wiring up invocations to this slot, creating the required structure in the process.

### [magic.modules.install-module]

This slot installs a module that has been previously unzipped into your modules folder by making sure
all startup files are executed. Typically you wouldn't want to execute this directly yourself, but rely
upon Magic's middleware to invoke the slot. If you unzip a zip file inside of your _"modules"_ folder,
and/or download a bazar item, this slot will be automatically invoked.

### [transformers.hash-password]

This slot is a _"transformer"_ and typically used for input payloads originating from HTTP invocations,
such as when creating a new user, etc. The following Hyperlambda illustrates its usage.

```
.arguments
   password:foo
eval:x:+
signal:transformers.hash-password
   reference:x:@.arguments/*/password
```

The idea of the slot is that it transforms in place the specified argument by reference. Implying executing
the above Hyperlambda will result in something resembling the following.

```
.arguments
   password:$2b$10$ZjOhP3DecbgqYsTKknvLmODs1H1C6bfCheBug6iTk5TNmEckE9H3e
```

This makes it perfect for _"transforming"_ input payloads containing passwords before persisting these into
your database.

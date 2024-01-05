---
title: Slots
description: Here you can find the documentation for the most important dynamic slots you can find in Magic's middleware
---

Magic creates the following dynamic slots during startup. Notice, most of these slots are there exclusively
to make sure the middleware of Magic works correctly, and are _not_ intended to be used directly by you
in your own [Hyperlambda](/hyperlambda/) code, unless explicitly stated otherwise, and/or you're extending
Magic, or replacing parts of its core with your own custom logic.

* __[magic.auth.authenticate]__ - Authenticates a user and returns a JWT token
* __[magic.auth.change-password]__ - Allows a user to reset his or her password
* __[magic.auth.create-user]__ - Creates a new user in Magic
* __[magic.auth.ensure-role]__ - Ensures the specified role exists, and if not, creates it
* __[magic.db.mysql.databases]__ - Returns all databases for a specified connection string
* __[magic.db.mysql.tables]__ - Returns all tables for the specified connection-string/database combination
* __[magic.db.mysql.columns]__ - Returns all columns for a specified connection-string/database/table combination
* __[magic.db.mysql.foreign_keys]__ - Returns all foreign keys for a specified connection-string/database/table combination
* __[magic.db.mysql.indexes]__ - Returns all indexes for the specified connection-string/database/table combination
* __[magic.db.mssql.databases]__ - See the MySQL equivalent above
* __[magic.db.mssql.tables]__ - See the MySQL equivalent above
* __[magic.db.mssql.columns]__ - See the MySQL equivalent above
* __[magic.db.mssql.foreign_keys]__ - See the MySQL equivalent above
* __[magic.db.mssql.indexes]__ - Returns all indexes for the specified connection-string/database/table combination
* __[magic.db.pgsql.databases]__ - See the MySQL equivalent above
* __[magic.db.pgsql.tables]__ - See the MySQL equivalent above
* __[magic.db.pgsql.columns]__ - See the MySQL equivalent above
* __[magic.db.pgsql.foreign_keys]__ - See the MySQL equivalent above
* __[magic.db.pgsql.indexes]__ - Returns all indexes for the specified connection-string/database/table combination
* __[magic.db.sqlite.databases]__ - See the MySQL equivalent above
* __[magic.db.sqlite.tables]__ - See the MySQL equivalent above
* __[magic.db.sqlite.columns]__ - See the MySQL equivalent above
* __[magic.db.sqlite.foreign_keys]__ - See the MySQL equivalent above
* __[magic.db.sqlite.indexes]__ - Returns all indexes for the specified connection-string/database/table combination
* __[magic.emails.send]__ - Sends a _"braided"_ email
* __[magic.io.file.load-recursively]__ - Loads all files from within some folder recursively
* __[magic.modules.ensure-database]__ - Ensures some database exists by executing its create database SQL file
* __[magic.modules.install-module]__ - Installs a module in your system
* __[transformers.hash-password]__ - Hashes a specified password in place

## Authentication and authorisation related slots

These are slots related to authentication and authorisation, and allows you to authenticate, 
change password of users, and other things related to the _"auth"_ parts of the system. Notice, you would
rarely if ever use these slots directly, since the system contains several endpoints helping you out with
the consumption of these slots. However, to be complete, we've chosen to document these none the less.

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

### [magic.auth.change-password]

Allows a user to change his or her password. This slot requires the user to be already authenticated and having a valid
JWT token. An example of changing your own password to _"admin2"_ can be found below.

```
signal:magic.auth.change-password
   password:admin2
```

If you invoke the above Hyperlambda, and log out from Magic, you'll need to use _"admin2"_ as your password to
authenticate again. Notice, this slot will evaluate within the context of the _"current user"_, implying the only
person who can change his or her password is the user currently being authenticated.

Yet again, Magic contains helper endpoints for these types of operations, and you would probably never want to
directly invoke the slots yourself, but rather use the helper endpoints from your own frontend if you wish to
use this type of functionality. See the [endpoints](/endpoints/) section for details.

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
execute the above Hyperlambda for then to go to your [Users & Roles](/dashboard/users-roles/) component item,
you will find this user. Notice, you might want to delete the user after having verified it exists.

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

If you execute the above Hyperlambda and go to USers & Roles afterwards, you will see how you now
have a _"foo-role"_ in your system.

## Database meta traversal

All the following slots are a part of the database meta system, and allows you to retrieve meta data about your
databases, such as database names, table names, columns names, and foreign keys for tables. These slots are heavily
relied upon by the CRUDifier, as it creates a Hyperlambda backend for you, in order to determine which arguments
your HTTP endpoints requires, and how to validate these during HTTP invocations towards your backend.

All these have at least 4 versions, one for SQLite, one for MySQL, one for PostgreSQL, and a fourth for SQL Server,
and their only difference is that the MySQL versions use _"mysql"_ as its slot name, SQL Server uses _"mssql"_, PostgreSQL
uses _"pgsql"_ and SQLite uses _"sqlite"_. Besides from this, they're identical in regards to their APIs, which is
the point, since it allows for these slots to be used transparently, or _"polymorphistically"_ towards any underlaying
database type. In the following section, we therefor document their MySQL version, implying you'll have to exchange
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

### [magic.db.mysql.indexes]

This slot returns all indexes for the specified **[connection-string]**/**[database]**/**[table]** combination.
Below is example usage.

```
signal:magic.db.mysql.indexes
   connection-string:generic
   database:magic
   table:users_roles
```

The above would return all indexes in your _"users\_roles"_ table.

## Misc slots

These are slots that don't belong to a specific category solving some problem related to your applications.

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

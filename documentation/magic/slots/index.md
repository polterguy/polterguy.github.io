
# Dynamic slots

Magic creates the following dynamic slots during startup. Notice, most of these slots are there exclusively
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
   email:info@aista.com
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

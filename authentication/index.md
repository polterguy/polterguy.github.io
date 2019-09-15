# Authentication

Although authentication is arguably beyond the scope of Magic, since it seeks
to be a database agnostic framework - I have added some helper functions to
help you with authentication as you implement Magic in your own solution(s).
The below video demonstrates a template you can use, that allows you to immediately
secure your Magic installation, following all industry best practices, such
as hashing your passwords with a per-user based salt, etc. The solution
depends upon a database called _"magic_auth"_, in addition to that you exchange
the default (static) authentication slot in its system Hyperlambda files.
But the video should be able to easily guide you through this process
in less than 10 minutes.

<div style="margin-left: auto; margin-right: auto; width: 560px;">
<iframe width="560" height="315" src="https://www.youtube.com/embed/DCMY-uT0UVw" 
frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>
</div>

The code I am using in the above video to cryptographically hash my passwords
using a BlowFish hashing algorithm, can be found below.

```
.arguments
   username:string
   password:string
auth.verify-ticket:root

crypto.password.hash:x:@.arguments/*/password

add:x:./*/signal/*/values
   get-nodes:x:@.arguments/*/username

unwrap:x:+/*/values/*/password
signal:magic.db.mysql.create
   database:magic_auth
   table:users
   values
      password:x:@crypto.password.hash
return-nodes:x:@signal/*
```

## Need more control?

If the above is not an optimal solution for you, you can still use the
code and modify it to your own needs, to use any other database and/or method to serve your
authentication and authorisation needs. For instance the **[crypto.password.hash]**
slot, allows you to use a blowfish hashing algorithm, and per-user based salt
for your passwords, allowing you to safely store them in a database, without
fearing rainbow dictionary attacks - In the case of that an adversary should gain
physical access to your database. The **[crypto.password.verify]** reverses the process,
and allows you to verify that its **[hash]** argument is matching the specified
password value.

The **[auth.create-ticket]** slot, allows you to create a JWT token,
that you can use as a _"ticket"_ for future HTTP requests towards your backend.
The **[auth.verify-ticket]** slot allows you to secure a piece of Hyperlambda,
and associate it with a list of roles, in such a way that unless the user
belongs to at least one of those roles, it will throw an exception, and
abort the execution of the rest of the Hyperlambda you are trying to evaluate.

All of the above slots can be found in the _"magic.lambda.auth"_ project, and
the _"magic.lambda.crypto"_ project. Below are all the relevant slots listed
for you for your convenience.

* __[crypto.password.hash]__ Creates a cryptographically secured hash value from a password
* __[crypto.password.verify]__ Verifies that some password is a match to some **[hash]** value of the same password
* __[auth.create-ticket]__ Creates a JWT authentication token for you with the specified **[username]** and associated **[roles]**
* __[auth.verify-ticket]__ Verifies that a user is authenticated, and that he or she belongs to the specified role
* __[magic.authenticate]__ The slot invoked when a user for some reasons is trying to authenticate to the system
* __[auth.refresh-ticket]__ The slot that allows you to _"refresh"_ your JWT token. Should be invoked a couple of minutes before your existing token expires

## Security concerns! IMPORTANT!

Before you actually implement Magic into production, _it is crucial that you change its 'auth' secret_.
You can do this by editing the _"appsettings.json"_ file, and make sure you provide
a fairly long string of _"random characters"_ to its _"auth:secret"_ configuration
setting. This is used to salt the internal JWT generator in .Net, and unless you
guard this _"random gibberish"_ the same way you'd guard the pin code to
your ATM card, an adversary can easily reproduce the creation of your JWT tokens,
and create fake tokens, to impersonate an actual user on your site.

[Helper endpoints](/helper-endpoints)

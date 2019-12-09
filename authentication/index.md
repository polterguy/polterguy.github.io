# Authentication

Magic contains an automagic JWT authentication module, that allows you to easily
administrated your users, and create a really secure auth backend. Possibly also
serving as a SSO (Single Sign On) for your enterprise apps. Watch the video below
for a demonstration of this module.

<div style="margin-left: auto; margin-right: auto; width: 560px;">
<iframe width="560" height="315" src="https://www.youtube.com/embed/oDf8EJhZu0s" 
frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>
</div>

Notice, if you want to use Microsoft SQL Server, you'll have to make sure you correctly
resolve the URL in your frontend's _"users-service.ts"_ file, and basically exchange all
occurencies of _"magic_auth"_ with _"magic_auth/dbo"_, since MS SQL server is namespaced,
in a way MySQL is not.

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

The **[auth.ticket.create]** slot, allows you to create a JWT token,
that you can use as a _"ticket"_ for future HTTP requests towards your backend.
The **[auth.ticket.verify]** slot allows you to secure a piece of Hyperlambda,
and associate it with a list of roles, in such a way that unless the user
belongs to at least one of those roles, it will throw an exception, and
abort the execution of the rest of the Hyperlambda you are trying to evaluate.

All of the above slots can be found in the _"magic.lambda.auth"_ project, and
the _"magic.lambda.crypto"_ project. Below are all the relevant slots listed
for you for your convenience.

* __[crypto.password.hash]__ Creates a cryptographically secured hash value from a password
* __[crypto.password.verify]__ Verifies that some password is a match to some **[hash]** value of the same password
* __[auth.ticket.create]__ Creates a JWT authentication token for you with the specified **[username]** and associated **[roles]**
* __[auth.ticket.verify]__ Verifies that a user is authenticated, and that he or she belongs to the specified role
* __[magic.authenticate]__ The slot invoked when a user for some reasons is trying to authenticate to the system
* __[auth.ticket.refresh]__ The slot that allows you to _"refresh"_ your JWT token. Should be invoked a couple of minutes before your existing token expires

## Security concerns! IMPORTANT!

Before you actually implement Magic into production, _it is crucial that you change its 'auth' secret_.
You can do this by editing the _"appsettings.json"_ file, and make sure you provide
a fairly long string of _"random characters"_ to its _"auth:secret"_ configuration
setting. This is used to salt the internal JWT generator in .Net, and unless you
guard this _"random gibberish"_ the same way you'd guard the pin code to
your ATM card, an adversary can easily reproduce the creation of your JWT tokens,
and create fake tokens, to impersonate an actual user on your site.

[Helper endpoints](/helper-endpoints)

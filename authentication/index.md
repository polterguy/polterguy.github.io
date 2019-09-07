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
<iframe width="560" height="315" src="https://www.youtube.com/embed/I0eN8XGlcqQ" 
frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>
</div>

## Need more control?

If the above is not an optimal solution for you, you can still use its
demonstrated code, to use any other database and/or method to serve your
authentication and authorisation needs. For instance the **[crypto.password.hash]**
slot, allows you to create a blowfish hashing algorithm, and per-user based salt
for your passwords, allowing you to safely store them in a database, without
fearing rainbow dictionary attacks, in case an adversary should gain access
to your database. The **[crypto.password.verify]** reverses the process,
and allows you to very that its **[hash]** argument is matching the specified
password value.

The **[auth.create-ticket]** slot, allow you to create a JWT token,
that you can use as a _"ticket"_ for future HTTP requests towards your backend.
The **[auth.verify-ticket]** slot allows you to secure a piece of Hyperlambda,
and associate it with a list of roles, in such a way that unless the user
belongs to at least one of those roles, it will throw an exception, and
abort the execution of the rest of the Hyperlambda you are trying to evaluate.

All of the above slots can be found in the _"magic.lambda.auth"_ project, and
the _"magic.lambda.crypto"_ project.

[Helper endpoints](/helper-endpoints)

---
title: Alternative Authentication mechanisms for Magic
description: In this article we help you to understand the internals of authentication and authorization in Magic and Hyperlambda, allowing you to exchange the default authentication with for instance Windows LDAP or something else.
---

# Alternative authentication mechanisms

In this tutorial we will cover the following parts of Magic and Hyperlambda.

* How to exchange the default authentication mechanism in Magic with your own
* How to use LDAP and Windows _"automatic logins"_

Magic allows you to configure its internal authentication mechanism almost exactly as
you see fit, to accommodate for whatever needs you might have in your app. The easiest
way to modify it is to exchange the default **[crypto.password.verify]**
invocation in its **[magic.auth.authenticate]** dynamic slot with whatever slot you want
to use to verify the user's username and password.

**Notice** - Don't start editing the file itself, since you can more easily accomplish
this by configuring it to use another mechanism. This implies your own Magic code base
will _stay unmodified_, allowing you to update Magic in the future, without having to
apply manual changes.

This approach allows you to use external authentication, by creating your own slot,
that will be invoked with the user's username and password, every time a user tries
to authenticate. This can be done with either a dynamic slot, or a static (C#) slot,
doing whatever you want for it to do to authenticate your users. If you do this, the
slot should return boolean `true` if the user gives you his correct username and
password, otherwise it should return `false`. This is done by changing the
configuration of Magic as follows.

```json
{
  "magic": {
    "auth": {
      "authentication": "your-slot-here",
```

... _keep_ the rest of the file as is.

To use a dynamic Hyperlambda slot, simply set the above value to `signal:your-slot`.
To use a static C# slot, set it to `your-slot`. For instance, imagine you have
a third party URL which is actually responsible for authenticating your users, and that
it will return `SUCCESS 200` if the user is providing the correct username/password
combination as query parameters. This can be accomplished by creating a dynamic slot
such as the one below.

```
// Creates an external grant to authenticate users
slots.create:acme.authenticate

   // Making sure [username] and [password] was given
   validators.mandatory:x:@.arguments/*/username
   validators.mandatory:x:@.arguments/*/password

   // Building our URL
   strings.concat
      .:"https://acme.com/authenticate?username="
      strings.url-encode:x:@.arguments/*/username
      .:"&password="
      strings.url-encode:x:@.arguments/*/password

   // Invoking external HTTP endpoint
   http.get:x:@strings.concat

   // Checking if external invocation was a success
   switch:x:@http.get

      case:int:200
         return:bool:true

      default
         return:bool:false
```

Then you configure your _"authentication"_ value in your _"appsettings.json"_ file
to use the above slot by providing a value for it as follows `signal:acme.authenticate`.
Below is an example.

```json
{
  "magic": {
    "auth": {
      "authentication": "signal:acme.authenticate",
```

**Notice** - Magic does not allow you to exchange its _authorisation_ mechanism, implying
you'll still need a user record in your `magic`/`users` database table matching the usernames
you want to grant access to Magic. In addition, this user needs to be associated with his
_roles_ in the `magic`/`users_roles` table. Hence, create your users with the _"Auth"_ menu
item, and just give these a gibberish password, and a username that matches their usernames
in the external authentication service. The password is not important, since it'll never be
checked, but instead your external authentication service will be responsible for verifying
their passwords.
The last point is true for all forms of alternative authentication, and hence applies for
all authentication permutations described further down in this document.

## Windows authentication

Magic also supports Windows authentication. This part requires some configuration parts on
your side, in addition to adding a NuGet package to Magic that allows you to access your LDAP
directory from within your LAN.
You can find an optional additional NuGet package for Magic
called _"magic.lambda.ad-auth"_ [here](https://www.nuget.org/packages/magic.lambda.ad-auth). The idea of
this package is that instead of checking your database for a matching password, it will pass in your
username and password combination to your Windows domain, and only authenticate you if you provide
it with the correct Windows username/password combination. You can find its main
documentation [here](/documentation/magic.lambda.ad-auth/).

**Notice** - This method also requires that the username exists in your `magic`/`users` database, and
it is still using the default `magic`/`users_roles` table for _authorisation_, just like all other
alternative authentication mechanisms in Magic.

First pull in the _"magic.lambda.ad-auth"_ package into your _"backend.csproj"_ file somehow, this can
be done by checking out its [NuGet repository](https://www.nuget.org/packages/magic.lambda.ad-auth).
Then make sure you edit your _"appsettings.json"_ file, since this package needs to know your LDAP
URL, and also which slot to use to verify users' usernames and passwords. Below is an example of
the parts you'll need to modify.

```json
{
  "magic": {
    "auth": {
      "authentication": "auth.ad.authenticate",
      "ldap": "LDAP://foo.acme.somewhere"
```

... keep the rest of the file as is.

And that's it. You've now got Single Sign On in your Magic app. Login to Magic using your Windows
username and passsword from now on instead of the password stored in the users table.
Your Windows username is typically something such as follows `ACME\username`, where
ACME is the domain name on your Windows network. This approack _might_ also work with your
company email address as your username, depending upon how your network has been configured.
The web server that runs Magic also needs to be a part of your Windows domain.

## Windows automatic authentication

Magic also supports automatic Windows authentication, although this requires a bit more manual work from your
side, but most of it can be done by correctly configuring Magic. This allows you to automatically authenticate
your users, but only from within your LAN, implying that a user that is already logged on to your Windows
network, can _automatically_ authenticate towards Magic _without_ providing his username or password.
All changes required to make Windows authentication from above working also applies
for this mechanism, implying you'll have to pull in the _"magic.lambda.ad-auth"_ NuGet package, you'll
have to setup the configuration parts from above - But in addition to these steps, you also have to
make sure you _turn on_ automatic authentication in Magic by changing the `auto-auth` configuration
key and set its value to `auth.ad.get-username`. In addition this feature also requires that you turn
_on_ CORS for your frontend domains needing to use this feature. Hence, if you intend to use this
from e.g. two domains that are as follows _"dashboard.acme.com"_ and _"babelfish.acme.com"_, you'll
have to instruct Magic to allow for sending credentials back and forth between your Magic backend
and these two domains. The latter can be done by changing the _"magic.frontend.urls"_ and applying all
domains you want to allow for as a comma separated list.

Below is an example of the relevant configuration changes you need to apply.

```json
{
  "magic": {
    "frontend": {
      "urls": "https://dashboard.acme.com,https://babelfish.acme.com"
    },
    "auth": {
      "auto-auth": "auth.ad.get-username",
```

... _keep_ the rest of the file as is.

As you invoke the _"authenticate"_ HTTP method from any of the above domains, you no longer need
to supply a username or a password. If you don't, the **[auth.ad.get-username]** slot will be
invoked to retrieve your Windows username, and the default password check will be bypassed.
You still need to invoke the _"magic/modules/auth/authenticate"_ endpoint and retrieve a JWT
token that you associate with future requests, but you no longer need to supply any username or
password to this endpoint.
This method assumes that your web server is a part of your Windows domain, and
that you are logged into your client machine with your domain/Windows credentials.
Angular also needs to be specifically configured on a per request level to pass in the
NTLM/Negotiate credentials by configuring the HTTP GET invocation with a `withCredentials: true`
value. Below is an example of the latter.

```typescript
// Assumes httpClient is an instance of Angular HttpClient
this.httpClient
  .get<any>('/magic/system/auth/authenticate', {
    withCredentials: true
  }).subscribe((result: any) => {

      // Success!
      console.log('SUCCESS!')
      console.log(result);

  }, (error: any) => {

    // Error!
    console.log('FAILURE!');
    console.log(error);

  });
```

You can no longer access your backend through its web based DNS entry to make
automatic logins work, but you _must_ use your LAN DNS entry, which might be something such
as for instance _"acme-foo-web-server01"_. However, the frontend can be accessed using its
web based DNS entry, and you can also configure your server to expose itself over a web
based DNS entry, and resort to _manual_ Windows logins if the application is accessed over
the public web, and only using automatic Windows authentication if the app is accessed from
within your LAN. How you solve these parts though, is a matter of taste, opinions, requirements
related to convenience, and your organisation's security regime.
This only works because of that the default _"web.config"_ file deployed with
the backend turns _on_ Windows authentication _and_ anonymous authentication - In addition to
that the _"launchSettings.json"_ does the same. If you don't care about these settings, and
you have no needs for these, you can change these as you see fit - However, deploying to
nGinx or anything _not_ being IIS will typically just ignore these settings, and hence
we chose to release Magic out of the box as this, to make it as easily configured as
possible. If you are super paranoid, and don't care about this at all, you might want to
turn _off_ these features.

This was probably the most complex authentication mechanism in Magic so far, ignoring
[cryptographically secured lambda invocations](/tutorials/crypto-lambda-http/) and
[cryptographic challenges](https://dzone.com/articles/zero-username-and-password-authentication).
Hence, to sum it all up we'll repeat the required steps below.

1. Include the NuGet package called _"magic.lambda.ad-auth"_.
2. Make sure your Windows username exists in the `users` database table by creating it through the _"Auth"_ menu item.
3. Modify the following configuration settings in your _"appsettings.json"_ file.
 - magic.auth.authentication
 - magic.auth.ldap
 - magic.auth.auto-auth
 - magic.frontends.urls
4. Use your LAN URL for invocations towards your backend.
5. If you're using Angular, make sure you invoke the _"authenticate"_ endpoint with `withCredentials` turned _on_.

**Notice** - There is a helper endpoint you can invoke at _"magic/system/auth/auto-auth"_ that
will return _"on"_ if automatic authentication has been enabled in your backend. Authentication can still
only be used from within the LAN - But at least it allows you to query your backend to check if
automatic Windows authentication has been turned on.

* [Continue with using Magic with Microsoft SQL Server](/tutorials/sql-server/)

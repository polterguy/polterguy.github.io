
# Authentication with your Windows username/password

You can find an optional additional NuGet package for Magic
called [magic.lambda.ad-auth](https://www.nuget.org/packages/magic.lambda.ad-auth). The main idea of
this package is that instead of checking your database for a matching password, it will pass in your
username and password combination to your Active Directory, and only authenticate you if you provide
it with the correct Active Directory username/password combination. You can find its main
documentation [here](/documentation/magic.lambda.ad-auth/).

**Notice** - This package still requires that the username exists in your `magic/users` database, and
it is still using the default `magic/roles` table for _authorisation_, as in deciding which roles your
users belongs to - But at least it provides your with SSO or Single Sign On capabilities in your Magic
installation. Hence, _before_ you start configuring your Magic installation to use SSO through AD,
please make sure you create a user in Magic using the _"Auth"_ dashboard menu item with a username
that matches your Windows user. The password for this user will not be important, since once you've
applied the rest of the changes to use Windows SSO, Magic is no longer responsible for checking your
password as you login.

First pull in the _"magic.lambda.ad-auth"_ package into your _"backend.csproj"_ file somehow, this can
be done by checking out its [NuGet repository](https://www.nuget.org/packages/magic.lambda.ad-auth).
Then make sure you edit your _"appsettings.json"_ file, since this package needs to know your LDAP
domain and also which slot to use to verify users' passwords. Below is an example of only the parts you
need to add to your file.

```json
{
  "magic": {
    "auth": {
      "authentication": "ad-auth.authenticate",
      "ldap": "LDAP://foo.acme.somewhere"
```

... keep the rest of the file _as is!_

And that's it. You've now got Single Sign On in your Magic app. Login to Magic using your Windows
username and passsword from now on instead of the password stored in the users table.

**Notice** - Your AD username is typically your company email address.

## Zero username/password authentication

Magic also supports Windows authentication, although this requires a bit more manual work from your
side. This allows you to automatically authenticate your users, but only from within your LAN,
implying a user already logged on to your Windows network, can automatically authenticate towards
Magic _without_ even providing any username or password. In order to turn this on, you'll have to
do some manual changes to your Magic installation. First you'll have to modify your _"launchSettings.json"_
file, and turn _on_ Windows authentication. This can be done by making sure it resembles something such as
the following.

```json
{
  "iisSettings": {
    "windowsAuthentication": true,
    "anonymousAuthentication": false,
```

Notice how the default values in that file have been reverted above.

Then you'll have to turn on IIS Windows authentication by modifying your _"Startup.cs"_ file's
`ConfigureServices` method to resemble the following.

```csharp
public void ConfigureServices(IServiceCollection services)
{
    services.AddSingleton(Configuration);
    services.AddControllers().AddNewtonsoftJson();

    /*
        * Initializing Magic.
        *
        * Notice, must be done AFTER you invoke "AddControllers".
        */
    services.AddAuthentication(IISDefaults.AuthenticationScheme);
    services.AddMagic(Configuration);

    /*
        * Checking if SignalR is enabled, and if so, making sure we
        * add support for it.
        */
    if (Configuration["magic:sockets:url"] != null)
        services.AddSignalR();
}
```

**Notice** - You'll have to make sure you're also using the following namespace
at the top of that file.

```csharp
using Microsoft.AspNetCore.Server.IISIntegration;
```

Then you will have to create a new HTTP GET endpoint, not taking any arguments. The purpose
of this endpoint is to return a JWT token, such that the rest of your Magic app works transparently,
having a JWT token, that is built from your Windows user, instead of the default database login logic.
This file should resemble the following.

```
/*
 * Automatically authenticates a user using Windows Authentication.
 */
.description:Authenticates a user with Windows authentication, returning a JWT token if successful.


/*
 * Retrieves Windows username.
 *
 * This will only succeed if the user is already authenticated with his Windows user.
 */
ad-auth.authenticate-auto


/*
 * Invokes our authenticate slot to associate roles with user.
 *
 * Notice how we pass in [check-password] as false.
 * This ensure that the user's password will not be checked.
 */
unwrap:x:+/*
signal:magic.auth.authenticate
   username:x:@ad-auth.authenticate-auto
   check-password:bool:false


/*
 * Returns the authentication JWT ticket created above to the caller.
 */
unwrap:x:+/*
return-nodes
   result:x:@signal/*
```

You can save this file as e.g. `/backend/files/modules/system/auth/authenticate-auto-ad.get.hl`.

This will result in a relative endpoint having the following URL `/magic/modules/system/auth/authenticate-auto-ad`.
If you invoke that URL using the HTTP GET verb, and you're on your Windows intranet/LAN, logged in as a user,
this should result in you having a JWT token returned to your client.

**Notice** - Like the first AD authenticate solution from above, you will still need to create the user
in your Magic database first, since only authentication is given through Windows, and _not_ authorisation.

At this point you should probably delete the original `auth/authenticate.get.hl` file to avoid users
from being able to login using an explicit username. Alternatively, you can provide _both_ solutions,
to allow for logging in over the internet using a username/password approach, with your Windows user's
username and password, and automatically logging in users on the LAN/intranet using the latter solution.
At which point you could try automatically loggin on the user, and if this doesn't work, allow the user
to explicitly login using his Windows username/password.

* [Documentation](/documentation/)

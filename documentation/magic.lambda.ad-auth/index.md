
# Magic Lambda Windows Authentication

This project gives your Magic installation the capability of authenticating users through your Windows Domain.
The project contains _two_ methods for authentication; One method where you supply your Windows username and
password, and Magic checks these towards the `DirectoryEntry` object for your LDAP Domain.

## Common configuration

Both of these methods implies that you configure Magic such that it knows your LDAP URL.
This is done by changing the `magic.auth.ldap` value from your _"appsettings.json"_ file,
such that it points to your LDAP URL. Typically, your network administrator knows this value.
Below is an example of this configuration. Make sure you change the `LDAP://foo.acme.somewhere`
to your actual LDAP URL.

```json
{
  "magic": {
    "auth": {
      "ldap": "LDAP://foo.acme.somewhere",
```

... _keep_ the rest of the file as is.

## Windows username/password authentication

Assuming you've applied the above configuration changes, you can authenticate such that the username and
password the user supplies is passed into your Windows LDAP Domain to perform the actual authentication.
Below is an example of using Windows username/password authentication.

```
auth.ad.authenticate
   username:foo@acme.com
   password:SomePa$$wordHere
```

If the authentication is successful, the above slot will return boolean true to caller. If the credentials
are incorrect the slot will return false to caller.

**Notice** - The web server needs to be within your Windows domain for this to work.
However, the client machine doe _not_ need to be a part of your Windows domain, which makes
this solution suitable for applications exposed to the web, where you still want to use
Windows SSO (Single Sign On) to allow for users to authenticate towards your Magic application.

## Zero username/password Windows authentication

The second method assumes your client is already logged on to your domain with his Windows
credentials, in addition to that you're accessing the application through your LAN, and that
the web server is configured to use Windows authentication. This method allows you to invoke
the **[auth.ad.get-username]** slot to retrieve the user's username, which you then later
can use to authenticate the user in the Hyperlambda middleware. Below is an example of usage.

```
auth.ad.get-username
```

The above slot will return the Windows username of the user if successful. If not successful
it will return null. Notice, this method assumes you've configured your Magic installation to
use Windows authentication in your _"launchSettings.json"_ file, such as the following
illustrates.

```json
{
  "iisSettings": {
    "windowsAuthentication": true,
    "anonymousAuthentication": false,
```

... _keep_ the rest of the file as is. [Read more about Windows authentication](https://docs.microsoft.com/en-us/aspnet/core/security/authentication/windowsauth?view=aspnetcore-5.0&tabs=visual-studio)
to understand the internals of how this works.

In addition to the above changes to your _"launchSettings.json"_ file, you'll also have to
change the `magic.auth.auto-auth` setting in your _"appsettings.json"_ file, and set its value
to _"auth.ad.get-username"_. Below is an example for how to turn on _both_ of these mechanisms
assuming you change the _"LDAP://foo.acme.somewhere"_ value to the URL of your _actual_ LDAP server.

```json
{
  "magic": {
    "auth": {
      "authentication": "auth.ad.authenticate",
      "ldap": "LDAP://foo.acme.somewhere",
      "auto-auth": "auth.ad.get-username",
```

... _keep_ the rest of the file as is.

## Combination authentication schemes

Both of the above authentication mechanisms can actually be _combined_, such that the authenticate
endpoint in Magic no longer requires the **[username]**/**[password]** arguments as mandatory,
and if not given, it will try to automatically authenticate the user using the **[auth.ad.get-username]**
slot.

If a **[username]**/**[password]** argument _is_ provided though, it will try to authenticate the
user using the **[auth.ad.authenticate]** slot. This allows the end user to explicitly login to
Magic providing a username/password combination, which is useful for instance over a machine where
the user is not logged into his Windows account, allowing the user to access Magic over the web - While
automatically logging in the user if the user is on his intranet. The flow for this is simply
to invoke the authenticate endpoint _without_ a username/password combination first, and if
this fails then ask the user for his username/password combination, and invoke the endpoint
again, this time with the user's username and password as arguments to the invocation.

## Getting started with Windows authentication

Before you can turn any of these features on, you'll have to somehow bring in the NuGet package into
your project encapsulating this, which you can do by checking out the
[package's NuGet project](https://www.nuget.org/packages/magic.lambda.ad-auth/) page. Also notice that
_before_ you apply the above changes, you'll have to create a user in your Magic database with the same username
you're using to sign on to your domain. This is typically your company email address. After you've created this user,
you'll have to associate this user with the root role somehow, since after you've applied the above
configurations you can no longer login using your default root account.

The last parts is crucial since this package _only_ changes authentication, and _not_ authorisation. This implies
that you'll still need to use the default role assignment from Magic, which does a lookup
into the _"magic/roles"_ database table - And in order to associate a user with roles, you'll need an actual
username to associate the user with these role(s). However, the passwords of your users as you create these
are irrelevant, since the default password logic of Magic is never applied once you've configured your Magic
application to function according to the above recipe.

This allows you to still apply (most) of the default auth parts to your users, such as locking them out,
imprison them, impersonate them, etc - See the video documentation for the _"Auth"_ menu item to understand
what this implies. The one thing that will _not_ work though is the ability send a user a _"forgot password link"_,
etc for obvious reasons - Since Magic no longer is responsible for maintaining your users' passwords,
but rather your Windows Domain now controls your users passwords, etc.

## Project website

The source code for this repository can be found at [github.com/polterguy/magic.lambda.ad-auth](https://github.com/polterguy/magic.lambda.ad-auth),
and you can provide feedback, provide bug reports, etc at the same place.

## Quality gates

- [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.ad-auth&metric=alert_status)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.ad-auth)
- [![Bugs](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.ad-auth&metric=bugs)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.ad-auth)
- [![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.ad-auth&metric=code_smells)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.ad-auth)
- [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.ad-auth&metric=coverage)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.ad-auth)
- [![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.ad-auth&metric=duplicated_lines_density)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.ad-auth)
- [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.ad-auth&metric=ncloc)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.ad-auth)
- [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.ad-auth&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.ad-auth)
- [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.ad-auth&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.ad-auth)
- [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.ad-auth&metric=security_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.ad-auth)
- [![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.ad-auth&metric=sqale_index)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.ad-auth)
- [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.ad-auth&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.ad-auth)

## License

This project is the copyright(c) 2020-2021 of Thomas Hansen thomas@servergardens.com, and is licensed under the terms
of the LGPL version 3, as published by the Free Software Foundation. See the enclosed LICENSE file for details.

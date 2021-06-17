
# Authentication internals

Magic allows you to configure its internal authentication mechanism almost exactly as
you see fit, to accommodate for whatever needs you might have in your app. The easiest
way to modify it is to exchange the default **[crypto.password.verify]**
invocation in its **[magic.auth.authenticate]** dynamic slot with whatever slot you want
to use to verify the user's username and password.

**Notice** - Don't start editing the file itself, since you can more easily accomplish
this by configuring it to use another mechanism. This implies your own Magic code base
will stay unmodified, more easily allowing you to update Magic in the future.

This approach allows you to use external authentication, by creating your own slots,
that will be invoked with the user's username and password, every time a user tries
to authenticate. This can with either a dynamic slot, or a static (C#) slot, doing
whatever you want for it to do to authenticate your users. If you do this, the slot
should return boolean `true` if the user gives you his correct username and password,
otherwise it should return `false`. This is done by changing the configuration of
Magic as follows.

```json
{
  "magic": {
    "auth": {
      "authentication": "your-slot",
```

To use a dynamic Hyperlambda slot, simply set the above value to `signal:your-slot`.
To use a static C# slot, simply change it to `your-slot`. For instance, imagine you have
a third party URL which is actually responsible for authenticating your users, and that
it will return `SUCCESS 200` if the user is providing the correct username/password
combination as query parameters. This can be accomplished by creating a dynamic slot
such as the one below.

```
slots.create:acme.authenticate

   // Making sure [username] and [password] was given
   validators.mandatory:x:@.arguments/*/username
   validators.mandatory:x:@.arguments/*/password

   // Building our URL
   strings.concat
      .:"https://acme.foo?username="
      strings.url-encode:x:@.arguments/*/username
      .:"&password="
      strings.url-encode:x:@.arguments/*/password

   // Invoking external HTTP endpoint
   http.get:x:@strings.concat

   // Figuring out if external invocation was a success
   switch:x:@http.get

      case:int:200
         return:bool:true

      default
         return:bool:false
```

The you configure your _"authentication"_ value in your _"appsettings.json"_ file
to use the above slot by providing a value for it as follows `signal:acme.authenticate`.

**Notice** - Magic does not allow you to exchange its _authorisation_ mechanism, so
you still need to have the username for users you wish to externally authenticate such
as we illustrate above in your magic/users database table - In addition to associating
this user with whatever roles the user has in your Magic installation.

## Windows authentication

You can find an optional additional NuGet package for Magic
called _"magic.lambda.ad-auth"_ [here](https://www.nuget.org/packages/magic.lambda.ad-auth). The idea of
this package is that instead of checking your database for a matching password, it will pass in your
username and password combination to your Windows domain, and only authenticate you if you provide
it with the correct Windows username/password combination. You can find its main
documentation [here](/documentation/magic.lambda.ad-auth/).

**Notice** - This package still requires that the username exists in your `magic/users` database, and
it is still using the default `magic/roles` table for _authorisation_, as in deciding which roles your
users belongs to - But at least it provides your with SSO or Single Sign On capabilities in your Magic
installation. Hence, _before_ you start configuring your Magic installation to use SSO through AD,
please make sure you create a user in Magic using the _"Auth"_ dashboard menu item with a username
that matches your Windows user. The password for this user will not be important, since once you've
applied the rest of these changes to use Windows authentication, Magic is no longer responsible for
checking your password as you login.

First pull in the _"magic.lambda.ad-auth"_ package into your _"backend.csproj"_ file somehow, this can
be done by checking out its [NuGet repository](https://www.nuget.org/packages/magic.lambda.ad-auth).
Then make sure you edit your _"appsettings.json"_ file, since this package needs to know your LDAP
URL, and also which slot to use to verify users' usernames and passwords. Below is an example of
the parts you'll need to modify.

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

**Notice** - Your Windows username is typically something such as follows `ACME\username`, where
ACME is the domain name on your Windows network. This approack _might_ also work with your
company email address as your username, depending upon how your network has been configured.

## Windows automatic login

Magic also supports automatic Windows authentication, although this requires a bit more manual work from your
side. This allows you to automatically authenticate your users, but only from within your LAN,
implying that a user that is already logged on to your Windows network, can _automatically_ authenticate towards
Magic _without_ providing his username or password. In order to turn this on, you'll have to
do some manual changes to your Magic installation.

* [Documentation](/documentation/)

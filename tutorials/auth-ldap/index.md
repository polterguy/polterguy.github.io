
# Authentication over LDAP

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

And that's it! You've now got Single Sign On in your Magic app!

* [Documentation](/documentation/)

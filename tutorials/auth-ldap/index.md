
# Authentication over LDAP

You can find an optional additional NuGet package for Magic
called [magic.lambda.ad-auth](https://www.nuget.org/packages/magic.lambda.ad-auth). The main idea of
this package is that instead of checking your database for a matching password, it will pass in your
username and password combination to your Active Directory, and only authenticate you if you provide
it with the correct Active Directory username/password combination. To see its code you can checkout
its [project website](https://github.com/polterguy/magic.lambda.ad-auth).

**Notice** - This package still requires that the username exists in your `magic/users` database, and
it is still using the default `magic/roles` table for _authorisation_, as in deciding which roles your
users belongs to. But at least it provides your with SSO or Single Sign On capabilities in your Magic
installation. the main idea of the package is to exchange the password verification in Magic with an
invocation to instead **[crypto.password.verify]**. However, first pull in the _"magic.lambda.ad-auth"_
package into your _"backend.csproj"_ file somehow. Then make sure you edit your _"appsettings.json"_
file, since this package needs to know your LDAP domain. Below is an example of only the parts you
need to add to your file.

```json
{
  "magic": {
    "ldap": {
      "path": "LDAP://foo.acme.somewhere"
    },
```

... keep the rest of the file _as is!_

Then you will need to edit your _"/files/modules/system/auth/magic.startup/magic.auth.authenticate.hl"_ file
somehow. The smartest way to do this is to use the Magic Hyper IDE, and then find its slot invocation to
the **[crypto.password.verify]** slot, and exchange it with the following Hyperlambda.

```
            ad-auth.authenticate
               username:x:@.arguments/*/username
               password:x:@.arguments/*/password
```

**Notice** - Remove the existing **[hash]** argument to the existing slot too.

Then either restart your .Net 5 backend somehow, or simply execute the above file if you're in Hyper IDE
by clicking the _"Execute"_ button. However, before you can log out, you obviously will have to create
your root AD user in the `magic/users` database table first. You can do this using the _"Auth"_ menu item,
and create a new user, with your AD username, and just whatever password. The password for this user it
not important, since it will never be checked in fact, so you can just put in random gibberish if you wish.

**Important** - Before you now log out, make sure you associate your new root user with the _"root"_ role.

Now you can log out, and login again, but this time with your AD domain username/password, instead of the
default root account. The latter will in fact no longer work, unless you've got an AD user called _"root"_,
with the exact same password as you used while setting up Magic.

Notice, you can no longer update Magic, without at the very least manually applying the above changes to
your _"magic.auth.authenticate.hl"_ file. I will try to squeeze my head in the future, to figure out some
intelligent method to solve this - But at least for the time being, you've now got Single Sign On (SSO)
and AD authentication if you wish.

* [Documentation](/documentation/)

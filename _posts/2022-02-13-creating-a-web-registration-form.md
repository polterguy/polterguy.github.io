---
layout: post
author: thomas
title: Creating a Web Registration form
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/blogs/online-registration.jpg"
description: Magic allows you to easily create your own UI wrapping the existing HTTP backend endpoints to create your own custom registration form.
---

Magic contains everything you need to create a registration form. Below is a screenshot of Magic's
internal registration form. However, what you probably didn't know is that you can use the same backend
logic to create your own frontend with for instance Angular or ReactJS, while having Magic take care
of all backend parts automatically. Double optin? Check! Verifying user's email address? Check! Reset
password emails? Check! Assuming you have access to an SMTP server somewhere, Magic automatically wires
up _everything_ related to user registration for you, before you have to write as much as a single line
of (backend) code yourself.

![Online registration forms](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/blogs/online-registration.jpg)


## Magic endpoints related to authentication and registration

Registration, authentication, and authorisation of course is tightly coupled together - Implying if you want one,
you'll have to take all. Below are all endpoints related to user registration.

* __POST__ - `magic/system/auth/register` - Register a user in your backend
* __POST__ - `magic/system/auth/verify-email` - Verifies a user's email address
* __PUT__ - `magic/system/auth/change-password` - Changes the active user's password
* __POST__ - `magic/system/auth/send-reset-password-linkz` - Sends a reset password email to a user

After you've created your user registration parts, the next part becomes how to apply authorisation
and authentication in your application, implying how to allow your users to actually login, and
prevent non-authorised users from accessing your application. Endpoints related to authentication and
authorisation are listed below.

* __GET__ - `magic/system/auth/authenticate` - Login a user
* __GET__ - `magic/system/auth/verify-ticket` - Ensures JWT token is valid
* __GET__ - `magic/system/auth/refresh-ticket` - Refresh JWT token endpoint, returning a _"fresh"_ JWT token
* __GET__ - `magic/system/auth/endpoints` - Returns authorisation requirements associated with all endpoints

The last endpoint above is what returns your backend's _"access rights"_, implying what endpoints
your user can invoke, given his or her existing role(s). The easiest way to get started with the process
of creating a user registration form, is to [install Magic locally](/tutorials/getting-started/), use
the _"Endpoints"_ menu item to browse the above endpoints, for then to play around with the endpoints,
invoking them, and experience how the backend ties together everything for you - However, before you can
do that you'll need to configure an SMTP server such that Magic can send emails to users registering.
Open up the _"Analytics/Endpoints"_ dashboard component, and make sure you apply some valid SMTP settings
for your Magic installation. Below is an example of using GMail's SMTP server, which will only work if
you open up your GMail account for _"Insecure apps"_.

```json
"smtp":{
  "host":"smtp.gmail.com",
  "port":465,
  "secure":true,
  "username":"username@gmail.com",
  "password":"gmail-password",
  "from": {
    "name":"John Doe",
    "address":"john@doe.com"
  }
}
```

Exchange the above settings with whatever SMTP server settings you've got access to, and save
your configuration. If you're using GMail all you've got to do is to exchange your username/password combination
above, and ensure you've opened up your GMail account for _"Insecure apps"_. Below is a screenshot of how
this should look like in Magic.

![SMTP configuration settings](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/blogs/smtp-config.jpg)

Now you can open your _"Endpoints"_ dashboard component, and start playing around with the above
endpoints. Magic will automatically determine which payload/query-parameters your endpoints
requires, allowing you to parametrise your endpoints as you see fit. Below is a screenshot of
how it would look like if you invoke _"/magic/system/auth/endpoints"_.

![Auth endpoints invoked](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/blogs/auth-endpoints.jpg)

Notice, in the above endpoints the `auth` return value from the endpoint is a list of roles that are
allowed to invoke your endpoint. If the `auth` field does not exist on an endpoint, this implies _all_
users are allowed to invoke the endpoint, including non-authenticated users. If an endpoint has
only one value, and its value is `*`, this implies _any authenticated_ user can invoke the endpoint.
You can use the response of invoking the above endpoint to build stuff such as _"authentication guards"_,
preventing users from accessing frontend components your users are not allowed to access.

At this point you can play around with the registration related endpoints, by providing a valid
email address, and see how Magic sends you a _"Verify your email address"_ email as you invoke the
endpoint. Notice, at this point you'll need to [understand the registration logic](/tutorials/registering/),
such as how Magic requires a `frontendUrl` and a `template` argument as you invoke the `register`
and `verify-email` endpoints. You can find these parts under _"User registration"_ in the previous link.
Basically, this implies creating a frontend somewhere that is able to parse the automatically created
query parameters that Magic appends to your registration email's hyperlink. You can use
a `localhost` URL here to test your code.

## Managing your users

Magic allows you to easily manage your users, assign users to roles, and all other aspects related to
user administration. Below is a screenshot of the _"Users"_ component. This component allows you to
lock out users, impersonate users, search for users, and/or assign/remove users from roles as you see fit.

![Managing users](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/registered-user.jpg)

To dive deeper into registering users, managing users, and how the registration process work, you might
benefit from reading the article linked to further up on this article. However, if you like to create a a CRUD HTTP
API wrapping your database, that only allows for users having verified their email address to be allowed
to invoke your endpoints, you can use the _"Crudifier"_ in Magic, choose your database, click _"Set defaults"_,
and apply the following settings before you crudify your tables. Notice how I appended the _"user"_ role to the
default values.

![Crudifying sakila with auth](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/blogs/sakila-user-authentication.jpg)

To understand how Magic prevents non-authorised users from accessing your automatically generated wep API,
you might benefit from reading [this article](/tutorials/database-crud/), and scroll down to
the _"Authorisation and authentication"_ parts. This article also explains how Magic automatically generates
a CRUD web API wrapping your database.

## Using Magic as a SSO server

Magic's authentication and authorisation module builds upon [JWT](https://jwt.io). This is an open standard,
and allows you to automatically verify JWT tokens Magic creates in most other server side frameworks. If
you use the same hashing algorithm for your auth secrets, and you share your auth secret between Magic and
your other backend web APIs, you will also ensure your users are automatically authorised as the same user
in any other backend web API you choose to use in combination with Magic, as long you somehow pass the tokens
that Magic creates into your other web APIs. This allows you to use Magic as a _"Single Sign On"_ web API
backend for any other backend projects you might have, ranging from PHP projects and Python projects, to .Net
projects and Java projects. This allows you to manage and administrate your users from Magic's dashboard,
while integrating your authentication and authorisation logic into another backend.

## Security

Magic takes security seriously. As an example of this realise that Magic is using BlowFish hashing to
securely store passwords into your database, with per record based salts, implying the amount of energy
required to brute force your database using constructs such as Rainbow Dictionary Attacks is equal to
the amount of energy required to boil all the water in our solar system. Below you can see a screenshot
of a password stored in the `users` database table, automatically created for you as you install Magic.
This implies that even if a malicious user should somehow gain physical access to your users database,
the passwords stored in it will still be 100% perfectly safe, and there exists no known mechanisms
the malicious user can apply to figure out the actual password stored in your database.

![Crudifying sakila with auth](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/blowfish.jpg)

### Password entropy

In addition Magic allows you to use any password you wish, including passwords such as follows.

> This is actually a very, very, very secure password, yet still easily remembered

The above password is actually several orders of magnitudes more secure than a password such as the
following.

> $5pRqSx&

The reasons are because an average $500 laptop can easily brute force an 8 character long password in
roughly 20 minutes today. While the first password above is probably some 70/100 characters long,
implying even super computers would need millions of years brute forcing the first password. Still
the first password is much more easily remembered than the second pasword, allowing users to use unique
passwords for all their sites and services, yet still easily remember all passwords. This is the reason
why Magic does not require _"special characters"_ or _"upper case characters"_ or _"at least one number"_,
etc. Because once we drop these (quite frankly) ridiculous requirements, creating extremely long and
secure passwords becomes much easier for the end user.

If you didn't already read it, to finish up understanding everything related to user registrations,
you should probably read the article linked to below. How you'd go about creating your frontend of course,
varies from framework to framework, and while we might go through these parts in future articles, you
can probably find dozens of examples in these regards if you search for user registration and appends
your favourite framework to your search query, such as Angular, React, or Swift. However, as you can
clearly understand now, Magic eliminates an entire axiom related to user registration, implying probably
its most difficult to understand axiom, being the server side parts, user administration, security,
and all other server side parts related to registering users into your app.

* [User registration internals](/tutorials/registering/)

---
title: Authentication and Authorisation in Magic
description: This tutorial helps you understand how the authentication and authorization mechanisms in Magic and Hyperlambda works. It also shows you how to create and administrate your users, and touches upon JWT a little bit.
---

# Authentication and authorisation

In this tutorial we will cover the following parts of Magic and Hyperlambda.

* How authentication works in Magic
* How authorisation works in Magic
* Some JWT internals
* How to administrate users and roles using your Magic dashboard

Magic was created to solve all the repetitive problems we experienced in our day jobs. One of these problems
happens to be authentication and authorisation, which is a problem you have to solve every time
you create a new application. At this point some might argue that OAuth2 solves these problems, and while
technically that is true, OAuth2 is also extremely complex and over engineered, and very easy to
get wrong. With Magic authentication and authorisation simply works out of the box, without you having
to configure anything at all, making it almost impossible to have something going wrong. Watch the following
video for a walkthrough of how the auth parts in Magic works.

<div class="video">
<iframe width="560" height="315" style="position:absolute; top:0; left:0; width:100%; height:100%;" src="https://www.youtube.com/embed/xD9NEWbgfYY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## User administration

As you can see in the above video, Magic contains a million parts helping you out with your authentication and
authorisation requirements, such as the ability to lock users, implement double optin registrations, having users
confirm their email address before being accepted into your site, resetting passwords, etc. In addition to
of course that the Magic Dashboard contains high level UI components, allowing you
to easily administrate your user database such as illustrated below.

![Authentication and Authorisation in Magic](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/auth.jpg)

As you are working on your own internal systems it is highly unlikely you will find the time to 
implement something resembling the above. With Magic, it's simply there. Combining this with the auditing
and diagnostic features of Magic, allowing you to see high level KPI charts related to security issues, such as
illustrated below - Probably gives you everything you will ever need related to authentication and authorisation.

![Security audit logging in Hyperlambda](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/health-security.jpg)

## Endpoints

Magic exposes several endpoints related to authentication that simplifies your life. These are as follows.

* GET magic/system/auth/authenticate - Authenticates a user with a username/password combination
* PUT magic/system/auth/change-password - Allows a user to change his or her password
* GET magic/system/auth/refresh-ticket - Refresh a user's JWT token granting a new token with a new expiration value
* POST magic/system/auth/register - Allows others to register as users in your system
* POST magic/system/auth/send-reset-password-link - Sends a reset password link to the user's email address
* POST magic/system/auth/verify-email - Double optin endpoint allowing users to verify their emails
* GET magic/system/auth/verify-ticket - Returns success status code if JWT token is valid

Combining the above endpoints gives you more or less everything you need related to authentication and authorisation
for your own applications, allowing you to focus on the unique parts of your domain problem, instead of commodity
problems experienced by everyone every time they're to implement a new system.

## JWT internals

JWT is very easy to understand. It is based upon a secret that you can find in Magic as a configuration setting.
Below are all configuration settings related to auth in Magic.

```json
{
  "magic": {
    "auth": {
      "secret": "TD98Y37V78hBp91C2HWo2QEYJSN4LGzalimoYhPj7PU6gp87Zd6yOda7DyCQ4d5HQijYrj926AaGixgRdaadbn5YUz5TSscg",
      "https-only": false,
      "valid-minutes": 120,
      "registration": {
        "allow": true,
        "confirm-email": null
      }
    }
  }
}
```

Assuming you can keep the above secret a _secret_, your auth system is highly secure. The idea is that once a JWT
token is generated, its payload is concatenated with the above secret, and a SHA256/HMAC is constructed, which
unless can be correctly reproduced in the .Net middleware upon consecutive requests, results in that the token
is considered invalid, and the user will not be authorised to do anything requiring authorisation. By default
Magic will use the BouncyCastle CSRNG classes to generate your auth secret. But if you're super paranoid, you
can also manually edit it as you see fit.

In fact, using Magic as your JWT auth server, to integrate it into your own custom C# apps, is as simple as
configuring the correct middleware by implementing a handful of lines of custom C# code. You can get an idea
of how to get started by looking at the C# code for [magic.lambda.auth](https://github.com/polterguy/magic.lambda.auth/blob/master/magic.lambda.auth/helpers/TicketFactory.cs). This allows you to share the secret Magic has with your own custom
application, and use Magic as an _"auth server"_ having single sign on in your company. As long as you
can keep your auth secret a secret, this is a perfectly legitimate method to implement SSO.

## Slots

On the server side Magic contains a lot of helper slots simplifying your life as you create your apps.
These are as follows.

* __[auth.ticket.create]__ - Creates a new JWT token
* __[auth.ticket.get]__ - Returns the username and roles associated with the current request
* __[auth.ticket.in-role]__ - Returns true if user belongs to any of the specified roles
* __[auth.ticket.refresh]__ - Creates a refreshed JWT token from the old token
* __[auth.ticket.verify]__ - Verifies that the user is authenticated, and optionally belongs to one or more roles

You can find the complete documentation for these parts in the [magic.lambda.auth](/documentation/magic.lambda.auth/)
parts of the documentation. Most of these are _"AOP'ish in nature"_, allowing you to simply inject them into
your own Hyperlambda code, resulting in some sort of expected result meeting your requirements related to auth.

## Internals

Internally Magic will generate an authentication and authorisation database for you as you
initially configure Magic. This is one of the reasons why it asks you for a valid database connection during its
setup process. The tables related to auth in this database are as follows.

* __users__
* __roles__
* __users_roles__

This structure is of course easily expanded upon if you need additional information, such as extra information
associated with users, containing for instance user's full names, etc. If you use for instance the _"SQL"_ menu
item and you select all records from your users table using something such as the following ...

```sql
select * from users
```

... you can see how the passwords are stored using _slow BlowFish hashing with individual record based salts_.
The latter of course is crucial for anybody taking passwords seriously on behalf of their users.

![Blowfish hashed passwords](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/blowfish.jpg)

This is one of those million things that might go wrong as you implement your own authentication,
which if done wrong, opens up your password database for Rainbow Dictionary attacks, allowing at least
in theory adversaries to brute force your users' passwords. Which of course is a _major_ security threat,
since users tends to reuse the same passwords on multiple sites/applications - Implying if an adversary
gains access to your user's password in _one_ app, he effectively gains access to your user's passwords
in _all_ apps the user is using, and can easily impersonate the user across the entirety of the web.

### Password entropy

When you initially configured Magic, you probably noticed that you can use any password you wish, and that
Magic does not require you to use special characters, numbers, caps, etc. This actually _increases_ the password
entropy of your database, since it allows users to for instance provide sentences and phrases as passwords. The
following is a perfectly legitimate password in Magic.

> This is a perfectly fine password

Paradoxically, and a bit counter intuitive may I add, this actually results in _much stronger passwords_ than
the commonly accepted dogma of providing something such as follows.

> Rf5$!fgh

The above password is 8 characters long. On average it takes a normal laptop approximately 20
minutes to brute force the above password. While the first password above, containing 33 characters,
would require more energy than what is required to boil all water on earth to brute force. Hence, 
restrictions such as for instance Apple puts on your passwords for their AppStore, is quite
counterintuitively much simpler to brute force than simple phrases and sentences such as Magic allows you to use.
Simply since allowing a user to use a normal sentence, increases password length easily by one order of
magnitude, making the brute force approach require trillions of times the number of iterations to guess
your users' passwords using a brute force approach. Combining this with the fact of that users have different
native languages, might be using slang, etc - Results in that the entropy becomes the same, only
exponentially growing for each additional character the user adds to his password. The point of course
being that for me as a Norwegian, the following password is quite easy to remember, since it's a
Norwegian sentence, that makes perfectly sense for me, that I could easily memorise.

> Heisann, teisann, mitt navn er Thomas Hansen og jeg er KUL!

The above password contains 71 characters, and brute forcing it with any known technology we have at our
disposal today, would require more energy than the amount of energy required to boil all the water that
exists in our galaxy. Implying it's not even possible in theory to brute force the above password. So the
above password is actually _stronger_ than the 8 letter _"special character password"_ above it - In addition
to that it's much easier to remember for the human brain, and allows your users to create _unique_ passwords for
all their online services, reducing the likelihood of having your password compromised at _one_ site
resulting in that your entire online life is compromised.
However, since Magic also is using individual per record based salts, combined with BlowFish hashing,
even if your user has a single character password,
_the CPU time required to brute force a single character password would still be practically impossible_,
even if an adversary had access to your entire password database. This is due to the nature of BlowFish
hashing, combined with per record based salts.

* Continue with [Hyperlambda and Web Sockets](/tutorials/web-sockets/)

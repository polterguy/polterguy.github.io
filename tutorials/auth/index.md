
# Authentication and authorisation

Magic was created to solve all the repetetive problems I experience in my day job. One of these problems
happens to be authentication and authorisation, which is a problem you have to solve every time
you create a new application. At this point some might argue that OAuth2 solves these problems, and while
technically that _is_ true, OAuth2 is also ridiculously complex and over engineered, and very easy to
get wrong. And of course if you get your app's auth parts wrong, you might as well not have auth at all,
since it exposes your apps for adversaries doing whatever they want to do with your app. Authorisation is
one of those things together with cryptography you really _should not solve yourself_, unless you _really_
know what you're doing. Watch the following video for a walkthrough of how the auth parts in Magic works.

<div style="position:relative; padding-bottom:56.25%; padding-top:30px; height:0; overflow:hidden;margin-top:4rem;margin-bottom:4rem;">
<iframe width="560" height="315" style="position:absolute; top:0; left:0; width:100%; height:100%;" src="https://www.youtube.com/embed/tR2kyM6HKxw" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## User administration

As you can see in the above video, Magic contains a million parts helping you out with your authentication and
authorisation requirements, such as the ability to lock users, implement double optin registrations, having users
confirm their email address before being accepted into your site, resetting passwords, etc. In addition
of course, the coolest parts is that the Magic Dashboard also contains high level UI components, allowing you
to easily adiministrate your user database, such as illustrated below.

![Auth Dashboard Module](https://servergardens.files.wordpress.com/2021/04/auth-dashboard.png)

Imagining your manager giving you the required time to implement the above is probably at best delusional,
regardless of what company you work for. With Magic, it's _simply there_. Combining this with the auditing
and diagnostic features of Magic, allowing you to see high level KPI charts related to security issues, such as
illustrated below - Results in that Magic's features from a conceptual point of view related to this,
is something you're probably never going to be able to reproduce using any other means.

![Auth diagnostics and KPI](https://servergardens.files.wordpress.com/2021/04/auth-diagnostics.png)

## Endpoints

Magic exposes a couple of crucial endpoints related to authentication that simplifies your life. These are as follows.

* GET magic/modules/system/auth/authenticate - Authenticates a user with a username/password combination
* PUT magic/modules/system/auth/change-password - Allows a user to change his or her password
* GET magic/modules/system/auth/refresh-ticket - Refresh a user's JWT token granting a new token with a new expiration value
* POST magic/modules/system/auth/register - Allows others to register as users in your system
* POST magic/modules/system/auth/send-reset-password-link - Sends a reset password link to the user's email address
* POST magic/modules/system/auth/verify-email - Double optin endpoint allowing users to verify their emails
* GET magic/modules/system/auth/verify-ticket - Returns success status code if JWT token is valid

Combining the above endpoints gives you more or less everything you need related to authentication and authorisation,
allowing you to build UI components in any framework of choice, wrapping the above backend endpoints.

## JWT internals

JWT is easily explained to a child. OAuth2 on the other hand, is ridiculously complicated and over engineered,
to the point where even the guy in charge of the standardisation committee went on a 2 year long tour throwing
sessions who's names were as follows; _"OAuth2 sucks!"_ OAuth2 might be cool if you're Google or Facebook, but
if you're anything else, it's a _hot smoking pile of garbage_!

JWT on the other hand is ridiculously simple to understand. It's based upon a secret, which you can find
in Magic as a configuration setting. Below are all configuration settings related to auth in Magic.

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

Assuming you can keep the above `secret` a secret, your auth system is secure enough to be consumed by FSB,
MI6 and CIA. the idea is that once a JWT token is generated, its payload is concatenated with the above secret,
and a SHA256/HMAC is constructed, which unless can be correctly reproduced in the .Net middleware upon consecutive
requests, results in that the token is considered invalid, and the user will not be authorised to do anything
requiring authorisation.

In fact, using Magic as your JWT auth server, to integrate it into your own custom C# apps, is as simple as
configuring the correct middleware by implementing a handful of lines of custom C# code. You can get an idea
for how to get started by looking at the C# code for [magic.lambda.auth](https://github.com/polterguy/magic.lambda.auth/blob/master/magic.lambda.auth/helpers/TicketFactory.cs). This allows you to share the secret Magic has with your own custom
application, and use Magic as an _"auth server"_ having single sign on in your enterprise. As long as you
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
parts of the documentation. Most of these are _"APO'ish in nature"_, allowing you to simply inject them into
your own Hyperlambda code, resulting in some sort of expected result meeting your requirements related to auth.

## Internals

Internally Magic will generate an authentication and authorisation database for you 100% automagically as you
initially configure Magic. This is one of the reasons why it asks you for a valid database connection during its
setup process. The tables related to auth in this database are as follows.

* __users__ - Contains usernames and passwords
* __roles__ - Contains all roles
* __users_roles__ - A many to many link table containing the association between users and roles

This structure is of course easily expanded upon, if you need additional information, such as extra information
associated with users, containing for instance user's full names, etc. If you use for instance the _"SQL"_ menu
item and you select all records from your users table using something such as the following.

```sql
select * from users
```

You can see how the passwords are stored using _slow BlowFish hashing_ With _individual record based salts_.

![Users table from Magic database](https://servergardens.files.wordpress.com/2021/04/users-table.png)

This is one of those million things that might go wrong as you implement your own authentication,
which if done wrong, opens up your password database for Rainbow Dictionary attacks, allowing at least
in theory adversaries to brute force your users' passwords. Which of course is a _major_ security threat,
since users tends to reuse the same passwords on multiple sites/applications - Implying if an adversary
gains access to your user's password in _one_ app, he effectively gains access to your user's passwords
in _all_ apps the user is using, and can easily impersonate the user across the entirety of the web.

This results in that you might get sued over your _"free pony website"_ since one of your users reused
his or her password on _your_ site also for his internet bank website. I cannot emphasize this strongly
enough; Unless you know with 100% certainty what you are doing ...

> Do NOT implement your own auth system!

### Password entropy

When you initially configured Magic, you probably noticed that you can use any password you wish, and that
Magic does not require you to use special characters, numbers, caps, etc. This actually _increases_ the password
entropy of your database, since it allows users to for instance provide sentences and phrases as passwords. The
following is a perfectly legitimate password in Magic.

> This is a perfectly fine password

Paradoxically, and a bit counter intuitive may I add, this actually results in _much stronger passwords_ than
the commonly accepted dogma of providing something such as follows.

> Rf5$!fgh

The above password for instance is 8 characters long. On average it takes a normal laptop approximately 20
minutes to brute force the above password. While the first passsword above, containing 33 characters,
would require more energy than that which is required to boil all water on earth to brute force. Hence, these
ridiculous restrictions for instance Apple has as you creates passwords for their AppStore, is quite
counterintuitively much simpler to guess than simple phrases and sentences such as Magic allows you to use.
Simply since allowing a user to use a simple sentence, increases password length easily by one order of
magnitude, making the brute force approach require trillions of times the number of iterations to guess
your users' passwords using a brute force approach. Combining this with the fact of that users have different
mother tongues, might be using slang language, etc - Results in that the entropy becomes the same, only
exponentially growing for each additional character the user adds to his password. The point of course
being that for me as a Norwegian, the following password is ridiculously simple to remember, since it's a
Norwegian sentence, that makes perfectly sense for me, which I could easily memorize.

> Heisann, teisann, mitt navn er Thomas Hansen og jeg er KUL!

The above password contains 71 characters, and brute forcing it with any known technology we have at our
disposal today, would require more energy than the amount of energy required to boil all the water that
exists in our galaxy. Implying it's not even possible in theory to brute force the above password. So the
above password is actualyl _stronger_ than the 8 letter _"special character password"_ above it - In addition
to that it's a trillion times easier to remember, and allows your users to create _unique_ passwords for
all their online services, reducing the likelyhood of having your password compromised at _one_ site
results in that your _entire online life_ is compromised.

However, since Magic also is using individual per record based salts, combined with BlowFish hashing,
even if your user _has a single character password_, the CPU time required to brute force a single
password would still be practically impossible, even if an adversary had access to your entire password
database. This is due to the nature of BlowFish hashing, combined with per record based salts.

## Don't do this at home kids!

Seriously, _do not implement your own authentication system_. As you can see, there are clearly a
million things that can go wrong. For instance, one of the most popular OAuth2 implementations for .Net
literally _contains thousands of security issues_ (no, I will not tell you which project I am talking about) -
I should know, because I ran it through SonarQube to check it out in one of my previous jobs. It contained
so many security holes that SonarQube almost crashed and refused to continue. Then compare this to Magic's
auth system ...

![SonarQube and Magic Auth](https://servergardens.files.wordpress.com/2021/04/sonar-qube.png)

79.3% Unit Test coverage, zero security holes, and the 4 code smells above are actually simplifications
for its unit tests, carrying no semantic changes. Unless you can implement your auth system having
traits such as the above, you _basically have no auth system_, and you might as well publish your users'
passwords in clear text on the dark web for all to see ...

> DO NOT IMPLEMENT YOUR OWN AUTH!

Even if you've got the skills to do it correctly, you highly unlikely will be given the _time_ from your
manager to do it correctly.

## Wrapping up

In this article we walked through some of the features of the authentication and authorisation system of
Magic, and we showed the high level UI modules giving you administration and KPI capabilities, in addition
to how you could use this to your own advantage in your own apps. Afterwards we walked through several general
security concerns, such as slow hashing, password entropy, and general security concerns related to auth.

* [Documentation](/documentation/)

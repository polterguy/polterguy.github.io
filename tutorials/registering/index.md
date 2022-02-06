---
title: Registration and authentication in Magic
description: This article walks you through how to use the integrated registration endpoints and helpers in Magic, to create your own frontend registration component, allowing you to verify user's email address, implement forgot password forms, etc
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/og-registering.jpg"
---

# Registration and authentication in Magic

In this article we will walk you through the following parts of Magic and Hyperlambda.

* How Magic's registration endpoints work, and how you can use these in your own projects
* How to allow for users to change their passwords
* How to send forgot password emails to registered users

**Notice** - To fully take advantage of these features in Magic, you'll first need to configure your email/SMTP settings.
To configure how Magic sends emails you can read [the following article](/tutorials/sending-emails/). If you do not
correctly configure your SMTP settings, Magic will _not_ be able to send _"confirm email"_ emails, or _"reset password"_
emails. Notice also that we do not cover frontend technologies, and/or frameworks in this article. This is left to the
reader and obviously varies according to which framework, and/or technology you want to use.

## Endpoints related to authentication and user registrations

Magic contains a whole range of HTTP endpoints you can take advantage of in your own frontends to solve
registration, authentication, and related problems. Some of the more important endpoints related to this
are as follows.

* __POST__ - magic/system/auth/register - Allows users to register in your backend
* __POST__ - magic/system/auth/verify-email - Allow users to verify their email address
* __GET__ - magic/system/auth/authenticate - Allow users to authenticate
* __GET__ - magic/system/auth/verify-ticket - Verifies validity of a JWT token
* __GET__ - magic/system/auth/refresh-ticket - Refresh JWT token endpoint, returning a _"fresh"_ JWT token
* __GET__ - magic/system/auth/endpoints - Returns authorisation requirements associated with all endpoints
* __PUT__ - magic/system/auth/change-password - Allows a user to change his or her password
* __POST__ - magic/system/auth/send-reset-password-link - Sends a reset password email to a registered user

The above should cover most needs related to creating simple registration forms, allowing others to register
in your Magic backend. So let's walk through how you can use the above endpoints in your own frontend code
to allow for registrations, verify your user's email address, allow them to change their passwords, etc.

## User registration

Assuming you've configured Magic's SMTP settings, registering a user results in a two phase commit workflow,
where the user is supposed to provide his or her email address as a username, resulting in a _"confirm email address"_
email being sent to the user, allowing the user to confirm the email address supplied during registration. Only
when the user has confirmed the email address supplied, the user will have a fully functional user in Magic.
There are two important endpoints related to this workflow, and these are as follows.

* __POST__ - magic/system/auth/register - Allows users to register in your backend
* __POST__ - magic/system/auth/verify-email - Allow users to verify their email address

The first endpoint above allows a user to register at your site, and if you have configured your SMTP
server correctly, it will create a _"double optin"_ workflow, where the user needs to verify his or
her email address before given access to the site. The _"register"_ endpoint requires the following payload.

```json
{
  "username": "john@doe.com",
  "password": "some-password",
  "frontendUrl": "https://your-frontend-url.com",
  "template": "/some/path/to-some-email-template.html",
  "subject": "Subject line of registration email"
}
```

The most important argument above is the **[username]** obviously. Usernames must be a unique email address,
implying the email address cannot have been used previously to register towards the same backend. The
**[frontendUrl]** argument allows you to provide the registration endpoint with a URL where you later extract
query parameters automatically created by the registration process and sent to the user as a hyperlink he or
she must click to verify their email address. The **[template]** is a HTML file somewhere in your backend
that the registration welcome email is automatically generated from, and the **[subject]** is the subject
line of this welcome email. Both the **[template]** and the **[subject]** arguments are optional, and default
values will be used if they are not supplied.

As the user registers he or she is associated with the _"unconfirmed"_ role. This is the most restricted role
in the system, and doesn't allow the user to do anything, except of course verifying his or her email address.
When the user registers a welcome email is created and sent to the user's email address. This
welcome email will ask the user to verify his or her email address by clicking a link in the email.
This link will resemble the following.

```
https://your-frontend-url.com?
token=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855&
username=john@doe.com&
url=https://your-backend-url.com
```

The token is a security token created to uniquely identify the email address, ensuring nobody but
the recipient of the welcome email is able to verify the email address. If you create your own
frontend allowing for registrations in your Magic backend, you have to extract this token and the
username, and pass both into the **POST** _"magic/system/auth/verify-email"_ endpoint. Implying
you would create an HTTP POST invocations towards the `verify-email` endpoint resembling the
following.

```json
{
  "username": "john@doe.com",
  "token": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
}
```

When you have passed the above payload into your `verify-email` endpoint, the user will be de-associated
with the _"unconfirmed"_ role and associated with the _"guest"_ role. This gives the user
slightly more access in your backend, but is still a highly restricted role, and does not
give the user access to any of your system endpoints allowing him to tamper with your
backend in any ways. If you want to grant the user additional access in your backend, you'll
have to manually add him or her to additional roles through the Magic dashboard's _"Auth"_ menu
item. When the above workflow is completely done executing, the user has registered, and verified
his or her email address, the user can login to the system as a _"guest"_ account. Below you can
see two such registered users; One having not yet confirmed his or her email address, and the
other having confirmed his or her email address.

![Registering users in Magic](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/registered-user.jpg)

You can see which user has confirmed his or her email address by the role association the user has.

## Changing passwords and implementing "forgot password"

Sometimes users forgets their passwords, and need to have the system send them a _"reset password"_ type
of email. For those cases Magic contains the following endpoint.

* __POST__ - magic/system/auth/send-reset-password-link

**Notice** - This endpoint also obviously assumes you've already configured your Magic backend to have
access to some email/SMTP server. This endpoint works more or less the same as the above _"register"_
endpoint, and requires the following payload.

```json
{
  "username": "john@doe.com",
  "frontendUrl": "https://your-frontend-url.com",
  "template": "/some/path/to-some-email-template.html",
  "subject": "Subject line of forgot password email"
}
```

Notice that the URL constructed towards your frontend for a _"forgot password"_ email
and a _"register email"_ is the same in structure, except the _"forgot password"_ email will
construct a URL with its `token` query parameter being a _real_ JWT token, while the register
email will send a simple hash. The way to separate these two different links is to check
in your frontend code if the `token` query parameter contains a `.` or not, and if it does,
you can assume it's a valid JWT token, and use it to allow the user to invoke the `change-password`
endpoint. If the `token` query parameter does _not_ contain a `.` it should be assumed to be
a registration token type, and you need to pass it into your `verify-email` endpoint instead.
If you use different URLs for registrations and forgot password logic this doesn't
really matter. Below is an example of a URL created as the user forgets his or her password.

```
https://your-frontend-url.com?
token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.
eyJuYW1lIjoiZm9vMDVAc2VydmVyZ2FyZGVucy5jb20iLCJyb2xlIjpbInJ
lc2V0LXBhc3N3b3JkIiwiMGQ5MTAzMDJjYjIyMjc5YzE2OGIwNmE3YTM5NT
JiMDc2NDQwMWZhZGMyNjI1YjhiZDAxYjViMjcxYmU3ZjU2OSJdLCJuYmYiO
jE2NDM4MDYzMDgsImV4cCI6MTY0MzgxMzUwOCwiaWF0IjoxNjQzODA2MzA4fQ.
9xz3txhNX_z13_j7zksgnp0VpVZAxVXkySw3ZFtIync
username=john@doe.com&
url=https://your-backend-url.com
```

Notice the `.` parts separating it from a _"welcome as registered user"_ email. When you have extracted the
above `token` you need to invoke the following endpoint to actually allow the user to change his or her
password.

* __PUT__ - magic/system/auth/change-password

The payload to the endpoint should be as follows.

```json
{
  "password": "new-password"
}
```

At this point you can ask the user for a new password, and use the JWT token found in the query perameters
of your URL as the Authorization _"Bearer"_ token associated with the request. Once you've invoked the
above endpoint, you'll need to allow the user to login again to get a _"real"_ JWT token, that the user
can use for other things besides only changing his or her password.
You can use the same endpoint if you want to allow users to simply change their passwords using a normal
flow, without any _"forgot password"_ parts.

## Authenticating users

To authenticate a user you can use the following endpoint.

* __GET__ - magic/system/auth/authenticate - Allow users to authenticate

The endpoint requires two argument.

* __[username]__ - The username, or email typically if it's a registered user
* __[password]__ - The user's password

The endpoints returns a JWT token if successful, which you can use in consecutive HTTP requests towards
the backend to authorise the user. Below is an example of the response from the endpoint if succesful.

```json
{
   "ticket":"eyJhbGciOiJIUzxyz.eyJuYxyx.jWNVFWxyz"
}
```

Notice, a real JWT token would typically be much longer, but we snippet it to keep it relevant. When you
want to use the JWT token you have to attach it to your consecutive HTTP requests as a _"Bearer"_ token
in the `Authorization` HTTP header. Notice, only the _value_ of the above `ticket` field is your actual
token. For more details about the internals of what goes on beneath the hoods, you can
read [this article](/tutorials/auth/).

* Continue with [Expressions, slots and nodes](/tutorials/expressions-slots-nodes/)

---
title: Authentication and authorisation endpoints
description: Magic's built-in authentication and authorisation endpoints; authenticating, changing and resetting passwords, refreshing and verifying JWT tokens.
header:
  image: /assets/images/hero/endpoints-top.webp
  og_image: /assets/images/hero/endpoints-top-og.png
  image_description: Authentication and authorisation endpoints
---

## Authentication and authorisation endpoints

These are the endpoints related to the authentication and authorisation parts of Magic. You can find their Hyperlambda files in the _"/system/auth/"_ folder. These endpoints are typically useful for you as you implement your own authentication logic in your own code, and most of these endpoints are intended for you to consume yourself as you see fit.

### GET magic/system/auth/authenticate

This endpoint allows you to authenticate towards your Magic backend with a username and password combination. It's mostly a thin layer on top of your **[magic.auth.authenticate]** slot. **[magic.auth.authenticate]** requires two query arguments being as follows.

* __[username]__ - Username of user wanting to authenticate
* __[password]__ - Password of user wanting to authenticate

The endpoint can be invoked by anyone, and does not have any authorisation requirements. The endpoint
will return a JWT token you can use for consecutive requests towards your backend, authorising you
to invoke endpoints your user is authorised to invoke.

Magic relies upon the JWT tokens
being transmitted as _"Bearer"_ tokens in the _"Authorization"_ HTTP header, implying you'll have to
ensure the resulting JWT token from invoking the above endpoint is attached to consecutive HTTP requests.
This endpoint can be invoked by anyone, including non-authenticated clients.
This endpoint is intended for you to consume from your own code.

### GET magic/system/auth/can-reset-password

This endpoint returns _"true"_ in its _"result"_ field if the backend is able to send password reset links, otherwise
_"false"_. It takes no arguments. It returns _"true"_ only if both _"magic:smtp:host"_ and _"magic:smtp:from:address"_
have been configured, see the _"Configuring password reset"_ section below. The Magic dashboard invokes it to decide
whether or not to show its _"Forgot password"_ option on the login screen, since offering a link that can never be
delivered is worse than not offering it.

The endpoint can be invoked by anyone, and does not have any authorisation requirements.

### PUT magic/system/auth/change-password

This endpoint allows an existing user to change his or her password. It can only change the password of
the currently authenticated user, and takes the new password as the following payload.

```
{
  "password": "new-password"
}
```

This endpoint can be invoked by anyone as long as they have authenticated towards your backend previously.
This endpoint is intended for you to consume from your own code.

### GET magic/system/auth/endpoints

This endpoint returns the authorisation requirements for all endpoints in the system. It does not require
any arguments. It returns one item for each Hyperlambda endpoint in the system, with its associated verb,
and a list of roles the user must belong to in order to invoke the endpoint, if the endpoint requires
authorisation.

The endpoint can be invoked by anyone, and does not have any authorisation requirements.
This endpoint caches its result for 5 minutes, implying changes done to the authorisation
requirements of your endpoints will not be accessible for clients before 5 minutes after your changes have
been applied, unless you explicitly delete the cache item for the endpoint.
This endpoint is intended for you to consume from your own code.

### GET magic/system/auth/refresh-ticket

This endpoint allows an already authenticated user to retrieve a new JWT token with an expiration date
further into the future. The idea of the endpoint is to allow for an authenticated user to non-stop
constantly invoke this endpoint some few minutes before his existing JWT token expires, to retrieve
a new JWT token, preventing the user from being thrown out of the backend as his or her existing token
expires.

The endpoint does not take any arguments, but can only be invoked by an already authenticated
user, implying you'll need to pass in your JWT token to it in the Authorization HTTP header as a
_"Bearer"_ token or the endpoint will return _"Access denied"_.
This endpoint is intended for you to consume from your own code.

### POST magic/system/auth/send-reset-password-link

This endpoint emails a one time sign in link to a user who has forgotten his or her password. Clicking the link
signs the user into the Magic dashboard without a password, after which the user can change his or her password
with the **[change-password]** endpoint above. It takes the following payload.

```
{
  "user": "username-or-email"
}
```

* __[user]__ - Mandatory string, 1 to 256 characters. Either the username or the email address of the user.

The endpoint first matches the argument against usernames. If no user has that username, it matches it against the
_"email"_ extra field of your users. The link is sent to the email address in that extra field, so a user without an
email address on file cannot receive a link.

The link is valid for 20 minutes and carries the same roles the user would have received by authenticating
with his or her password. It points at the dashboard's _"/authentication/magic-link"_ page, and contains both
the backend URL and the token as query parameters.

The endpoint can be invoked by anyone, and does not have any authorisation requirements. Since it is public it
deliberately returns exactly the same result, _"If that account exists, a sign in link is on its way"_, whether or
not the user exists, whether or not the user has an email address, and whether or not SMTP is configured. This
prevents the endpoint from being used to discover which usernames and email addresses are real. The reason an email
was not sent is written to your log instead. The endpoint is also throttled by the shared _"auth.ip"_ (10 requests
per minute per IP address) and _"auth.global"_ (120 requests per minute in total) throttles, which it shares with
the other unauthenticated auth endpoints.

#### Configuring password reset

The endpoint will not send anything unless **all** of the following settings have been configured in your
_"appsettings.json"_ file, which you can edit from the dashboard's configuration screen. Remember that environment
variables override values in this file, with a double underscore replacing each colon.

* __"magic:smtp:host"__ - Your SMTP server, for instance _"smtp.sendgrid.net"_. Mandatory.
* __"magic:smtp:from:address"__ - The email address the link is sent from. Mandatory. An SMTP server without a sender address cannot send anything.
* __"magic:smtp:port"__, __"magic:smtp:secure"__, __"magic:smtp:username"__ and __"magic:smtp:password"__ - How to connect and authenticate towards your SMTP server. These are required by most SMTP providers.
* __"magic:smtp:from:name"__ - Optional display name for the sender.
* __"magic:backend:url"__ - The public URL of your backend, for instance _"https://api.example.com"_. Mandatory. The link is built from this value and nothing else, as described below.
* __"magic:frontend:urls"__ - Optional comma separated list of the origins of your frontends, for instance _"https://dashboard.example.com"_. This is the same setting your backend uses for CORS.

An example configuration might look like the following.

```json
{
  "magic": {
    "backend": {
      "url": "https://api.example.com"
    },
    "frontend": {
      "urls": "https://dashboard.example.com"
    },
    "smtp": {
      "host": "smtp.example.com",
      "port": 465,
      "secure": true,
      "username": "your-smtp-username",
      "password": "your-smtp-password",
      "from": {
        "name": "Your Company",
        "address": "no-reply@example.com"
      }
    }
  }
}
```

The two URL settings control where the link in the email points, and the difference between them matters.

* The link's token is a session for the user. The _"Host"_ and _"Origin"_ headers of a request to this public endpoint are controlled by whoever sends the request, so trusting them would let an attacker ask for a link for somebody else's account and have the token sent to a domain of their own. For this reason the backend part of the link always comes from __"magic:backend:url"__. If this setting is missing no link is sent, and an error is written to your log.
* The dashboard part of the link comes from the _"Origin"_ header of the request, but only if it matches, case insensitively, one of the origins in __"magic:frontend:urls"__. If the setting is empty, or the origin is not on the list, the link falls back to __"magic:backend:url"__. You only need to set __"magic:frontend:urls"__ if your dashboard is served from a different origin than your backend.

If your link is not arriving, check your log. It will tell you if SMTP is not configured, if __"magic:backend:url"__ is missing, or if the user has no email address on file. You can also invoke **[can-reset-password]** to see if SMTP is configured.

### GET magic/system/auth/verify-ticket

This endpoint allows a frontend to verify an existing JWT token, and it will return _"success"_ if
the JWT token is valid and can be used in consecutive invocations requiring authorisation somehow.
The endpoint can be invoked by any user as long as the user is authenticated.

The endpoint does not
require any arguments, but can only be invoked by an already authenticated user, implying you'll need
to pass in your JWT token to it in the Authorization HTTP header as a _"Bearer"_ token. If the JWT
token is not valid the endpoint will return a 401 status code with _"Access denied"_ as its message.
This endpoint is intended for you to consume from your own code.

---
title: Authentication and authorisation endpoints
description: Magic's built-in authentication and authorisation endpoints; authenticating, changing passwords, refreshing and verifying JWT tokens.
header:
  image: /assets/images/hero/endpoints-top.png
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

### GET magic/system/auth/verify-ticket

This endpoint allows a frontend to verify an existing JWT token, and it will return _"success"_ if
the JWT token is valid and can be used in consecutive invocations requiring authorisation somehow.
The endpoint can be invoked by any user as long as the user is authenticated.

The endpoint does not
require any arguments, but can only be invoked by an already authenticated user, implying you'll need
to pass in your JWT token to it in the Authorization HTTP header as a _"Bearer"_ token. If the JWT
token is not valid the endpoint will return a 401 status code with _"Access denied"_ as its message.
This endpoint is intended for you to consume from your own code.

---
title: Configuration endpoints
description: Magic's built-in configuration endpoints, loading and saving appsettings.json, and setting up your cloudlet.
header:
  image: /assets/images/hero/endpoints-top.webp
  og_image: /assets/images/hero/endpoints-top-og.png
  image_description: Configuration endpoints
---

## Configuration related endpoints

These endpoints are related to configuration of your system, and allow you to read and modify
configuration settings as you see fit. These endpoints are typically not intended for being used
directly by your code, but for the most parts only used during initialisation of your Magic server,
and/or as you change configuration settings in Magic.
None of these endpoints are intended to be consumed in your own code, but only
for internal usage by Magic itself.

### GET magic/system/config/load

This endpoint loads your configuration settings and returns it to the caller. The endpoint
can only be invoked by a root user and does not require any arguments.

This endpoint is not intended for you to consume in your own code.

### POST magic/system/config/save

This endpoint allows you to save your configuration settings. The specified payload will
in its entirety overwrite your existing _"appsettings.json"_ file. The endpoint
can only be invoked by a root user.

The endpoint can accept any type of JSON payload,
however whatever you supply to the endpoint will in its entirety be persisted in
your backend as your _"appsettings.json"_ file, implying if you supply bogus data,
your backend will no longer function correctly.
This endpoint is not intended for you to consume in your own code.

### GET magic/system/config/status

This endpoint returns the setup status of your system, implying if the system has been correctly
initialised. The endpoint requires no argument. If this endpoint does _not_ return true, the
frontend dashboard will guide you through the process of finishing the configuration process before
allowing you to gain access to other parts of your Magic server. The endpoint can only be invoked
by a root user. This endpoint is not intended for you to consume in your own code.

### POST magic/system/config/setup

This endpoint will setup Magic, and should only be used initially as you install Magic, and should
never be invoked afterwards, unless you need to reset your root user's password. This endpoint is
being used as you setup your Magic cloudlet initially, and creates a root user, in addition to creating
a JWT secret, etc. The endpoint requires the following payload.

```
{
  "username": "root",
  "password": "some-password",
  "is_hashed": false,
  "name": "John Doe",
  "email": "john@doe.com",
  "subscribe": false
}
```

The above arguments imply the following.

* __[username]__ - Username for your root user
* __[password]__ - Password for your root user
* __[is_hashed]__ - If true, the password is assumed to already be hashed
* __[name]__ - Full name of the root user
* __[email]__ - Email address of the root user
* __[subscribe]__ - If true, subscribes the email address to AINIRO's newsletter

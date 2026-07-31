---
title: Misc endpoints
description: Magic's miscellaneous built-in endpoints; endpoint meta data, OpenAPI specifications, Hyperlambda evaluation, and system diagnostics.
header:
  image: /assets/images/hero/endpoints-top.webp
  og_image: /assets/images/hero/endpoints-top-og.png
  image_description: Misc endpoints
---

## Misc endpoints

These are endpoints not belonging to a particular category of endpoints, but still a part of the Magic
middleware, and used by the frontend dashboard somehow.

### GET magic/system/endpoints/list

This endpoint returns all endpoints in the system, their meta data such as description, input arguments,
and resulting response if possible. The endpoint can only be invoked by a root user. The endpoint requires
no argument(s).

This endpoint is not intended for you to consume in your own code.

### GET magic/system/endpoints/openapi

This endpoint returns an OpenAPI (Swagger) specification. The endpoint handles the following optional
query argument(s).

* __[filter]__ - Partial path endpoints must match to be included in the specification
* __[system]__ - If true, system endpoints are included
* __[base-url]__ - Overrides the base URL declared in the specification's servers section
* __[scheme]__ - Overrides the scheme (http or https) declared in the specification's servers section

This endpoint is intended for you to consume in your own code and it does not require authentication.

### POST magic/system/evaluator/evaluate

This endpoint executes the specified Hyperlambda and returns the result of the invocation back to caller.
The endpoint can only be invoked by a root user and takes the following payload.

```
{
  "hyperlambda": "/* ... Some Hyperlambda here ... */"
}
```

This endpoint is not intended for you to consume in your own code.

### GET magic/system/evaluator/vocabulary

This endpoint returns the Hyperlambda vocabulary from the backend, implying which Hyperlambda slots
exist on the server. The endpoint can only be invoked by a root user.

This endpoint is not intended for you to consume in your own code.

### GET magic/system/misc/gibberish

This endpoint returns cryptographically secured random characters to the caller, optionally
taking **[min]** and **[max]** as query parameters, being the minimum length and maximum length
of the returned _"gibberish"_. With gibberish we imply CSRNG characters. This endpoint can
be invoked by anyone and optionally handles the following argument(s).

* __[min]__ - Minimum length of gibberish returned
* __[max]__ - Maximum length of gibberish returned

This endpoint is intended for you to consume from your own code.

### GET magic/system/diagnostics/system-information

This endpoint returns system related information to the caller, such as Magic backend version, number of
tasks, 10 last log items, etc. The endpoint is the foundation for the KPIs displayed in your dashboard.
The endpoint does not require any arguments. The endpoint can only be invoked by a root user.

This endpoint is not intended for you to consume in your own code.

---
title: "How to use [response.cookies.set]"
description: "How to use [response.cookies.set] - Since cookies have more parameters than just a simple key/value declaration, the [response.cookies.set] slot takes the following arguments."
generated: true
guide: true
---

The reference page of [`response.cookies.set`](/reference/slots/response/response.cookies.set/) has its arguments, constraints and declaration.

Since cookies have more parameters than just a simple key/value declaration, the **[response.cookies.set]**
slot takes the following arguments.

* __[value]__ - The string content of your cookie
* __[expires]__ - Absolute expiration date of your cookie, as a Hyperlambda `date` value
* __[http-only]__ - Boolean value declaring whether or not the cookie should only be accessible on the server
* __[secure]__ - Boolean value declaring whether or not cookie should only be transmitted from the client to the server over a secure (https) connection
* __[domain]__ - Domain value of your cookie
* __[path]__ - Path value of your cookie
* __[same-site]__ - Same-site value of your cookie

Only the **[value]** from above is mandatory. To delete a cookie on the client, set the expiration date to a value
in the past.

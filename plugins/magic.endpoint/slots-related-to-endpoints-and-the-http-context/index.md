---
title: "Slots related to endpoints and the HTTP context"
description: "Slots related to endpoints and the HTTP context - In addition to the meta retrieval endpoint described above, the module contains the following slots."
generated: true
---

This page is part of the [magic.endpoint](/plugins/magic.endpoint/) documentation.

In addition to the meta retrieval endpoint described above, the module contains the following
slots.

* __[server.ip]__ - Returns the IP address of the server itself
* __[response.status.set]__ - Sets the status code (e.g. 404) on the response object
* __[request.cookies.list]__ - Lists all HTTP request cookies
* __[request.cookies.get]__ - Returns the value of a cookie sent by the request
* __[response.cookies.set]__ - Creates a cookie that will be returned to the client over the response
* __[request.headers.list]__ - Lists all HTTP request headers sent by the request
* __[request.headers.get]__ - Returns a single HTTP header associated with the request
* __[request.ip]__ - Returns the IP address of the HTTP request
* __[request.url]__ - Returns the relative URL associated with the request, without its magic/ prefix, and query parameters as children nodes as a key/value list
* __[request.host]__ - Returns the host name associated with the request
* __[request.scheme]__ - Returns the scheme associated with the request
* __[response.headers.set]__ - Adds an HTTP header to the response object
* __[mime.add]__ - Associates a file extension with a MIME type, only relevant for the `HttpFileExecutorAsync` resolver
* __[mime.list]__ - Lists registered MIME type mappings
* __[request.verb]__ - Returns the HTTP verb of the current invocation

## Hyperlambda and cookies

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

---

[&larr; Hyperlambda code behind files](/plugins/magic.endpoint/hyperlambda-code-behind-files/) | [all of magic.endpoint](/plugins/magic.endpoint/)

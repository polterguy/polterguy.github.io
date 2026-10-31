---
title: "Accepted Content-Type values for Hyperlambda endpoints"
description: "Accepted Content-Type values for Hyperlambda endpoints - The POST, PUT and PATCH endpoints can intelligently handle any of the following Content-Types."
generated: true
---

This page is part of the [magic.endpoint](/plugins/magic.endpoint/) documentation.

The POST, PUT and PATCH endpoints can intelligently handle any of the following Content-Types.

* `application/json`
* `application/x-json`
* `application/www-form-urlencoded`
* `application/x-www-form-urlencoded`
* `multipart/form-data`

JSON types of payloads are fairly well described above, and URL encoded form payloads are handled
the exact same way, except of course the **[.arguments]** node is built from URL encoded values instead
of JSON - However, internally this is transparent for you, and JSON, query parameters, URL encoded
forms, and _"multipart/form-data"_ can be interchanged 100% transparently from your code's perspective -
Except _"multipart/form-data"_ might have **[file]** arguments wrapping streams that you need to
handle separately as such. File attachments will be passed into your endpoint as follows.

```
.arguments
   file
      name:filename-on-client.txt
      stream:[raw Stream object here]
```

All other types of payloads will be passed in as the raw stream, not trying to read from it in any
ways, allowing you to intercept reading with things such as authentication, authorisation, logic of
where to persist content, etc. To understand how you can handle these streams, check out
the _"magic.lambda.io"_ project's documentation, and specifically the **[io.stream.xxx]** slots.

## Extending the Hyperlambda Content-Type request and response resolver

The Content-Type resolver/parser is extendible, allowing you to change its behaviour by providing
your own callback that will be invoked for some specific Content-Type value provided. This is useful
if you want to be able to for instance handle _"text/xml"_ or _"text/csv"_ types of request/response
objects, and intelligently and automatically create an argument collection from it. Below is example
code illustrating how to create your own HTTP request resolver for the MIME type of _"application/x-foo"_.

```csharp
EndpointController.RegisterContentType("application/x-foo", async (signaler, request) =>
{
   var args = new Node();

   /* ... Create some sort of collection of arguments and put into args node here ... */

   return args;
});
```

**Notice** - The argument sanity checking will still be invoked with a custom handler, implying
your Content-Type handler and the **[.arguments]** declaration in your Hyperlambda file still
needs to agree upon the arguments, and if a non-valid argument is specified to a Hyperlambda file,
an exception will be thrown. Also notice that registering a custom Content-Type is _not_ thread
safe, and should be done as you start your application, and not during its life time.

You can also provide your own HTTP response resolver that will be invoked given some specified
Content-Type from your Hyperlambda file. This is done in a similar manner using something resembling
the following.

```csharp
EndpointController.RegisterContentType("application/x-foo", (response) =>
{
   /* ... Return some sort of IActionResult here ... */
   return new ObjectResult(response.Content) { StatusCode = response.Result };
});
```

The above method should also exclusively be used during startup, and not later,
since it is _not_ thread safe. The above method assumes you register your Content-Type handlers
as your application is starting.

---

[&larr; Hyperlambda endpoints and arguments](/plugins/magic.endpoint/hyperlambda-endpoints-and-arguments/) | [all of magic.endpoint](/plugins/magic.endpoint/) | [Hyperlambda endpoints and meta information &rarr;](/plugins/magic.endpoint/hyperlambda-endpoints-and-meta-information/)

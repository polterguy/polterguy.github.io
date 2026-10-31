---
title: "Hyperlambda endpoints and meta information"
description: "Hyperlambda endpoints and meta information - Due to the semantic structure of Hyperlambda, retrieving meta information from your HTTP endpoints using this module is very easy."
generated: true
---

This page is part of the [magic.endpoint](/plugins/magic.endpoint/) documentation.

## Hyperlambda endpoints and meta information

Due to the semantic structure of Hyperlambda, retrieving meta information from your HTTP endpoints
using this module is very easy. The project has one slot called **[endpoints.list]** that returns
meta information about _all_ your endpoints. This slot again can be invoked using the following URL.

```
http://localhost:5000/magic/system/endpoints/list
```

This endpoint/slot will semantically traverse your endpoints, recursively loading up all Hyperlambda
files from disc that are resolved from a valid URL, and return meta information about the file/endpoint
back to the caller. This allows the system to easily figure out things such as the following about
your endpoints.

* What is the endpoint's HTTP VERB
* What is the endpoint's URL
* What arguments can the endpoint handle
* Has the file been given a friendly description, through a **[.description]** node
* Etc ...

This slot/endpoint is what allows you to see meta information about all your HTTP REST endpoints
in the _"Endpoints"_ menu item in the Magic dashboard for instance. The return value from this
slot/endpoint again, is what's used as some sort of frontend is being generated using the Magic
dashboard.

### Extending the meta data retrieval process

You can extend the meta data retrieval process by
invoking `ListEndpoints.AddMetaDataResolver`, and pass in your own function. This class can be
found in the `magic.endpoint.services.slots` namespace.
The `AddMetaDataResolver` method takes one function object, which will be invoked for every file
the meta generator is trying to create meta data for, with the complete `lambda`, `verb` and `args`
of your endpoint. This allows you to semantically traverse the lambda/args nodes, and append
any amount of (additional) meta information you wish - Allowing you to extend the generating
of meta data, if you have some sort of general custom Hyperlambda module, creating custom
HTTP endpoints of some sort.

This function will be invoked for _every_ single Hyperlambda file in your system,
every time meta data is retrieved, so you might want to ensure it executes in a fairly short
amount of time, not clogging the server or HTTP endpoint meta generating process in any ways.


## Changing your Hyperlambda endpoint's response type

Unless you explicitly change the `Content-Type` of your response object, by using
the **[response.headers.set]** slot, a Content-Type of `application/json` will be assumed,
and this header will be added to the resulting HTTP response object. If you wish to override
this behavious and return plain text for instance, you could create an endpoint containing
the following.

```
response.headers.set
   Content-Type:text/plain
return:Hello from Magic Backend
```

If you intend to return anything but JSON, you _must_ set the `Content-Type` header, because
the resolver will by default try to serialize your content as JSON, and obviously fail unless it is
valid JSON.
You can also return stream objects using for instance the **[return-value]** slot, at which point
ASP.NET Core will automatically stream your content back over the response object, and `Dispose`
your stream automatically for you afterwards. This allows you to for instance return large files back
to the client without loading them into memory first. If you do this, you'll have to change
your `Content-Type` accordingly.

---

[&larr; Accepted Content-Type values for Hyperlambda endpoints](/plugins/magic.endpoint/accepted-content-type-values-for-hyperlambda-endpoints/) | [all of magic.endpoint](/plugins/magic.endpoint/) | [Hyperlambda code behind files &rarr;](/plugins/magic.endpoint/hyperlambda-code-behind-files/)

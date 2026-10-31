---
title: "API URLs"
description: "API URLs - The HttpApiExecutorAsync resolver will be invoked for all relative URLs starting with \"magic/\", for the following verbs."
generated: true
---

This page is part of the [magic.endpoint](/plugins/magic.endpoint/) documentation.

The `HttpApiExecutorAsync` resolver will be invoked for all relative URLs starting with _"magic/"_,
for the following verbs.

* `GET`
* `POST`
* `PUT`
* `DELETE`
* `PATCH`

The default service implementation will resolve everything after the _"magic/"_ parts in the
given URL to a Hyperlambda file assumed to be found relatively inside your _"/files/"_ folder.
The HTTP verb is assumed to be the last parts of your
filename, before its extension, implying an HTTP request such as the following.

```
GET magic/modules/foo/bar
```

Will resolve to the following physical file on disc.

```
files/modules/foo/bar.get.hl
```

Only the _"magic"_ part of your URL is rewritten before the verb is appended to the URL, and
finally the extension _".hl"_ appended. Then the file is loaded and parsed as Hyperlambda, and whatever
arguments you pass in, either as query parameters or as your JSON payload is appended into your
resulting lambda node's **[.arguments]** node as arguments to your Hyperlambda file invocation.

The resolver will never return files directly, but is only able to execute Hyperlambda files,
so by default there is no way to get static files starting with _"magic/"_ as the URL, unless
you create a Hyperlambda endpoint that returns a static file somehow.

The default resolver will only allow the client to resolve files inside your _"/files/modules/"_
folder and _"/files/system/"_ folder. This allows you to safely keep files that parts of your system
relies upon inside your dynamic _"/files/"_ folder, without accidentally creating endpoints clients can
resolve, resulting in breaches in your security.

Only the characters a-z, 0-9 and '-', '\_' and '/' are legal
characters for the resolvers, and only lowercase characters to avoid file system incompatibilities between
Linux and Windows.

There is _one exception_ to this rule though, which is that the resolver will resolve
files and folder starting out with a period (.) character, since this is necessary to allow for having
_"hidden files"_ being resolved as endpoints - Which is a requirement to make things such as
Apple's _".well-known"_ endpoints being resolved.

Below is probably the simplest HTTP endpoint you could create. Save the following Hyperlambda in a
file at the path of `/modules/tutorials/foo.get.hl` using for instance your Magic 
_"Hyper IDE"_ menu item.

```
return
   result:Hello from Magic Backend
```

Then invoke the endpoint using the GET verb with the following URL.

```
http://localhost:5000/magic/modules/tutorials/foo
```

---

[all of magic.endpoint](/plugins/magic.endpoint/) | [Hyperlambda endpoints and arguments &rarr;](/plugins/magic.endpoint/hyperlambda-endpoints-and-arguments/)

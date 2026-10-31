---
title: magic.lambda.http
moved_anchors: {"automatic-conversion": "/plugins/magic.lambda.http/automatic-conversion/", "how-to-use-httpdelete": "/reference/slots/http/http.delete/#guide", "how-to-use-httpget": "/reference/slots/http/http.get/#guide", "how-to-use-httppatch": "/reference/slots/http/http.patch/#guide", "how-to-use-httppost": "/reference/slots/http/http.post/#guide", "how-to-use-httpput": "/reference/slots/http/http.put/#guide"}
---

The magic.lambda.http project provides HTTP invocation capabilities for Magic and Hyperlambda. More specifically the
project contains the following 5 slots.

* __[\[http.get\]](/reference/slots/http/http.get/)__ - Returns some resource using the HTTP GET verb towards the specified URL
* __[\[http.delete\]](/reference/slots/http/http.delete/)__ - Deletes some resource using the HTTP DELETE verb
* __[\[http.post\]](/reference/slots/http/http.post/)__ - Posts some resources to some URL using the HTTP POST verb
* __[\[http.put\]](/reference/slots/http/http.put/)__ - Puts some resources to some URL using the HTTP PUT verb
* __[\[http.patch\]](/reference/slots/http/http.patch/)__ - Patches some resources to some URL using the HTTP PATCH verb

The __[\[http.put\]](/reference/slots/http/http.put/)__, __[\[http.post\]](/reference/slots/http/http.post/)__ and __[\[http.patch\]](/reference/slots/http/http.patch/)__ slots requires you to provide a __[payload]__
or __[filename]__ argument that will be transferred to the endpoint as is. All 5 endpoints can (optionally)
take a __[token]__ argument, which will be transferred as a `Bearer Authorization` token to the endpoint
in the `Authorization` header of your request. If you provide a __[filename]__ argument, this is assumed
to be a file relatively found within your _"/files/"_ folder somewhere. Below is an example of
retrieving the document found at the specified URL by creating an HTTP GET request.

```
http.get:"https://google.com"
```

The above will result in something resembling the following.

```
http.get:int:200
   headers
      Cache-Control:no-store, must-revalidate, no-cache, max-age=0
      Pragma:no-cache
      Date:"Mon, 29 Nov 2021 06:11:01 GMT"
      // ... etc ...
   content:"... content here ..."
```

The status code of the request is returned as the value of **[http.xxx]**, headers returned by the server
can be found in **[headers]** as a key/value pair, and **[content]** contains the actual content response
object returned by the server.

All of these slots can optionally take a **[timeout]** argument, that overrides the default timeout of 300 seconds,
with whatever integer value you provide. The timeout is specified as an integer value, being the number of seconds
to allow for the invocation, before the request is aborted and given up on. If the timeout period elapses, an
exception will be thrown.


## HTTP headers

If you want to have more control over your HTTP request, you can also explicitly add your own
**[headers]** collection, which will become the HTTP request's headers, where the header name is the name
of the node, and its value is the value of the node.  Below is an example.

```
http.get:"https://google.com"
   headers
      Accept:text/html
```

If you don't add an explicit **[headers]** collection the invocation will assume your request payload and
accepted response is JSON. If you want to change this you'll have to add at least one header to your request,
at which point the default headers will _not_ be applied.


## QUERY parameters

Instead of having to manually modify the URL according to query parameters, you can optionally pass in a **[query]**
argument, which can either contain an expression leading to a node set that will be used as query parameters - Or you
can add child nodes to the query node. See example below.

```text
.query
   foo1:bar1
   foo2:bar2
http.get:"https://foo.com"
   query:x:@.query/*

// Or, alternatively ...

http.get:"https://foo.com"
   query
      foo1:bar1
      foo2:bar2
```


## URL parameters

URL parameters are dynamically substituting parts of your URL to make it easier to create REST invocations. Below is an example.

```text
http.put:"https://api.example.com/v1/contacts/{id}"
   convert:true
   url-params
      id:int:5
   payload
      name:John
      email:john@doe.com
```

The point being that the above `{id}` will be dynamically replaced with the integer `5`. You can also use expressions here, allowing you to easily build your URL dynamically. URL parameters can be used for all verbs.


## POSTing, PUTting, and PATCHing data

The POST, PUT and PATCH slots, requires a **[payload]** argument, or a **[filename]** argument,
that becomes the body of the request. Below is an example illustrating how to create a POST request, with
a Bearer token to access the end resource.

```
http.post:"https://some-url.com"
   token:qwerty_secret_JWT_token_goes_here
   payload:some mumbo jumbo payload, typically JSON and not text though ...
```

**Notice** - If you want to submit a large file to some endpoint, without loading the file into memory
first, you should rather use **[filename]** instead of **[payload]**. This ensures the file is submitted
to your endpoint without loading it into memory first.

```
http.post:"https://some-url.com"
   filename:/README.md
```


## Passing in multipart/form-data payloads with your HTTP requests

You can also transfer multipart/form-data with all HTTP slots in Hyperlambda. This internally will use
the MIME parser to semantically create a multipart message. Below is example code of how to achieve this.

```
http.post:"http://localhost:5000/magic/modules/foo/foo"
   headers
      Content-Type:multipart/form-data
   payload
      entity:text/plain
         headers
            Content-Disposition:"form-data; name=\"foo\""
         content:Foo bar
      entity:text/plain
         headers
            Content-Disposition:"form-data; filename=\"README.md\""
         filename:/README.md
```

If you create an HTTP endpoint in Hyperlambda with the filename of _"/modules/foo/foo.post.hl"_,
resembling the following, you can see how the content is transferred in your log.

```
.accept:multipart/form-data
request.headers.list
lambda2hyper:x:../*
log.info:x:-
```


## SSE or Server-Side Events

All slots also support SSE by adding an **[.sse]** lambda object, which will be invoked once for each event published by the
server. Your lambda object will be invoked with a **[message]** argument containing the raw message published by the server.
You are responsible to convert the message to the correct type, since it's passed in as a UTF8 encoded raw string.



## Topics

* [Automatic conversion](/plugins/magic.lambda.http/automatic-conversion/) - You can also automatically convert the resulting response object to a lambda object if you have a registered conversion function, and you provide a [convert] argument, and set its value to boolean tru

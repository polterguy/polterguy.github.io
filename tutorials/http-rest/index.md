---
title: HTTP invocations with Hyperlambda
description: In this article we help you understand Hyperlambda's and Magic's HTTP capabilities, by playing around with the HTTP slots in Hyperlambda, allowing you to invoke external HTTP JSON endpoints, to retrieve data from 3rd parties, and/or integrate your code with other systems.
---

# HTTP invocations with Hyperlambda

In this tutorial we will cover the following parts of Magic and Hyperlambda.

* Invoking HTTP endpoints from Hyperlambda
* How the POST, PATCH, PUT, GET and DELETE HTTP slots differs in logic
* How to automatically transform back and forth between lambda objects and JSON, and/or other request/response types

The purpose of Magic and Hyperlambda is to simplify your life as a developer without compromising scalability, execution speed, or maintainability.
One example of this is how easy it is to integrate your Hyperlambda backend with other HTTP based services by utilising
its HTTP slots. Let's illustrate with some code.

```
http.get:"https://jsonplaceholder.typicode.com/posts"
   convert:true
```

If you execute the above Hyperlambda in your Magic's dashboard _"Eval"_ menu item, you will see something resembling
the following.

```
http.get:int:200
   headers
      Date:"Wed, 24 Nov 2021 05:56:07 GMT"
      Transfer-Encoding:chunked
      Connection:keep-alive
      X-Powered-By:Express
      x-ratelimit-limit:1000
      x-ratelimit-remaining:999
      x-ratelimit-reset:1637717108
      Vary:Origin;Accept-Encoding
      Access-Control-Allow-Credentials:true
      Cache-Control:max-age=43200
      // etc ...
   content
      .
         userId:long:1
         id:long:1
         title:sunt aut facere repellat provident occaecati excepturi optio reprehenderit
         body:"quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
      .
         userId:long:1
         id:long:2
         title:qui est esse
         body:"est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"
... etc ...
```

The status code is the value of your **[http.get]** node after invoking your endpoint, and the headers collection
is returned as the **[headers]** node. At this point you can easily traverse the array of items returned by the
endpoint using code resembling the following.

```
http.get:"https://jsonplaceholder.typicode.com/posts"
   convert:true

for-each:x:@http.get/*/content/*
   // Do stuff with '@.dp/#' here ...
```

Two lines of code, and you're returning the result of an HTTP invocation in a structured format, assuming the endpoint
you are invoking is returning JSON. The crucial parts of course as usual is what is _not_ there; No `IHttpClientFactory`,
no `IDisposable` objects you'll need to dispose, no IoC container wiring, no async/await statements, etc.
By removing the complex parts from your resulting code, maintaining things becomes much easier for both
yourself in the future, in addition to making things easier for developers inheriting your project later down the road.

> Everything is "syntax"

With the above we imply that the less syntax you've got, and the less lines of code you've got, the easier it becomes
to maintain things in the future. The primary axiom around which Hyperlambda evolves, is that _code is technical debt_,
implying the less code you've got, the less technical debt you have. Technical debt again is a _bad_ thing!

## POSTing, PUTing and PATCHing data

These three HTTP verbs requires a payload of some sort. You can easily pass in any payload by adding
a **[payload]** node to your invocations, such as the following illustrates.

```
http.post:"https://jsonplaceholder.typicode.com/posts"
   payload:@"{""userId"": 1, ""id"": 1}"
```

**Notice** - Due to not passing in a **[convert]** argument in the above snippet, any response returned by
the above endpoint will _not_ be automatically parsed into its equivalent lambda object. If you want to have
the returned payload automatically converted to a lambda object you can add a **[convert]** argument and
set its value to boolean true. Below is an example.

```
http.post:"https://jsonplaceholder.typicode.com/posts"
   payload:@"{""userId"": 1, ""id"": 1}"
   convert:true
```

You can also post files directly, _without_ loading your files into memory first, by replacing your above **[payload]**
argument with a **[filename]** argument, having the value of a relative path within your _"/files/"_ folder, that
is an existing file on your server somewhere. This has the advantage of resulting in a stream copy operation, never
exhausting your server's memory, regardless of how large your files are. You can also pass in streams as your
**[content]** value in a similar fashion, and/or as expressions leading to streams, strings, or anything really -
Including a byte array. Below is an example of passing in a file to some POST endpoint.

```
http.post:"https://foo-bar.com"
   filename:/README.md
```

Most of the times you want to post something to another endpoint, it's typically JSON you want to post.
Hyperlambda implements a lot of helper slots and features to help you out with this. The code below for instance
will automatically transform your lambda object to JSON, dynamically populate its `id` field with the value
of **[.userId]**, before transmitting your JSON to the endpoint.

```
.userId:int:1
http.post:"https://jsonplaceholder.typicode.com/posts"
   payload
      userId:x:@.userId
      id:int:1
```

You can do the same with **[http.patch]** and **[http.put]**. This simplifies the process of dynamically
creating your payloads to some HTTP endpoint, passing in lambda objects dynamically built according to
your own business logic.

### Alternating your Content-Type

Hyperlambda also has strong support for alternative content types, and it automatically transforms the
following content types for you.

* __application/json__
* __application/x-json__
* __application/hyperlambda__
* __application/x-hyperlambda__
* __application/www-form-urlencoded__
* __application/x-www-form-urlencoded__
* __multipart/form-data__

To use any of the above automatic conversions, make sure you _do not_ provide a value for your **[payload]**,
but rather provide a semantic lambda structure such as the following illustrates.

```
http.post:"https://foo.com/hyperlambda-endpoint"
   headers
      Content-Type:application/hyperlambda
   payload
      .foo
         .:Thomas
         .:John
      for-each:x:@.foo
         // ... etc ...
```

The above will automatically create a Hyperlambda text representation of the specified lambda object,
and transfer that Hyperlambda to the specified URL. Similar things can be achieved with JSON, URL encoded
payloads, and multipart form data payloads. To transmit your payload as URL encoded data, you can use
something such as the following.

```
http.post:"https://foo.com/hyperlambda-endpoint"
   headers
      Content-Type:application/www-form-urlencoded
   payload
      arg1:value1
      arg2:value2
      // ... etc ...
```

You can also have Hyperlambda automatically create a _"multipart/form-data"_ **[payload]** for you. To understand
how, please refer to the [magic.lambda.mime](/documentation/magic.lambda.mime/) project, that explains how to
semantically create a MIME message using Hyperlambda. Then imagine the **[payload]** node being your **[mime.create]**
node, without any Content-Type, having the Content-Type automatically set to _"multipart/form-data"_. This allows you
to simulate a form data submission arguably automating the behaviour of a browser.
If your endpoint _returns_ any of the following content types, you can add a **[convert]** argument
to your invocation to automatically reverse the process, and have Hyperlambda convert the response _to_ a lambda
object.

* __application/json__
* __application/x-json__
* __application/hyperlambda__
* __application/x-hyperlambda__
* __application/www-form-urlencoded__
* __application/x-www-form-urlencoded__

**Notice** - Currently there is no automatic conversion from _"multipart/form-data"_ responses to lambda objects.

## HTTP headers

Passing in your own HTTP headers is also easy. By default Hyperlambda will associate some default
headers with your invocation, specifically the `Accept` header and the `Content-Type` header, depending
upon whether or not your invocation is using a verb requiring a payload or not. The default values for these
headers is _"application/json"_. If you pass in your own **[headers]** collection, Hyperlambda will _not_ add
these headers for you automatically, and you'll have to manually add them if you want them to be associated
with your request. Below is an example of content negotiation, telling the other party that you're only
interested in Hyperlambda being returned to you.

```
http.get:"https://foo.com"
   headers
      Accept:application/hyperlambda
```

You can add any HTTP header you wish, including your own custom headers. However, you cannot add content headers
with a request that doesn't accept content.

## HTTP slots

There are 5 HTTP slots in Hyperlambda wrapping their associated HTTP verbs. These are as follows.

* __[http.get]__ - Returns a resource, no payload
* __[http.delete]__ - Deletes a resource, no payload
* __[http.put]__ - Updates a resource, requires a payload
* __[http.post]__ - Creates a new resource, requires a payload
* __[http.patch]__ - Modifies an existing resource, requires a payload

Of course the exact semantics of what your endpoints are actually doing, differs from API to API - But
the above is the default (and correct) way to think of HTTP verbs. Only the 3 last slots in the list above
can be given a **[payload]** or a **[filename]** argument - And you can only provide _one_ of these arguments.
To further dive into the semantics of invoking HTTP endpoints with Hyperlambda you can check out the
documentation for [magic.lambda.http](/documentation/magic.lambda.http).

* Continue with [Expressions, slots and nodes](/tutorials/expressions-slots-nodes/)

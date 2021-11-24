
# HTTP REST invocations with Hyperlambda

The purpose of Magic and Hyperlambda is to _simplify your life as a developer without compromising scalability, execution speed, or maintainability_.
One example of this is how easy it is to integrate your Hyperlambda backend with other HTTP based services by utilising
the HTTP slots from Hyperlambda. Let's illustrate with some code.

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
no `IDisposable` objects you'll need to remember to dispose, no IoC container wiring, no async/await statements, etc.
By removing the complex parts from your resulting code, maintaining things becomes much easier for both
yourself in the future, in addition to obviously also any junior developers inheriting your project later down the road.

> EVERYTHING is "syntax"

With the above we imply that the less syntax you've got, and the less lines of code you've got, the easier it becomes
to maintain things in the future. Of course, if you compare the above **[http.get]** invocation to the average C#
equivalent, you'll rapidly understand the benefits.

## POSTing, PUTing and PATCHing data

These three HTTP verbs requires a payload of some sort. You can easily pass in any arbitrary payload by simply adding
a **[payload]** node to your invocations, such as the folloing illustrates.

```
http.post:"https://jsonplaceholder.typicode.com/posts"
   convert:true
   payload:@"{""userId"": 1, ""id"": 1}"
```

You can also post files directly, _without_ loading your files into memory first, by replacing your above **[payload]**
argument with a **[filename]** argument, having the value of a relative path within your _"/files/"_ folder, that
is an actual existing file. This has the advantage of simply doing a stream copy, never exhausting your server's memory,
regardless of how large your files are. You can also pass in streams as your **[content]** value in a similar fashion,
and/or as expressions leading to streams, strings, or anything really - Including a byte array.

However, most of the times you want to post something to another endpoint, it's typically JSON you want to post.
Hyperlambda implements a lot of helper slots and features to help you out with this. The code below for instance,
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

## HTTP headers

Passing in your own HTTP headers is also easy. Notice, by default Hyperlambda will associate some default
headers with your invocation, specifically the `Accept` header and the `Content-Type` header, depending
upon whether or not your invocation is using a verb requiring a payload or not. The default values for these
headers is `application/json`. If you pass in your own **[headers]** collection, Hyperlambda will _not_ add
these headers for you automatically, and you'll have to manually add them if you want them to be associated
with your request. Below is an example of content negotiation, telling the other party that you're only
interested in Hyperlambda being returned to you.

```
http.get:"https://foo.com"
   headers
      Accept:application/x-hyperlambda
```

You can add any HTTP header you wish, including your own custom headers using the above syntax.

## Wrapping up

In this article we walked you through how to invoke HTTP endpoints using Hyperlambda. We talked about HTTP headers,
automatic conversion back and forth between lambda objects and JSON, in addition to some additional features of
the HTTP slots in Hyperlambda.

* [Documentation](/documentation/)

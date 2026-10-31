---
title: "Automatic conversion"
description: "Automatic conversion - You can also automatically convert the resulting response object to a lambda object if you have a registered conversion function, and you provide a [convert] argument, and set its value to boole..."
generated: true
---

This page is part of the [magic.lambda.http](/plugins/magic.lambda.http/) documentation.

You can also automatically convert the resulting response object to a lambda object if you have a registered
conversion function, and you provide a **[convert]** argument, and set its value to boolean `true`. Below is an
example.

```
http.get:"https://jsonplaceholder.typicode.com/posts"
   convert:bool:true
```

The above will result in something resembling the following.

```
http.get:int:200
   headers
      Date:"Mon, 29 Nov 2021 06:19:29 GMT"
      Transfer-Encoding:chunked
      Connection:keep-alive
      // ... etc ...
   content
      .
         userId:long:1
         id:long:1
         title:sunt aut facere repellat provident occaecati excepturi optio reprehenderit
         body:qwerty1
      .
         userId:long:1
         id:long:2
         title:qui est esse
         body:qwerty2
      // ... etc ...
```

The project contains automatic conversions for the following types out of the box, but you can easily register
your own C# based conversion types for specific _"Content-Type"_ values.

* `application/json`
* `application/x-json`
* `application/hyperlambda`
* `application/x-hyperlambda`
* `application/www-form-urlencoded`
* `application/x-www-form-urlencoded`
* `multipart/form-data`

You can also convert a semantic lambda object to the correct _request_ content in a similar fashion, by instead
of providing a value to your **[payload]** node provide a lambda object such as illustrated below.

```
.userId:int:1
http.post:"https://jsonplaceholder.typicode.com/posts"
   payload
      id:int:1
      userId:x:@.userId
```

The above will transform your payload to a JSON object automatically for you, and also unwrap any expressions
found in your lambda object before JSON transformation is applied. Automatic transformation will only be applied
if you've got a transformation function registered. If you want to extend the list of supported
content types to automatically transform back and forth to, you can use either `Magic.Http.AddRequestHandler` or
`MagicHttp.AddResponseHandler` to add support for your own automatic transformation for both the request
payload and/or the response content.

**Notice** - The **[payload]** node above must have a _null_ value, otherwise the slot will prioritise the value,
and not attempt to transform from a semantic lambda object in any ways. Values in your **[payload]** will be
transferred as is, and you can provide `byte[]` arrays, streams or strings as the value of your **[payload]**
node.

**Notice** - Both the URL encoded request transformer and the JSON request transformer will automatically
evaluate expressions in your semantic **[payload]** object, but this is _not_ true for the Hyperlambda request
transformer, since in Hyperlambda it might make sense to actually pass in expressions to the endpoint. Below
is an example of how to semantically pass in a Hyperlambda object to some URL.

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

The above will automatically serialize your lambda object as Hyperlambda, since the `Content-Type` is of
a type supported by the automatic conversion functions, and transfer the request as a string to the endpoint,
preserving expressions as is _without_ unwrapping them before transmitting your **[payload]**.

---

[all of magic.lambda.http](/plugins/magic.lambda.http/)


# Invoking HTTP endpoints from Hyperlambda

This project provides HTTP invocation capabilities for Magic and Hyperlambda. More specifically the
project contains the following 5 slots.

* __[http.get]__ - Returns some resource using the HTTP GET verb towards the specified URL
* __[http.delete]__ - Deletes some resource using the HTTP DELETE verb
* __[http.post]__ - Posts some resources to some URL using the HTTP POST verb
* __[http.put]__ - Puts some resources to some URL using the HTTP PUT verb
* __[http.patch]__ - Patches some resources to some URL using the HTTP PATCH verb

The __[http.put]__, __[http.post]__ and __[http.patch]__ slots requires you to provide a __[payload]__
or __[filename]__ argument that will be transferred to the endpoint as is. All 5 endpoints can (optionally)
take a __[token]__ arguments, which will be transferred as a `Bearer Authorization` token to the endpoint
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

## Automatic conversion

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

## Project website

The source code for this repository can be found at [github.com/polterguy/magic.lambda.http](https://github.com/polterguy/magic.lambda.http,
and you can provide feedback, provide bug reports, etc at the same place.

## Quality gates

- ![Build status](https://github.com/polterguy/magic.lambda.http/actions/workflows/build.yaml/badge.svg)
- [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.http&metric=alert_status)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.http)
- [![Bugs](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.http&metric=bugs)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.http)
- [![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.http&metric=code_smells)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.http)
- [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.http&metric=coverage)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.http)
- [![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.http&metric=duplicated_lines_density)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.http)
- [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.http&metric=ncloc)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.http)
- [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.http&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.http)
- [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.http&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.http)
- [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.http&metric=security_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.http)
- [![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.http&metric=sqale_index)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.http)
- [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.http&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.http)

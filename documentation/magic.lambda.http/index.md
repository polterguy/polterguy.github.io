
# Magic Lambda HTTP

Provides HTTP REST capabilities for Magic. More specifically this project provides the following 4 slots.

* __[http.get]__ - Returns some resource using the HTTP GET verb towards the specified URL
* __[http.delete]__ - Deletes some resource using the HTTP DELETE verb
* __[http.post]__ - Posts some resources to some URL using the HTTP POST verb
* __[http.put]__ - Puts some resources to some URL using the HTTP PUT verb
* __[http.patch]__ - Patches some resources to some URL using the HTTP PATCH verb

The __[http.put]__, __[http.post]__ and __[http.patch]__ slots requires you to provide a __[payload]__
or __[filename]__ argument that will be transferred to the endpoint as is. All 4 endpoints can (optionally)
take a __[token]__ arguments, which will be transferred as a `Bearer Authorization` token to the endpoint
in the HTTP Authorization header of your request. If you provide a __[filename]__ argument, this is assumed
to be a file relatively existing within your _"/files/"_ folder somewhere.

Notice, if you want to have more control over your HTTP request, you can also explicitly add your own
**[headers]** collection, which will become the HTTP request's headers, where the header name is the name
of the node, and its value is the value of the node. Below is a simple example of retrieving the document
found at the specified URL, using a simple GET HTTP request, without neither a **[token]** nor **[header]**
collection.

```
http.get:"https://google.com"
```

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

You can also supply a lambda object to your endpoint directly instead of JSON, which will by default
transform your lambda object to JSON before it is sent to the endpoint. Below is an example of the latter.

```
http.post:"https://jsonplaceholder.typicode.com/posts"
   payload
      userId:int:1
      id:int:1
```

**Notice** - If you pass in a lambda object as illustrated above, then all expressions in all nodes inside
of your **[payload]** argument will be automatically evaluated and _"unwrapped"_. Consider the following.

```
.userId:int:1
http.post:"https://jsonplaceholder.typicode.com/posts"
   payload
      userId:x:@.userId
      id:int:1
```

The above will evaluate the `:x:@.userId` expression, resulting in the integer value of 1, before the lambda
object is converted to JSON. If you want to actually pass in expressions as JSON values, you have to pass
these in as strings.

## HTTP headers

Below is another example invoking DELETE with an explicit **[headers]** collection.

```
http.delete:"https://foo-url.com"
   headers
      Accept:application/zip
      X-Foo:Bar-Header-Value
```

## Project website

The source code for this repository can be found at [github.com/polterguy/magic.lambda.http](https://github.com/polterguy/magic.lambda.http,
and you can provide feedback, provide bug reports, etc at the same place.

## Quality gates

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

## License

This project is the copyright(c) 2020-2021 of Thomas Hansen thomas@servergardens.com, and is licensed under the terms
of the LGPL version 3, as published by the Free Software Foundation. See the enclosed LICENSE file for details.

* [Magic Documentation](https://polterguy.github.io/)

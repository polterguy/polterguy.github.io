
# magic.endpoint - How Hyperlambda endpoints are resolved

magic.endpoint is a dynamic endpoint URL controller, allowing you to declare endpoints that are dynamically
resolved using your `IHttpExecutorAsync` service implementation. The default implementation of this interface,
is the class called `HttpExecutorAsync`, and the rest of this file will be focused on documenting this
implementation, since it is the default service implementation for magic.endpoint - Although, technically, you
could exchange this with your own implementation if you wish, completely changing the behaviour of the library
if you wish to for instance resolve endpoints to Python, Ruby, or any other dynamic programming language
implementation, and you have some means to execute such code from within a .Net 6 environment.
The resolver will be invoked for all relative URLs starting with _"magic/"_, for the following verbs.

* `GET`
* `POST`
* `PUT`
* `DELETE`
* `PATCH`

The default service implementation will resolve everything after the _"magic/"_ parts in the
given URL, to a Hyperlambda file assumed to be found relatively beneath your _"/files/"_ folder -
Although, exactly where you physically put your files on disc, can be configured
through your _"appsettings.json"_ file. The HTTP verb is assumed to be the last parts of your
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
so by default there is no way to get static files, unless you create a Hyperlambda endpoint that returns
a static file somehow.

The default resolver will only allow the client to resolve files inside your _"/files/modules/"_
folder and _"/files/system/"_ folder. This allows you to safely keep files that parts of your system
relies upon inside your dynamic _"/files/"_ folder, without accidentally creating endpoints clients can
resolve, resulting in breaches in your security. Only characters a-z, 0-9 and '-', '\_' and '/' are legal
characters for the resolvers, and only lowercase characters to avoid file system incompatibilities between
Linux and Windows. There is _one exception_ to this rule though, which is that the resolver will resolve
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

## Hyperlambda endpoints and arguments

The default `IHttpExecutorAsync` implementation can explicitly declare what arguments the file can
legally accept, and if an argument is given during invocation that the file doesn't allow for, an
exception will be thrown and the file will never be executed. This allows you to declare what
arguments your Hyperlambda file can accept, and avoid having anything _but_ arguments explicitly
declared in your Hyperlambda file from being sent into your endpoint during invocation of your
HTTP endpoint. An example Hyperlambda file taking two arguments can be found below.

```
.arguments
   arg1:string
   arg2:int

strings.concat
   get-value:x:@.arguments/*/arg1
   .:" - "
   get-value:x:@.arguments/*/arg2

unwrap:x:+/*
return
   result:x:@strings.concat
```

If you save this file on disc as `/files/modules/tutorials/foo2.get.hl`, you can invoke it as follows
using the HTTP GET verb - Assuming your backend is running on localhost at port 5000.

```
http://localhost:5000/magic/modules/tutorials/foo2?arg1=howdy&arg2=5
```

JSON payloads and form URL encoded payloads are automatically converted to lambda/nodes -
And query parameters are treated indiscriminately the same way as JSON payloads -
Except of course, query parameters cannot pass in complex graph objects, but only
simply key/value arguments. Only POST, PUT and PATCH endpoints can handle payloads. If you
supply a payload to a GET or DELETE endpoint, an exception will be thrown, and an error
returned to the caller.

To allow for _any_ arguments to your files, simply _ommit_ the **[.arguments]** node
in your Hyperlambda althogether, or supply an **[.arguments]** node and set its value to `*`.
Alternatively, you can also _partially_ ignore arguments sanity checking of individual nodes,
by setting their values to `*`, such as the following illustrates.

```
.arguments
   arg1:string
   arg2:date
   arg3:*
```

In the above arguments declaration, **[arg1]** and **[arg2]** will be sanity checked, and input converted
to `string` or `date` (DateTime) - But the **[arg3]** parts will be completely ignored, allowing the caller
to invoke it with _anything_ as `arg3` during invocation - Including complete graph JSON objects, assuming
the above declaration is for a `PUT`, `POST` or `PATCH` Hyperlambda file. The '\*' value for an argument also turn
off all conversion, implying everything will be given to your lambda object with the JSON type the argument
was passed in as.
All arguments declared are considered optional, and the file will still resolve if the argument is not given,
except of course the argument won't exist in the **[.arguments]** node. However, no argument _not_ found
in your **[.arguments]** declaration can be provided during invocations, assuming you choose to declare
an **[.arguments]** collection in your Hyperlambda endpoint file, and you don't set its value to `*`.

To declare what type your arguments can be, set the value of the argument declaration node to
the Hyperlambda type value inside of your arguments declaration, such as illustrated above.
Arguments will be converted if possible, to the type declaration in your argument's declaration.
If no conversion is possible, an exception will be thrown.
Although the sanity check will check graph objects, passed in as JSON payloads, it has its restrictions,
such as not being able to sanity check complex objects passed in as arrays, etc. If you need stronger
sanity checking of your arguments, you will have to manually check your more complex graph objects
yourself in your own Hyperlambda files.

Also realise that if the value originates from a payload, as in from a PUT, PATCH or POST JSON object
for instance, these types of objects might contain null values. If they do, no conversion will be attempted,
and internally within your endpoint's Hyperlambda code, you might therefor expect to see for instance
`long` values being in fact _null_, even though technically these are not nullable types in .Net.

## Accepted Content-Type values for Hyperlambda endpoints

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

### Extending the Hyperlambda Content-Type request and response resolver

The Content-Type resolver/parser is extendible, allowing you to change its behaviour by providing
your own callback that will be invoked for some specific Content-Type value provided. This is useful
if you want to be able to for instance handle _"text/xml"_ or _"text/csv"_ types of request/response
objects, and intelligently and automatically create an argument collection from it. Below is example
code illustrating how to create your own HTTP request resolver for the MIME type of _"application/x-foo"_.

```
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

```
EndpointController.RegisterContentType("application/x-foo", (response) =>
{
   /* ... Return some sort of IActionResult here ... */
   return new ObjectResult(response.Content) { StatusCode = response.Result };
});
```

The above method should also exclusively be used during startup, and not later,
since it is _not_ thread safe. The above method assumes you register your Content-Type handlers
as your application is starting.

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

## Slots related to endpoints and the HTTP context

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
* __[mime.add]__ - Associates a file extension with a MIME type

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

### Hyperlambda and cookies

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

### How to use [mime.add]

This slots associates a file extension with a MIME type. Notice, it will override previous associations if existing.
Example usage can be found below.

```
mime.add:py
   .:application/python
```

Then later when the endpoint resolver is returning files ending with _".py"_, it will return these with
a `Content-Type` of _"application/python"_.

## Hyperlambda code behind files

The resolver will resolve anything not starting out with `/magic/` as a static file, optionally applied
as a mixin file having a Hyperlambda code behind file for mixing in dynamic content with any _".html"_
files. This allows you to render HTML, CSS, JavaScript and _"whatever"_, with the ability to dynamically
render parts of your HTML files using Hyperlambda. This logic relies upon the **[io.file.mixin]** slot
from the _"magic.lambda.io"_ project. If you create two files such as follows and put both of these
files in your _"/etc/www/"_ folder, you can see this logic in action.

**index.html**

```
<html>
    <head>
        <title>Hell world</title>
    </head>
    <body>
        <h1>Hello world</h1>
        <p>
           Hello there Thomas Hansen, {{*/.calculate}}
        </p>
    </body>
</html>
```

**index.hl**

```
.calculate
   math.add
      .:int:2
      .:int:2
   return:x:-
```

The above will substitute your `{{*/.calculate}}` parts with the result of invoking your **[.calculate]** lambda
object, resulting in 4. To understand how this works, you need to read about the **[io.file.mixin]** slot in
the _"magic.lambda.io"_ project, and realise that the above will actually transform to the following as the
mixin logic is executed.

```
io.file.mixin:/etc/www/index.html
   .calculate
      math.add
         .:int:2
         .:int:2
      return:x:-
```

This allows you to serve dynamically rendered HTML files, where parts of your HTML is substituted with the
result of invoking some lambda object. If you have an HTML file _without_ a Hyperlambda code behind file,
it will be served as a static file. CSS files, JavaScript files, and images will also be served as static
files.

Notice, interceptor files will be executed as normally, allowing you to apply interceptor files similarly
to how you apply these with your _"/magic/"_ endpoints. In addition, any file called _"default.html"_ having
a Hyperlambda counterpart will be used for default URL resolving if no explicit URL is found, allowing
you to handle dynamica URLs with this file.

## Project website for magic.endpoint

The source code for this repository can be found at [github.com/polterguy/magic.endpoint](https://github.com/polterguy/magic.endpoint), and you can provide feedback, provide bug reports, etc at the same place.

- ![Build status](https://github.com/polterguy/magic.endpoint/actions/workflows/build.yaml/badge.svg)
- [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.endpoint&metric=alert_status)](https://sonarcloud.io/dashboard?id=polterguy_magic.endpoint)
- [![Bugs](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.endpoint&metric=bugs)](https://sonarcloud.io/dashboard?id=polterguy_magic.endpoint)
- [![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.endpoint&metric=code_smells)](https://sonarcloud.io/dashboard?id=polterguy_magic.endpoint)
- [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.endpoint&metric=coverage)](https://sonarcloud.io/dashboard?id=polterguy_magic.endpoint)
- [![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.endpoint&metric=duplicated_lines_density)](https://sonarcloud.io/dashboard?id=polterguy_magic.endpoint)
- [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.endpoint&metric=ncloc)](https://sonarcloud.io/dashboard?id=polterguy_magic.endpoint)
- [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.endpoint&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.endpoint)
- [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.endpoint&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.endpoint)
- [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.endpoint&metric=security_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.endpoint)
- [![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.endpoint&metric=sqale_index)](https://sonarcloud.io/dashboard?id=polterguy_magic.endpoint)
- [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.endpoint&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=polterguy_magic.endpoint)

## Copyright and maintenance

The projects is copyright of Aista, Ltd 2021 - 2023, and professionally maintained by [AINIRO your friendly ChatGPT website chatbot vendor](https://ainiro.io).

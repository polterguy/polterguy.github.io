---
title: Hyperlambda Hello World
description: This article helps you to manually create a Hello World type of Hyperlambda app, and gives you an understanding of the basics of Hyperlambda, and how it allows for you to create more with less.
---

# Hyperlambda Hello World

In this tutorial we will cover the following parts of Magic and Hyperlambda.

* Creating an HTTP GET and an HTTP POST Hyperlambda endpoint
* How to use Hyper IDE to create Hyperlambda files
* How the endpoint resolver in Magic matches your URL to Hyperlambda files

Creating a Hyperlambda endpoint in Magic is easy. Use your Magic dashboard and open _"Hyper IDE"_. Select
your _"modules"_ folder and create a new folder inside of it. Name your new folder _"tutorials"_. Select your
newly created folder and create a file named _"hello.get.hl"_.  To create a file or folder in Magic use the
_"Add"_ button in the top/right corner of Hyper IDE, and click the checkbox if you want to create a folder,
otherwise if you want to create a file keep it unchecked. Then provide Magic with the name of your file or
folder in the _"Name"_ textbox. Below is a screenshot illustrating how to create our _"hello.get.hl"_ file.

![Creating a Hyperlambda file in Hyper IDE](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/hyper-ide-create-endpoint.jpg)

When you have clicked the _"Create"_ button, put the following content into your file and click the _"Save"_
button.

```
return-nodes
   result:Hello World
```

You have now created your first Hyperlambda endpoint, and you can already invoke it using the [following
URL](http://localhost:4444/magic/modules/tutorials/hello). Make sure you get the port correctly. 4444 is
the correct port if you're using the docker images, and might need to be changed to e.g. 5000 if you're
using the source code version of Magic. Notice how Magic automatically transforms your lambda object to
JSON, and returns it as follows.

```json
{"result":"Hello World"}
```

## Adding arguments

No hello world tutorial is complete without the ability to provide your name as input. Modify the file
and replace its existing content with the following Hyperlambda.

```
.arguments
   name:string

strings.concat
   .:"Hello "
   get-value:x:@.arguments/*/name

unwrap:x:+/*
return-nodes
   result:x:@strings.concat
```

Save the file, an invoke the [following relative URL](http://localhost:4444/magic/modules/tutorials/hello?name=thomas)
using your browser - _"/magic/modules/tutorials/hello?name=thomas"_. The result should resemble the following.

```json
{"result":"Hello thomas"}
```

### Internals

Magic will map your `name` query parameter automatically to the **[.arguments]**/**[name]** node's value,
and from within your Hyperlambda code this value will be concatenated with the text _"Hello"_, and returned
back to your browser as JSON. There are two new slots being used in this code.

* __[strings.concat]__ - Concatenates two or more strings
* __[unwrap]__ - Forward evaluates expressions

For details about how these two slots works, check out the documentation to [magic.lambda.strings](/documentation/magic.lambda.strings)
and [magic.lambda](/documentation/magic.lambda/) respectively.

## The endpoint resolver

Magic will automatically resolve your file to the HTTP GET verb. The reason for this, is because your file
ends with _".get.hl"_. Its `get` parts indicate the HTTP verb, and its `hl` parts indicates Hyperlambda.
You can also create POST, PUT, PATCH and DELETE endpoints, by simply replacing the _".get."_ parts of
your filename with _".xxx."_ where xxx is your verb of choice. If you do this, you can no longer
use your browser to test the endpoint, but need to open up the _"Endpoints"_ file menu to test your
endpoint(s), and provide payloads and arguments to them. You can also use e.g. Postman to invoke such
endpoints. For details about how endpoints are resolved, check out the documentation for the [magic.endpoint](/documentation/magic.endpoint/) project.

**Notice** - You can _only_ create endpoints inside of your _"modules"_ folder. This allows you to
create helper Hyperlambda files _outside_ of this folder that can never be resolved by clients trying
to create malicious URLs to execute hidden code on your server.

## Creating a POST endpoint

Create a new file in your tutorials folder, and name your file _"hello.post.hl"_. Put the same content
into your post file as you have in your get.

```
.arguments
   name:string

strings.concat
   .:"Hello "
   get-value:x:@.arguments/*/name

unwrap:x:+/*
return-nodes
   result:x:@strings.concat
```

This time though, we cannot invoke the file as a simple GET URL HTTP invocation, but must rely upon the endpoints
menu item in Magic to invoke our file. Open up your _"Endpoints"_ menu item, and filter for _"hello"_. Notice how
you have _two_ endpoints, one resolved using the `GET` verb and another resolved using the `POST` verb. Expand the
post endpoint, and paste the following into its payload parts.

```json
{
  "name": "John Doe"
}
```

Invoke the endpoint, and notice how we get a similar type of result back as our GET endpoint above. If you want
to see the internals of what is happening, you can use Chrome Developer tools to _"inspect"_ your HTTP requests
as you click the _"Invoke"_ button - At which point you can see how an HTTP POST invocation is created instead of
an HTTP GET invocation.
You can repeat the same exercise for PUT, DELETE and PATCH if you wish - However, both GET and DELETE endpoints
can only be given arguments as query parameters - While POST, PUT and PATCH endpoints requires JSON payloads.
You can also create alternative endpoint types, returning for instance files and similar constructs instead of
pure JSON, but that's an exercise for later.

## Commenting your code

Hyperlambda accepts comments the same way C# or C++ do. To provide an example, let's finish our
little tutorial by adding some comments to our above endpoint.

```
// Declaring arguments for your endpoint.
.arguments
   name:string

/*
 * Concatenating specified [name] with a greeting.
 */
strings.concat
   .:"Hello "
   get-value:x:@.arguments/*/name

/*
 * Forward evaluating the [result] node below,
 * and returning it to caller as JSON.
 */
unwrap:x:+/*
return-nodes
   result:x:@strings.concat
```

* Continue with [Invoking HTTP endpoints from Hyperlambda](/tutorials/http-rest/)

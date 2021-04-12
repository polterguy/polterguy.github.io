
# Hyperlambda Hello World

Creating a Hyperlambda endpoint is extremely easy. Use your Magic dashboard and go to the _"Files"_
menu item. Open up your _"modules"_ folder, and create a folder named _"tutorials"_. Open this folder
and create a file named _"hello.get.hl"_. Put the following content into your file.

```
return-nodes
   result:Hello World
```

Save the file, and open up [http://localhost:4444/magic/modules/tutorials/hello](http://localhost:4444/magic/modules/tutorials/hello)
using your browser. Make sure you get the port correctly. 4444 is if you're using the Docker images,
and might need to be changed to e.g. 55247 if you're using the source code version directly.

Congratulations, you have now created your first Hyperlambda HTTP endpoint. Notice how Magic automatically
transforms your lambda object to JSON, and returns it as follows.

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

Save the file, an invoke the following relative URL using your browser - `/magic/modules/tutorials/hello?name=thomas`.

The result should resemble the following.

```json
{"result":"Hello thomas"}
```

### Internals

Magic will map your `name` query parameter automatically to the **[.arguments]**/**[name]** node's value,
and from within your Hyperlambda code, this value will be concatenated with the text _"Hello"_, and returned
back to your browser as JSON. There are two new slots being used in this code.

* __[strings.concat]__ - Concatenates two or more strings
* __[unwrap]__ - Forward evaluates expressions

For details about how these two slots works, check out the documentation to magic.lambda.strings
and magic.lambda respectively.

## The endpoint resolver

Magic will automatically resolve your file to the HTTP GET verb. The reason for this, is because your file
ends with _".get.hl"_. Its `get` parts indicate the HTTP verb, and its `hl` parts indicates Hyperlambda.
You can also create POST, PUT, PATCH and DELETE endpoints, by simply replacing the _".get."_ parts of
your filename with _".xxx."_ where xxx is your verb of choice. If you do this, you can no longer
use your browser to test the endpoint, but need to open up the _"Endpoints"_ file menu to test your
endpoint(s), and provide payloads and arguments to them. For details about how endpoints are resolved,
check out the documentation for the magic.endpoint project.

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
pure JSON - But that's an exercise for later.

## Documenting your code

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

* [Documentation](/documentation/)

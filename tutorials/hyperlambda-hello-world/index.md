# Hyperlambda Hello World

The word _"Hyperlambda"_ originates from _"hyper"_ and _"lambda"_, implying _"web functions"_.
In order to understand Hyperlambda's usefulness, it is therefor valuable to use Hyperlambda to create
an HTTP REST endpoint, or a _"web function"_.

To create an HTTP REST endpoint, we will need to create a Hyperlambda file. Use for instance
the _"Files"_ menu item in the Magic Dashboard, and open up the folder called _"modules"_.
Create a new folder inside of this folder, and name your new folder _"tutorials"_.

**Notice** - By default Magic will protect files inside of the modules folder, so you'll
have to explicitly click the _"Safe mode"_ slider to be allowed to create files and
folders here. See the screenshot below.

![Creating a new tutorials folder](https://servergardens.files.wordpress.com/2020/09/create-folder.png)

Then open this folder, and create a new Hyperlambda file and name it _exactly_ as follows.
Its name _is_ important.

```
hello-world.get.hl
```

Then click the file to edit it, and replace its default content with the following Hyperlambda.

```
return
   result:Hello World from Hyperlambda
```

Save the file, and open up the _"Endpoints"_ dashboard link, in for instance a different tab
in your browser. Click the _"Show endpoints"_ slider, and filter for _"hello-world"_ if this
gives you a lot of files. Click the endpoint, at which point you'll see something such
as the following.

![How your Hello World endpoint will look like](https://servergardens.files.wordpress.com/2020/09/invoke-endpoint.png)

Then click the _"get"_ button. This will invoke the endpoint, and give you the following result.

```json
{
   "result": "Hello World from Hyperlambda"
}
```

## Gory details

Remember the filename we used for our endpoint, which was _"hello-world.get.hl"_. The first
parts of the filename, before the _".get.hl"_ parts becomes it relative URL. Since we placed
the file inside of our _"modules/tutorials/"_ folder, its complete URL becomes
_"magic/modules/tutorials/hello-world"_. If you're using Magic from your development machine
on localhost, you can use
[the following URL to invoke your endpoint](http://localhost:55247/magic/modules/tutorials/hello-world).

The first parts of its extension, the _"get"_ parts, declares that our file is an HTTP GET
endpoint, which we can invoke using the GET verb.

The last parts, the _".hl"_ parts, simply declares that this is a Hyperlambda file,
making the Hyperlambda parser kick in and transform it to a lambda object, which then
is evaluated, and whatever the file returns, is afterwards transformed to JSON, which
again is returned to the client as its HTTP response object.

You can use the following verbs for your Hyperlambda files, as an extension before the
.hl parts.

* get
* post
* put
* delete

This allows you to easily create an HTTP endpoint, wrapping your HTTP verb, controlling
its URL in the process.

## Creating an echo service

Create a new file called _"echo.post.hl"_ in the same folder, and put the following
Hyperlambda into it.

```
add:x:../*/return
   get-nodes:x:@.arguments/*
return
```

Then go back to your _"Endpoints"_ menu item, filter for _"echo"_, click it, and paste in
the following payload into your file.

```json
{
  "name": "Thomas Hansen",
  "age": 77
}
```

When you click the _"post"_ button, the endpoint returns the exact same payload as it
was given.

Congratulations, you have now created an endpoint that can accept arguments. The way
this works, is that any arguments passed into your endpoint, will end up inside of
an **[.arguments]** node, inside of your lambda, as it is being executed. So your
lambda will actually look like the following when it's executed, due to its arguments collection
being passed into it.

```
.arguments
   name:Thomas Hansen
   age:long:77
add:x:../*/return
   get-nodes:x:@.arguments/*
return
```

Of course, the above **[.arguments]** node, will contain whatever you pas into it,
allowing you to pass in _any_ argument you wish. Try modifying the file to see
this process, and change your _"echo"_ file's content to the following.

```
lambda2hyper:x:../*
log.info:x:-
add:x:../*/return
   get-nodes:x:@.arguments/*
return
```

Execute your endpoint, and go to your _"Logs"_ menu item, in your dashboard, and click
the top item - At which point you'll see something like the following.

![Log item result](https://servergardens.files.wordpress.com/2020/09/echo-log-item.png)

As you can see, we were able to successfully transform the entire lambda object, as it
was being executed, into a string - For the to store this string into our log. And as
we did, we could clearly see the **[.arguments]** collection, that wasn't a part of
our original Hyperlambda, but rather dynamically injected into the lambda object as
arguments, after it had been parsed by the Hyperlambda parser. You can of course
pass in any JSON object you wish to this endpoint, try the following JSON as your
payload to understand how JSON is transformed into a lambda object during invocation.

```json
{
  "name": "Thomas Hansen",
  "age": 77,
  "addresses": [
     {
        "address": "Foo bar st 77",
        "zip": "98765",
        "state": "California",
        "type": "residence"
     },
     {
        "address": "Howdy Street 67",
        "zip": "12345",
        "state": "Greece",
        "type": "vacation-residence"
     }
  ]
}
```

Then refresh your log, and click on the last log item to see its details. This will
result in something resembling the following.

```
.arguments
   name:Thomas Hansen
   age:long:77
   addresses
      .
         address:Foo bar st 77
         zip:98765
         state:California
         type:residence
      .
         address:Howdy Street 67
         zip:12345
         state:Greece
         type:vacation-residence
lambda2hyper:x:../*
log.info:x:-
add:x:../*/return
   get-nodes:x:@.arguments/*
return
```

So obviously, the entire payload is transformed from JSON to lambda, and passed into your
endpoint's execution, as an **[.argument]** node.

### Restricting arguments

If you want to, you can explicitly declare what arguments your endpoint can handle,
by creating a declaration **[.arguments]** node, in your Hyperlambda, such as the
following illustrates.

```
.arguments
   name:string
   age:long
add:x:../*/return
   get-nodes:x:@.arguments/*
return
```

If you save the above Hyperlambda into some file called e.g. _"explicit-arguments.get.hl"_,
and you refresh your _"Endpoints"_, and select the new endpoint - You will see that the
endpoint evaluator automatically determines that this endpoint can (optionally) handle
arguments, what the argument names are, and what their types are. See screenshot below
for how this should look like.

![Passing in arguments to Hyperlambda endpoints](https://servergardens.files.wordpress.com/2020/09/explicit-arguments.png)

You can now add arguments to your file, by for instance pasting the following into
your query parameters.

```
name=Thomas&age=25
```

If you invoke the endpoint now, you'll end up with the following result.

```json
{
  "name": "Thomas",
  "age": 25
}
```

If you try to invoke it with a _"foo"_ argument however, such as the following illustrates,
the endpoint will throw an exception.

![Invoking endpoint with unknown argument](https://servergardens.files.wordpress.com/2020/09/argument-exception.png)

The Hyperlambda evaluator doesn't really discriminate between JSON payload arguments,
and QUERY parameters. From your Hyperlambda file, an argument is an argument - Period!

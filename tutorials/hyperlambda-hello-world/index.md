# Hyperlambda Hello World

The word _"Hyperlambda"_ originates from _"hyper"_ and _"lambda"_, implying _"web functions"_.
In order to understand Hyperlambda's usefulness, it is therefor valuable to use Hyperlambda to create
an HTTP REST endpoint. Notice, if you prefer to watch video tutorials, here's a video where I walk
you through everything.

<div style="position:relative; padding-bottom:56.25%; padding-top:30px; height:0; overflow:hidden;margin-top:4rem;margin-bottom:4rem;">
<iframe width="560" height="315" style="position:absolute; top:0; left:0; width:100%; height:100%;" src="https://www.youtube.com/embed/5CRhCpxM8Ho" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>


To create an endpoint, we will need
to create a Hyperlambda file. Use for instance the _"Files"_ menu item in the Magic Dashboard,
and open up the folder called _"modules"_. Create a new folder inside of this folder, and
name your new folder _"tutorials"_.

**Notice** - By default Magic will protect files inside of the modules folder, so you'll
have to explicitly click the _"Safe mode"_ slider to be allowed to create files and
folders here. See the screenshot below.

![Creating a new tutorials folder](https://servergardens.files.wordpress.com/2020/09/create-folder.png)

Open this folder, and create a new Hyperlambda file and name it _exactly_ as follows.
Its name _is_ important.

```
hello-world.get.hl
```

Click the file to edit it, and replace its default content with the following code.

```
return
   result:Hello World from Hyperlambda
```

Save the file, and open up the _"Endpoints"_ dashboard link. Click the _"Show endpoints"_ slider,
and click the endpoint named _"hello-world"_, at which point you'll see something resembling
the following.

![How your Hello World endpoint will look like](https://servergardens.files.wordpress.com/2020/09/hello-world-endpoint.png)

Click the _"get"_ button. This will invoke the endpoint, and give you the following result.

```json
{
   "result": "Hello World from Hyperlambda"
}
```

## Explanation

The first parts of the filename, the _"hello-world"_ parts, becomes it relative URL.
Since we placed the file inside of our _"modules/tutorials/"_ folder, its relative URL
becomes _"magic/modules/tutorials/hello-world"_. The initial _"magic/"_ parts of your
endpoint's URL, informs Magic that this is a dynamic endpoint, and will resolve to a
Hyperlambda file inside your _"backend/files/"_ folder. If you're using Magic from
your development machine on localhost, you can use
[the following URL to invoke your endpoint](http://localhost:55247/magic/modules/tutorials/hello-world).

The first parts of the file extension, the _"get"_ parts, declares that our file is an HTTP GET
endpoint, which we can invoke using the GET verb. The last parts, the _".hl"_ extension,
declares that this is a Hyperlambda file, making the Hyperlambda parser kick in and transform
it to a lambda object. The lambda object is then evaluated, and whatever it returns, is
transformed to JSON, which becomes the HTTP response.
You can use the following verbs for your Hyperlambda files as an extension before the
.hl parts.

* get
* post
* put
* delete

This allows you to easily create an HTTP endpoint, wrapping your HTTP verb, controlling
its URL in the process. Magic will treat your Hyperlambda files as if they were _"functions"_,
and use your file extension to figure out what HTTP verb to use to resolve it.

## Creating an echo service

Create a new file called _"echo.post.hl"_ in the same folder, and put the following
Hyperlambda into it.

```
add:x:../*/return
   get-nodes:x:@.arguments/*
return
```

Then go back to your _"Endpoints"_ menu item, find your _"echo"_ endpoint, click it,
and invoke it with the following JSON payload.

```json
{
  "name": "Thomas Hansen",
  "age": 77
}
```

When you click the _"post"_ button, the endpoint returns the exact same payload as it
was given. The way this works, is that any arguments passed into your endpoint, will
end up inside of an **[.arguments]** node, inside of your lambda, as it is being executed.
So your lambda will actually look like the following when it's executed, due to its
arguments collection being passed into it.

```
.arguments
   name:Thomas Hansen
   age:long:77
add:x:../*/return
   get-nodes:x:@.arguments/*
return
```

Of course, the above **[.arguments]** node, will contain whatever you pass into it,
allowing you to pass in _any_ argument you wish. Try modifying the file to see
this process, and change your _"echo"_ file's content to the following.

```
lambda2hyper:x:../*
log.info:x:-
add:x:../*/return
   get-nodes:x:@.arguments/*
return
```

Execute your endpoint, and go to your _"Logs"_ menu item in your dashboard, and click
the top item - At which point you'll see something like the following.

![Log item result](https://servergardens.files.wordpress.com/2020/09/echo-log-item.png)

As you can see, we were able to successfully transform the entire lambda object into
a string, as it was being executed - For then to put this string into our log. And as
we did, we could clearly see the **[.arguments]** collection, that wasn't a part of
our original Hyperlambda, but rather dynamically injected into the lambda object as
arguments. You can of course pass in any JSON object you wish to this endpoint. Try
the following JSON as your payload to understand how JSON is transformed into a lambda
object during invocation.

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

So obviously, the entire payload is transformed from JSON to lambda, and sent into your
endpoint as an **[.arguments]** node. The `.` parts above, implies that `addresses` is an array,
and each `.` is an entry in the array.

### Restricting arguments

You can also explicitly declare what arguments your endpoint can handle,
by creating a declaration **[.arguments]** node in your Hyperlambda, such as the
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
endpoint evaluator automatically determines that this endpoint can handle
arguments, what the argument names are, and what their types are. See screenshot below
for how this should look like.

![Passing in arguments to Hyperlambda endpoints](https://servergardens.files.wordpress.com/2020/09/explicit-arguments.png)

You can now add arguments to your HTTP endpoint, by for instance
pasting the following into your query parameters textbox.

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

If you try to invoke the endpoint with a _"foo"_ argument however, such as the
following illustrates, the endpoint will return an error.

![Invoking endpoint with unknown argument](https://servergardens.files.wordpress.com/2020/09/argument-exception.png)

The Hyperlambda evaluator doesn't really discriminate between JSON payload arguments,
and QUERY parameters. From your Hyperlambda file, an argument is an argument - Period.
But if you try to pass in an argument that the endpoint doesn't allow for, the
file will never be executed for security reasons.

## Selecting data from your database

**Notice** - This Hyperlambda assumes you've somehow got the _"Sakila"_ database from
MySQL installed. If you don't, you can exchange the _"sakila"_ parts below with
an existing database you've got somewhere, and modify the SQL to become valid SQL,
towards that database. Just make sure you restrict the number of records you
select, in case you have thousands of records in your table, to avoid having
to wait a long time for the result to show up.
If you're not using MySQL, you'll also have to exchange the above **[mysql.]** parts
with for instance **[mssql.]** to retrieve data from a Microsoft SQL Server installation.

Create a new file in your _"Files"_ menu, inside your _"/modules/tutorials/"_ folder,
and name it _"read-data.get.hl"_. Put the following content into your file.

```
mysql.connect:sakila
   mysql.select:select * from actor limit 10
   return:x:-/*
```

Go to your _"Endpoints"_ menu item, and refresh it if necessary, for then to
choose the _"read-data"_ endpoint, and click _"get"_. At which point you'll
see something resembling the following.

```json
[
  {
    "actor_id": 1,
    "first_name": "PENELOPE",
    "last_name": "GUINESS",
    "last_update": "2006-02-15T02:34:33.000Z"
  },
  {
    "actor_id": 2,
    "first_name": "NICK",
    "last_name": "WAHLBERG",
    "last_update": "2006-02-15T02:34:33.000Z"
  }
```

### Parametrizing your SQL

By combining the above endpoint with arguments, we can easily parametrize
our SQL, to allow for things such as paging, filtering, sorting, etc. Modify your
existing _"read-data.get.hl"_ file, and put the following code into it.

```
.arguments
   limit:long
   offset:long
mysql.connect:sakila
   mysql.select:select * from actor limit @limit offset @offset
      @limit:x:@.arguments/*/limit
      @offset:x:@.arguments/*/offset
   return:x:-/*
```

Then try invoking the endpoint, but this time with the following arguments.
![Paging your result](https://servergardens.files.wordpress.com/2020/09/sql-read-with-offset.png)

### Authorization

Put the following line of code at the top of your file, just beneath its **[.arguments]** node.

```
auth.ticket.verify:root, admin
```

You have now secured access to this endpoint, such that _only_ users belonging
to the _"root"_ or _"admin"_ roles can invoke it. The above value is a comma separated list
of roles, allowing a user to access the endpoint, if he or she belongs
to _any_ of the roles listed. All other users will be denied access. The
complete code we ended up with can be found below.

```
.arguments
   limit:long
   offset:long
auth.ticket.verify:root, admin
mysql.connect:sakila
   mysql.select:select * from actor limit @limit offset @offset
      @limit:x:@.arguments/*/limit
      @offset:x:@.arguments/*/offset
   return:x:-/*
```

You can also add comments to the file, to make it more
readable. Hyperlambda accepts both multiline and
single line comments, but you _cannot_ put a comment on any line where
you have Hyperlambda code. The **[.description]**
node below, adds meta data to your endpoint, which gives it
a humanly readable descriptive text. The meta data generator
will return this when meta data is requested. Below is our file
from above, but this time with a meta description node, in
addition to some comments.

```
/*
 * This file selects items from your Sakila actor
 * database table, and returns them to the client
 * as JSON.
 */
.description:Returns actors from your Sakila database

// Arguments this endpoint can handle
.arguments
   limit:long
   offset:long

// Making sure only root and admin users can access the endpoint
auth.ticket.verify:root, admin

// Connecting to our database
mysql.connect:sakila

   // Selecting items from our database
   mysql.select:select * from actor limit @limit offset @offset
      @limit:x:@.arguments/*/limit
      @offset:x:@.arguments/*/offset

   // Returning the results of the above select statement
   return:x:-/*
```

**Notice** - You can of course use your favourite IDE or text editor
to edit your Hyperlambda, but the Dashboard's Hyperlambda editor
happens to have very good Hyperlambda support, such as auto
completion, syntax highlightning, etc - So it's probably
easier to use the Dashboard Hyperlambda editor.

* [Continue to database CRUD operations](/tutorials/database-crud-operations)

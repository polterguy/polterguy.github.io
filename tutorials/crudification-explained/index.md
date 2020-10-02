# Super Duper Meta data

If you have gone through all of the articles here, you now know everything
necessary to understand how the _"crudification"_ process works. Hence, in this article I
will walk you through the semantics of this process, to literally reveal the Magic
of Magic - In addition to teaching you some _"super duper meta data Magic"_ in the process.
Notice, if you prefer to watch video tutorials, you can watch the following video
where I explain parts of what goes on under the hood of Magic, and also show you
how you can configure the crudification process, and some of its powerful meta data
capabilities.

<div style="position:relative; padding-bottom:56.25%; padding-top:30px; height:0; overflow:hidden;margin-top:4rem;margin-bottom:4rem;">
<iframe width="560" height="315" style="position:absolute; top:0; left:0; width:100%; height:100%;" src="https://www.youtube.com/embed/PgqiaChEd6s" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Meta data

Meta data is at the core of Magic. Without meta data, there cannot exist neither any intelligent
crudification process, nor any intelligent frontend generator. The first meta data retrieval occurs as
you crudify your database, at which point Magic retrieves meta data from your database, such as
table names, column names, data types for columns, whether or not your column is a part of the
primary key for the table, etc. The second meta data process however, is 1.000 times more
powerful. Because at this point, Magic will semantically open your Hyperlambda endpoint files,
and inspect _exactly what they do_. This creates the foundation for the frontend scaffolding
process, which again results in your frontend being automatically generated. At this point,
Hyperlambda becomes _instrumental_ for Magic's ability to perform its job. To illustrate the
importance of Hyperlambda at this point, imagine Hyperlambda as reflection from .Net, only
1.000 times more powerful.

After having crudified your database, the meta data retrieval process of Magic allows you
to ask questions such as.

1. What is the URL of your endpoint?
2. What is its HTTP verb?
3. Does this endpoint read from a database?
4. _What_ database is it reading from?
5. What columns are the endpoint returning?
6. If it reads from a database, is it a MySQL or an SQL Server database?
7. Etc, etc, etc ...

In fact, as I try to explain the value proposition of Hyperlambda, I often end up saying
that _"Hyperlambda understands Hyperlambda"_, which probably doesn't make any sense at all for
software developers that are used to traditional programming languages - But which still
is at the _core_ of the automation process in Magic.

> When the computer understands its own code, it can create and modify its code, and the human software developer arguably becomes obsolete

### Your first Meta Data endpoint

To illustrate Hyperlambda's meta data capabilities, let's create an HTTP endpoint, that takes
a file path as an input argument, and answers the question _"does this file read from the Sakila/actor table?"_
Create a file in your _"modules/tutorials/"_ folder, and give it the name _"meta.post.hl"_.
Put the following content into your file.

```
.arguments
   file:string
auth.ticket.verify:root
io.file.load:x:@.arguments/*/file
hyper2lambda:x:-
if
   exists:x:@hyper2lambda/*/mysql.connect/=sakila/*/mysql.read/*/table/=actor
   .lambda
      return
         result:Yup, this file reads from your actor table
else
   return
      result:Nope! This file doesn't read from your actor table
```

Invoke the above endpoint, and pass in _"/modules/sakila/actor.get.hl"_
as its `file` argument. At which point you'll end up with the following result.

```json
{
  "result": "Yup, this files reads from your actor table"
}
```

Try invoking it again, but this time pass in _"/modules/sakila/address.delete.hl"_
as its file argument - At which point you'll get something resembling the following
as your result.

```json
{
  "result": "Nope! This file doesn't read from your actor table"
}
```

As you can see, the above 12 lines of Hyperlambda code, is
easily capable of answering the above question for us. Doing the equivalent in for
instance C# would require monumental amounts of work, and it would probably be specific to
one particular construct. While the above Hyperlambda endpoint could easily be modified to take
an expression as an argument, resulting in that it could answer _any_ question we might have
relating to what our files do.

This effectively results in that we end up with
_"Hyperlambda 'query language' capabilities"_, allowing us to treat code, the same way
we treat data, reflect upon the code, and query the code - Giving us a high level
view of what our codebase as a whole does, in addition to exactly understanding what individual
files does. This allows us to build _tools_ on top of
our Hyperlambda code, that automates the maintenance of our code. And in fact,
the crudifier itself is mereley _one_ such tool. We could build hundreds of
similar tools, doing _other_ tasks for us automatically.

### Querying your code

Let's illustrate this by creating a generic _"code query endpoint"_, where
we can supply an expression as _input_, and have it evaluated towards _every single file_
in our _"/modules/"_ folder. Add the following file into your _"/modules/tutorials/"_
folder.

**query.post.hl**

```
.arguments
   query:string
auth.ticket.verify:root

// Lists files recursively inside of /modules/ folder
signal:magic.io.file.list-recursively
   .:/modules/

// Prepends specified expression with @.code
strings.concat
   .:@.code/
   get-value:x:@.arguments/*/query
   
// Changes the value of the [exists] node below to become our query expression
set-x:x:./**/.lambda/*/if/*/exists
   convert:x:@strings.concat
      type:x

// Looping through each file inside of our /modules/ folder.
for-each:x:@signal/*

   // Checking that the currentlty iterated file is a Hyperlambda file.
   if
      strings.ends-with:x:@.dp/#
         .:.hl
      .lambda

         /*
          * Hyperlambda file, loading file and adding its content
          * into the [.code] segment below as lambda.
          */
         .code
         io.file.load:x:@.dp/#
         add:x:@.code
            hyper2lambda:x:@io.file.load
            
         /*
          * Evaluating the specified expression. [exists] here
          * is parametrized from the input argument.
          */
         if
            exists
            .lambda
            
               // Expression returned true, hence returning filename to caller.
               unwrap:x:+/*/*
               add:x:../*/return
                  .
                     .:x:@.dp/#
         
// Dynamically built above according to result of [exists] invocation
return
```

The above code might be difficult for you to understand until you've got some experience
with Hyperlambda, but our endpoint basically takes a `query` parameter, which is converted
into an expression on the server. Then it loads every single Hyperlambda file inside of your
_"/modules/"_ folder, and runs the expression towards the currently iterated file. If the
expression yields one or more results, it adds the filename of the currently iterated file
into the **[return]** invocation at the bottom. Hence, the endpoint will return the filenames
of every single Hyperlambda file in your _"/modules/"_ folder, that somehow matches the
specified expression. To understand its purpose, let's try to invoke it with the following
payload.

```json
{
  "query": "**/mysql.connect/*/*/table/=address"
}
```

Assuming you've crudified your Sakila database, the results
should resemble the following.

```json
[
  "/modules/sakila/address-count.get.hl",
  "/modules/sakila/address.delete.hl",
  "/modules/sakila/address.get.hl",
  "/modules/sakila/address.post.hl",
  "/modules/sakila/address.put.hl"
]
```

What the endpoint told us, was basically as follows.

> Give me the filenames of all files that are reading/updating/deleting/creating
MySQL records in a table named address.

To have the endpoint return all files that are opening a MySQL database connection,
you can invoke it with the following payload.

```json
{
  "query": "**/mysql.connect"
}
```

To open all files that are somehow loading other files from disc, pass in the
following payload

```json
{
  "query": "**/io.file.load"
}
```

Which should return something resembling the following.

```json
[
  "/modules/system/crudifier/crudify.post.hl",
  "/modules/system/crudifier/custom-sql.post.hl",
  "/modules/system/endpoints/template.get.hl",
  "/modules/system/magic.startup/misc/magic.io.file.load-recursively.hl",
  "/modules/system/setup/setup.post.hl",
  "/modules/tutorials/meta.post.hl",
  "/modules/tutorials/query.post.hl"
]
```

To list all files that are invoking **[mysql.create]**, you can pass in the following
payload.

```json
{
  "query": "**/mysql.create"
}
```

Etc, etc, etc. Hence, we can now _query_ our code, and ask it arguably any question
we can phrase, and our Magic backend will instantly answer our question, and return
the answer to our question, relating to what our code actually does, and what files
are doing it. So with some Hyperlambda creativity, we have _"read"_ for our code,
almost like the following pseudo SQL would yield.

```sql
select filename from Hyperlambda.files where @some_condition
```

### Automatically updating your code

It doesn't stop there though. Combining the above query capabilities with patching
capabilities, allows us to modify all Hyperlambda files meeting some criteria
of some sort. Below is another endpoint. Save the following Hyperlambda in a
file called _"update.post.hl"_ in the same folder.

```
.arguments
   query:string
   hyperlambda:string
auth.ticket.verify:root

// Tracks the number of modified files.
.no:int:0

// Lists files recursively inside of /modules/ folder
signal:magic.io.file.list-recursively
   .:/modules/
   
// Converting Hyperlambda to lambda
hyper2lambda:x:@.arguments/*/hyperlambda

// Prepends specified expression with @.code
strings.concat
   .:@.code/
   get-value:x:@.arguments/*/query
   
// Changes the value of the [exists] node below to become our query expression
set-x:x:./**/.lambda/*/if/*/exists
   convert:x:@strings.concat
      type:x

// Looping through each file inside of our /modules/ folder.
for-each:x:@signal/*

   // Checking that the currentlty iterated file is a Hyperlambda file.
   if
      strings.ends-with:x:@.dp/#
         .:.hl
      .lambda

         /*
          * Hyperlambda file, loading file and adding its content
          * into the [.code] segment below as lambda.
          */
         .code
         io.file.load:x:@.dp/#
         add:x:@.code
            hyper2lambda:x:@io.file.load
            
         /*
          * Evaluating the specified expression. [exists] here
          * is parametrized from the input argument.
          */
         if
            exists
            .lambda
            
               // Expression returned true, hence patching Hyperlambda file.
               insert-after:x:@.code/*/.arguments
                  get-nodes:x:../*/hyper2lambda/*

               /*
                * Saving file, now patched with whatever
                * Hyperlambda caller supplied
                */
               io.file.save:x:@.dp/#
                  lambda2hyper:x:@.code/*
               math.increment:x:@.no

// Returns the number of affected files.
unwrap:x:+/*
return
   files-updated:x:@.no
```

Then try to invoke it with the following payload.

```json
{
  "query": "**/mysql.connect/=sakila/*/mysql.create",
  "hyperlambda": "log.info:Creating database item"
}
```

The above little payload just updated _every single Hyperlambda file_
that creates Sakila database records, making sure each of these file creates a log item,
as the endpoint is invoked. The execution of this patching took us maybe some 30-50
milliseconds, and the process automatically loaded every single file in our Magic
server for us, checked if it was a _"create"_ invocation towards Sakila - And if it was, it
made sure it creates a log item every single time the endpoint is invoked.
Arguably, we just created the following little pseudo SQL you might argue.

```sql
update codebase add(@new_code) where @condition
```

Some roughly 100 files were inspected semantically in 0.1 seconds, and
all files creating database records for us, are now logging this fact.
We modified some roughly 10 files in 0.1 second.

### Code delete

We can also easily create a _"delete code part"_ endpoint. Create a
new file in your _"/modules/tutorials/"_ folder and name your
file _"delete-code.post.hl"_, and put the following content into it.

```
.arguments
   query:string
   delete:string
auth.ticket.verify:root

// Tracks the number of modified files.
.no:int:0

// Lists files recursively inside of /modules/ folder
signal:magic.io.file.list-recursively
   .:/modules/

// Prepends specified expression with @.code
strings.concat
   .:@.code/
   get-value:x:@.arguments/*/query
   
/*
 * Changes the value of the [exists] node below
 * to have our [query] expression
 */
set-x:x:./**/.lambda/*/if/*/exists
   convert:x:@strings.concat
      type:x

// Prepends specified delete expression with @.code
strings.concat
   .:@.code/
   get-value:x:@.arguments/*/delete
   
/* 
 * Changes the value of the [remove-nodes] node below
 * to have our [delete] expression.
 */
set-x:x:./**/.lambda/*/if/*/.lambda/*/remove-nodes
   convert:x:@strings.concat
      type:x

// Looping through each file inside of our /modules/ folder.
for-each:x:@signal/*

   // Checking that the currentlty iterated file is a Hyperlambda file.
   if
      strings.ends-with:x:@.dp/#
         .:.hl
      .lambda

         /*
          * Hyperlambda file, loading file and adding its content
          * into the [.code] segment below as lambda.
          */
         .code
         io.file.load:x:@.dp/#
         add:x:@.code
            hyper2lambda:x:@io.file.load
            
         /*
          * Evaluating the specified expression. [exists] here
          * is parametrized from the input argument.
          */
         if
            exists
            .lambda
            
               /*
                * Expression returned true, hence patching
                * Hyperlambda file, and removing nodes caller
                * told us to remove.
                */
               remove-nodes

               /*
                * Saving file, now patched with whatever
                * Hyperlambda caller supplied
                */
               io.file.save:x:@.dp/#
                  lambda2hyper:x:@.code/*
               math.increment:x:@.no

// Returns the number of affected files.
unwrap:x:+/*
return
   files-updated:x:@.no
```

Then invoke your newly created endpoint with the following payload.

```json
{
  "query": "**/mysql.connect/=sakila/*/mysql.create",
  "delete": "**/log.info"
}
```

And you now deleted the **[log.info]** invocation in every single file that
creates items in your Sakila database - Effectively _"undoing"_ what we
did in the above update code invocation - And you did it _semantically_,
by inspecting the code, filtering out parts of your files, and removing
_only_ the requested parts of your Hyperlambda files. Effectively resulting
in something resembling the following

```
delete @code from Hyperlambda.files where @condition
```

Hence, you now have more or less CRUD capacity on your Hyperlambda
code.

## Wrapping up

What we did in this article, was to create query, update, and delete
capability on our codebase, by using Hyperlambda's ability to inspect
and reflect upon its own code - And in that process we ended up adding
more or less _"CRUD capabilities"_ on our code. This of course easily
lends itself to automation, and is at the _heart_ of what Magic does
in fact, as it's creating your backend code. This allows you to not
only generate, but also modify your code base as a whole, using
automation processes - Capable of updating at least in theory thousands
of Hyperlambda files, in the blink of an eye. Effectively replacing
manual software development with intelligently created automation
processes, 1 million times faster than a _"mere human being"_ when
it comes to creating and modifying code - Being 1 million times more
accurate too as it does its job. This effectively reduces the number
of bugs to ZERO, and makes you a million times more productive,
and capable of maintaining (in theory) millions of such codebases,
by automatically patching your code, using automation techniques
like those we described in this article. Or to say it with a little bit
of humour ...

> Take me to your leader ;)

Psst, below is a video where I demonstrate what I am doing here, in
case you want to watch me doing it before trying it out for yourself.

<div style="position:relative; padding-bottom:56.25%; padding-top:30px; height:0; overflow:hidden;margin-top:4rem;margin-bottom:4rem;">
<iframe width="560" height="315" style="position:absolute; top:0; left:0; width:100%; height:100%;" src="https://www.youtube.com/embed/3B-4g-aAncY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

* [The scaffolded Angular frontend](/tutorials/angular-scaffolder/)

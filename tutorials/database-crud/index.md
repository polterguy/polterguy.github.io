---
title: Generating a Hyperlambda CRUD app
description: In this article we generate a Hyperlambda CRUD web API using Magic, for then to analyse the generated code, providing you with the knowledge required to understand how Magic is doing its Magic.
---

# Generating a Hyperlambda CRUD app

This is going to be a _"different"_ tutorial, since instead of creating code ourselves, we will use
Magic to generate our code, and analyse what Magic did afterwards. If you prefer to
watch a video where I demonstrate this process, you can watch the following video.

<div class="video">
<iframe width="560" height="315" style="position:absolute; top:0; left:0; width:100%; height:100%;" src="https://www.youtube.com/embed/mv9MNnoP9-s" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

What Magic just did for us in the above video was providing us with a starting
point, from where we can modify the code afterwards.
However, in order to modify the code, we'll need to understand it. So let us walk through it step
by step, starting out with the creation of our database, ending up with an understanding of the
Hyperlambda code that Magic produced for us.

## Creating your database

Open the _"SQL"_ menu item in your dashboard, and click the _"Load"_ button. If you're using MySQL
as your main database then choose _"babelfish"_ - If you're using SQL Server, choose _"northwind-simplified"_.
Load the database script, and click the _"Execute"_ button.

![Creating your Babelfish database](https://servergardens.files.wordpress.com/2021/04/sql-editor.png)

This creates a database for you, which will be the foundation for generating our HTTP CRUD backend.

## Generating your backend

Before we can generate our backend we will have to purge our database cache. Click the little spiral
icon in your SQL menu item below the SQL editor.
Then open the _"CRUD"_ menu item, choose your newly created database,
and click _"Crudify all tables"_. Below you can see how this process should look like.

![Generating your backend](https://servergardens.files.wordpress.com/2021/04/generator.png)

As you generate your backend you will notice that Magic says something like _"xxx LOC generated"_.
This number is the lines of code that Magic automatically generated for you, and depends upon
your database and its number of tables. A small database such as babelfish will typically only
generate some 3-400 hundred lines of code - While a larger database might generate tens of
thousands of lines of code for you.

## Playing with our CRUD endpoints

After having done the above, Magic will have created a bunch of Hyperlambda files for you in
your _"/modules/xxx"_ folder, where _"xxx"_ is your database name. Open the _"Hyper IDE"_ menu
item in your dashboard, and take a look at this folder. These files will wrap
all the 4 main CRUD operations towards your tables, in addition to a count endpoint. The
structure should resemble the following.

* Create - _"xxx.post.hl"_
* Read - _"xxx.get.hl"_
* Update - _"xxx.put.hl"_
* Delete - _"xxx.delete.hl"_
* Count - _"xxx-count.get.hl"_

You will have 5 files resembling the above structure for each of your tables in your database.
We will study the files generated around one of these tables, but it doesn't matter which
database you generated, or which table you select - The structure will be similar enough
regardless of which table you choose. However, before we start looking at the code, let's
play around with the code, by going to the _"Endpoints"_ menu item, and filter on one of
your tables. In the screenshot below, we've chosen _"babelfish/language"_. Click the
_"get"_ endpoint, at which point you should see something resembling the following.

![Your CRUD endpoints](https://servergardens.files.wordpress.com/2021/04/endpoints-tutorial.png)

You can already execute your endpoint by clicking the _"Invoke"_ button for your endpoint.
If you do this, you should see a bunch of JSON objects returned from your server resembling
the following, depending upon which table you chose.

```json
[
  {
    "locale": "en",
    "language": "English"
  },
  {
    "locale": "es",
    "language": "Spanish"
  },
  {
    "locale": "fr",
    "language": "French"
  },
  {
    "locale": "it",
    "language": "Italian"
  },
  {
    "locale": "no",
    "language": "Norwegian"
  }
]
```

The read endpoint supports all of the following features.

* Paging through **[limit]** and **[offset]**
* Ordering items through **[order]** and **[direction]**
* Filtering
* Specifying a boolean **[operator]** for filter criteria

The above is what you'd typically need most of the times as you read items from your database.
If you'd like to find items only matching a specific criteria, you can add a filter for your criteria,
to have your backend only return items matching your filter. You will see a whole range of possible
filters for every column in your table, such as I illustrate for the **locale** column below.

* __locale.eq__ - Locale being exact match of the specified string
* __locale.neq__ - Locale _not_ equal to the specified string
* __locale.like__ - Locale contains the specified string supporting wildcards as `%`
* __locale.mt__ - Locale more than the specified string
* __locale.lt__ - Locale less than the specified string
* __locale.mteq__ - Locale more than or equal to the specified string
* __locale.lteq__ - Locale less than or equal to the specified string

**Notice** - Depending upon whether or not you checked of the _"Verbose"_ checkbox as you crudified
your backend, you will see more or less options for filtering on each column.

Each column will have a range of filter options matching the above comparison operators. If some
of your filter conditions doesn't make sense for a particular column, you can delete these later
as we start editing the endpoint's code. However, try clicking the **locale.eq** filter button for
instance, and add the value _"en"_ into it, click _"Add"_, and invoke your endpoint again. This
time of course only items matching your filter condition are returned, such as the following JSON
illustrates.

```json
[
  {
    "locale": "en",
    "language": "English"
  }
]
```

You can combine as many conditions as you wish the same way we added the above **eq** filter.
Conditions are by default **and**'ed together, implying _all conditions must match_ - But
this can be changed to **or** by changing the value of the **[operator]** argument.

You can also create and update items if you select your **post** or **put** endpoints. However,
these endpoints require you to provide a JSON payload instead of parametrising
your endpoint using query parameters. Try to create and update some items using these
two endpoints. Just remember that regardless of what table you choose, the primary key parts
to the update endpoint is the criteria of _which item to update_. Magic only creates endpoints
that supports updating _one item at the time by default_. And the generator does not produce
code allowing you to change the primary key.

### Meta data

If you go through your endpoints, you will see a _lot_ of meta information. This was generated
automatically based upon your database schema, and is also publicly exposed to the client, almost
the same way the Open Web API or Swagger is able to enumerate and document your HTTP endpoints.
Hence, we've already documented our HTTP endpoints, even though we haven't even manually created a
single line of code. Magic also creates meta information like this for your manually
created endpoints.

This meta data becomes crucial as we later start looking at how Magic creates your frontend code
using similar techniques as it used to create your backend. You can see this meta information as
properties of your endpoint if you go to the _"Endpoints"_ menu item, and click any of your
endpoints.

## Analysing the code

Once you're done playing around with your endpoints, open up the _"Files"_ menu item. Click the _"modules"_
folder, then click the folder with the same name as the name of the database you generated above.
Click for instance the _"languages.get.hl"_ file, at which point you should see something resembling
the following.

![Editing your Hyperlambda CRUD files](https://servergardens.files.wordpress.com/2021/04/files-crud-editor.png)

**Notice** - If you didn't generate CRUD endpoints for your babelfish database, then at least make
sure that whatever file you're looking at ends with _".get.hl"_ such that we're looking at roughly the
same thing in the rest of this tutorial.

What you are looking at now is the Hyperlambda Magic automatically generated for you. The most important
part of this code is the following section.

```
   data.read
      database-type:mysql
      table:languages
      columns
         locale
         language
      where
         and
```

The above invocation to the **[data.read]** slot is _"transpiled"_ by Magic into an SQL statement,
retrieving your records from your database, according to your filter conditions. The result of this
SQL is then returned back to the client as JSON in the **[return-nodes]** line below. The above slot
will expect an existing open database connection, which is accomplished with the **[data.connect]** slot
invocation. The below code shows you how to connect to a database.

```
data.connect:[generic|babelfish]
   database-type:mysql
```

Notice how the generated Hyperlambda for your **[data.read]** invocation can be found _inside_
your **[data.connect]** invocation. This implies that your read invocation will use this database
connection implicitly, since the read invocation is _"a lambda object inside of your database connection"_.
Hence all database operations inside of a **[data.connect]** invocation will by default use that
database connection to connect to your database and execute its SQL. Think of these slots as
an **SqlConnection** instance and an **SqlDataReader** instance, where the reader uses the connection
you previously opened. Then realise that the 3 carriage returns found in front of the **[data.read]**
invocation becomes kind of like _"the scope"_ of the **[data.connect]** invocation, implying the
code inside of **[data.connect]** is actually a lambda object, or an _"argument"_ to your connect
invocation.

> In Hyperlambda code is always an argument, and all arguments are code

This is why it's called Hyperlambda, because _everything_ is a lambda object. Hyperlambda is
said to be _"a functional programming language"_. We will go through the exact syntax of Hyperlambda
in a later tutorial, but for now realise that in Hyperlambda _spaces counts_ - Kind of like the
same way they do in YAML or Python, and that 3 spaces declares a _"scope"_, while a colon `:`
declares the beginning of a node's value. Nodes again is a tree structure in the form of value, name,
and children - And is the foundation of Hyperlambda. Hyperlambda is simply the textual representation
of a tree structure, the same way YAML, JSON, or XML is. Nodes is Hyperlambda's object implementation
again. See the documentation for [magic.node](/documentation/magic.node/) for more details.

### Arguments passing

If you look at the top of your file, you will see something resembling the following.

```
.arguments
   limit:long
   offset:long
   order:string
   direction:string
   operator:string
   locale.like:string
   locale.mt:string
// Etc, etc, etc
```

The endpoint resolver will actually read the above **[.arguments]** node, and use it to
retrieve meta information about which arguments your endpoint can accept. If you edit it,
save it, and go back to your endpoints file menu, you can see how it's automatically updated,
and the arguments provided by the meta information parts of the endpoint resolver automatically
changes. The **[.arguments]** node is said to _"declare which arguments your endpoint can accept"_.
Editing the arguments your endpoint accepts is typically among one of the first things you
want to do if you want to modify your endpoint. In the above arguments node for instance, the
**[locale.mt]** argument probably doesn't make much sense, and can be deleted to simplify
your endpoint.

### Authorisation and authentication

Your endpoint will by default require authentication and authorisation, preventing anonymous
users from accessing it. This is done with the **[auth.ticket.verify]** slot with something
resembling the following.

```
auth.ticket.verify:root, admin
```

The above line of code basically verifies that your JWT token is valid, and that the user
invoking the endpoint belongs to one of the following roles.

* root
* admin

If the user has an invalid token, and/or the user doesn't belong to any of the above roles,
this slot will throw an exception, preventing the rest of the Hyperlambda code from executing.
This is the core authentication and authorisation parts of Magic, and allows you to secure
your web APIs easily. If you want users belonging to different roles to be able to invoke
your endpoint, you can simply edit the above code, by for instance adding _another_ role
to it, save your file - And voila; Your authorisation requirements have automagically changed.
Below is an example of how to add the _"translator"_ role as a role allowed to invoke the endpoint.

```
auth.ticket.verify:root, admin, translator
```

The above slot requires a comma separated list of roles as its input. You can also completely
remove the above node's value parts, resulting in that _any_ authenticated user can invoke
your endpoint, as long as he or she has a valid JWT token. This completely ignores the roles
the user belongs to, as long as the user is authenticated with a valid JWT token. Below is
an example.

```
auth.ticket.verify
```

The rest of the file basically just provides meta information to the endpoint resolver, and
correctly parametrises your invocation to **[data.read]** - However, this will be a subject
of a later tutorial. If you're curious about how this work, you can check out for instance
the **[add]** slot in the documentation for [magic.lambda](/documentation/magic.lambda/).

### CRUD slots

An invocation to for instance **[data.read]** is referred to by Magic as a _"slot"_. If you
view your other CRUD files, you will see that they are using slightly different slots, to wrap
other CRUD functions. The basic CRUD operations in Magic are implemented with the following slots.

* __[data.read]__
* __[data.delete]__
* __[data.create]__
* __[data.update]__

Besides from using different slots, all of your generated Hyperlambda files are actually quite
similar in structure. You still typically want to have separate files for these operations, since
this allows you to easily modify for instance authorisation requirements, arguments passing, add
additional business logic to your files, etc. So even though the code is not very _DRY_
in its original state, separate endpoint files for separate operations are still typically
useful and a feature you will learn to appreciate further down the road, as you start
modifying your Hyperlambda files.
If you want to see the power of these CRUD slots you can check out the documentation for the
[magic.data.common](/documentation/magic.data.common/) module, which you can find in the
reference documentation for Magic.

* [Continue with SQL Web APIs](/tutorials/sql-web-api/)

---
title: Automatically generate a CRUD Web API using Hyperlambda
description: In this article we generate a Hyperlambda CRUD web API using Magic, for then to analyse the generated code, providing you with the knowledge required to understand how Magic is doing its Magic.
---

# Automatically generate a CRUD Web API using Hyperlambda

This is a _"hands on tutorial"_, and assumes you've already [installed Magic](/tutorials/getting-started/)
locally or at some server. This tutorial covers the following parts of Magic and Hyperlambda.

* How to automatically generate a Hyperlambda HTTP CRUD API wrapping your database
* The SQL, CRUD, Endpoints and Hyper IDE menu items
* CRUD database slots
* Passing arguments to Hyperlambda endpoints
* Validating arguments
* Authorisation and authentication

This is going to be a _"different"_ tutorial, since instead of creating code ourselves, we will use
Magic to generate our code, and analyse what Magic did afterwards. If you prefer to
watch a video where I demonstrate this process, you can watch the following video.

<div class="video">
<iframe width="560" height="315" style="position:absolute; top:0; left:0; width:100%; height:100%;" src="https://www.youtube.com/embed/HA0PDQITbZI" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

What Magic just did for us in the above video was providing us with a starting
point, from where we can modify the code afterwards.
However, in order to modify the code, we'll need to understand it. So let us walk through it step
by step, starting out with the creation of our database, ending up with an understanding of the
Hyperlambda code that Magic created for us.

## Creating your database

Open the _"SQL"_ menu item in your dashboard and click the _"Load"_ button. Choose _"sakila"_
if you're using MySQL as your primary database. Choose _"northwind-simplified"_ if you're using SQL Server.
Choose _"pagila"_ if you're using PostgreSQL. Load the database script, and click the _"Execute"_ button.

![Creating your Sakila database](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/sql-editor.jpg)

This creates a database for you, which will be the foundation for generating our HTTP CRUD backend.

## Generating your backend

Before we can generate our backend we will have to purge our database cache. Click the little spiral
icon in your SQL menu item beneath the SQL editor. Below is a screenshot showing you how.

![Purging your server side database cache](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/purge-cache.jpg)

Open the _"CRUD"_ menu item, choose your newly created database, and click _"Crudify all tables"_.
Below you can see a screenshot.

![Generating your backend](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/backend-crud.jpg)

As you generate your backend you will notice that Magic says something like _"xxx LOC generated"_.
This number is the lines of code that Magic automatically generated for you, and depends upon
your database and its number of tables. A small database such as sakila will typically only
generate some 3,500 lines of code - While a larger database might generate tens of
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
regardless of what table you choose. However, before we start looking at the code, let's
play around with the code, by going to the _"Endpoints"_ menu item, and filter on one of
your tables. In the screenshot below, we've chosen _"sakila/actor"_. Click the
_"get"_ endpoint, at which point you should see something resembling the following.

![Invoking your HTTP endpoints](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/endpoints.jpg)

You can already invoke your endpoint by clicking the _"Invoke"_ button for your endpoint.
If you do this, you should see a bunch of JSON objects returned from your server resembling
the following, depending upon which table you chose.

```json
[
  {
    "actor_id": 1,
    "first_name": "PENELOPE",
    "last_name": "GUINESS",
    "last_update": "2006-02-15T04:34:33.000Z"
  },
  {
    "actor_id": 2,
    "first_name": "NICK",
    "last_name": "WAHLBERG",
    "last_update": "2006-02-15T04:34:33.000Z"
  },
  {
    "actor_id": 3,
    "first_name": "ED",
    "last_name": "CHASE",
    "last_update": "2006-02-15T04:34:33.000Z"
  }
]
```

The read endpoint supports all of the following features.

* Paging through **[limit]** and **[offset]**
* Ordering items through **[order]** and **[direction]**
* Filtering
* Specifying a boolean **[operator]** for filter criteria

The above is what you would typically need most of the times as you read items from your database.
If you'd like to find items only matching a specific criteria, you can add a filter for your criteria
to have your backend only return items matching your filter. You will see a whole range of possible
filters for each column in your table such as illustrated for the **first_name** column below.

* __actor.first_name.eq__ - First name being exact match of the specified string
* __actor.first_name.neq__ - First name _not_ equal to the specified string
* __actor.first_name.like__ - First name contains the specified string supporting wildcards as `%`
* __actor.first_name.mt__ - First name more than the specified string
* __actor.first_name.lt__ - First name less than the specified string
* __actor.first_name.mteq__ - First name more than or equal to the specified string
* __actor.first_name.lteq__ - First name less than or equal to the specified string

**Notice** - Depending upon whether or not you checked of the _"Verbose"_ checkbox as you crudified
your backend, you will see more or less options for filtering on each column. The _"Verbose"_ checkbox
allows you to create _more_ filtering options for your generated endpoints.

Each column will have a range of filter options matching the above comparison operators. If some
of your filter conditions doesn't make sense for a particular column, you can delete these later
as we start editing the endpoint's code. However, try clicking the **actor.first_name.like** filter
button for instance, and add the value _"A%"_ into it, click _"Add"_, and invoke your endpoint again.
This time only items matching your filter condition are returned, such as the following JSON
illustrates.

```json
[
  {
    "actor_id": 29,
    "first_name": "ALEC",
    "last_name": "WAYNE",
    "last_update": "2006-02-15T04:34:33.000Z"
  },
  {
    "actor_id": 34,
    "first_name": "AUDREY",
    "last_name": "OLIVIER",
    "last_update": "2006-02-15T04:34:33.000Z"
  }
]
```

You can combine as many conditions as you wish the same way we added the above **like** filter.
Conditions are by default **and**'ed together, implying _all conditions must match_ - But
this can be changed to **or** by changing the value of the **[operator]** argument.

You can also create and update items if you select your **post** or **put** endpoints. However,
these endpoints require you to provide a JSON payload instead of parametrizing
your endpoint using query parameters. Try to create and update some items using these
two endpoints. Just remember that regardless of what table you choose, the primary key parts
to the update endpoint is the criteria of _which item to update_. Magic only creates endpoints
that supports updating _one item at the time by default_ - And the generator does not produce
code allowing you to change the primary key. For the _"put"_ and _"delete"_ endpoints,
the primary key(s) for your tables are also _mandatory_ and you have to supply these, otherwise
the backend will return an error to you.

### Meta data

If you go through your endpoints, you will see a lot of meta information. This was generated
automatically based upon your database schema, and is also publicly exposed to the client, almost
the same way the Open Web API or Swagger is able to enumerate and document your HTTP endpoints.
Hence, we've already documented our HTTP endpoints, even though we haven't manually created a
single line of code. Magic also creates meta information like this for your manually
created endpoints. This meta data becomes crucial as we later start looking at how Magic creates
your frontend. You can see this meta information as properties of your endpoint if you go to
the _"Endpoints"_ menu item and click any of your endpoints.

## Analysing the code

Once you're done playing around with your endpoints, open up _"Hyper IDE"_. Click
the _"modules"_ folder, then click the folder with the same name as the name of the database you generated above.
Click for instance the _"actor.get.hl"_ file, at which point you should see something resembling
the following.

![Editing your Hyperlambda using Hyper IDE](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/hyper-ide.jpg)

If you didn't generate CRUD endpoints for your sakila database then at least make
sure that whatever file you're looking at ends with _".get.hl"_ such that we're looking at roughly the
same thing. What you are looking at now is the Hyperlambda Magic automatically
generated for you. The most important part of this code is the following section.

```
   data.read
      database-type:mysql
      table:actor
      columns
         actor.actor_id
         actor.first_name
         actor.last_name
         actor.last_update
      where
         and
```

The above invocation to the **[data.read]** slot is _"transpiled"_ by Magic into an SQL statement,
retrieving your records from your database according to your filter conditions. The result of this
SQL is then returned back to the client as JSON in the **[return-nodes]** line at the bottom of your
code. The above slot will expect an already open database connection. To open a database connection
we use the **[data.connect]** slot. The following code shows you how to connect to a database.

```
data.connect:[generic|sakila]
   database-type:mysql
```

In the above **[data.connect]** invocation we are referencing a connection string who's name is
_"generic"_ and we're choosing to open the _"sakila"_ database in this instance. Since we supply
_"mysql"_ as our value to **[database-type]** this will ensure Magic uses the MySQL connection
string named _"generic"_. You can add additional connection strings to Magic by opening the
_"Config"_ menu item from your dashboard and edit your configuration settings.

Notice how the generated Hyperlambda for your **[data.read]** invocation can be found _inside_
your **[data.connect]** invocation. This implies that your read invocation will use this database
connection implicitly, since the read invocation is _"a lambda object inside of your database connection"_.
Hence all database operations inside of a **[data.connect]** invocation will by default use that
database connection to connect to your database and execute its SQL. Think of these slots as
an **SqlConnection** instance and an **SqlDataReader** instance, where the reader uses the connection
you previously opened - Then realise that the 3 carriage returns found in front of the **[data.read]**
invocation becomes kind of like _"the scope"_ of the **[data.connect]** invocation, implying the
Hyperlambda inside **[data.connect]** is actually a lambda object, or a _"lambda argument"_ to your connect
invocation.

> In Hyperlambda code is always an argument, and all arguments are code

This is why it's called Hyperlambda, because _everything_ is a lambda object. Hyperlambda is
said to be _"a functional programming language"_. We will go through the exact syntax of Hyperlambda
in a later tutorial, but for now realise that in Hyperlambda _spaces counts_ - Kind of like the
same way they do in YAML or Python, and 3 spaces declares a _"scope"_, while a colon `:`
declares the beginning of a node's value. Nodes again is a tree structure having a value, a name,
and children. This is the foundation of Hyperlambda. Hyperlambda is actually just a text representation
of a tree structure, the same way YAML, JSON, or XML is. Nodes are Hyperlambda's object implementation
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
   actor.actor_id.eq:long
   actor.first_name.like:string
   actor.first_name.eq:string
   actor.last_name.like:string
   actor.last_name.eq:string
   actor.last_update.eq:date
```

The endpoint resolver will actually read the above **[.arguments]** node, and use it to
retrieve meta information about which arguments your endpoint can accept. If you edit it,
save it, and go back to your endpoints file menu, you can see how it's automatically updated,
and the arguments provided by the meta information parts of the endpoint resolver automatically
changes. The **[.arguments]** node is said to _"declare which arguments your endpoint can accept"_.
You can add or remove arguments as you see fit.

#### Validating arguments

If you open one of your _"xxx.delete.hl"_ endpoint files in Hyper IDE, you will see something
resembling the following just below your **[.arguments]** collection.

```
validators.mandatory:x:@.arguments/*/xxx
```

This is a mandatory validator, and makes sure the endpoint cannot be invoked without passing in
an **[xxx]** argument. Hyperlambda contains many similar validators for validating numbers,
emails, date and time objects, etc. If you want to see what validators you can use
in Hyperlambda, you can checkout the documentation for [magic.lambda.validators](/documentation/magic.lambda.validators).
You can also use the autocomplete features of the Hyperlambda editor, by finding an empty
line and click FN+CONTROL+SPACE on a Mac or CTRL+SPACE on Windows. This will show you
the autocompleter for Hyperlambda slots, allowing you to filter on for instance validator
slots, such as the following illustrates.

![Autocomplete on validators](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/autocomplete.jpg)

### Authorisation and authentication

Your endpoint will by default require authentication and authorisation, preventing anonymous
users from accessing it. This is done with the **[auth.ticket.verify]** slot with something
resembling the following.

```
auth.ticket.verify:root, admin
```

The above line of code verifies that your JWT token is valid, and that the user
invoking the endpoint belongs to at least one of the following roles.

* root
* admin

If the user has an invalid token, and/or the user doesn't belong to any of the above roles,
this slot will throw an exception, preventing the rest of your Hyperlambda code from executing.
This is the core authentication and authorization parts of Magic, and allows you to secure
your web APIs. If you want users belonging to different roles to be able to invoke
your endpoint, you can simply edit the above code, by for instance adding _another_ role
to it, save your file - And voila; Your authorization requirements have automagically changed.
Below is an example of how to add the _"director"_ role as a role allowed to invoke the endpoint.

```
auth.ticket.verify:root, admin, director
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

An invocation to for instance **[data.read]** is referred to by Magic as a _"slot invocation"_
or a _"signal"_. A _"slot"_ is kind of like a function, and a _"signal"_ is kind of like a function
invocation. However, fundamentally Magic doesn't have _"functions"_ the way a traditional
programming language has, which is why we refer to these as signals and slots.
If you view your other CRUD files, you will see that they are using slightly
different slots to wrap other CRUD functions. The basic CRUD operations in Magic are implemented
with the following slots.

* __[data.read]__
* __[data.delete]__
* __[data.create]__
* __[data.update]__

Besides from using different slots, all of your generated Hyperlambda files are actually quite
similar in structure. You still typically want to have separate files for these operations, since
this allows you to easily modify for instance authorization requirements, arguments passing, add
additional business logic to your files, etc. So even though the code is not very _DRY_
in its original state, separate endpoint files for separate operations are still typically
useful, and a feature you will appreciate further down the road.
If you want to see the power of these CRUD slots you can check out the documentation for the
[magic.data.common](/documentation/magic.data.common/) module that you can find in the
reference documentation for Magic.

* Continue with [Create a Web API with SQL](/tutorials/sql-web-api/)

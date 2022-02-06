---
title: Create a Web API with SQL and Hyperlambda
description: This article shows you how you can create a complete HTTP Web API using nothing but SQL. This is possible since Magic and Hyperlambda completely abstracts away everything related to the wiring of your endpoint code, leaving only the SQL parts for you.
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/og-sql.jpg"
---

# Create a Web API with SQL and Hyperlambda

In this tutorial we will cover the following parts of Magic and Hyperlambda.

* Generating an HTTP endpoint using SQL
* Magic's integrated SQL editor
* Mandatory validators

The CRUD/SQL parts of Magic allows you to automatically wrap
your SQL into an HTTP endpoint, without having to do anything except provide Magic with SQL.
To understand the idea, you can watch the following video where I demonstrate this feature.

<div class="video">
<iframe width="560" height="315" style="position:absolute; top:0; left:0; width:100%; height:100%;" src="https://www.youtube.com/embed/FFLVqSuWjnI" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

As illustrated above, this feature allows you to dynamically wrap your SQL into
a secured HTTP endpoint, where you provide a URL, an HTTP verb, authorisation requirements,
a list of arguments, and some SQL - For then to have Magic automatically generate your endpoint.
The way this works is similar to the CRUD generator parts,
except this time the responsibility is reversed, allowing you to provide the SQL, and have Magic do the rest.

## DRY code

One of the most important architectural design principles in software development is **DRY**, as in _"Don't Repeat Yourself"_.
Magic simply brings this to the next level, which is why it can do what we did in the
above video. This is quite easy too, since 90% of such endpoints have similar requirements, being
a list of roles allowed to access the endpoint, a JSON payload or some query
parameters, for then to simply return whatever the SQL returns back to the client as JSON. Automating
this process is a no-brainer. Below you can find the SQL I am using in the above video.

```sql
select a.first_name, f.title, f.description
   from actor a
      inner join film_actor fa on a.actor_id = fa.actor_id
         inner join film f on f.film_id = fa.film_id
   where a.first_name like @filter
      or f.title like @filter
      or f.description like @filter
```

Below is a screenshot of how this looks like in Magic's dashboard.

![Creating a Web API using SQL](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/sql-web-api.jpg)

The Hyperlambda code Magic automatically creates for you will resembles the following.

```

/*
 * Template for custom SQL HTTP request.
 * This file was automatically generated using Magic's CRUDifier.
 */
.arguments
   filter:string
.type:sql
auth.ticket.verify:root, admin

// Ensures that the [filter] argument is specified, or throws an exception.
validators.mandatory:x:@.arguments/*/filter

// Opening up a database connection
data.connect:sakila
   database-type:mysql

   // Parametrizing [data.select].
   add:x:./*/data.select
      get-nodes:x:@.arguments/*

   // Evaluating [xxx.select] slot.
   data.select:@"
select a.first_name, f.title, f.description
   from actor a
   inner join film_actor fa on a.actor_id = fa.actor_id
   inner join film f on f.film_id = fa.film_id
where a.first_name like @filter
   or f.title like @filter
   or f.description like @filter"
      database-type:mysql

   /*
    * Checking if we should return a list of items, or only a
    * single item.
    */
   if
      .is-list:bool:true
      .lambda

         // Returning a list of items to caller.
         return-nodes:x:@data.select/*

   // Returning a single result to caller.
   return-nodes:x:@data.select/*/*
```

The only parts of the above code we had to manually apply ourselves is the invocation to
**[validators.mandatory]**. If you want to return a scalar value instead of a list
of items, you can change the above **[.is-list]** value to false. This will return a single
value to the client instead of a list of items, which might be useful sometimes.

* Continue with [Hyperlambda Hello World](/tutorials/hello-world-endpoint/)

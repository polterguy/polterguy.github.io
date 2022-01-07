---
title: Create a Web API with SQL
description: This article shows you how you can create a complete HTTP Web API using nothing but SQL. This is possible since Magic and Hyperlambda completely abstracts away everything related to the wiring of your endpoint code, leaving only the SQL parts for you.
---

# Create a Web API with SQL

In this tutorial we will cover the following parts of Magic and Hyperlambda.

* Generating a Web API using SQL
* The CRUD menu item
* Magic's integrated SQL editor

The CRUD/SQL parts of Magic allows you to automatically wrap
your SQL into an HTTP endpoint, without having to do anything except provide Magic with SQL.
To understand the idea, you can watch the following video where I demonstrate this feature.

<div class="video">
<iframe width="560" height="315" style="position:absolute; top:0; left:0; width:100%; height:100%;" src="https://www.youtube.com/embed/GSGYzXxlgG0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

As illustrated above, this feature allows you to dynamically wrap your SQL into
a secured HTTP endpoint, where you simply provide a URL, an HTTP verb, authorization requirements,
and a list of arguments - Without having to create as much as a single line of
code yourself. Then you provide Magic with an SQL statement, click the button, and Magic generates your
HTTP endpoint 100% automatically. Of course the way it works, is similar to the CRUD generator parts,
except this time the responsibility is reversed, allowing you to provide the SQL, and have Magic do the rest.
The endpoint can be easily secured, only providing access to whatever roles you want to have access
100% automatically.

## DRY code

One of the most important architectural principles in the world today is **DRY**, as in _"Don't Repeat Yourself"_.
Magic simply brings this idea to the next level, which of course is why it can do what we demonstrate in the
above video. This is quite easy too, since 90% of such endpoints, have similar requirements, being
a list of roles allowed to access the endpoint, a JSON payload of some sort, maybe some query
arguments, for then to simply return whatever the SQL returns back to the client as JSON. Automating
this process is a no-brainer. Below you can find the SQL I am using in the above video.

```sql
select l.locale, l.language, t.id, t.content
  from languages l
    inner join translations t on l.locale = t.locale
  where t.content like @filter
```

Below is a screenshot of how this looks like in Magic's dashboard.

![Creating a Web API using SQL](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/sql-web-api.jpg)

The Hyperlambda code Magic automatically creates for you for the above resembles the following.

```
.arguments
   filter:string
.type:sql
auth.ticket.verify:root, admin

data.connect:babelfish
   database-type:mysql

   add:x:./*/data.select
      get-nodes:x:@.arguments/*

   data.select:"select l.locale, l.language, t.id, t.content\n  from languages l\n    inner join translations t on l.locale = t.locale\n  where t.content like @filter"
      database-type:mysql

   if
      .is-list:bool:true
      .lambda

         return-nodes:x:@data.select/*

   return-nodes:x:@data.select/*/*
```

If you want to return a scalar value instead of a list of items, you can change the above **[.is-list]**
value to false. This will return a single value to the client instead of a list of items, which sometimes might
be useful.

* Continue with [Hyperlambda Hello World](/tutorials/hello-world-endpoint/)

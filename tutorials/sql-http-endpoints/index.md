# Custom SQL endpoints

If you know SQL but you don't know other programming languages, or you simply want to increase
your productivity, by avoiding having to create boilerplate code - You can create
a _"Custom SQL HTTP REST endpoint"_, wrapping your SQL statement, allowing you to parametrise it in
the process. This allows you to take almost any SQL statement you might have laying around, and
turn it into an HTTP REST endpoint in some few seconds - Parametrising it in the process if you
wish.

<div style="position:relative; padding-bottom:56.25%; padding-top:30px; height:0; overflow:hidden;margin-top:4rem;margin-bottom:4rem;">
<iframe width="560" height="315" style="position:absolute; top:0; left:0; width:100%; height:100%;" src="https://www.youtube.com/embed/Ci6a_ZVueXg" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

If you watch the above video, you will see me walk you through the process.
The only thing you really need to understand afterwards, is the association between the arguments
and SQL parameters, implying that for instance `foo:string` as an argument, can be referenced
as `@foo` in your SQL statement, and that it's expected to be of type string. Hence, just add your
arguments as a CR/LF list of names, and reference these in your SQL. Currently, there is no
ability to supply default argument values, which means all arguments ends up becoming mandatory,
unless you're actually doing a `null` comparison of course.

## Internals

Internally Magic will create a Hyperlambda file for you, resembling the following.

```
.arguments
   offset:long
   limit:long
auth.ticket.verify:root
.type:sql
mysql.connect:sakila
   add:x:+
      get-nodes:x:@.arguments/*
   mysql.select:@"select co.country, c.city
  from city c inner join country co on c.country_id = co.country_id
  order by country
  limit @limit
  offset @offset"
   return-nodes:x:-/*
```

## Wrapping up

Although this is arguably a _"naive feature"_ for seasoned developers, it's easily underestimated,
since it adds authentication and authorisation in the process to your endpoint - Securing it such
that no un-authorised agent can invoke it. In addition to that it also is 1.000 times faster than
writing out the C# coiler plate code yourself - Implying the model, C# connection code, etc for
your endpoint - Instead allowing you to simply paste in an existing SQL, and save your endpoint.
The performance of your endpoint, will also be much faster than if you used Entity Framework
and for instance AutoMapper to create something similar - Probably somewhere around 5-10 times
faster in fact. And the code actually executing internally in Magic, is executed `async`, implying
it also scales very well. Hence, it's probably a nice feature to create things such as reports,
charts, etc.

Another interesting fact, is that it's also _"raw SQL"_, allowing some DB admin or SQL expert
to write the SQL, and then simply copy and paste his or her code into an endpoint. If you have
ever tried to _"translate"_ some SQL a guy wrote for a report into its Entity Framework
`IQueryable` equivalent, you will understand why this is a positive thing. With Hyperlambda,
you can simply copy and paste the SQL expert's code, into an endpoint, and you're already up
running.

* [Documentation](/documentation/)


# Create your Web APIs with SQL

This tutorial walks you through Magic's SQL generator. This part of Magic allows you to automatically wrap
your SQL into an HTTP endpoint, without having to do anything except provide Magic with SQL.
To understand the idea, you can watch the following video where I demonstrate it.

<div style="position:relative; padding-bottom:56.25%; padding-top:30px; height:0; overflow:hidden;margin-top:4rem;margin-bottom:4rem;">
<iframe width="560" height="315" style="position:absolute; top:0; left:0; width:100%; height:100%;" src="https://www.youtube.com/embed/GSGYzXxlgG0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

As illustrated above, this feature allows you to dynamically wrap your SQL into
a secured HTTP endpoint, where you simply provide a URL, an HTTP verb, authorization requirements,
and a list of arguments - Without having to create as much as a single line of
code yourself. Then you provide Magic with an SQL statement, click the button, and Magic generates your
HTTP endpoint 100% automatically. Of course the way it works, is similar to the CRUD generator parts,
except this time the responsibility is reversed, allowing you to provide the SQL, and Magic to do the rest.

And the endpoint can be easily secured, only providing access to whatever roles you want to have access
to it 100% automatically for you.

## DRY code

One of the most important architectural principles in the world today is **DRY**, as in _"Don't Repeat Yourself"_.
Magic simply brings this idea to the next level, which of course is why it can do what I demonstrate in the
above video. This is quite easy too, since 90% of such endpoints, have similar requirements, being
a list of roles allowed to access the endpoint, a JSON payload of some sort, maybe some query
arguments, for then to simply return whatever the SQL returns back to the client as JSON. Automating
this process _should_ be a no-brainer.

Below you can find the SQL I am using in the above video.

```sql
select l.locale, l.language, t.id, t.content
  from languages l
    inner join translations t on l.locale = t.locale
  where t.content like @filter
```

Below is a screenshot of how this looks like in Magic's dashboard.

![SQL HTTP endpoints](https://servergardens.files.wordpress.com/2021/04/sql-http-endpoints.png)

## Wrapping up

In this micro-tutorial we created an HTTP REST endpoint without writing a single line of code,
and only providing Magic with an SQL statement, for then to let Magic do the work for us, arguably
automating the entirety of the process.

* [Documentation](/documentation/)

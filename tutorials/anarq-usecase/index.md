
# AnarQ, a Social Media example use case

It might be tempting to believe that Magic is only for CRUD HTTP REST endpoints. However, Magic and
Hyperlambda makes it possible to create anything you can create in any other programming languages.
In this tutorial, we will look at one specific use case, and create a backend for a Social Media website,
similar to Reddit in functionality. You can download the backend at its
[GitHub project website](https://github.com/polterguy/anarq). In the below video you can see me demonstrate
the system, how to install it, and its basic structure. Watch the video first, and then let's go over
some of its key concepts.

<div style="position:relative; padding-bottom:56.25%; padding-top:30px; height:0; overflow:hidden;margin-top:4rem;margin-bottom:4rem;">
<iframe width="560" height="315" style="position:absolute; top:0; left:0; width:100%; height:100%;" src="https://www.youtube.com/embed/ZnrhlelXH_s" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Key points from the system

AnarQ does a lot beyond simple CRUD. For instance, it sends emails, it creates database transactions,
it returns graph objects back to the client as JSON, it creates joins from multiple tables as it is
executing SQL, etc. So let's look at some of its key points, since it demonstrates the capacity of
Hyperlambda and Magic.

### SQL Joins

If you look at the _"feed"_ endpoint's code, you will see that it creates fairly rich and complex SQL joins.
Below is a part of its code.

```
data.read
   database-type:mysql
   table:posts
      as:p
      join:likes
         as:l
         type:left
         on
            and
               p.id:l.post_id
   columns
      p.id
      p.topic
      p.created
      p.user
         as:user
      p.visibility
      p.content
         as:excerpt
      count(l.post_id)
         as:licks
   where
      and
         p.parent.eq
   group
      p.id
   order:licks
      direction:desc
   order:p.created
      direction:desc
```

What the above code basically does, is to join the posts table with the likes table, grouping by post IDs,
and returning an aggregate result of the number of likes a post have, for then to order descendingly
on number of likes a post has. A simple little trick that allows us to retrieve the most popular posts
first, effectively becoming the ghist of the algorithm from Reddit, that ensures the most popular posts
are listed at the top of its _"feed"_.

In addition it filters out everything older than some threshold amount of time, implying over time,
posts will _"drop out"_ of the feed, depending upon what range you invoke the endpoint with. For instance,
if you set its **[minutes]** argument to 60, it will _only_ return posts that was posted less that 60
minutes ago, yet still order such that posts with the most likes ends up being returned first.

### Sending emails

Typically you want users to confirm their email address as they're registering. This creates a bit more
accountability, resulting in hopefully increasing the quality of what people post. Magic contains one
slot that significantly simplifies this for us, which is consumed in AnarQ as follows.

```
signal:magic.emails.send
   template-file:x:@.template-file
   name:x:@.arguments/*/full_name
   email:x:@.arguments/*/email
   subject:Confirm your email address to AnarQ please
   mime-type:text/html
   substitutes
      confirm-url:x:@.confirm-url
      secret:x:@.secret
```

What the above basically does, is to send a _"template email"_. A template email is an email
where you have template fields, that has variables that are dynamically substituted with some
sort of arguments. Such template emails in magic are simple files, typically HTML files,
containing dynamically substituted portions, such as the email below illustrates with its
`\{\{confirm-url\}\}` part.

```html
<p>
    Welcome as a registered user in AnarQ. However, before you
    can start posting, you will have to confirm your email address.
    You can confirm your email address by visiting the URL below.
</p>
<a href="{{confirm-url}}">Confirm your email address by clicking this link</a>
<p>
    If you didn't request this email, just ignore it - AnarQ will
    not send you anymore emails.
</p>
<p>
    Kind Regards,
    <br>
    <br>
    Superior Emperor and Benevolent Dictator @ AnarQ,
    <br>
    Thomas Hansen
</p>
```

The actual value of the `\{\{confirm-url\}\}` again, is passed in as **[substitutes]**/**[confirm-url]**. The
**[magic.emails.send]** dynamic slot again, will then create a personalised email, by substituting whatever
you pass in as substitutes with its template placeholder such as illustrated above. Of course, in order to
actually send emails though, you'll need to configure an SMTP server, which is typically done by adding
something such as the following to your _"appsettings.json"_ file.

```json
"magic": {
    "smtp": {
      "host": "smtp.sendgrid.net",
      "port": 465,
      "secure": true,
      "username": "apikey",
      "password": "SG.sdfSDF34GGDdfgDFG234SDF54gFDgdfgsd324",
      "from": {
        "name": "Thomas Hansen",
        "address": "thomas@servergardens.com"
      }
    }, etc ...
```

The above configuration is how it would typically look like if you're using SendGrid, but Magic supports
any SMTP server you wish.

### Returning files

Another interesting thing AnarQ does is to return contens of files. For instance the terms and
conditions to use AnarQ is actually just a Markdown file, wrapped inside an endpoint, such that the terms
can easily be modified according to your needs, allowing the endpoint that returns the terms immediately
return whatever terms you want your users to agree to before signing up. Below is the endpoint in its
entirety to illustrate one way you could return a file's content directly to the caller over a Hyperlambda
endpoint.

```
/*
 * Returns Terms and Conditions to use the site.
 */
io.file.load:/modules/anarq/data/tnc.md
.description:Returns the terms and conditions to use the site


/*
 * Making sure we add caching HTTP headers.
 */
response.headers.add
   Cache-Control:public, max-age=3600


/*
 * Returning value to caller.
 */
unwrap:x:+/*
return-nodes
   result:x:@io.file.load
```

What the above does is simply to load the _"tnc.md"_ file, add some HTTP caching, and return
the file as is to the caller.

### Database transactions

AnarQ requires database transactions in one place, which is when a comment it created. This is
because the database actually implements something referred to as _"materialised path"_,
allowing us to store data being a relational tree structure into an SQL database. However,
in order to accomplish this, we need to first insert our comment, retrieve its automatically
assigned ID, for then to afterwards update the post. During this process we need atomicity,
since if something goes wrong, we don't want _any_ changes to our database. You can see the
relevant code in the _"comment.post.hl"_ file, but its most important parts can be found below,
which is the part that creates the transaction.

```
/*
 * Connecting to database.
 */
data.connect:[generic|anarq]
   database-type:mysql


   /*
    * Creating a transation object two wrap both insert and update inside of,
    * to avoid race conditions when trying to retrieve post afterwards, resulting
    * in returning wrong path for post.
    */
   data.transaction.create
      database-type:mysql
```

* [Read more about materialised path here](https://dzone.com/articles/materialized-paths-tree-structures-relational-database)

### Dynamic Hyperlambda slots

AnarQ also creates its own dynamic Hyperlambda slots. This occurs in its _"magic.startup"_ folder,
who's name is important, since folders with that exact name inside of modules will have all
Hyperlambda files automatically executed during installation, and/or startup. If you check
out the file caller _"anarq.emails.comment-received.hl"_, you will see some code resembling
the following.

```
slots.create:anarq.emails.comment-received

   /*
    * Opening connection to database.
    */
   .email
   .name
   data.connect:[generic|anarq]
      database-type:mysql

// Etc ...
```

What this file does is to simply make sure as somebody is commenting on a post, the original
poster is notified through emails, unless he's turned _off_ email notifications.

### Dynamically creating its database

In addition, AnarQ also automatically creates its database during initialisation. This
is done in its _"create-database.hl"_ file, also inside of its _"magic.startup"_ folder, which
implies the file will always execute as Magic is started, and/or the module is initialised.
You can probably get a lot of ideas from that specific file in regards to how you'd like to
achieve something similar in your own apps.

## Wrapping up

In this tutorial we looked at some of the basic elements of AnarQ, to illustrate that Magic
is more than CRUD. If you want to download AnarQ and install in your own Magic server,
you can find it below.

* [Download AnarQ](https://github.com/polterguy/anarq)

Notice, as I wrote this article, I used AnarQ version 0.8, and I might expand on the project
in the future, implying some of the specific parts we walked through here are changed. Have
that in mind if you're dissecting a different version than what I used in this article.

* [Documentation](/documentation/)

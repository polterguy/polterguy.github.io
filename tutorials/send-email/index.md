# Sending emails from your web app

A 5 minute read, teaching you how to create an HTTP endpoint that allows
you to send an email. Also dives a bit into the async parts of Magic,
making your Magic apps scale 100x better, by releasing threads back
to the thread pool, during IO operations.

Although CRUD is important for most web apps, it's not enough, and
sometimes you need more complex logic, such as for instance the
ability to sending emails from your backend. But before you can
start sending emails, you'll have to configure your backend's
_"appsettings.json"_ file, such that you have email configurations,
that allows you to securely connect to an SMTP server.

Add the following to your _"appsettings.json"_ file, inside
your backend, using for instance Visual Studio or VS Code.

```json
{
   "magic":{
      "smtp":{
        "host":"smtp.gmail.com",
        "port":465,
        "secure":true,
        "username":"username@gmail.com",
        "password":"gmail-password",
        "from": {
           "name":"John Doe",
           "address":"john@doe.com",
        }
      }
   }
}
```

**Notice** - The _"magic"_ part already exists in your settings, so
the above _"smtp"_ parts, needs to be added _inside_
of your existing _"magic"_ section. You will also have to change
the actual settings to point to a valid SMTP server. The above
settings will normally work if you're using your GMail account,
you exchange your username/password combination with your GMail
credentials, and you enable your GMail account for _"insecure apps"_.

When you have done the above, you can create a new HTTP POST
endpoint inside your _"/modules/tutorials/"_ folder, and name
your file _"send-email.post.hl"_. Put the following content
into your file.

```
.arguments
   to:string
   subject:string
   body:string
validators.email:x:@.arguments/*/to
unwrap:x:+/**
wait.mail.smtp.send
   message
      to
         :x:@.arguments/*/to
      subject:x:@.arguments/*/subject
      entity:text/plain
         content:x:@.arguments/*/body
```

**Notice** - This time we are using an _"async"_ slot. This is
because our invocation to smtp.send starts with **[wait.]**.
This implies that as Magic is waiting for data to be returned
from the socket connection it is using to actually transmit
the email to your SMTP server, the web server thread will be
released back to the operating system. In general, this results
in sometimes 100 times better scaling in web apps that have
a _lot_ of users simultaneously consuming your web app.

We are also using the email validator above, before we
try to send our email. This validator will throw an exception
unless the expression it's pointing to, is a valid email
address. After you have saved your file, go to your _"Endpoints"_,
and find your send-email endpoint, and fill it out as follows.

![Sending an email](https://servergardens.files.wordpress.com/2020/09/send-email-tutorial.png)

Click the _"post"_ button, and your email is on its way.
Of course, you should replace the above _"to"_ argument with
a valid email address, preferably one of your own, such that
you can verify it's actually working, and actually sends
your email.

It's sometimes easy to get lost in Magic's CRUD parts, and
sure, automatically creating CRUD HTTP endpoints, wrapping
your database, is really cool. But Magic can do _much_ more
than CRUD. Hopefully this little 3 minute long read have
opened your eyes in regards to this.

* [Continue to extending Hyperlambda with C#](/tutorials/extending-hyperlambda)

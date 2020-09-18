# Creating a send email HTTP endpoint

Although CRUD is important for most web apps, it's not enough, and
sometimes you need more complex logic, such as for instance the
ability to sending emails from your backend. But before you can
start sending emails, you'll have to configure your backend's
_"appsettings.json"_ file with valid SMTP connection settings.
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

When you have done the above, you can create a new Hyperlamdba file
inside your _"/modules/tutorials/"_ folder, and name
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
released back to the operating system. This results
in 100x better scaling of your web app, since no thread is
blocked as Magic is waiting for IO to finish.

We are also using the email validator above, before we
try to send our email. This validator will throw an exception
unless the expression it's pointing to, is a valid email
address. After you have saved your file, go to your _"Endpoints"_,
and find your send-email endpoint, and fill it out as follows.

![Sending an email](https://servergardens.files.wordpress.com/2020/09/send-email-tutorial.png)

Click the _"post"_ button, and your email is on its way.
Of course, you should replace the above _"to"_ argument with
a valid email address, preferably one of your own emails, such that
you can verify it's actually working.

* [Continue to extending Hyperlambda with C#](/tutorials/extending-hyperlambda)

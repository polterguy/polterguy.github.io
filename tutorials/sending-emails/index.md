---
title: Sending emails with Hyperlambda and Magic
description: In this article we show you how you can use Magic and Hyperlambda to send emails, and how you can configure Magic to use an SMTP server of your chosing.
---

# Sending emails with Hyperlambda and Magic

Most web applications needs to send emails at some point. These can be simple _"Thank you for registering"_ emails,
to _"Reset your password"_ template emails, where you need to braid in the user's full name, his or her email address,
and additional data to create a customised email from some template of some sort. However, before you can send emails
at all, you'll have to configure Magic such that it has access to some SMTP server of some sort. Below you can see
the configuration settings related to this.

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
        "address":"john@doe.com"
      }
    }
  }
}
```

Notice, _keep_ the rest of your settings as is and make sure you only _add_ the above `smtp` section to your root
`magic` configuration object. The exact values of the above fields varies according to your particular SMTP server's
values of course, but if you want to use GMail as your SMTP server, all you need to do is to open up your GMail account
for _"Insecure apps"_ and change the above username/password to your GMail account's username and password. Below is a
screenshot of how you can edit your configuration settings using the _"Config"_ menu item in Magic.

![Configuring your SMTP settings](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/configuring-smtp.jpg)

At this point you can try your SMTP configuration be executing the following in Magic's _"Eval"_ menu item.

```
mail.smtp.send
   message
      to
         Your Name Here:your-email@address-here.com
      from
         Whatever From Name Here:whatever-email@address-here.com
      subject:Test email from Magic
      entity:text/plain
         content:This is a test!
```

Below is a screenshot of how this looks like for me.

![Sending an email using Hyperlambda](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/sending-email-from-hyperlambda.jpg)

## Internals

The above invocation to **[mail.smtp.send]** is given one **[message]** argument. Notice, you can supply as
many **[message]** arguments as you wish in a single invocation to the slot. This has some advantages since
each invocation to **[mail.smtp.send]** has to negotiate a new connection to your SMTP server, which carries
some overhead. Also notice the **[entity]** argument above. This declares a MIME entity, which is extremely
flexible in Magic, allowing you to reference files directly from disc as attachments, create multipart messages,
etc. For a slightly more complex example consider the following Hyperlambda.

```
mail.smtp.send
   message
      to
         Your Name Here:your-email@address-here.com
      from
         Whatever From Name Here:whatever-email@address-here.com
      subject:Test email from Magic

      entity:multipart/mixed

         entity:text/plain
            content:This is a test!

         entity:text/plain
            filename:/README.md
```

If you execute the above Hyperlambda, you will notice that it creates an attachment. The reasons for that
is because you've got a **[filename]** entity child argument to your `multipart/mixed` part. This results
in that the MIME parts of Magic automatically adds it as an attachment using the `Content-Disposition` header,
and adds the correct relative filename. You can use any feature from MIME as illustrated above in Magic and
Hyperlambda, to construct emails any ways you see fit. Below is a screenshot illustrating how it looks like
as I received the above email in my personal inbox.

![Reading my Hyperlambda email](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/gmail-email.jpg)

## Template emails

Typically when creating a web app needing to send emails, you've got a _"template"_ of some sort, which you
use as your foundation, for then to use this template, apply some string replacements to add personalised data,
before you send your email. Magic has strong support for sending such emails out of the box. More specifically
Hyperlambda contains a dynamic slot named **[magic.emails.send]** that allows you to create such _"braided"_
emails. However, this slot assumes you've already got a _"template"_ that you want to base your email
upon. Hence, for the sake of testing the slot, first make sure you create a file inside your _"/etc/"_ folder
named _"test-email.html"_ and add the following content to it. You can use Hyper IDE to create this file.

**Content of your "test-email.html" file**

&lt;p&gt;Thank you &#123;&#123;name&#125;&#125; for wanting to read my email. This makes me so jazzed!&lt;/p&gt;

&lt;p&gt;Feel free to &lt;a href="https://docs.aista.com"&gt;check out the docs&lt;/a&gt; for Aista Magic Cloud ^_^&lt;/p&gt;


Then execute the following Hyperlambda in your _"Eval"_ menu item.

```
signal:magic.emails.send
   subject:Template email from Hyperlambda
   email:your-email@address.com
   name:Your Name Here
   mime-type:text/html
   template-file:/etc/test-email.html
   substitutes
      name:Your Name Here
   attachments
      entity:text/plain
         filename:/README.md
      entity:text/plain
         filename:/exceptions.hl
```

Below is how it looks like if I send myself an email after having substituted the above **[email]** and **[name]**
argument(s).

![Reading my Hyperlambda template email](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/gmail-template-email.jpg)

As you can see above the &#123;&#123;name&#125;&#125; part from the template was automatically substituted
with my name. You can provide as many substitutions as you wish. Notice, how the attachments are automatically
transformed into attachments in the resulting email. If you want to further study the email capabilities of
Magic and Hyperlambda you can check out the documentation for [magic.lambda.mail](/documentation/magic.lambda.mail/)
and [magic.lambda.mime](/documentation/magic.lambda.mime/).

* Continue with [Expressions, slots and nodes](/tutorials/expressions-slots-nodes/)

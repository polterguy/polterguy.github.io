---
title: "How to use [mail.smtp.send]"
description: "How to use [mail.smtp.send] - mail.smtp.send    server       host:foo.com       port:123       secure:true       username:xxx       password:yyy    message       to          John Doe:john@doe.com       from          J..."
generated: true
guide: true
---

This is the guide to [`mail.smtp.send`](/reference/slots/mail/mail.smtp.send/), whose reference page has its arguments, constraints and declaration.

```
mail.smtp.send
   server
      host:foo.com
      port:123
      secure:true
      username:xxx
      password:yyy
   message
      to
         John Doe:john@doe.com
      from
         Jane Doe:jane@doe.com
      subject:Subject line
      entity:text/plain
         content:Body content
```

You can send multiple **[message]** objects at the same time, using the same SMTP connection and credentials.
This allows you to connect _once_ to the SMTP server, and use the same connection to send multiple emails.

The entirety of the **[server]** node above is optional, and if it's not given, it will be fetched from your
configuration settings. You can also override only one or two parts in your **[server]** segment above, and
have the system read the rest of the settings from your application's configuration. In addition, the **[from]**
node is also optional, assuming you have a default `from` configured in your configuration settings. Below are
the keys used to fetch configuration settings for SMTP connections, and from object, if not explicitly given as
part of the invocation.

* magic.smtp.host
* magic.smtp.port
* magic.smtp.secure
* magic.smtp.username
* magic.smtp.password
* magic.smtp.from.name
* magic.smtp.from.address

An example of how your configuration might look like, if you choose to use configuration settings,
instead of having to supply server configuration every time you invoke the slot, can be found below.

```
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

**FYI** - If you exchange the above username/password combination, and open your GMail account for _"insecure apps"_,
the above will allow you to send emails using your GMail account.

Assuming you have the above somewhere in your configuration, you can construct and send an email using something
like the following. Which probably makes things more convenient, allowing you to avoid thinking about connection
settings, from addresses, etc - And leave this as a part of your deployment transformation pipeline(s), etc.

```
mail.smtp.send
   message
      to
         Jane Doe:jane@doe.com
      subject:Subject line
      entity:text/plain
         content:Body content
```

You can also add **[cc]**, **[bcc]** and **[reply-to]** recipients for your emails, using the same structure you're using
for **[to]**. In addition you can attach files to your messages, by instead of adding a **[content]** node to your
invocation, adding a **[filename]** node, with a relative path pointing to the file you want to attach to your message.
Below is an example of an email with a single attachment.

```
mail.smtp.send
   message
      to
         Jane Doe:jane@doe.com
      subject:Subject line
      entity:multipart/mixed
        entity:text/plain
           content:Body content
        entity:text/plain
           filename:/files/foo.txt
```

To construct your email's **[message]** part, see the documentation for the [magic.lambda.mime](/plugins/magic.lambda.mime/) project.

**Notice** - You can also construct **[from]**, **[to]** and **[cc]** arguments such as follows.

```
mail.smtp.send
   message
      to
         .
            name:Jane Doe
            email:jane@doe.com
```

This makes it easier to dynamically **[unwrap]** arguments to the slot.

## Creating MIME messages

This project relies upon [magic.lambda.mime](/plugins/magic.lambda.mime/) for parsing MIME message. Magic's MIME project again, is a complete section in the documentation by itself, and for a detailed description, please refer to magic.lambda.mime's documentation. However, the basic idea is that a MIME message is actually a tree structure, allowing you to create MIME entities, that consists of children MIME entities, to add attachments etc to your emails. Below is an example of how to create a message with an attachment.

```
mail.smtp.send
   message
      to
         .
            email:someemail@whatever.com
            name:John Doe
      subject:Some subject line
      entity:multipart/mixed
         entity:text/plain
            content:Some text content
         entity:text/markdown
            headers
               Content-Disposition:@"attachment; filename=""README.md"""
            content:Some Markdown content here
```

The above will construct a plain text email with a Markdown file attachment. The point being that each child of the above **[headers]** node will be considered a MIME header for that particular entity, allowing you to supply MIME headers for specific entities in your tree hierarchy.

You can add any MIME header like the above code illustrates, including custom headers.

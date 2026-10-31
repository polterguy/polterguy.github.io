---
title: "How to use [mail.pop3.fetch]"
description: "How to use [mail.pop3.fetch] - To retrieve emails from a POP3 server is equally easy."
generated: true
guide: true
---

This is the guide to [`mail.pop3.fetch`](/reference/slots/mail/mail.pop3.fetch/), whose reference page has its arguments, constraints and declaration.

To retrieve emails from a POP3 server is equally easy. Below is an example.

```
mail.pop3.fetch
   server
      host:foo.com
      port:123
      secure:true
      username:xxx
      password:yyy
   max:int:50
   raw:bool:false
   .lambda

      /*
       * Some lambda object invoked once for every email fetched.
       * Given message as [.message] node structured as lambda.
       */
```

Just like its SMTP counterpart, the entirety of the above **[server]** node is optional, and fetched
from your configuration if omitted. Below are the keys used to fetch configuration settings for your
POP3 connection, if not explicitly given as part of invocation.

* magic.pop3.host
* magic.pop3.port
* magic.pop3.secure
* magic.pop3.username
* magic.pop3.password


You can find an example of how your configuration might look like below if you choose to use configuration
settings instead of having to supply server configuration every time you invoke the slot.

```
{
  "magic":{
    "pop3":{
      "host":"pop.gmail.com",
      "port":995,
      "secure":true,
      "username":"username@gmail.com",
      "password":"gmail-password",
    }
  }
}
```

**FYI** - If you exchange the above username/password combination, and open up your GMail account for _"insecure apps"_,
the above will allow you to send emails using your GMail account.

Notice, if **[raw]** is true, the message will _not_ be parsed and turned into a structural lambda object,
but passed into your **[.lambda]** as its raw MIME message instead. The default value for **[raw]** is false.
Your **[.lambda]** callback will be invoked for each message with a **[.message]** node, containing the
structured/raw version of the MIME message wrapping the actual email message. Refer to
the magic.lambda.mime project's documentation for details to understand this
structure. If you choose to retrieve messages in **[raw]** format, the message node's value will contain
the raw MIME message as text. If you choose this path, and you later want to actually parse the message,
to make it become a structured lambda object - You can use the **[mime.parse]** slot from magic.lambda.mime.

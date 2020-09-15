
# Magic Lambda Mail

[![Build status](https://travis-ci.com/polterguy/magic.lambda.mail.svg?master)](https://travis-ci.com/polterguy/magic.lambda.mail)

 SMTP and POP3 helpers for Magic. More specifically, this project contains the following POP3 and SMTP slots
 helpers for Magic.

1. **[mail.pop3.fetch]** - Fetches emails from some POP3 server
2. **[mail.smtp.send]** - Sends email(s) over an SMTP server

Both of the above slots have async (wait.) overrides for executing asynchronously.

## Sending email(s)

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

The entirety of the **[server]** node above is optional, and if not given, will be fetched from your
configuration settings, using the `IConfiguration` object, which is given through dependency injection.
You can also override only one or two parts in your **[server]** segment above, and have the system
read the rest of the settings from your application's configuration. In addition, the **[from]** node is also
optional, assuming you have a default `from` configured in your configuration settings. Below are the keys used
to fetch configuration settings for SMTP connections, and from object, if not explicitly given as part of
invocation.

* magic.smtp.host
* magic.smtp.port
* magic.smtp.secure
* magic.smtp.username
* magic.smtp.password
* magic.smtp.from.name
* magic.smtp.from.address

An example of how your configuration might look like, if you choose to use configuration settings,
instead of having to supply server configuration every time you invoke the slot.

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

**FYI** - If you exchange the above username/password combination, and open your GMail account for _"insecure apps"_,
the above will actually allow you to send emails using your GMail account.

Assuming you have the above somewhere in your configuration, you can construct and send an email using something
like the following. Which probably makes things more convenient, allowing you to avoid bothering about connection
settings, from addresses, etc - And leave this as a part of your Azure transformation pipeline(s), or something
similar.

```
mail.smtp.send
   message
      to
         Jane Doe:jane@doe.com
      subject:Subject line
      entity:text/plain
         content:Body content
```

You can also add **[cc]** and **[bcc]** recipients for your emails, using the same structure you're using for **[to]**.
In addition you can attach files to your messages, by instead of adding a **[content]** node to your invocation, adding
a **[filename]** node, with a relative path pointing to the file you want to attach to your message. Below is an example
of an email with a single attachment.

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
           filename:foo.txt
```

To construct your email's **[message]** part, [see Magic Mime for details](https://github.com/polterguy/magic.lambda.mime).

## Retrieving emails

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

Just like its SMTP counterpart, parts of, or the entirety of the above **[server]** node is optional.
Below are the keys used to fetch configuration settings for SMTP connections, if not explicitly given
as part of invocation.

* magic.pop3.host
* magic.pop3.port
* magic.pop3.secure
* magic.pop3.username
* magic.pop3.password

Notice, if **[raw]** is true, the message will _not_ be parsed and turned into a structural lambda object,
but passed into your **[.lambda]** as its raw MIME message instead. The default value for **[raw]** is false.

Your **[.lambda]** callback will be invoked with a single **[.message]** node, containing the
structured version of the MIME message wrapping the actual email message. Refer to
[see Magic Mime for details](https://github.com/polterguy/magic.lambda.mime) to understand this
structure. If you choose to retrieve messages in **[raw]** format, the message node's value will contain
the raw MIME message as text. If you choose this path, and you later want to actually parse the message,
to make it become a structured lambda object - You can use the **[mime.parse]** slot from Magic Lambda Mime.

## Quality gates

- [![Build status](https://travis-ci.com/polterguy/magic.lambda.mail.svg?master)](https://travis-ci.com/polterguy/magic.lambda.mail)
- [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.mail&metric=alert_status)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda,mail)
- [![Bugs](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.mail&metric=bugs)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.mail)
- [![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.mail&metric=code_smells)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.mail)
- [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.mail&metric=coverage)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.mail)
- [![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.mail&metric=duplicated_lines_density)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.mail)
- [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.mail&metric=ncloc)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.mail)
- [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.mail&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.mail)
- [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.mail&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.mail)
- [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.mail&metric=security_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.mail)
- [![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.mail&metric=sqale_index)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.mail)
- [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.mail&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.mail)

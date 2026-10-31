---
title: "[mail.smtp.send]"
description: "mail.smtp.send is a slot in the mail namespace of Magic Cloud. Sends one or more email messages through SMTP from child [message] nodes."
generated: true
llms: "guide"
slot_json: "/reference/slots/mail/mail.smtp.send/slot.json"
---

`mail.smtp.send` is a slot in the `mail` namespace, in Hyperlambda, the language of Magic Cloud. Sends one or more email messages through SMTP from child [message] nodes.

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[message]` | lambda | yes | Email message to send. Can be repeated. |
| `[message]` / `[to]` | lambda | yes | Email address collection. |
| `[message]` / `[to]` / _unnamed child node_ | lambda | yes | Structured address containing [email] and optional [name]. Can be repeated. |
| `[message]` / `[to]` / _unnamed child node_ / `[email]` | string | yes | Email address. |
| `[message]` / `[to]` / _unnamed child node_ / `[name]` | string | no | Display name. |
| `[message]` / `[entity]` | string | yes | MIME entity declaration for the message body; node value is the MIME content type. |
| `[message]` / `[entity]` / `[headers]` | lambda | no | MIME headers. |
| `[message]` / `[entity]` / `[headers]` / _any node name_ | string | no | Header name and value. Can be repeated. |
| `[message]` / `[entity]` / `[content]` | string | no | Inline MIME part content. |
| `[message]` / `[entity]` / `[filename]` | string | no | File path to use as MIME part content. |
| `[message]` / `[subject]` | string | no | Message subject. |
| `[message]` / `[from]` | lambda | no | Email address collection. |
| `[message]` / `[from]` / _unnamed child node_ | lambda | no | Structured address containing [email] and optional [name]. Can be repeated. |
| `[message]` / `[from]` / _unnamed child node_ / `[email]` | string | yes | Email address. |
| `[message]` / `[from]` / _unnamed child node_ / `[name]` | string | no | Display name. |
| `[message]` / `[cc]` | lambda | no | Email address collection. |
| `[message]` / `[cc]` / _unnamed child node_ | lambda | no | Structured address containing [email] and optional [name]. Can be repeated. |
| `[message]` / `[cc]` / _unnamed child node_ / `[email]` | string | yes | Email address. |
| `[message]` / `[cc]` / _unnamed child node_ / `[name]` | string | no | Display name. |
| `[message]` / `[bcc]` | lambda | no | Email address collection. |
| `[message]` / `[bcc]` / _unnamed child node_ | lambda | no | Structured address containing [email] and optional [name]. Can be repeated. |
| `[message]` / `[bcc]` / _unnamed child node_ / `[email]` | string | yes | Email address. |
| `[message]` / `[bcc]` / _unnamed child node_ / `[name]` | string | no | Display name. |
| `[message]` / `[reply-to]` | lambda | no | Email address collection. |
| `[message]` / `[reply-to]` / _unnamed child node_ | lambda | no | Structured address containing [email] and optional [name]. Can be repeated. |
| `[message]` / `[reply-to]` / _unnamed child node_ / `[email]` | string | yes | Email address. |
| `[message]` / `[reply-to]` / _unnamed child node_ / `[name]` | string | no | Display name. |

_Nodes nested deeper than 6 levels, and nodes that repeat one of their own ancestors, are not listed. The JSON declaration below has all of them._

### Guide

<!-- guide -->
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

#### Creating MIME messages

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
<!-- /guide -->

### JSON declaration

This is the complete declaration of `mail.smtp.send`, as the running system describes it. It is also published as [slot.json](slot.json).

<details class="slot-declaration slot-json" data-src="slot.json">
<summary>JSON declaration (loads when opened)</summary>
<noscript><p><a href="slot.json">Open the JSON declaration</a>.</p></noscript>
</details>

---

[&larr; `mail.pop3.fetch`](/reference/slots/mail/mail.pop3.fetch/) | [all `mail.*` slots](/reference/slots/mail/)


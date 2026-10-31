---
title: "[mail.pop3.fetch]"
description: "mail.pop3.fetch is a slot in the mail namespace of Magic Cloud. Fetches messages from a POP3 mailbox using child-node options and a required [.lambda] callback."
generated: true
llms: "guide"
slot_json: "/reference/slots/mail/mail.pop3.fetch/slot.json"
---

`mail.pop3.fetch` is a slot in the `mail` namespace, in Hyperlambda, the language of Magic Cloud. Fetches messages from a POP3 mailbox using child-node options and a required [.lambda] callback.

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[.lambda]` | lambda | yes | Callback evaluated once per fetched message with [.message] injected. |
| `[raw]` | bool | no | Whether to pass raw MIME text to the callback. |
| `[max]` | int | no | Maximum number of messages to fetch. |

### Guide

<!-- guide -->
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
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.mail](/plugins/magic.lambda.mail/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `mail.pop3.fetch`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "mail.pop3.fetch",
  "description": "Fetches messages from a POP3 mailbox using child-node options and a required [.lambda] callback",
  "signature": {
    "children": {
      "raw": {
        "type": "bool",
        "description": "Whether to pass raw MIME text to the callback",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      },
      "max": {
        "type": "int",
        "description": "Maximum number of messages to fetch",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      },
      ".lambda": {
        "type": "lambda",
        "description": "Callback evaluated once per fetched message with [.message] injected",
        "required": true,
        "mode": "ExecutableLambda",
        "cardinality": "ExactlyOne",
        "role": "Callback",
        "evaluation": "EvalBlock",
        "projection": "Self"
      }
    }
  }
}
```

</details>

---

[all `mail.*` slots](/reference/slots/mail/) | [`mail.smtp.send` &rarr;](/reference/slots/mail/mail.smtp.send/)


---
title: "[mail.pop3.fetch]"
description: "mail.pop3.fetch is a slot in the mail namespace of Magic Cloud. Fetches messages from a POP3 mailbox using child-node options and a required [.lambda] callback."
generated: true
llms: false
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
| `[server]` | lambda | no | Connection settings, where anything left out comes from the configured server. |
| `[server]` / `[host]` | string | no | Host name of the server. |
| `[server]` / `[port]` | int | no | Port of the server. |
| `[server]` / `[secure]` | bool | no | Whether to connect securely. |
| `[server]` / `[username]` | string | no | User name to authenticate with. |
| `[server]` / `[password]` | string | no | Password to authenticate with. |

### Guide

[How to use `mail.pop3.fetch`](/plugins/magic.lambda.mail/mail.pop3.fetch/)

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
      "server": {
        "type": "lambda",
        "description": "Connection settings, where anything left out comes from the configured server",
        "required": false,
        "mode": "StructuredArguments",
        "cardinality": "ZeroOrOne",
        "role": "StructuredObject",
        "projection": "StructuredTree",
        "children": {
          "host": {
            "type": "string",
            "description": "Host name of the server",
            "required": false,
            "mode": "ValueOrExpression",
            "cardinality": "ZeroOrOne",
            "role": "Option",
            "projection": "Value"
          },
          "port": {
            "type": "int",
            "description": "Port of the server",
            "required": false,
            "mode": "ValueOrExpression",
            "cardinality": "ZeroOrOne",
            "role": "Option",
            "projection": "Value"
          },
          "secure": {
            "type": "bool",
            "description": "Whether to connect securely",
            "required": false,
            "mode": "ValueOrExpression",
            "cardinality": "ZeroOrOne",
            "role": "Option",
            "projection": "Value"
          },
          "username": {
            "type": "string",
            "description": "User name to authenticate with",
            "required": false,
            "mode": "ValueOrExpression",
            "cardinality": "ZeroOrOne",
            "role": "Option",
            "projection": "Value"
          },
          "password": {
            "type": "string",
            "description": "Password to authenticate with",
            "required": false,
            "mode": "ValueOrExpression",
            "cardinality": "ZeroOrOne",
            "role": "Option",
            "projection": "Value"
          }
        }
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


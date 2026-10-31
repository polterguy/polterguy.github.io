---
title: magic.lambda.mail slot reference
description: Every slot in magic.lambda.mail with its value, arguments and return value, generated from the source code.
generated: true
---

_This page is generated from the `[Slot]` attributes in the source code of [magic.lambda.mail](https://github.com/polterguy/magic/tree/master/plugins/magic.lambda.mail). Do not edit it; improve the attribute instead. The hand-written guide is at [magic.lambda.mail](/plugins/magic.lambda.mail/)._

## [mail.pop3.fetch]

Fetches messages from a POP3 mailbox using child-node options and a required [.lambda] callback.


| Argument | Type | Required | Description |
|---|---|---|---|
| `[raw]` | bool | no | Whether to pass raw MIME text to the callback |
| `[max]` | int | no | Maximum number of messages to fetch |
| `[.lambda]` | lambda | yes | Callback evaluated once per fetched message with [.message] injected |

Guide: [How to use [mail.pop3.fetch]](/plugins/magic.lambda.mail/#how-to-use-mailpop3fetch)

## [mail.smtp.send]

Sends one or more email messages through SMTP from child [message] nodes.


| Argument | Type | Required | Description |
|---|---|---|---|
| `[subject]` | string | no | Message subject |
| `[name]` | string | no | Display name |
| `[email]` | string | yes | Email address |
| `[.]` | lambda | no | Structured address containing [email] and optional [name] |

Guide: [How to use [mail.smtp.send]](/plugins/magic.lambda.mail/#how-to-use-mailsmtpsend)


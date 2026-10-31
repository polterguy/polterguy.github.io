---
title: mail.* slots
description: The 2 slots named mail.* in Magic Cloud and Hyperlambda, with their arguments and return values, generated from the running system.
generated: true
---

_Generated from the running system, see [how this reference is built](/reference/slots/). Do not edit this page._

## [mail.pop3.fetch]

Fetches messages from a POP3 mailbox using child-node options and a required [.lambda] callback.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[raw]` | bool | no | Whether to pass raw MIME text to the callback. |
| `[max]` | int | no | Maximum number of messages to fetch. |
| `[.lambda]` | lambda | yes | Callback evaluated once per fetched message with [.message] injected. |

Guide: [How to use [mail.pop3.fetch]](/plugins/magic.lambda.mail/#how-to-use-mailpop3fetch)

## [mail.smtp.send]

Sends one or more email messages through SMTP from child [message] nodes.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[message]` | lambda | yes | Email message to send. Can be repeated. |
| `[message]` / `[subject]` | string | no | Message subject. |
| `[message]` / `[to]` | lambda | yes | Email address collection. |
| `[message]` / `[to]` / _unnamed child node_ | lambda | yes | Structured address containing [email] and optional [name]. Can be repeated. |
| `[message]` / `[from]` | lambda | no | Email address collection. |
| `[message]` / `[from]` / _unnamed child node_ | lambda | no | Structured address containing [email] and optional [name]. Can be repeated. |
| `[message]` / `[cc]` | lambda | no | Email address collection. |
| `[message]` / `[cc]` / _unnamed child node_ | lambda | no | Structured address containing [email] and optional [name]. Can be repeated. |
| `[message]` / `[bcc]` | lambda | no | Email address collection. |
| `[message]` / `[bcc]` / _unnamed child node_ | lambda | no | Structured address containing [email] and optional [name]. Can be repeated. |
| `[message]` / `[reply-to]` | lambda | no | Email address collection. |
| `[message]` / `[reply-to]` / _unnamed child node_ | lambda | no | Structured address containing [email] and optional [name]. Can be repeated. |
| `[message]` / `[entity]` | string | yes | MIME entity declaration for the message body; node value is the MIME content type. |
| `[message]` / `[entity]` / `[headers]` | lambda | no | MIME headers. |
| `[message]` / `[entity]` / `[content]` | string | no | Inline MIME part content. |
| `[message]` / `[entity]` / `[filename]` | string | no | File path to use as MIME part content. |

_Nodes nested deeper than 3 levels, and nodes that repeat one of their own ancestors, are not listed._

Guide: [How to use [mail.smtp.send]](/plugins/magic.lambda.mail/#how-to-use-mailsmtpsend)


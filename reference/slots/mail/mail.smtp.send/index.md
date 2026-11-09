---
title: "[mail.smtp.send]"
description: "mail.smtp.send is a slot in the mail namespace of Magic Cloud. Sends one or more email messages through SMTP from child [message] nodes."
generated: true
llms: false
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
| `[server]` | lambda | no | Connection settings, where anything left out comes from the configured server. |
| `[server]` / `[host]` | string | no | Host name of the server. |
| `[server]` / `[port]` | int | no | Port of the server. |
| `[server]` / `[secure]` | bool | no | Whether to connect securely. |
| `[server]` / `[username]` | string | no | User name to authenticate with. |
| `[server]` / `[password]` | string | no | Password to authenticate with. |

_Nodes nested deeper than 6 levels, and nodes that repeat one of their own ancestors, are not listed. The JSON declaration below has all of them._

### Guide

[How to use `mail.smtp.send`](/plugins/magic.lambda.mail/mail.smtp.send/)

### JSON declaration

This is the complete declaration of `mail.smtp.send`, as the running system describes it. It is also published as [slot.json](slot.json).

<details class="slot-declaration slot-json" data-src="slot.json">
<summary>JSON declaration (loads when opened)</summary>
<noscript><p><a href="slot.json">Open the JSON declaration</a>.</p></noscript>
</details>

---

[&larr; `mail.pop3.fetch`](/reference/slots/mail/mail.pop3.fetch/) | [all `mail.*` slots](/reference/slots/mail/)


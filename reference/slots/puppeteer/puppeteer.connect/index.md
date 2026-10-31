---
title: "[puppeteer.connect]"
description: "puppeteer.connect is a slot in the puppeteer namespace of Magic Cloud. Creates or reuses a Puppeteer browser session."
generated: true
llms: false
slot_json: "/reference/slots/puppeteer/puppeteer.connect/slot.json"
---

`puppeteer.connect` is a slot in the `puppeteer` namespace, in Hyperlambda, the language of Magic Cloud. Creates or reuses a Puppeteer browser session.

* **Returns**: Resolves to the created Puppeteer session ID
* **Scope**: provides `puppeteer-session` - Creates an open Puppeteer browser session scope for puppeteer.* slots

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| `[args]` | string\|lambda | no | Browser launch arguments. |
| `[args]` / _unnamed child node_ | string | no | Argument value. Can be repeated. |
| `[executable]` | string | no | Browser executable path. |
| `[executable-path]` | string | no | Browser executable path. |
| `[headless]` | bool | no | Whether the browser should run headless. Default: `true`. |
| `[max-lifetime-minutes]` | int | no | Maximum session lifetime in minutes. |
| `[timeout]` | int | no | Browser launch timeout in milliseconds. |
| `[timeout-minutes]` | int | no | Idle timeout in minutes. |
| `[user-data-dir]` | string | no | Browser user data directory. |

### Constraints

* **AtMostOneOf**: [executable] and [executable-path] are aliases; supply at most one (`[executable]`, `[executable-path]`)

Guide: [How to use [puppeteer.connect]](/plugins/magic.lambda.puppeteer/#puppeteerconnect)

### JSON declaration

This is the complete declaration of `puppeteer.connect`, as the running system describes it. It is also published as [slot.json](slot.json).

<details class="slot-declaration slot-json" data-src="slot.json">
<summary>JSON declaration (loads when opened)</summary>
<noscript><p><a href="slot.json">Open the JSON declaration</a>.</p></noscript>
</details>

---

[&larr; `puppeteer.close`](/reference/slots/puppeteer/puppeteer.close/) | [all `puppeteer.*` slots](/reference/slots/puppeteer/) | [`puppeteer.content` &rarr;](/reference/slots/puppeteer/puppeteer.content/)


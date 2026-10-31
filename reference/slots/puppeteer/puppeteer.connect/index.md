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

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[timeout-minutes]` | int | no | Idle timeout in minutes. |
| `[max-lifetime-minutes]` | int | no | Maximum session lifetime in minutes. |
| `[headless]` | bool | no | Whether the browser should run headless. Default: `true`. |
| `[timeout]` | int | no | Browser launch timeout in milliseconds. |
| `[args]` | string\|lambda | no | Browser launch arguments. |
| `[args]` / _unnamed child node_ | string | no | Argument value. Can be repeated. |
| `[user-data-dir]` | string | no | Browser user data directory. |
| `[executable]` | string | no | Browser executable path. |
| `[executable-path]` | string | no | Browser executable path. |

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


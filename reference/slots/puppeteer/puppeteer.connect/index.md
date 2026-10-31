---
title: "[puppeteer.connect]"
description: "puppeteer.connect is a slot in the puppeteer namespace of Magic Cloud. Creates or reuses a Puppeteer browser session."
generated: true
llms: "guide"
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

### Guide

<!-- guide -->
Launches Chromium, opens a page, and returns a `session_id`.

Arguments:

* `headless` - Boolean. Launch Chromium in headless mode. Defaults to true.
* `executable` - Full path to Chromium/Chrome binary.
* `executable-path` - Alias for `executable`.
* `timeout` - Launch timeout in milliseconds.
* `user-data-dir` - Directory for Chromium user data.
* `args` - Additional Chromium arguments. Each child value is one argument string.
* `timeout-minutes` - Sliding inactivity timeout in minutes. Defaults to 15.
* `max-lifetime-minutes` - Maximum session lifetime in minutes. Defaults to 120.

Examples:

```
puppeteer.connect
```

```
puppeteer.connect
   headless:true
   executable:"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
   timeout:30000
   args
      .:--no-sandbox
      .:--disable-dev-shm-usage
   timeout-minutes:30
   max-lifetime-minutes:120
```
<!-- /guide -->

### JSON declaration

This is the complete declaration of `puppeteer.connect`, as the running system describes it. It is also published as [slot.json](slot.json).

<details class="slot-declaration slot-json" data-src="slot.json">
<summary>JSON declaration (loads when opened)</summary>
<noscript><p><a href="slot.json">Open the JSON declaration</a>.</p></noscript>
</details>

---

[&larr; `puppeteer.close`](/reference/slots/puppeteer/puppeteer.close/) | [all `puppeteer.*` slots](/reference/slots/puppeteer/) | [`puppeteer.content` &rarr;](/reference/slots/puppeteer/puppeteer.content/)


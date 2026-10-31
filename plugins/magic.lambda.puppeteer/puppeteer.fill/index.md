---
title: "How to use [puppeteer.fill]"
description: "How to use [puppeteer.fill] - Clears and types text into a selector."
generated: true
guide: true
---

This is the guide to [`puppeteer.fill`](/reference/slots/puppeteer/puppeteer.fill/), whose reference page has its arguments, constraints and declaration.

Clears and types text into a selector.

Arguments:

* Slot value - Session identifier.
* `selector` - CSS selector to fill.
* `text` - Text to type after clearing.
* `config-key` - Configuration key resolving the text value.
* `delay` - Delay between key presses in milliseconds.

Supply exactly one of `text` or `config-key`.

Examples:

```
puppeteer.fill:SESSION_ID
   selector:"#email"
   text:"thomas@gaiasoul.com"
```

```
puppeteer.fill:SESSION_ID
   selector:"#password"
   config-key:"magic:secrets:example-password"
```

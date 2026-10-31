---
title: "How to use [puppeteer.type]"
description: "How to use [puppeteer.type] - Types text into a selector."
generated: true
guide: true
---

This is the guide to [`puppeteer.type`](/reference/slots/puppeteer/puppeteer.type/), whose reference page has its arguments, constraints and declaration.

Types text into a selector.

Arguments:

* Slot value - Session identifier.
* `selector` - CSS selector to type into.
* `text` - Text to type.
* `config-key` - Configuration key resolving the text value.
* `delay` - Delay between key presses in milliseconds.

Supply exactly one of `text` or `config-key`.

Examples:

```
puppeteer.type:SESSION_ID
   selector:"#name"
   text:"Thomas Hansen"
```

```
puppeteer.type:SESSION_ID
   selector:"#info"
   text:"Hello from AI agent"
   delay:25
```

```
puppeteer.type:SESSION_ID
   selector:"#password"
   config-key:"magic:secrets:example-password"
```

---
title: "How to use [puppeteer.evaluate]"
description: "How to use [puppeteer.evaluate] - Evaluates a JavaScript expression in the page."
generated: true
guide: true
---

This is the guide to [`puppeteer.evaluate`](/reference/slots/puppeteer/puppeteer.evaluate/), whose reference page has its arguments, constraints and declaration.

Evaluates a JavaScript expression in the page.

Arguments:

* Slot value - Session identifier.
* `expression` - JavaScript expression string.
* `args` - Optional arguments for JS function invocation. Each child value is one argument.

Examples:

```
puppeteer.evaluate:SESSION_ID
   expression:"document.title"
```

```
puppeteer.evaluate:SESSION_ID
   expression:"typeof window.mcaptcha"
```

---
title: "How to use [puppeteer.goto]"
description: "How to use [puppeteer.goto] - Navigates to a URL. Arguments: Examples:"
generated: true
guide: true
---

The reference page of [`puppeteer.goto`](/reference/slots/puppeteer/puppeteer.goto/) has its arguments, constraints and declaration.

Navigates to a URL.

Arguments:

* Slot value - Session identifier.
* `url` - URL to navigate to.
* `timeout` - Navigation timeout in milliseconds.
* `wait-until` - One of `load`, `domcontentloaded`, `networkidle0`, `networkidle2`.

Examples:

```
puppeteer.goto:SESSION_ID
   url:"https://ainiro.io"
```

```
puppeteer.goto:SESSION_ID
   url:"https://ainiro.io"
   timeout:30000
   wait-until:networkidle2
```

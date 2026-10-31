---
title: "How to use [puppeteer.screenshot]"
description: "How to use [puppeteer.screenshot] - Saves a screenshot to disk."
generated: true
guide: true
---

This is the guide to [`puppeteer.screenshot`](/reference/slots/puppeteer/puppeteer.screenshot/), whose reference page has its arguments, constraints and declaration.

Saves a screenshot to disk.

Arguments:

* Slot value - Session identifier.
* `filename` - Output file path.
* `full-page` - Boolean. Capture full scrollable page.
* `type` - `png` or `jpeg`.
* `quality` - JPEG quality 0-100 (only for `jpeg`).

Examples:

```
puppeteer.screenshot:SESSION_ID
   filename:"/etc/tmp/example.png"
   full-page:true
```

```
puppeteer.screenshot:SESSION_ID
   filename:"/etc/tmp/example.jpg"
   type:jpeg
   quality:85
```

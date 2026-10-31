---
title: "How to use [puppeteer.wait-for-url]"
description: "How to use [puppeteer.wait-for-url] - Waits until the page URL matches."
generated: true
guide: true
---

This is the guide to [`puppeteer.wait-for-url`](/reference/slots/puppeteer/puppeteer.wait-for-url/), whose reference page has its arguments, constraints and declaration.

Waits until the page URL matches.

Arguments:

* Slot value - Session identifier.
* `url` - URL string to wait for.
* `timeout` - Timeout in milliseconds.

Examples:

```
puppeteer.wait-for-url:SESSION_ID
   url:"https://ainiro.io/contact-us"
```

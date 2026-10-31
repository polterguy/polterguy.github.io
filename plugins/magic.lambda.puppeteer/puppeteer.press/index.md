---
title: "How to use [puppeteer.press]"
description: "How to use [puppeteer.press] - Presses a key on a selector."
generated: true
guide: true
---

This is the guide to [`puppeteer.press`](/reference/slots/puppeteer/puppeteer.press/), whose reference page has its arguments, constraints and declaration.

Presses a key on a selector.

Arguments:

* Slot value - Session identifier.
* `selector` - CSS selector to focus.
* `key` - Key name (for example `Enter`).
* `delay` - Delay in milliseconds.

Examples:

```
puppeteer.press:SESSION_ID
   selector:"#submit_contact_form_button"
   key:Enter
```

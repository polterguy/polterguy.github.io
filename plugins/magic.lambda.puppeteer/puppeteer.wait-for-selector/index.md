---
title: "How to use [puppeteer.wait-for-selector]"
description: "How to use [puppeteer.wait-for-selector] - Waits until a selector appears in the DOM."
generated: true
guide: true
---

The reference page of [`puppeteer.wait-for-selector`](/reference/slots/puppeteer/puppeteer.wait-for-selector/) has its arguments, constraints and declaration.

Waits until a selector appears in the DOM.

Arguments:

* Slot value - Session identifier.
* `selector` - CSS selector to wait for.
* `timeout` - Timeout in milliseconds.
* `visible` - Boolean. Require element to be visible.
* `hidden` - Boolean. Require element to be hidden.

Examples:

```
puppeteer.wait-for-selector:SESSION_ID
   selector:"#name"
   visible:true
```

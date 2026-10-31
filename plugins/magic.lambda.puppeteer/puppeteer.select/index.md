---
title: "How to use [puppeteer.select]"
description: "How to use [puppeteer.select] - Selects option values from a selector."
generated: true
guide: true
---

This is the guide to [`puppeteer.select`](/reference/slots/puppeteer/puppeteer.select/), whose reference page has its arguments, constraints and declaration.

Selects option values from a selector.

Arguments:

* Slot value - Session identifier.
* `selector` - CSS selector for a `<select>` element.
* `values` - Values to select. Provide as children or a comma-separated string.

Examples:

```
puppeteer.select:SESSION_ID
   selector:"#plan"
   values
      .:basic
      .:pro
```

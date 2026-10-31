---
title: "How to use [puppeteer.click]"
description: "How to use [puppeteer.click] - Clicks a selector. Arguments: Examples: puppeteer.click:SESSIONID    selector:\"#submitcontactformbutton\" puppeteer.click:SESSIONID    selector:\"#submitcontactformbutton\"    click-count:2"
generated: true
guide: true
---

The reference page of [`puppeteer.click`](/reference/slots/puppeteer/puppeteer.click/) has its arguments, constraints and declaration.

Clicks a selector.

Arguments:

* Slot value - Session identifier.
* `selector` - CSS selector to click.
* `button` - Mouse button: `left`, `middle`, or `right`.
* `click-count` - Number of clicks.
* `delay` - Delay between down and up in milliseconds.

Examples:

```
puppeteer.click:SESSION_ID
   selector:"#submit_contact_form_button"
```

```
puppeteer.click:SESSION_ID
   selector:"#submit_contact_form_button"
   click-count:2
```

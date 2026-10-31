---
title: "How to use [validators.recaptcha]"
description: "How to use [validators.recaptcha] - This is probably the most complex validator, and requires 3 arguments."
generated: true
guide: true
---

The reference page of [`validators.recaptcha`](/reference/slots/validators/validators.recaptcha/) has its arguments, constraints and declaration.

This is probably the most complex validator, and requires 3 arguments.

* __[site-key]__ - Site key as provided to you by Google's reCAPTCHA admin panel
* __[secret]__ - Secret as provided to you by Google's reCAPTCHA admin panel
* __[min]__ - Minimum value, a decimal value between 0 and 1. A good value here is typically 0.3

To use this validator you will need a Google reCAPTCHA account, version 3, at which point you can use it as
follows.

```
validators.recaptcha:x:@.arguments/*/recaptcha_value
   site-key:xyz
   secret:qwerty
   min:decimal:0.3
```

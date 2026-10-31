---
title: "How to use [validators.email]"
description: "How to use [validators.email] - This slot takes no arguments besides an expression, and will throw an exception unless the value of the node the expression is leading to is a valid email address."
generated: true
guide: true
---

The reference page of [`validators.email`](/reference/slots/validators/validators.email/) has its arguments, constraints and declaration.

This slot takes no arguments besides an expression, and will throw an exception unless the value of the node
the expression is leading to is a valid email address. Below is example usage.

```
.arg:foo@bar.com
validators.email:x:@.arg
```

---
title: "How to use [validators.regex]"
description: "How to use [validators.regex] - This validator requires a [regex] argument, that is a regular expression that must match the argument specified."
generated: true
guide: true
---

The reference page of [`validators.regex`](/reference/slots/validators/validators.regex/) has its arguments, constraints and declaration.

This validator requires a **[regex]** argument, that is a regular expression that must match the argument
specified. Usage can be found below.

```
.arguments
   foo:howdy world
validators.regex:x:@.arguments/*/foo
   regex:howdy
```

If you remove the _"howdy"_ parts of your above argument, an exception will be thrown.

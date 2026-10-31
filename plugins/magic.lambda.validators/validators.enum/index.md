---
title: "How to use [validators.enum]"
description: "How to use [validators.enum] - This validator will throw an exception unless the specified string argument is one of the legal values."
generated: true
guide: true
---

The reference page of [`validators.enum`](/reference/slots/validators/validators.enum/) has its arguments, constraints and declaration.

This validator will throw an exception unless the specified string argument is one of the legal values. Usage
could be as follows.

```
validators.enum:x:@.arguments/*/enum_value
   .:val1
   .:val2
```

If the above **[enum_value]** is not either `val1` or `val2` the validator will throw an exception.

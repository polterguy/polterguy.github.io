---
title: "How to use [csv2lambda]"
description: "How to use [csv2lambda] - This slot converts a CSV string into a lambda object."
generated: true
guide: true
---

The reference page of [`csv2lambda`](/reference/slots/core/csv2lambda/) has its arguments, constraints and declaration.

This slot converts a CSV string into a lambda object. In its simplest form it would resemble the following.

```
.csv:@"name,age
Thomas Hansen,47
John Doe,67"

csv2lambda:x:@.csv
```

It can optionally take a type declaration through a **[types]** argument, which allows you to add typing support
to the slot.

---
title: "How to use [data.execute]"
description: "How to use [data.execute] - This slot should be used if you don't expect any type of result at all, such as in for instance delete or update invocations, where you don't care about the result of the operation."
generated: true
guide: true
---

The reference page of [`data.execute`](/reference/slots/data/data.execute/) has its arguments, constraints and declaration.

This slot should be used if you don't expect any type of result at all, such as in for instance
delete or update invocations, where you don't care about the result of the operation. You can
find an example below.

```
data.connect:sakila

   // Notice, will throw! (hopefully!)
   data.execute:delete from non_existing_table
```

Yet again, prefer **[data.delete]** if you can.

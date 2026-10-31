---
title: "How to use [data.scalar]"
description: "How to use [data.scalar] - This slot is similar to the [data.select] slot, but will only return one value as the value of its node after execution."
generated: true
guide: true
---

The reference page of [`data.scalar`](/reference/slots/data/data.scalar/) has its arguments, constraints and declaration.

This slot is similar to the **[data.select]** slot, but will only return one value as the
value of its node after execution. This slot is typically used for aggregate results. You can see
an example below.

```
data.connect:sakila
   data.scalar:select count(*) from actor
```

After execution, your result will resemble the following.

```
data.connect
   data.scalar:long:200
```

Yet again you should prefer the **[data.\*]** slots if you can.

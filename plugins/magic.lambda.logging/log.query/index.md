---
title: "How to use [log.query]"
description: "How to use [log.query] - To retrieve log items sequentially you can use [log.query]."
generated: true
guide: true
---

The reference page of [`log.query`](/reference/slots/log/log.query/) has its arguments, constraints and declaration.

To retrieve log items sequentially you can use **[log.query]**. This slot can optionally take a **[from]** argument
being the id of an existing log item from where to start retrieving items, and a **[max]** argument being the maximum
number of records to return. If no **[max]** argument is specified, the default value of this is 10. In addition the
invocation can be fiven a string as its value, which if given must match the content of your log items for an item
to be returned. Below is an example of usage.

```
log.query:"We successfully authenticated user 'root'"
   from:555
   max:20
```

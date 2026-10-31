---
title: "Querying your log"
description: "Querying your log - your particular log implementation can actually do what you need for it to do, since not all implementations have the same capabilities - Implying things such as filtering log items according to conte"
generated: true
---

This page is part of the [magic.lambda.logging](/plugins/magic.lambda.logging/) documentation.

**Notice** - To see the capabilities of your particular log implementation please invoke **[\[log.capabilities\]](/reference/slots/log/log.capabilities/)** and verify
your particular log implementation can actually do what you need for it to do, since not all implementations have the
same capabilities - Implying things such as filtering log items according to content, and/or timeshifting log items, etc,
might not be implemented for your particular implementation.

To retrieve log items sequentially you can use **[\[log.query\]](/reference/slots/log/log.query/)**. This slot can optionally take a **[from]** argument
being the id of an existing log item from where to start retrieving items, and a **[max]** argument being the maximum
number of records to return. If no **[max]** argument is specified, the default value of this is 10. In addition the
invocation can be fiven a string as its value, which if given must match the content of your log items for an item
to be returned. Below is an example of usage.

```
log.query:"We successfully authenticated user 'root'"
   from:555
   max:20
```

The above will return log items starting from id 554 and down, and return only 20 records, and all returned records
will have a content value of _"We successfully authenticated user 'root'"_. To return a single log item you can use
**[\[log.get\]](/reference/slots/log/log.get/)**  and pass in the id of the log item you want to retrieve as its value.

**Notice** - If your particular log implementation does not support querying you _cannot_ query items
according to content as illustrated above, but rather only page items. Invoke **[\[log.capabilities\]](/reference/slots/log/log.capabilities/)** to see if
your implementation supports querying before relying upon its existence.

---

[all of magic.lambda.logging](/plugins/magic.lambda.logging/)

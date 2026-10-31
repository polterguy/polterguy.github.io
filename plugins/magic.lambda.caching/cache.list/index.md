---
title: "How to use [cache.list]"
description: "How to use [cache.list] - Lists all items in cache, and returns to caller."
generated: true
guide: true
---

This is the guide to [`cache.list`](/reference/slots/cache/cache.list/), whose reference page has its arguments, constraints and declaration.

Lists all items in cache, and returns to caller.

```
cache.set:cache-item-key
   expiration:5
   value:Howdy world
cache.list
```

This slot also supports the following optional arguments.

* __[limit]__ - Maximum number of items to return.
* __[offset]__ - Offset of where to start returning items.
* Filter as value of node being the filter condition declaring which items to return. See the __[cache.clear]__ slot to understand how it works, since this argument works in the exact same way, assuming your filter is a _"namespace"_.

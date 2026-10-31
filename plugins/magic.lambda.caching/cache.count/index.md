---
title: "How to use [cache.count]"
description: "How to use [cache.count] - This slot works similarly to the [cache.list] slot, except it only returns the number of items."
generated: true
guide: true
---

This is the guide to [`cache.count`](/reference/slots/cache/cache.count/), whose reference page has its arguments, constraints and declaration.

This slot works similarly to the **[cache.list]** slot, except it only returns the number of items.
Below is an example of creating a new cache entry, for then to count how many cache items exists
in your cache.

```
cache.set:cache-item-key
   expiration:5
   value:Howdy world
cache.count
```

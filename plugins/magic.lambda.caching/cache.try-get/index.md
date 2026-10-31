---
title: "How to use [cache.try-get]"
description: "How to use [cache.try-get] - This slot checks your cache to look for an item matching your specified key, and if not found, it will invoke its [.lambda] argument, and save its returned value to the cache with the spec..."
generated: true
guide: true
---

This is the guide to [`cache.try-get`](/reference/slots/cache/cache.try-get/), whose reference page has its arguments, constraints and declaration.

This slot checks your cache to look for an item matching your specified key, and if not found, it will
invoke its **[.lambda]** argument, and save its returned value to the cache with the specified key,
before returning the created item to caller.

```
cache.try-get:cache-key
   expiration:5
   .lambda
      return:Howdy world
```

If you are using the default memory based cache, then this slot is implemented in such a way that
only the first invocation towards the specified key will actually execute your **[.lambda]** object,
allowing you to have very expensive executions to create your items, that you want to store into
the cache, without experiencing race conditions, or having more than one thread actually create the
item and store into the cache. Notice, this is _not_ true if you are using an out of process cache
implementation, such as the one found in the _"magic.data.cql"_ project. This should in general be
your _"goto slot"_ whenever you want to use the cache slots in this project.

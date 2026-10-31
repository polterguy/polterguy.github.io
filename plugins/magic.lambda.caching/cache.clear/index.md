---
title: "How to use [cache.clear]"
description: "How to use [cache.clear] - This is a shorthand slot to completely clear cache, removing all items."
generated: true
guide: true
---

This is the guide to [`cache.clear`](/reference/slots/cache/cache.clear/), whose reference page has its arguments, constraints and declaration.

This is a shorthand slot to completely clear cache, removing all items.

```
cache.set:cache-item-key
   expiration:5
   value:Howdy world

cache.clear
cache.get:cache-item-key
```

Notice, the above Hyperlambda should not return any item in its last invocation to **[cache.get]**
since the cache was cleared before invoking it. The slot also optionally takes a filter argument
as its value, which if provided, will _only_ delete items starting out with the specified filter.
Usage example can be found below.

```
cache.clear:foo.bar
```

The above will _only_ remove cache items having a key that starts out with _"foo.bar"_ implying
that for instance the following items will be cleared.

* foo.bar
* foo.bar.xyz1
* foo.bar.xyz2

While an item with a key of _"x.foo.bar"_ will _not_ be removed. This allows you to _"namespace"_
your cache items, and clearing out for instance all cache items matching the specified namespace
in one invocation.

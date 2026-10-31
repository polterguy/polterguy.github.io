---
title: magic.lambda.caching
moved_anchors: {"how-to-use-cacheclear": "/plugins/magic.lambda.caching/cache.clear/", "how-to-use-cachecount": "/plugins/magic.lambda.caching/cache.count/", "how-to-use-cacheget": "/plugins/magic.lambda.caching/cache.get/", "how-to-use-cachelist": "/plugins/magic.lambda.caching/cache.list/", "how-to-use-cacheset": "/plugins/magic.lambda.caching/cache.set/", "how-to-use-cachetry-get": "/plugins/magic.lambda.caching/cache.try-get/", "hyperlambda-caching-internals": "/plugins/magic.lambda.caching/hyperlambda-caching-internals/"}
---

This project contains caching helper slots for Hyperlambda. More specifically this project provides the following slots.

* __[\[cache.set\]](/plugins/magic.lambda.caching/cache.set/)__ - Adds the specified item to the cache
* __[\[cache.get\]](/plugins/magic.lambda.caching/cache.get/)__ - Returns a previously cached item, if existing, if not returns nothing
* __[\[cache.try-get\]](/plugins/magic.lambda.caching/cache.try-get/)__ - Attempts to retrieve an item from cache, and if not existing, invokes __[.lambda]__ to create item, saves the resulting item to the cache, before returning the item to caller
* __[\[cache.clear\]](/plugins/magic.lambda.caching/cache.clear/)__ - Completely empties cache, optionally taking a filter condition
* __[\[cache.list\]](/plugins/magic.lambda.caching/cache.list/)__ - Lists all items in cache, optionally taking a filter condition
* __[\[cache.count\]](/plugins/magic.lambda.caching/cache.count/)__ - Returns the number of cache items in total, optionally taking a filter condition

All of the above slots requires a key as its value, and/or a filter argument, as the value of the identity node
for the invocation of the slot. Notice, the cache can _only_ persist string values, implying if you want to store
something else besides a string, you'll need to correctly convert the object before storing it into your cache,
and correctly convert it after extracting it again later. If you need to preserve typing information, you can
store Hyperlambda strings into your cache.


## Topics

* [Hyperlambda caching internals](/plugins/magic.lambda.caching/hyperlambda-caching-internals/) - Internally the cache implementation is not using the MemoryCache from .Net, since this class suffers from a whole range of problems in regards to its API, such as not being able to count or iterate it

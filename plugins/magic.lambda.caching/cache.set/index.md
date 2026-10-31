---
title: "How to use [cache.set]"
description: "How to use [cache.set] - Invoke this slot to save an item to the cache."
generated: true
guide: true
---

The reference page of [`cache.set`](/reference/slots/cache/cache.set/) has its arguments, constraints and declaration.

Invoke this slot to save an item to the cache. The slot takes 3 properties, which are as follows.

* Value of node, being the _key_ for your cache item.
* __[value]__ - The item to actually save to the cache. If you pass in null, any existing cache items matching your key will be removed
* __[expiration]__ - Number of seconds to keep the item in the cache. Defaults to 5

Below is an example of a piece of Hyperlambda that simply saves the value of _"Howdy world"_ to your
cache, using _"cache-item-key"_ as the key for the cache item.

```
cache.set:cache-item-key
   expiration:5
   value:Howdy world
```

To remove the above item, you can use the following Hyperlambda.

```
cache.set:cache-item-key
```

---
title: "[cache.clear]"
description: "cache.clear is a slot in the cache namespace of Magic Cloud. Clears cached items matching the optional filter."
generated: true
llms: "guide"
slot_json: "/reference/slots/cache/cache.clear/slot.json"
---

`cache.clear` is a slot in the `cache` namespace, in Hyperlambda, the language of Magic Cloud. Clears cached items matching the optional filter.

* **Value** (`cache-key`), optional: Optional filter for cache keys

### Guide

<!-- guide -->
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
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.caching](/plugins/magic.lambda.caching/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `cache.clear`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "cache.clear",
  "description": "Clears cached items matching the optional filter",
  "signature": {
    "input": {
      "kind": "cache-key",
      "description": "Optional filter for cache keys",
      "required": false,
      "mode": "ValueOrExpression"
    }
  }
}
```

</details>

---

[all `cache.*` slots](/reference/slots/cache/) | [`cache.count` &rarr;](/reference/slots/cache/cache.count/)


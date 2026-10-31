---
title: "[cache.count]"
description: "cache.count is a slot in the cache namespace of Magic Cloud. Counts cached items matching the optional filter."
generated: true
llms: "guide"
slot_json: "/reference/slots/cache/cache.count/slot.json"
---

`cache.count` is a slot in the `cache` namespace, in Hyperlambda, the language of Magic Cloud. Counts cached items matching the optional filter.

* **Value** (`cache-key`), optional: Optional filter for cache keys
* **Returns**: Resolves to the number of cached items matching the optional filter

### Guide

<!-- guide -->
This slot works similarly to the **[cache.list]** slot, except it only returns the number of items.
Below is an example of creating a new cache entry, for then to count how many cache items exists
in your cache.

```
cache.set:cache-item-key
   expiration:5
   value:Howdy world
cache.count
```
<!-- /guide -->

### JSON declaration

This is the complete declaration of `cache.count`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "cache.count",
  "description": "Counts cached items matching the optional filter",
  "signature": {
    "input": {
      "kind": "cache-key",
      "description": "Optional filter for cache keys",
      "required": false,
      "mode": "ValueOrExpression"
    },
    "output": {
      "mode": "Value",
      "kind": "integer,number",
      "description": "Resolves to the number of cached items matching the optional filter"
    }
  }
}
```

</details>

---

[&larr; `cache.clear`](/reference/slots/cache/cache.clear/) | [all `cache.*` slots](/reference/slots/cache/) | [`cache.get` &rarr;](/reference/slots/cache/cache.get/)


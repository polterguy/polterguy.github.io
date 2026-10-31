---
title: "[cache.get]"
description: "cache.get is a slot in the cache namespace of Magic Cloud. Returns a cached value by key."
generated: true
llms: "guide"
slot_json: "/reference/slots/cache/cache.get/slot.json"
---

`cache.get` is a slot in the `cache` namespace, in Hyperlambda, the language of Magic Cloud. Returns a cached value by key.

* **Value** (`cache-key`), required: Cache key to retrieve
* **Returns**: Resolves to the cached value, or null if the key does not exist

### Guide

<!-- guide -->
Returns an item from your cache, or null if there are no items matching the specified key. Below is an
example of retrieving the item we saved to the cache above.

```
cache.get:cache-item-key
```
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.caching](/plugins/magic.lambda.caching/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `cache.get`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "cache.get",
  "description": "Returns a cached value by key",
  "signature": {
    "input": {
      "kind": "cache-key",
      "description": "Cache key to retrieve",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "output": {
      "mode": "Value",
      "kind": "cache-value,text",
      "description": "Resolves to the cached value, or null if the key does not exist"
    }
  }
}
```

</details>

---

[&larr; `cache.count`](/reference/slots/cache/cache.count/) | [all `cache.*` slots](/reference/slots/cache/) | [`cache.list` &rarr;](/reference/slots/cache/cache.list/)


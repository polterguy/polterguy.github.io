---
title: "[cache.set]"
description: "cache.set is a slot in the cache namespace of Magic Cloud. Stores a value in the in-memory cache under a key, with an optional sliding expiration."
generated: true
llms: "guide"
slot_json: "/reference/slots/cache/cache.set/slot.json"
---

`cache.set` is a slot in the `cache` namespace, in Hyperlambda, the language of Magic Cloud. Stores a value in the in-memory cache under a key, with an optional sliding expiration.

* **Value** (`cache-key`), required: Cache key to store

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[value]` | string | no | Value to store; omitted or null removes the cached item. |
| `[expiration]` | long | no | Expiration in seconds. Default: `5`. |

### Guide

<!-- guide -->
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
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.caching](/plugins/magic.lambda.caching/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `cache.set`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "cache.set",
  "description": "Stores a value in the in-memory cache under a key, with an optional sliding expiration",
  "signature": {
    "input": {
      "kind": "cache-key",
      "description": "Cache key to store",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "value": {
        "type": "string",
        "kind": "cache-value,text",
        "description": "Value to store; omitted or null removes the cached item",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      },
      "expiration": {
        "type": "long",
        "kind": "duration-seconds",
        "description": "Expiration in seconds",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "5",
        "role": "Option",
        "projection": "Value"
      }
    }
  }
}
```

</details>

---

[&larr; `cache.list`](/reference/slots/cache/cache.list/) | [all `cache.*` slots](/reference/slots/cache/) | [`cache.try-get` &rarr;](/reference/slots/cache/cache.try-get/)


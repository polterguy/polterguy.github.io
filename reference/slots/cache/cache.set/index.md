---
title: "[cache.set]"
description: "cache.set is a slot in the cache namespace of Magic Cloud. Stores a value in the in-memory cache under a key, with an optional sliding expiration."
generated: true
llms: false
slot_json: "/reference/slots/cache/cache.set/slot.json"
---

`cache.set` is a slot in the `cache` namespace, in Hyperlambda, the language of Magic Cloud. Stores a value in the in-memory cache under a key, with an optional sliding expiration.

* **Value** (`cache-key`), required: Cache key to store

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| `[expiration]` | long | no | Expiration in seconds. Default: `5`. |
| `[value]` | string | no | Value to store; omitted or null removes the cached item. |

Guide: [How to use [cache.set]](/plugins/magic.lambda.caching/#how-to-use-cacheset)

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


---
title: "[cache.try-get]"
description: "cache.try-get is a slot in the cache namespace of Magic Cloud. Returns a cached value by key if it exists, or creates a new cached item and returning it."
generated: true
llms: false
slot_json: "/reference/slots/cache/cache.try-get/slot.json"
---

`cache.try-get` is a slot in the `cache` namespace, in Hyperlambda, the language of Magic Cloud. Returns a cached value by key if it exists, or creates a new cached item and returning it.

* **Value** (`cache-key`), required: Cache key to retrieve
* **Returns**: Resolves to the cached value, or the newly created value when the key is missing

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[.lambda]` | lambda | yes | Callback executed to create the cached value when the key is missing. |
| `[expiration]` | long | no | Expiration in seconds for newly created value. Default: `5`. |

### Guide

[How to use `cache.try-get`](/plugins/magic.lambda.caching/cache.try-get/)

### JSON declaration

This is the complete declaration of `cache.try-get`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "cache.try-get",
  "description": "Returns a cached value by key if it exists, or creates a new cached item and returning it",
  "signature": {
    "input": {
      "kind": "cache-key",
      "description": "Cache key to retrieve",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "expiration": {
        "type": "long",
        "kind": "duration-seconds",
        "description": "Expiration in seconds for newly created value",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "5",
        "role": "Option",
        "projection": "Value"
      },
      ".lambda": {
        "type": "lambda",
        "description": "Callback executed to create the cached value when the key is missing",
        "required": true,
        "mode": "ExecutableLambda",
        "cardinality": "ExactlyOne",
        "role": "Callback",
        "evaluation": "EvalBlock",
        "projection": "Value"
      }
    },
    "output": {
      "mode": "Value",
      "kind": "cache-value,text",
      "description": "Resolves to the cached value, or the newly created value when the key is missing"
    }
  }
}
```

</details>

---

[&larr; `cache.set`](/reference/slots/cache/cache.set/) | [all `cache.*` slots](/reference/slots/cache/)


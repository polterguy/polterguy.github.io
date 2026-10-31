---
title: cache.* slots
description: The 6 slots named cache.* in Magic Cloud and Hyperlambda, with their arguments and return values, generated from the running system.
generated: true
---

_Generated from the running system, see [how this reference is built](/reference/slots/). Do not edit this page._

## [cache.clear]

Clears cached items matching the optional filter.

* **Value** (`cache-key`), optional: Optional filter for cache keys

Guide: [How to use [cache.clear]](/plugins/magic.lambda.caching/#how-to-use-cacheclear)

## [cache.count]

Counts cached items matching the optional filter.

* **Value** (`cache-key`), optional: Optional filter for cache keys
* **Returns**: Resolves to the number of cached items matching the optional filter

Guide: [How to use [cache.count]](/plugins/magic.lambda.caching/#how-to-use-cachecount)

## [cache.get]

Returns a cached value by key.

* **Value** (`cache-key`), required: Cache key to retrieve
* **Returns**: Resolves to the cached value, or null if the key does not exist

Guide: [How to use [cache.get]](/plugins/magic.lambda.caching/#how-to-use-cacheget)

## [cache.list]

Lists cached keys matching the optional filter.

* **Value** (`cache-key`), optional: Optional filter for cache keys
* **Returns**: Returns one child node per cached key matching the optional filter, each with [key] and [value] children

| Argument | Type | Required | Description |
|---|---|---|---|
| `[offset]` | int | no | Result offset. Default: `0`. |
| `[limit]` | int | no | Maximum number of items to return. Default: `10`. |

Returned nodes:

| Node | Type | Required | Description |
|---|---|---|---|
| _unnamed child node_ | lambda | no | One cached item; children carry the cache [key] and stored [value]. Can be repeated. |
| _unnamed child node_ / `[key]` | string | no | Cached item key. |
| _unnamed child node_ / `[value]` | string | no | Cached item value. |

Guide: [How to use [cache.list]](/plugins/magic.lambda.caching/#how-to-use-cachelist)

## [cache.set]

Stores a value in the in-memory cache under a key, with an optional sliding expiration.

* **Value** (`cache-key`), required: Cache key to store

| Argument | Type | Required | Description |
|---|---|---|---|
| `[value]` | string | no | Value to store; omitted or null removes the cached item. |
| `[expiration]` | long | no | Expiration in seconds. Default: `5`. |

Guide: [How to use [cache.set]](/plugins/magic.lambda.caching/#how-to-use-cacheset)

## [cache.try-get]

Returns a cached value by key if it exists, or creates a new cached item and returning it.

* **Value** (`cache-key`), required: Cache key to retrieve
* **Returns**: Resolves to the cached value, or the newly created value when the key is missing

| Argument | Type | Required | Description |
|---|---|---|---|
| `[expiration]` | long | no | Expiration in seconds for newly created value. Default: `5`. |
| `[.lambda]` | lambda | yes | Callback executed to create the cached value when the key is missing. |

Guide: [How to use [cache.try-get]](/plugins/magic.lambda.caching/#how-to-use-cachetry-get)


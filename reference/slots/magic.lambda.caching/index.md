---
title: magic.lambda.caching slot reference
description: Every slot in magic.lambda.caching with its value, arguments and return value, generated from the source code.
generated: true
---

_This page is generated from the `[Slot]` attributes in the source code of [magic.lambda.caching](https://github.com/polterguy/magic/tree/master/plugins/magic.lambda.caching). Do not edit it; improve the attribute instead. The hand-written guide is at [magic.lambda.caching](/plugins/magic.lambda.caching/)._

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
| `[offset]` | int | no | Result offset |
| `[limit]` | int | no | Maximum number of items to return |

| Returned node | Type | Description |
|---|---|---|
| `[.]` | lambda | One cached item; children carry the cache [key] and stored [value] |

Guide: [How to use [cache.list]](/plugins/magic.lambda.caching/#how-to-use-cachelist)

## [cache.set]

Stores a value in the in-memory cache under a key, with an optional sliding expiration.

* **Value** (`cache-key`), required: Cache key to store

| Argument | Type | Required | Description |
|---|---|---|---|
| `[value]` | string | no | Value to store; omitted or null removes the cached item |
| `[expiration]` | long | no | Expiration in seconds |

Guide: [How to use [cache.set]](/plugins/magic.lambda.caching/#how-to-use-cacheset)

## [cache.try-get]

Returns a cached value by key if it exists, or creates a new cached item and returning it.

* **Value** (`cache-key`), required: Cache key to retrieve
* **Returns**: Resolves to the cached value, or the newly created value when the key is missing

| Argument | Type | Required | Description |
|---|---|---|---|
| `[expiration]` | long | no | Expiration in seconds for newly created value |
| `[.lambda]` | lambda | yes | Callback executed to create the cached value when the key is missing |

Guide: [How to use [cache.try-get]](/plugins/magic.lambda.caching/#how-to-use-cachetry-get)


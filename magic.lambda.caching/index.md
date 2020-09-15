
# Magic Lambda Caching

[![Build status](https://travis-ci.com/polterguy/magic.lambda.caching.svg?master)](https://travis-ci.com/polterguy/magic.lambda.caching)

Cache helper slots for Magic, more specifically the following slots.

* __[cache.set]__ - Adds the specified item to the cache.
* __[cache.get]__ - Returns a previously cached item, if existing.
* __[cache.try-get]__ - Attempts to retrieve an item from cache, and if not existing, invokes __[.lambda]__ to retrieve item, and saves it to cache, before returning it to the caller.

All of the above slots requires a key as its value.

## [cache.set]

Invoke this slot to save an item to the cache. The slot takes 3 properties, which are as follows.

* __[value]__ - The item to actually save to the cache. If you pass in null, any existing cache items will be removed.
* __[expiration]__ - Number of seconds to keep the item in the cache.
* __[expiration-type]__ - Type of expiration, can be _"sliding"_ or _"absolute"_.

Absolute expiration implies that the item will be kept in the cache, for x number of seconds, before
evicted from the cache. Sliding expiration implies that if the cached item is accessed more frequently
than the sliding expiration interval, the item will never expire, until it's no longer accessed for
its **[expiration]** number of seconds. To remove a cached item, invoke this slot with a null **[value]**,
or no **[value]** node at all.

Below is an example of a piece of Hyperlambda that simply saves the value of _"Howdy world"_ to your
cache, using _"cache-item-key"_ as the key for the cache item. Notice, this example uses sliding expiration,
implying the item will _never_ be evicted from your cache, as long as it's accessed more frequently than
every 5 seconds.

```
cache.set:cache-item-key
   expiration:5
   expiration-type:sliding
   value:Howdy world
```

To remove the above item, you can use the following Hyperlambda.

```
cache.set:cache-item-key
```

## [cache.get]

Returns an item from your cache, or null if there are no items matching the specified key. Below is an
example of retrieving the item we saved to the cache above.

```
cache.get:cache-item-key
```

## [cache.try-get]

This slot checks your cache to look for an item matching your specified key, and if not found, it will
invoke its **[.lambda]** argument, and save its returned value to the cache with the specified key,
before returning the value to caller. This is a particularly useful slot, since it will synchronise
access to the cache key, preventing more than one lambda object from being invoked simultaneously,
given the same key.

```
cache.try-get:cache-key
   expiration:5
   expiration-type:absolute
   .lambda
      return:Howdy world
```

This slot contains an async overload, called **[wait.cache.try-get]**, allowing you to use async
slots in your **[.lambda]** argument.

## Configuration settings

You can provide default settings for both **[expiration]** and **[expiration-type]** in
your _"appsettings.json"_ file, allowing you to provide default values, used if no explicit arguments
are supplied as you invoke **[cache.set]** and **[cache.try-get]**. This can be done as follows.

```json
  "magic": {
    "caching": {
      "expiration": 5,
      "expiration-type": "sliding"
    }
```

* [Main documentation](https://polterguy.github.io/)

## Quality gates

- [![Build status](https://travis-ci.com/polterguy/magic.lambda.caching.svg?master)](https://travis-ci.com/polterguy/magic.lambda.caching)
- [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.caching&metric=alert_status)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.caching)
- [![Bugs](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.caching&metric=bugs)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.caching)
- [![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.caching&metric=code_smells)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.caching)
- [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.caching&metric=coverage)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.caching)
- [![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.caching&metric=duplicated_lines_density)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.caching)
- [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.caching&metric=ncloc)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.caching)
- [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.caching&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.caching)
- [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.caching&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.caching)
- [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.caching&metric=security_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.caching)
- [![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.caching&metric=sqale_index)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.caching)
- [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.caching&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.caching)

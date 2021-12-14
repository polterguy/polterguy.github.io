
# Magic Lambda Caching

Cache helper slots for Magic, more specifically the following slots.

* __[cache.set]__ - Adds the specified item to the cache.
* __[cache.get]__ - Returns a previously cached item, if existing.
* __[cache.try-get]__ - Attempts to retrieve an item from cache, and if not existing, invokes __[.lambda]__ to retrieve item, and saves it to cache, before returning it to the caller.
* __[cache.clear]__ - Completely empties cache.
* __[cache.list]__ - Lists all items in cache.
* __[cache.count]__ - Returns the number of cache items in total.

All of the above slots requires a key as its value.

## [cache.set]

Invoke this slot to save an item to the cache. The slot takes 3 properties, which are as follows.

* Value of node, being the _key_ for your cache item.
* __[value]__ - The item to actually save to the cache. If you pass in null, any existing cache items matching your key will be removed.
* __[expiration]__ - Number of seconds to keep the item in the cache.

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
   .lambda
      return:Howdy world
```

The slot is implemented in such a way that only the first invocation towards the specified key
will actually execute your **[.lambda]** object, allowing you to have very expensive executions
to create your items, that you want to store into the cache, without experiencing race conditions,
or having more than one thread actually create the item and store into the cache. This should in
general be your _"goto slot"_ whenever you want to use the cache slots in this project.

## [cache.clear]

This is a shorthand slot to completely clear cache, removing all items.

```
cache.set:cache-item-key
   expiration:5
   value:Howdy world
cache.clear
cache.get:cache-item-key
```

Notice, the above Hyperlambda should not return any item in its last invocation to **[cache.get]**
since the cache was cleared before invoking it. The slot also optionally takes a **[filter]** argument,
which if provided, will _only_ delete items starting out with the specified filter. Usage example
can be found below.

```
cache.clear:foo.bar
```

The above will _only_ remove cache items having a key that starts out with _"foo.bar"_ implying
that for instance the following items will be cleared.

* foo.bar
* foo.bar.xyz1
* foo.bar.xyz2

While an item with a key of _"x.foo.bar"_ will _not_ be removed. This allows you to _"namespace"_
your cache items, and clearing out for instance all cache items matching the specified namespace,
in one go.

## [cache.list]

Lists all items in cache, and returns to caller.

```
cache.set:cache-item-key
   expiration:5
   value:Howdy world
cache.list
```

This slot also supports the following optional arguments.

* __[limit]__ - Maximum number of items to return.
* __[offset]__ - Offset of where to start returning items.
* __[filter]__ - Filter condition declaring which items to return. See the __[cache.clear]__ slot to understand how it works, since this argument functions in the exact same way, assuming your filter is a _"namespace"_.

## Internals

Internally the cache this project is using is _not_ the `MemoryCache` from .Net, since this class
suffers from a whole range of problems in regards to its API, such as not being able to count or
iterate items, etc. Hence, the actual implementation is _completely custom_, and is based upon
the `IMagicMemoryCache` interface, which by default is wired up towards its `MagicMemoryCache`
implementation. This is a conscious choice, since first of all the `IMemoryCache` that .Net
provides out of the box is _really_ slow, in addition to that it is missing a _lot_ of crucial
parts expected from a mature memory based cache implementation.

If you want to access the actual cache from C# or something, make sure you use it through the dependency
injected `IMagicMemoryCache` interface, providing you with the implementation class needed to consume
it from C#. This interface has a lot of nice methods you can use to have a robust and fast memory
based cache implementation in your C# code - In addition to that it synchronises access such that
no race conditions can be experienced. However, _it is a memory based cache_. If you need better
caching features, going beyond what a basic memory based cache implementation can achieve, you might
want to implement Redis or something similar as your own custom C# extension.

## Project website

The source code for this repository can be found at [github.com/polterguy/magic.lambda.caching](https://github.com/polterguy/magic.lambda.caching), and you can provide feedback, provide bug reports, etc at the same place.

## Quality gates

- ![Build status](https://github.com/polterguy/magic.lambda.caching/actions/workflows/build.yaml/badge.svg)
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

## License

This project is the copyright(c) 2020-2021 of Aista, Ltd thomas@servergardens.com, and is licensed under the terms
of the LGPL version 3, as published by the Free Software Foundation. See the enclosed LICENSE file for details.

* [Magic Documentation](https://polterguy.github.io/)

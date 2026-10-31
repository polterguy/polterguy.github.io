---
title: "Hyperlambda caching internals"
description: "Hyperlambda caching internals - Internally the cache implementation is not using the MemoryCache from .Net, since this class suffers from a whole range of problems in regards to its API, such as not being able to coun..."
generated: true
---

This page is part of the [magic.lambda.caching](/plugins/magic.lambda.caching/) documentation.

Internally the cache implementation is _not_ using the `MemoryCache` from .Net, since this class
suffers from a whole range of problems in regards to its API, such as not being able to count or
iterate items, etc. Hence, the actual implementation is _completely custom_, and is based upon
the `IMagicCache` interface, which by default is wired up towards its `MagicMemoryCache`
implementation. This is a conscious choice, since first of all the `IMemoryCache` that .Net
provides out of the box is _really_ slow, in addition to that it is missing a _lot_ of crucial
parts expected from a mature memory based cache implementation.

If you want to access the actual cache from C# or something, make sure you use it through the dependency
injected `IMagicCache` interface, providing you with the implementation class needed to consume
it from C#. This interface has a lot of nifty methods you can use to have a robust and fast memory
based cache implementation in your C# code. However, _it is a memory based cache_. If you need better
caching features going beyond what a basic memory based cache implementation can achieve, you might
want to use the out of process based cache that can be found in the project called _"magic.data.cql"_.
The latter allows for storing cache items in Cassandra or ScyllaDB.

If you consume the `IMagicCache` interface from your own C# code, you can create _"hidden"_
cache items that are only possible to retrieve from C# code and not from Hyperlambda. This allows
you to create a C# only type of cache, where items added as hidden cannot in any ways what so ever
be retrieved from Hyperlambda. This is useful for C# only type of cache items that you don't want to
expose to Hyperlambda code. The _"magic.lambda.slots"_ project for instance is internally storing its
dynamically created slots in the cache as _"hidden"_ items.

---

[all of magic.lambda.caching](/plugins/magic.lambda.caching/)

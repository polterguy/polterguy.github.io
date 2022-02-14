---
title: Server side caching
description: Your cache component allows you to see your server side cache, and/or delete individual items. Intelligently using your cache component typically significantly speeds up your own apps.
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/og-cache.jpg"
---

# Server side caching

The cache component allows you to view and manage your server's cache. Magic's server
cache is typically used to make sure that expensive operations are cached, preventing your
server from becoming exhausted due to having to execute expensive operations often, when the
result of the expensive operation typically doesn't change for some time after initially
executed. There are a whole range of slots in Magic related to caching, and you can
[read more about the internals of your cache here](/documentation/magic.lambda.caching/).
Below is a screenshot of the cache component in Magic.

![Caching](https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/cache.jpg)

The cache component allows you to peek into your server's cache, and/or administrate
your items, in addition to purging/emptying your server's cache.

## Creating cache items from Hyperlambda

To create a and retrieve a cache item you can use the following Hyperlambda.

```
cache.set:foo.bar
   expiration:60
   value:Hello World

cache.get:foo.bar
```

The above stores your cache item of _"Hello World"_ for 60 seconds due to its **[expiration]** argument.
However, a smarter way to store and retrieve cache items is to retrieve and create items simultaneously
such as the following illustrates.

```
cache.try-get:foo.bar
   expiration:60
   .lambda
      return:Hello World
```

The above Hyperlambda will first see if it can find your _"foo.bar"_ cache item, and if not,
it will invoke your Hyperlambda code, store its returned value into its cache, and return
the newly created cache value in one operation. This allows you to put your expensive and
long lasting retrieval code inside of your **[.lambda]** object, ensuring it's only invoked
when it cannot find your item in your cache. Obviously, to avoid having your cache
items _"crash"_ with other modules cache items, you should _"namespace"_ your cache items,
and use keys for them such as for instance _"my-company.my-module.cache-key"_.

## Internals

The default cache service implementation stores items in memory. This implies that you should
be conservative when you choose to cache things, and only cache parts that are absolutely crucial
to cache to avoid exhausting your server's memory. In addition this results in that your cache
is not shared among multiple server instances. If you want to use an out of process cache
implementation that scales better, you can
see [how to use a NoSQL caching service here](/documentation/magic.data.cql/).

The default memory based cache implementation ensures that only _one_ thread tries to create
your cache item as you invoke **[cache.try-get]** with the same key, by wrapping creation inside
of a mutex, ensuring that only one thread invokes your **[.lambda]** object. However, since there
exists no ways to create a cross process/server mutex this is _not_ true for the NoSQL based cache.
If you are using a NoSQL based cache, and you want one thread _only_ to create your cache items,
additional steps is required from you to ensure this is happening.

Also realise that the cache can only store string values, but will automatically convert
to string if you provide it something else than a string. This implies that if you want to
store graph objects into your cache, you will have to use e.g. **[lambda2hyper]** to store
Hyperlambda, and **[hyper2lambda]** when retrieving items to convert back to lambda again.

* [Back to middleware documentation](/documentation/magic/)
* [Back to main documentation](/documentation/)

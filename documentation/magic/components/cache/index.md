---
title: Your Magic server side cache
description: The cache component allows you to view and administrate your server side cache, to purge items, and delete individual items.
og_image: "https://raw.githubusercontent.com/polterguy/polterguy.github.io/master/images/og-cache.jpg"
---

# Your Magic server side cache

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

* [Back to middleware documentation](/documentation/magic/)
* [Back to main documentation](/documentation/)

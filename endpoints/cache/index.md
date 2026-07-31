---
title: Cache endpoints
description: Magic's built-in cache endpoints, allowing you to delete server-side cache items.
header:
  image: /assets/images/hero/endpoints-top.webp
  og_image: /assets/images/hero/endpoints-top-og.png
  image_description: Cache endpoints
---

## Cache related endpoints

These are the endpoints related to your server side cache, and allow you to delete a single
cache item on the server. Internally Magic is using server-side cache sparingly for some
expensive operations, such as retrieving meta data from your database. Sometimes you need to
manually purge your cache, and/or delete individual cache items on your server, to re-retrieve
data invalidating your cache in the process. This section provides
information about such operations for such scenarios.

These endpoints are not intended to be consumed in your own code, but only
for internal usage by Magic itself.

### DELETE magic/system/cache/delete

This endpoint requires an **[id]** as a query parameter, and will delete the associated server side
cache item. It can only be invoked by a root user. The endpoint requires the following argument(s).

* __[id]__ - Mandatory id of cache item to evict

This endpoint is not intended for you to consume in your own code.

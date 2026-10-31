---
title: "How to use [request.verb]"
description: "How to use [request.verb] - This slot returns the HTTP verb (e.g."
generated: true
guide: true
---

The reference page of [`request.verb`](/reference/slots/request/request.verb/) has its arguments, constraints and declaration.

This slot returns the HTTP verb (e.g. _"get"_ or _"post"_) of the current incoming request as the value of the slot's node.
It takes no arguments, and is only meaningful when invoked from within an HTTP request, such as inside of a Hyperlambda endpoint.

This slot returns the HTTP verb of the current request, such as _"get"_ or _"post"_. Below is an example, to use inside of an endpoint.

```
request.verb
```

---
title: "How to use [http.get]"
description: "How to use [http.get] - This slot accepts a URL as its value, and optionally HTTP headers as a [headers] argument."
generated: true
guide: true
---

This is the guide to [`http.get`](/reference/slots/http/http.get/), whose reference page has its arguments, constraints and declaration.

This slot accepts a URL as its value, and optionally HTTP headers as a **[headers]** argument. In its simplest version
it would resemble something such as the following.

```
http.get:"https://docs.ainiro.io"
```

The slot returns the result of the specified HTTP GET invocation, including the HTTP headers returned from the endpoint,
and status code, in addition to the response object itself.

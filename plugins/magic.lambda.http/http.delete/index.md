---
title: "How to use [http.delete]"
description: "How to use [http.delete] - This slot accepts a URL as its value, and optionally HTTP headers as a [headers] argument."
generated: true
guide: true
---

This is the guide to [`http.delete`](/reference/slots/http/http.delete/), whose reference page has its arguments, constraints and declaration.

This slot accepts a URL as its value, and optionally HTTP headers as a **[headers]** argument. In its simplest version
it would resemble something such as the following.

```
http.delete:"https://your_website.com/your-delete-endpoint"
```

The slot returns the result of the specified HTTP DELETE invocation, including the HTTP headers returned from the endpoint,
and status code, in addition to the response object itself.

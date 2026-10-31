---
title: "How to use [response.headers.set]"
description: "How to use [response.headers.set] - Unless you explicitly change the Content-Type of your response object, by using the [response.headers.set] slot, a Content-Type of application/json will be assumed, and this header..."
generated: true
guide: true
---

The reference page of [`response.headers.set`](/reference/slots/response/response.headers.set/) has its arguments, constraints and declaration.

Unless you explicitly change the `Content-Type` of your response object, by using
the **[response.headers.set]** slot, a Content-Type of `application/json` will be assumed,
and this header will be added to the resulting HTTP response object. If you wish to override
this behavious and return plain text for instance, you could create an endpoint containing
the following.

```
response.headers.set
   Content-Type:text/plain
return:Hello from Magic Backend
```

If you intend to return anything but JSON, you _must_ set the `Content-Type` header, because
the resolver will by default try to serialize your content as JSON, and obviously fail unless it is
valid JSON.
You can also return stream objects using for instance the **[return-value]** slot, at which point
ASP.NET Core will automatically stream your content back over the response object, and `Dispose`
your stream automatically for you afterwards. This allows you to for instance return large files back
to the client without loading them into memory first. If you do this, you'll have to change
your `Content-Type` accordingly.

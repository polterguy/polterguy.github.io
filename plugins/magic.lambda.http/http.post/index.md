---
title: "How to use [http.post]"
description: "How to use [http.post] - This slot accepts a URL as its value, and optionally HTTP headers as a [headers] argument, and a mandatory it would resemble something such as the following."
generated: true
guide: true
---

This is the guide to [`http.post`](/reference/slots/http/http.post/), whose reference page has its arguments, constraints and declaration.

This slot accepts a URL as its value, and optionally HTTP headers as a **[headers]** argument, and a mandatory
**[payload]** argument, being whatever payload you want to transfer to the endpoint. In its simplest version
it would resemble something such as the following.

```
http.post:"https://some_website.com/your-post-endpoint"
   payload:@"{""foo"": ""bar""}"
```

The slot returns the result of the specified HTTP POST invocation, including the HTTP headers returned from the endpoint,
and status code, in addition to the response object itself. To automatically convert the response object to whatever
type of response your URL returns, provide a **[convert]** argument, and set its value to true, such as follows.

```
http.post:"https://some_website.com/your-post-endpoint"
   payload:@"{""foo"": ""bar""}"
   convert:true
```

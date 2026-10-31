---
title: "How to use [response.cookies.set]"
description: "How to use [response.cookies.set] - This slot sets a cookie on the response."
generated: true
guide: true
---

The reference page of [`response.cookies.set`](/reference/slots/response/response.cookies.set/) has its arguments, constraints and declaration.

This slot sets a cookie on the response. The cookie value is mandatory, and you can also set **[expires]**, **[http-only]**, **[secure]**, **[domain]**, **[path]** and **[same-site]**. Below is an example, to use inside of an endpoint.

```
response.cookies.set:my-cookie
   value:some value
   http-only:true
   secure:true
   same-site:Strict
```

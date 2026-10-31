---
title: "How to use [request.url]"
description: "How to use [request.url] - If you've got a file called \"default.html\", and the client is requesting a URL that does not have an associated physical file existing for the absolute path specified - Then your \"default.ht..."
generated: true
guide: true
---

The reference page of [`request.url`](/reference/slots/request/request.url/) has its arguments, constraints and declaration.

If you've got a file called _"default.html"_, and the client is requesting a URL that does not have an associated physical file existing for the absolute path specified - Then your _"default.html"_ file will resolve the specified URL. Such a _"default.html"_ file can also optionally have a Hyperlambda code behind file, allowing you to serve dynamic content based upon the URL of the request. This allows you to use dynamic URLs, to for instance lookup files from your database and serve back as dynamic content.

If you want to use dynamic pages, you can retrieve the request URL by invoking the **[request.url]** slot to retrieve the request URL.

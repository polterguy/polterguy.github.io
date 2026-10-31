---
title: "How to use [request.ip]"
description: "How to use [request.ip] - This slot returns the IP address of the client making the current request."
generated: true
guide: true
---

The reference page of [`request.ip`](/reference/slots/request/request.ip/) has its arguments, constraints and declaration.

This slot returns the IP address of the client making the current request. You can ask for an IPv4 or IPv6 address with the **[version]** argument. Below is an example, to use inside of an endpoint.

```
request.ip

request.ip
   version:ipv6
```

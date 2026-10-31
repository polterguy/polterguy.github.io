---
title: "How to use [server.ip]"
description: "How to use [server.ip] - This slot returns the local IP address of your server, IPv4 unless you set [version] to \"ipv6\", which is useful for logging or building absolute URLs."
generated: true
guide: true
---

The reference page of [`server.ip`](/reference/slots/server/server.ip/) has its arguments, constraints and declaration.

This slot returns the local IP address of your server, IPv4 unless you set **[version]** to _"ipv6"_, which is useful for logging or building absolute URLs. Below is an example.

```
server.ip

server.ip
   version:ipv6
```

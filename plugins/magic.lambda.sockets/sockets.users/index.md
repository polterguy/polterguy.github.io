---
title: "How to use [sockets.users]"
description: "How to use [sockets.users] - This slot lists the users currently connected through web sockets."
generated: true
guide: true
---

The reference page of [`sockets.users`](/reference/slots/sockets/sockets.users/) has its arguments, constraints and declaration.

This slot lists the users currently connected through web sockets. Each user becomes a child node holding the username and its connections. You can narrow the result with **[filter]**, **[offset]** and **[limit]**. Below is an example.

```
sockets.users
   limit:10
```

---
title: "How to use [log.fatal]"
description: "How to use [log.fatal] - This slot writes a fatal level log entry, which you should reserve for failures that cannot be recovered from and need attention at once."
generated: true
guide: true
---

The reference page of [`log.fatal`](/reference/slots/log/log.fatal/) has its arguments, constraints and declaration.

This slot writes a fatal level log entry, which you should reserve for failures that cannot be recovered from and need attention at once. It works like **[log.error]**. Below is an example.

```
log.fatal:The database is unreachable
   exception:Connection refused
```

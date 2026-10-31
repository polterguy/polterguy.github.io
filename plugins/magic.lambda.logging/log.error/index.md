---
title: "How to use [log.error]"
description: "How to use [log.error] - This slot writes an error level log entry, for exceptions you caught or operations that failed and need a follow up."
generated: true
guide: true
---

The reference page of [`log.error`](/reference/slots/log/log.error/) has its arguments, constraints and declaration.

This slot writes an error level log entry, for exceptions you caught or operations that failed and need a follow up. Child nodes become meta data stored with the entry, and you can attach exception text with **[exception]**. The value of the node becomes the ID of the new entry. Below is an example.

```
log.error:Could not process the order
   order-id:1234
   exception:The payment provider did not answer
```

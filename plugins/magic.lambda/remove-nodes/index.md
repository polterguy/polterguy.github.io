---
title: "How to use [remove-nodes]"
description: "How to use [remove-nodes] - This slot will remove all nodes its expression is pointing to."
guide: true
slots: ["remove-nodes"]
---

The reference page of [`remove-nodes`](/reference/slots/core/remove-nodes/) has its arguments, constraints and declaration.

This slot will remove all nodes its expression is pointing to.

```
.data
   foo1
   foo2
   foo3
remove-nodes:x:@.data/*/foo2
```

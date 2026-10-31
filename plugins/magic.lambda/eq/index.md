---
title: "How to use [eq]"
description: "How to use [eq] - [eq] is the equality \"operator\" in Magic, and it requires two arguments, both of which will be evaluated as potential signals - And the result of evaluating [eq] will only be true if the values of the"
guide: true
slots: ["eq"]
---

The reference page of [`eq`](/reference/slots/core/eq/) has its arguments, constraints and declaration.

**[eq]** is the equality _"operator"_ in Magic, and it requires two arguments, both of which will be evaluated as potential
signals - And the result of evaluating **[eq]** will only be true if the values of these two arguments are _exactly the same_.

```
.src:int:5
eq
   get-value:x:@.src
   .:int:5
```

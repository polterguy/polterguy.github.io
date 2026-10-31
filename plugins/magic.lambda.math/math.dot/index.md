---
title: "How to use [math.dot]"
description: "How to use [math.dot] - This slot returns the dot product of two lists."
generated: true
guide: true
---

This is the guide to [`math.dot`](/reference/slots/math/math.dot/), whose reference page has its arguments, constraints and declaration.

This slot returns the dot product of two lists.

```
.list1
   .:double:0.5
   .:double:0.7
   .:double:0.1
.list2
   .:double:0.56
   .:double:0.89
   .:double:0.33
math.dot
   get-nodes:x:@.list1/*
   get-nodes:x:@.list2/*
```

This slot is useful for calculating similarities between two different objects in Machine Learning, where
each list is an _"embedding"_ or a vector.

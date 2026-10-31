---
title: "How to use [filter]"
description: "How to use [filter] - Filter allows you to filter using a predicate."
generated: true
guide: true
---

The reference page of [`filter`](/reference/slots/core/filter/) has its arguments, constraints and declaration.

Filter allows you to filter using a predicate. If the predicate returns true for the currently iterated list item, it's included, otherwise not. Below is an example.

```
.src
   .:int:1
   .:int:2
   .:int:3
   .:int:4
filter:x:@.src/*
   mt
      get-value:x:@.dp/#
      .:int:2
   return:x:-
```

The above will return only nodes having a value above integer value _"2"_.

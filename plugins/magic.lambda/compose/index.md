---
title: "How to use [compose]"
description: "How to use [compose] - Compose allows you to dynamically create expressions by supplying it with a list of iterators."
generated: true
guide: true
---

The reference page of [`compose`](/reference/slots/core/compose/) has its arguments, constraints and declaration.

Compose allows you to dynamically create expressions by supplying it with a list of iterators. To understand it
realise the following invocation.

```
compose
   .:..
   .:*
   .:.data
   .:*
```

Results in the following result.

```
compose:x:../*/.data/*
```

Since expressions are for the most parts recursively evaluated, this allows you to dynamically compose
expressions you de-reference, allowing you to dynamically create expressions you're using in your code.

---
title: "How to use [time.total-milliseconds]"
description: "How to use [time.total-milliseconds] - This slot takes a time span as its value, such as one returned from [time], and returns the total number of milliseconds the time span represents."
generated: true
guide: true
---

The reference page of [`time.total-milliseconds`](/reference/slots/time/time.total-milliseconds/) has its arguments, constraints and declaration.

This slot takes a time span as its value, such as one returned from **[time]**, and returns the total number
of milliseconds the time span represents. Its value is mandatory, and it can be given either as a constant
or as an expression.

This slot returns the total number of milliseconds in a time span. Below is an example, returning the number of milliseconds in a minute.

```
time
   minutes:1
time.total-milliseconds:x:-
```

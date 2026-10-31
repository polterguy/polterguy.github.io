---
title: "How to use [time.format]"
description: "How to use [time.format] - This slot formats a time span as a string, using the same format patterns as TimeSpan.ToString in C#, and is invoked with the time span as its value."
generated: true
guide: true
---

The reference page of [`time.format`](/reference/slots/time/time.format/) has its arguments, constraints and declaration.

This slot formats a time span as a string, using the same format patterns as `TimeSpan.ToString` in C#,
and is invoked with the time span as its value. It requires the following argument.

- **[format]** - Format pattern to use. This argument is mandatory, and the slot throws an exception if it is missing.

The time span is typically a value returned from **[time]**, and the result of the slot is the formatted
string.

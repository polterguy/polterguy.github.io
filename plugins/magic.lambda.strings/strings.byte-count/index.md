---
title: "How to use [strings.byte-count]"
description: "How to use [strings.byte-count] - Returns the number of bytes the specified string occupies when UTF-8 encoded, as an integer."
generated: true
guide: true
---

This is the guide to [`strings.byte-count`](/reference/slots/strings/strings.byte-count/), whose reference page has its arguments, constraints and declaration.

Returns the number of bytes the specified string occupies when UTF-8 encoded, as an integer. This differs from
**[strings.length]**, which counts characters, since characters outside the ASCII range occupy more than
one byte. The slot takes a value, which can be a constant or an expression.

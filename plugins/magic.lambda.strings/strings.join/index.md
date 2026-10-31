---
title: "How to use [strings.join]"
description: "How to use [strings.join] - Similar to [strings.concat], except it also takes an optional separating character, allowing you to concatenate a bunch of strings, and making sure each original string is separated by some..."
generated: true
guide: true
---

This is the guide to [`strings.join`](/reference/slots/strings/strings.join/), whose reference page has its arguments, constraints and declaration.

Similar to **[strings.concat]**, except it also takes an optional separating character, allowing you to
concatenate a bunch of strings, and making sure each original string is separated by some sequence of strings.

```
.src
   .:foo
   .:bar
strings.join:x:@.src/*
   .:,

/*
 * Results in "foo,bar"
 */
```

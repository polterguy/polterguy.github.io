---
title: "How to use [strings.concat]"
description: "How to use [strings.concat] - Concatenates a list of strings into one string."
generated: true
guide: true
---

This is the guide to [`strings.concat`](/reference/slots/strings/strings.concat/), whose reference page has its arguments, constraints and declaration.

Concatenates a list of strings into one string. Similar to **[strings.join]**, except it doesn't take a
separating character.

```
.bar:Bar
strings.concat
   .:Thomas
   .:" "
   .:Hansen
   .:" "
   .:Foo
   .:" "
   get-value:x:@.bar

/*
 * Resulting in "Thomas Hansen Foo Bar" after invocation.
 */
```

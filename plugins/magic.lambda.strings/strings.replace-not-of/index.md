---
title: "How to use [strings.replace-not-of]"
description: "How to use [strings.replace-not-of] - This slot will replace every single character in your original string, that cannot be found in its first argument, with the value of its second argument."
generated: true
guide: true
---

The reference page of [`strings.replace-not-of`](/reference/slots/strings/strings.replace-not-of/) has its arguments, constraints and declaration.

This slot will replace every single character in your original string, that cannot be found in its first
argument, with the value of its second argument. This slot is useful if you want to remove all characters
that cannot be found in another character set, such as the following illustrates.

```
strings.replace-not-of:foo bar1howdy
   .:abcdefghijklmnopqrstuvwxyz
   .:-
```

The above will result in the following result 

```
strings.replace-not-of:foo-bar-howdy
```

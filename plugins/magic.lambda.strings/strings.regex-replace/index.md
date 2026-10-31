---
title: "How to use [strings.regex-replace]"
description: "How to use [strings.regex-replace] - Replaces matches of the given regular expression with some static sequence of characters."
generated: true
guide: true
---

This is the guide to [`strings.regex-replace`](/reference/slots/strings/strings.regex-replace/), whose reference page has its arguments, constraints and declaration.

Replaces matches of the given regular expression with some static sequence of characters.

```
// Results in "FOO bar hansen"
strings.regex-replace:foo bar hansen
   .:fo+
   .:FOO
```

The first argument is what regular expression to match, the second argument is what to replace
all matches with.

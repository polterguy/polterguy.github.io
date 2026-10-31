---
title: "How to use [strings.split]"
description: "How to use [strings.split] - Splits a string into multiple strings, where a sequence of characters can be found, removing the original sequence of characters from the resulting node set."
generated: true
guide: true
---

The reference page of [`strings.split`](/reference/slots/strings/strings.split/) has its arguments, constraints and declaration.

Splits a string into multiple strings, where a sequence of characters can be found, removing the original
sequence of characters from the resulting node set.

```
.foo:some input string
strings.split:x:-
   .:' '
```

The above will result in the following result.

```
.foo:some input string
strings.split:x:-
   .:some
   .:input
   .:string
```

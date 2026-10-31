---
title: "How to use [strings.substring]"
description: "How to use [strings.substring] - Returns a substring of the specified string."
generated: true
guide: true
---

This is the guide to [`strings.substring`](/reference/slots/strings/strings.substring/), whose reference page has its arguments, constraints and declaration.

Returns a substring of the specified string.

```
.input:Foo Bar Howdy World
strings.substring:x:-
   .:5
   .:7
```

The above will result in the following.

```
strings.substring:ar Howd
```

Notice, the second argument is the _number of characters to return_ and not the offset into the string
of where to stop returning. In such a regard, it works the same way as the C# `Substring` method.

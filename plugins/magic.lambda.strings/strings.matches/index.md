---
title: "How to use [strings.matches]"
description: "How to use [strings.matches] - Returns all regular expression matches from specified source string."
generated: true
guide: true
---

This is the guide to [`strings.matches`](/reference/slots/strings/strings.matches/), whose reference page has its arguments, constraints and declaration.

Returns all regular expression matches from specified source string.

```
.input:Foo Bar Howdy World {match1} and {match2} and that was it
strings.matches:x:-
   .:"\\{.+?\\}"
```

The above will result in the following.

```
strings.matches
   .:{match1}
   .:{match2}
```

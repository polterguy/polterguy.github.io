---
title: "How to use [strings.replace]"
description: "How to use [strings.replace] - This slot replaces occurrences of a string inside a string, with some other string."
generated: true
guide: true
---

This is the guide to [`strings.replace`](/reference/slots/strings/strings.replace/), whose reference page has its arguments, constraints and declaration.

This slot replaces occurrences of a string inside a string, with some other string. The simplest version is like
follows.

```
.foo:thomas hansen

strings.replace:x:-
   .:hansen
   .:tjobing hansen
```

You can also reference slots and dynamic slots for that matter, assuming your slots somehow returns strings,
or something that can be converted into a string, such as the following illustrates. Notice, this code will
throw an exception, since there are probably no slots called _"some-slot-returning-string"_ in your installation.

```
.what:hansen
.foo:thomas hansen

strings.replace:x:-

   get-value:x:@.what

   signal:some-slot-returning-string
      arg1-to-slot:foo
      arg2-to-slot:foo
```

Above the first argument is _"what to look for"_, and the second argument is _"what to substitute it with"_.
The above is a general pattern for most of these slots, where the node arguments supplied to the slot will be
evaluated as a lambda object, before the arguments are consumed, allowing you to use arguments that are the
result of invoking other slots as arguments to your original outer most slot.

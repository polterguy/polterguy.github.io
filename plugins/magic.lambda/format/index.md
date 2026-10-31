---
title: "How to use [format]"
description: "How to use [format] - This slot converts some expression or value according to some specified String.Format pattern."
guide: true
slots: ["format"]
---

The reference page of [`format`](/reference/slots/core/format/) has its arguments, constraints and declaration.

This slot converts some expression or value according to some specified `String.Format` pattern.
The following code will string format the number 57 to make sure it's prefixed with leading zeros, always ending
up having at least 5 digits. See .Net String.Format method for which patterns you can use. The culture used will
be the invariant one, unless you explicitly override the culture with a **[culture]** argument.

```
.foo:int:57
format:x:-
   pattern:"{0:00000}"
```

To override the **[culture]** argument used you can use something such as follows.

```
.foo:decimal:57
format:x:-
   pattern:"{0:0.00}"
   culture:nb-NO
```

Since the above is using Norwegian Bokmal as its **[culture]** argument, it will return the result with a `,`
as a decimal separator instead of the default which is `.`. You can use the same **[pattern]** values for
this slot as you can use in C# and .Net. To see an extensive list of for instance the formatting patterns you
can use for a date and time object, you can browse the [Microsoft documentation](https://docs.microsoft.com/en-us/dotnet/standard/base-types/standard-date-and-time-format-strings)
related to this. If you don't supply a **[culture]** argument the invariant culture will be used.

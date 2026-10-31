---
title: "How to use [strings.mixin]"
description: "How to use [strings.mixin] - Combines the result of the specified Hyperlambda and concatenates inline into its surrounding string."
generated: true
guide: true
---

This is the guide to [`strings.mixin`](/reference/slots/strings/strings.mixin/), whose reference page has its arguments, constraints and declaration.

Combines the result of the specified Hyperlambda and concatenates inline into its surrounding string.

{% raw %}
```
strings.mixin:@"2+2 equals {{
math.add
   .:int:2
   .:int:2
return:x:-
}}"
```
{% endraw %}

The above will result in the following.

```
strings.mixin:2+2 equals 4
```

Notice, any inline Hyperlambda is added by adding two braces around your Hyperlambda, at which point the inline Hyperlambda will be executed, and whatever it returns is _"mixed into the surrounding string inline"_. This slot can be used similarly to **[invoke]**, allowing you to pass in parameters to it by simply adding nodes as children when invoking it. To understand the last point consider the following code.

{% raw %}
```
strings.mixin:@"2 + val equals {{
math.add
   .:int:2
   get-value:x:@.arguments/*/val
return:x:-
}}"
   val:int:5
```
{% endraw %}

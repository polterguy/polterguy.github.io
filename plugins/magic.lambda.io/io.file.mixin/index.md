---
title: "How to use [io.file.mixin]"
description: "How to use [io.file.mixin] - This slot takes a filename as its primary argument, and optionally any amount of lambda children objects."
generated: true
guide: true
---

This is the guide to [`io.file.mixin`](/reference/slots/io/io.file.mixin/), whose reference page has its arguments, constraints and declaration.

This slot takes a filename as its primary argument, and optionally any amount of lambda children objects.
It allows for dynamically substituting for instance {% raw %}`{{*/.name}}`{% endraw %} segments in your original source file,
by invoking lambda objects it can find by evaluating your {% raw %}`{{xyz}}`{% endraw %} segment as an expression
leading to some lambda object you want to execute. Below is an example of usage that assumes you've got a
file named _"foo.html"_ at the root folder of your installation resembling the following.

**/foo.html**

{% raw %}
```
<html>
    <head>
        <title>Hello world</title>
    </head>
    <body>
        <h1>Hello world</h1>
        <p>
           Hello there {{*/.name}}, 2 + 5 is {{*/.add}}
        </p>
    </body>
</html>
```
{% endraw %}

If you create the above file you can invoke **[io.file.mixin]** as follows to see the result.

```
io.file.mixin:/foo.html
   .name:Thomas Hansen
   .add
      math.add
         .:int:2
         .:int:5
      return:x:-
```

The above will substitute all your {% raw %}`{{xyz}}`{% endraw %}segments and give you a result resembling the following.

```
<html>
    <head>
        <title>Hello world</title>
    </head>
    <body>
        <h1>Hello world</h1>
        <p>
           Hello there Thomas Hansen, 2 + 5 is 7
        </p>
    </body>
</html>
```

Notice, if the node your expression is leading to has a value such as illustrated above, it will return that value
instead of executing your node as a lambda object.

All **[.oninit]** lambda objects found as children of your **[io.file.mixin]** invocation will be executed before
any mixin logic is executed, allowing for you to create common initialisation logic, that runs once but is referenced
in multiple mixin expressions.

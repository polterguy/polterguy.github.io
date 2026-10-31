---
title: "[io.file.mixin]"
description: "io.file.mixin is a slot in the io namespace of Magic Cloud. Loads a static file, applies same-named Hyperlambda codebehind, and returns the mixed result."
generated: true
llms: "guide"
slot_json: "/reference/slots/io/io.file.mixin/slot.json"
---

{% raw %}`io.file.mixin` is a slot in the `io` namespace, in Hyperlambda, the language of Magic Cloud. Loads a static file, applies same-named Hyperlambda codebehind, and returns the mixed result.

* **Value** (`file-path`), required: Path to the static file to mix with its same-named .hl codebehind file
* **Returns**: Resolves to the mixed file content in value and any codebehind-produced child nodes

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | object | no | Optional argument available to codebehind lambda loaded for the mixed file. Can be repeated. |

### Guide

<!-- guide -->
This slot takes a filename as its primary argument, and optionally any amount of lambda children objects.
It allows for dynamically substituting for instance `{{*/.name}}` segments in your original source file,
by invoking lambda objects it can find by evaluating your `{{xyz}}` segment as an expression
leading to some lambda object you want to execute. Below is an example of usage that assumes you've got a
file named _"foo.html"_ at the root folder of your installation resembling the following.

**/foo.html**

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

The above will substitute all your `{{xyz}}`segments and give you a result resembling the following.

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
<!-- /guide -->

### JSON declaration

This is the complete declaration of `io.file.mixin`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "io.file.mixin",
  "description": "Loads a static file, applies same-named Hyperlambda codebehind, and returns the mixed result",
  "signature": {
    "input": {
      "kind": "file-path",
      "description": "Path to the static file to mix with its same-named .hl codebehind file",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "*": {
        "type": "object",
        "kind": "value",
        "description": "Optional argument available to codebehind lambda loaded for the mixed file",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrMore",
        "role": "Arguments",
        "projection": "ArgumentBag"
      }
    },
    "output": {
      "mode": "Both",
      "kind": "mixed-file-content,text",
      "description": "Resolves to the mixed file content in value and any codebehind-produced child nodes"
    }
  }
}
```

</details>

---

[&larr; `io.file.load.binary`](/reference/slots/io/io.file.load.binary/) | [all `io.*` slots](/reference/slots/io/) | [`io.file.move` &rarr;](/reference/slots/io/io.file.move/)
{% endraw %}

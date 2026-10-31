---
title: "[strings.mixin]"
description: "strings.mixin is a slot in the strings namespace of Magic Cloud. Applies string interpolation from child expressions."
generated: true
llms: "guide"
slot_json: "/reference/slots/strings/strings.mixin/slot.json"
---

{% raw %}`strings.mixin` is a slot in the `strings` namespace, in Hyperlambda, the language of Magic Cloud. Applies string interpolation from child expressions.

* **Value** (`mixin-template,text`), required: Template text to interpolate
* **Returns**: Resolves to the rendered string after applying codebehind and expressions

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[strip]` | bool | no | Whether to strip embedded Hyperlambda instead of executing it. Default: `false`. |
| _any node name_ | string | no | Argument passed to embedded Hyperlambda snippets invoked from the template. Can be repeated. |

### Guide

<!-- guide -->
Combines the result of the specified Hyperlambda and concatenates inline into its surrounding string.

```
strings.mixin:@"2+2 equals {{
math.add
   .:int:2
   .:int:2
return:x:-
}}"
```

The above will result in the following.

```
strings.mixin:2+2 equals 4
```

Notice, any inline Hyperlambda is added by adding two braces around your Hyperlambda, at which point the inline Hyperlambda will be executed, and whatever it returns is _"mixed into the surrounding string inline"_. This slot can be used similarly to **[invoke]**, allowing you to pass in parameters to it by simply adding nodes as children when invoking it. To understand the last point consider the following code.

```
strings.mixin:@"2 + val equals {{
math.add
   .:int:2
   get-value:x:@.arguments/*/val
return:x:-
}}"
   val:int:5
```
<!-- /guide -->

### JSON declaration

This is the complete declaration of `strings.mixin`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "strings.mixin",
  "description": "Applies string interpolation from child expressions",
  "signature": {
    "input": {
      "kind": "mixin-template,text",
      "description": "Template text to interpolate",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "strip": {
        "type": "bool",
        "description": "Whether to strip embedded Hyperlambda instead of executing it",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "false",
        "role": "Option",
        "projection": "Value"
      },
      "*": {
        "type": "string",
        "kind": "string-values",
        "description": "Argument passed to embedded Hyperlambda snippets invoked from the template",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrMore",
        "role": "Arguments",
        "projection": "ArgumentBag"
      }
    },
    "output": {
      "mode": "Value",
      "kind": "text",
      "description": "Resolves to the rendered string after applying codebehind and expressions"
    }
  }
}
```

</details>

---

[&larr; `strings.matches`](/reference/slots/strings/strings.matches/) | [all `strings.*` slots](/reference/slots/strings/) | [`strings.regex-replace` &rarr;](/reference/slots/strings/strings.regex-replace/)
{% endraw %}

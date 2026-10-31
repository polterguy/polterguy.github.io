---
title: "[strings.replace]"
description: "strings.replace is a slot in the strings namespace of Magic Cloud. Returns the text with every occurrence of [what] swapped for [with]; pass an empty [with] to strip matches."
generated: true
llms: "guide"
slot_json: "/reference/slots/strings/strings.replace/slot.json"
---

`strings.replace` is a slot in the `strings` namespace, in Hyperlambda, the language of Magic Cloud. Returns the text with every occurrence of [what] swapped for [with]; pass an empty [with] to strip matches.

* **Value** (`text`), required: Text to transform
* **Returns**: Resolves to the string after replacing the specified substring

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _unnamed child node_ | string | yes | Text or pattern to find. |
| _unnamed child node_ | string | no | Replacement text. |

### Guide

<!-- guide -->
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
<!-- /guide -->

### JSON declaration

This is the complete declaration of `strings.replace`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "strings.replace",
  "description": "Returns the text with every occurrence of [what] swapped for [with]; pass an empty [with] to strip matches",
  "signature": {
    "input": {
      "kind": "text",
      "description": "Text to transform",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": [
      {
        "type": "string",
        "kind": "text",
        "description": "Text or pattern to find",
        "required": true,
        "mode": "ExecutableLambda",
        "cardinality": "ExactlyOne",
        "role": "SourceExpression",
        "evaluation": "EvalSelf",
        "projection": "Value"
      },
      {
        "type": "string",
        "kind": "text",
        "description": "Replacement text",
        "required": false,
        "mode": "ExecutableLambda",
        "cardinality": "ZeroOrOne",
        "role": "SourceExpression",
        "evaluation": "EvalSelf",
        "projection": "Value"
      }
    ],
    "output": {
      "mode": "Value",
      "kind": "text",
      "description": "Resolves to the string after replacing the specified substring"
    }
  }
}
```

</details>

---

[&larr; `strings.regex-replace`](/reference/slots/strings/strings.regex-replace/) | [all `strings.*` slots](/reference/slots/strings/) | [`strings.replace-not-of` &rarr;](/reference/slots/strings/strings.replace-not-of/)


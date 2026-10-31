---
title: "[strings.join]"
description: "strings.join is a slot in the strings namespace of Magic Cloud. Concatenates the values yielded by the expression, inserting the separator between adjacent items."
generated: true
llms: "guide"
slot_json: "/reference/slots/strings/strings.join/slot.json"
---

`strings.join` is a slot in the `strings` namespace, in Hyperlambda, the language of Magic Cloud. Concatenates the values yielded by the expression, inserting the separator between adjacent items.

* **Value** (`string-list`), required: Expression yielding the values to join
* **Returns**: Resolves to the joined string

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _unnamed child node_ | string | no | Separator to place between joined values. |

### Guide

<!-- guide -->
Similar to **[strings.concat]**, except it also takes an optional separating character, allowing you to
concatenate a bunch of strings, and making sure each original string is separated by some sequence of strings.

```
.src
   .:foo
   .:bar
strings.join:x:@.src/*
   .:,

/*
 * Results in "foo,bar"
 */
```
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.strings](/plugins/magic.lambda.strings/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `strings.join`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "strings.join",
  "description": "Concatenates the values yielded by the expression, inserting the separator between adjacent items",
  "signature": {
    "input": {
      "kind": "string-list",
      "description": "Expression yielding the values to join",
      "required": true,
      "mode": "Expression"
    },
    "children": [
      {
        "type": "string",
        "kind": "string-separator",
        "description": "Separator to place between joined values",
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
      "description": "Resolves to the joined string"
    }
  }
}
```

</details>

---

[&larr; `strings.html-encode`](/reference/slots/strings/strings.html-encode/) | [all `strings.*` slots](/reference/slots/strings/) | [`strings.length` &rarr;](/reference/slots/strings/strings.length/)


---
title: "[strings.concat]"
description: "strings.concat is a slot in the strings namespace of Magic Cloud. Concatenates strings."
generated: true
llms: "guide"
slot_json: "/reference/slots/strings/strings.concat/slot.json"
---

`strings.concat` is a slot in the `strings` namespace, in Hyperlambda, the language of Magic Cloud. Concatenates strings.

* **Value** (`string-list`), optional: Expression yielding the text segments to concatenate when not supplied as child nodes
* **Returns**: Resolves to the concatenated string

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _unnamed child node_ | string | no | Text segment to concatenate. Can be repeated. |

### Constraints

* **ExactlyOneOf**: Provide either expression input or child text segments (`[input]`, `[.]`)

### Guide

<!-- guide -->
Concatenates a list of strings into one string. Similar to **[strings.join]**, except it doesn't take a
separating character.

```
.bar:Bar
strings.concat
   .:Thomas
   .:" "
   .:Hansen
   .:" "
   .:Foo
   .:" "
   get-value:x:@.bar

/*
 * Resulting in "Thomas Hansen Foo Bar" after invocation.
 */
```
<!-- /guide -->

### JSON declaration

This is the complete declaration of `strings.concat`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "strings.concat",
  "description": "Concatenates strings",
  "signature": {
    "input": {
      "kind": "string-list",
      "description": "Expression yielding the text segments to concatenate when not supplied as child nodes",
      "required": false,
      "mode": "Expression"
    },
    "children": [
      {
        "type": "string",
        "kind": "text",
        "description": "Text segment to concatenate",
        "required": false,
        "mode": "ExecutableLambda",
        "cardinality": "ZeroOrMore",
        "role": "SourceExpression",
        "evaluation": "EvalSelf",
        "projection": "Value"
      }
    ],
    "constraints": [
      {
        "description": "Provide either expression input or child text segments",
        "values": [
          "input",
          "."
        ],
        "kind": "ExactlyOneOf"
      }
    ],
    "output": {
      "mode": "Value",
      "kind": "text",
      "description": "Resolves to the concatenated string"
    }
  }
}
```

</details>

---

[&larr; `strings.capitalize`](/reference/slots/strings/strings.capitalize/) | [all `strings.*` slots](/reference/slots/strings/) | [`strings.contains` &rarr;](/reference/slots/strings/strings.contains/)


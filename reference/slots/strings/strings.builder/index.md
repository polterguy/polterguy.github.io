---
title: "[strings.builder]"
description: "strings.builder is a slot in the strings namespace of Magic Cloud. Creates a string builder scope for [strings.builder.append]."
generated: true
llms: false
slot_json: "/reference/slots/strings/strings.builder/slot.json"
---

`strings.builder` is a slot in the `strings` namespace, in Hyperlambda, the language of Magic Cloud. Creates a string builder scope for [strings.builder.append].

* **Returns**: Resolves to the text appended inside the builder scope
* **Scope**: provides `strings.builder` - Creates a string builder scope for [strings.builder.append]

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | no | Executable child slot evaluated while the StringBuilder is scoped; use [strings.builder.append] to append text. Can be repeated. |

Guide: [How to use [strings.builder]](/plugins/magic.lambda.strings/#how-to-use-stringsbuilder)

### JSON declaration

This is the complete declaration of `strings.builder`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "strings.builder",
  "description": "Creates a string builder scope for [strings.builder.append]",
  "signature": {
    "children": {
      "*": {
        "type": "lambda",
        "description": "Executable child slot evaluated while the StringBuilder is scoped; use [strings.builder.append] to append text",
        "required": false,
        "mode": "ExecutableLambda",
        "cardinality": "ZeroOrMore",
        "role": "ExecutableBody",
        "evaluation": "EvalSelf",
        "projection": "Self"
      }
    },
    "scope": {
      "provides": "strings.builder",
      "description": "Creates a string builder scope for [strings.builder.append]"
    },
    "output": {
      "mode": "Value",
      "kind": "text",
      "description": "Resolves to the text appended inside the builder scope"
    }
  }
}
```

</details>

---

[all `strings.*` slots](/reference/slots/strings/) | [`strings.builder.append` &rarr;](/reference/slots/strings/strings.builder.append/)


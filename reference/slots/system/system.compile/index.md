---
title: "[system.compile]"
description: "system.compile is a slot in the system namespace of Magic Cloud. Compiles C# code from child nodes into an assembly."
generated: true
llms: false
slot_json: "/reference/slots/system/system.compile/slot.json"
---

`system.compile` is a slot in the `system` namespace, in Hyperlambda, the language of Magic Cloud. Compiles C# code from child nodes into an assembly.

* **Returns**: Resolves to the compiled assembly bytes

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[code]` | string | yes | C# source code to compile. |
| `[assembly-name]` | string | yes | Name of the generated assembly. |
| `[references]` | lambda | yes | Assembly references required by the compilation. |
| `[references]` / _unnamed child node_ | string | yes | Assembly reference. Can be repeated. |

### Guide

[How to use `system.compile`](/plugins/magic.lambda.system/system.compile/)

### JSON declaration

This is the complete declaration of `system.compile`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "system.compile",
  "description": "Compiles C# code from child nodes into an assembly",
  "signature": {
    "children": {
      "code": {
        "type": "string",
        "kind": "csharp-code",
        "description": "C# source code to compile",
        "required": true,
        "mode": "ValueOrExpression",
        "cardinality": "ExactlyOne",
        "role": "Option",
        "projection": "Value"
      },
      "assembly-name": {
        "type": "string",
        "kind": "plugin-assembly-name",
        "description": "Name of the generated assembly",
        "required": true,
        "mode": "ValueOrExpression",
        "cardinality": "ExactlyOne",
        "role": "Option",
        "projection": "Value"
      },
      "references": {
        "type": "lambda",
        "description": "Assembly references required by the compilation",
        "required": true,
        "mode": "ValueOrExpression",
        "cardinality": "ExactlyOne",
        "role": "StructuredObject",
        "projection": "Children",
        "children": [
          {
            "type": "string",
            "kind": "assembly-reference",
            "description": "Assembly reference",
            "required": true,
            "mode": "ValueOrExpression",
            "cardinality": "OneOrMore",
            "role": "Option",
            "projection": "Value"
          }
        ]
      }
    },
    "output": {
      "mode": "Value",
      "kind": "plugin-assembly-bytes,binary-content",
      "description": "Resolves to the compiled assembly bytes"
    }
  }
}
```

</details>

---

[all `system.*` slots](/reference/slots/system/) | [`system.debug` &rarr;](/reference/slots/system/system.debug/)


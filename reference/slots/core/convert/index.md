---
title: "[convert]"
description: "convert is a core slot of Magic Cloud. Coerces a value to a different CLR type; useful for parsing strings into numbers, dates, booleans, or other strongly-typed values."
generated: true
llms: false
slot_json: "/reference/slots/core/convert/slot.json"
---

`convert` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Coerces a value to a different CLR type; useful for parsing strings into numbers, dates, booleans, or other strongly-typed values.

* **Value** (`single-object`), required: Expression selecting the value to convert
* **Returns**: Resolves to the value converted to the requested type

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[type]` | string | yes | Target Hyperlambda type name. |

Guide: [How to use [convert]](/plugins/magic.lambda/types/#how-to-use-convert)

### JSON declaration

This is the complete declaration of `convert`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "convert",
  "description": "Coerces a value to a different CLR type; useful for parsing strings into numbers, dates, booleans, or other strongly-typed values",
  "signature": {
    "input": {
      "kind": "single-object",
      "description": "Expression selecting the value to convert",
      "required": true,
      "mode": "Expression"
    },
    "children": {
      "type": {
        "type": "string",
        "kind": "type-name",
        "description": "Target Hyperlambda type name",
        "required": true,
        "mode": "ValueOrExpression",
        "cardinality": "ExactlyOne",
        "role": "Option",
        "projection": "Value"
      }
    },
    "output": {
      "mode": "Value",
      "description": "Resolves to the value converted to the requested type"
    }
  }
}
```

</details>

---

[&larr; `context`](/reference/slots/core/context/) | [all core slots](/reference/slots/core/) | [`csv2lambda` &rarr;](/reference/slots/core/csv2lambda/)


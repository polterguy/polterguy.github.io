---
title: "[format]"
description: "format is a core slot of Magic Cloud. Formats a value using a .NET format string and optional culture; useful for currencies, dates, and number rendering."
generated: true
llms: false
slot_json: "/reference/slots/core/format/slot.json"
---

`format` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Formats a value using a .NET format string and optional culture; useful for currencies, dates, and number rendering.

* **Value** (`scalar`), required: Value to format
* **Returns**: Resolves to the formatted string

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[pattern]` | string | yes | Composite format string. |
| `[culture]` | string | no | Optional culture name used when formatting. |

Guide: [How to use [format]](/plugins/magic.lambda/types/#how-to-use-format)

### Related documentation

* Part of the [magic.lambda](/plugins/magic.lambda/) plugin, which documents every slot it contains.
* Discussed in [Types and conversion](/plugins/magic.lambda/types/).

### JSON declaration

This is the complete declaration of `format`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "format",
  "description": "Formats a value using a .NET format string and optional culture; useful for currencies, dates, and number rendering",
  "signature": {
    "input": {
      "kind": "scalar",
      "description": "Value to format",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "pattern": {
        "type": "string",
        "kind": "format-pattern",
        "description": "Composite format string",
        "required": true,
        "mode": "ValueOrExpression",
        "cardinality": "ExactlyOne",
        "role": "Option",
        "projection": "Value"
      },
      "culture": {
        "type": "string",
        "kind": "culture-name",
        "description": "Optional culture name used when formatting",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      }
    },
    "output": {
      "mode": "Value",
      "kind": "text",
      "description": "Resolves to the formatted string"
    }
  }
}
```

</details>

---

[&larr; `fork`](/reference/slots/core/fork/) | [all core slots](/reference/slots/core/) | [`get-context` &rarr;](/reference/slots/core/get-context/)


---
title: "[compose]"
description: "compose is a core slot of Magic Cloud. Builds an expression at runtime by concatenating the evaluated child node values; useful for dynamic node selection."
generated: true
llms: false
slot_json: "/reference/slots/core/compose/slot.json"
---

`compose` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Builds an expression at runtime by concatenating the evaluated child node values; useful for dynamic node selection.

* **Returns**: Resolves to the composed expression

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | string | yes | Expression segment evaluated and joined into the resulting expression. Can be repeated. |

### Guide

[How to use `compose`](/plugins/magic.lambda/compose/)

### JSON declaration

This is the complete declaration of `compose`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "compose",
  "description": "Builds an expression at runtime by concatenating the evaluated child node values; useful for dynamic node selection",
  "signature": {
    "children": {
      "*": {
        "type": "string",
        "kind": "expression-segment",
        "description": "Expression segment evaluated and joined into the resulting expression",
        "required": true,
        "mode": "ExecutableLambda",
        "cardinality": "OneOrMore",
        "role": "SourceExpression",
        "evaluation": "EvalSelf",
        "projection": "Value"
      }
    },
    "output": {
      "mode": "Value",
      "kind": "expression",
      "description": "Resolves to the composed expression"
    }
  }
}
```

</details>

---

[&larr; `case`](/reference/slots/core/case/) | [all core slots](/reference/slots/core/) | [`context` &rarr;](/reference/slots/core/context/)


---
title: "[invoke]"
description: "invoke is a core slot of Magic Cloud. Invokes a lambda expression as a callable slot."
generated: true
llms: false
slot_json: "/reference/slots/core/invoke/slot.json"
---

`invoke` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Invokes a lambda expression as a callable slot.

* **Value** (`lambda-object,lambda-tree`), required: Expression yielding the single lambda node to invoke
* **Returns**: Resolves to the invoked lambda's value result and any returned child nodes

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | object | no | Argument passed to the invoked lambda through its [.arguments] node. Can be repeated. |

Guide: [How to use [invoke]](/plugins/magic.lambda/executing/#how-to-use-invoke)

### Related documentation

* Part of the [magic.lambda](/plugins/magic.lambda/) plugin, which documents every slot it contains.
* Discussed in [Executing lambda objects](/plugins/magic.lambda/executing/).

### JSON declaration

This is the complete declaration of `invoke`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "invoke",
  "description": "Invokes a lambda expression as a callable slot",
  "signature": {
    "input": {
      "kind": "lambda-object,lambda-tree",
      "description": "Expression yielding the single lambda node to invoke",
      "required": true,
      "mode": "Expression"
    },
    "children": {
      "*": {
        "type": "object",
        "kind": "value",
        "description": "Argument passed to the invoked lambda through its [.arguments] node",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrMore",
        "role": "Arguments",
        "projection": "ArgumentBag"
      }
    },
    "output": {
      "mode": "Both",
      "kind": "lambda-result",
      "description": "Resolves to the invoked lambda's value result and any returned child nodes"
    }
  }
}
```

</details>

---

[&larr; `int2words`](/reference/slots/core/int2words/) | [all core slots](/reference/slots/core/) | [`join` &rarr;](/reference/slots/core/join/)


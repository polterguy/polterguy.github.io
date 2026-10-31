---
title: "[unwrap]"
description: "unwrap is a core slot of Magic Cloud. Forward-evaluates expression values on the selected nodes, replacing them with their resolved values; commonly used before [signal] or [add]."
generated: true
llms: false
slot_json: "/reference/slots/core/unwrap/slot.json"
---

`unwrap` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Forward-evaluates expression values on the selected nodes, replacing them with their resolved values; commonly used before [signal] or [add].

* **Value** (`node-list,single-object`), required: Expression selecting the node or nodes whose expressions should be unwrapped

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[apply-lists]` | bool | no | Whether list results should be applied while unwrapping. Default: `false`. |

Guide: [How to use [unwrap]](/plugins/magic.lambda/nodes/#how-to-use-unwrap)

### Related documentation

* Part of the [magic.lambda](/plugins/magic.lambda/) plugin, which documents every slot it contains.
* Discussed in [Modifying your lambda object](/plugins/magic.lambda/nodes/).

### JSON declaration

This is the complete declaration of `unwrap`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "unwrap",
  "description": "Forward-evaluates expression values on the selected nodes, replacing them with their resolved values; commonly used before [signal] or [add]",
  "signature": {
    "input": {
      "kind": "node-list,single-object",
      "description": "Expression selecting the node or nodes whose expressions should be unwrapped",
      "required": true,
      "mode": "Expression"
    },
    "children": {
      "apply-lists": {
        "type": "bool",
        "description": "Whether list results should be applied while unwrapping",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "false",
        "role": "Option",
        "projection": "Value"
      }
    }
  }
}
```

</details>

---

[&larr; `types`](/reference/slots/core/types/) | [all core slots](/reference/slots/core/) | [`version` &rarr;](/reference/slots/core/version/)


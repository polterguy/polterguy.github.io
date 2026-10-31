---
title: "[apply]"
description: "apply is a core slot of Magic Cloud. Stamps a template lambda with values from child argument nodes, producing one fully-substituted output per [.dp]."
generated: true
llms: false
slot_json: "/reference/slots/core/apply/slot.json"
---

`apply` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Stamps a template lambda with values from child argument nodes, producing one fully-substituted output per [.dp].

* **Value** (`template,lambda-tree`), required: Expression selecting the template node or nodes to transform
* **Returns**: Resolves to the transformed template nodes after applying the supplied arguments

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | object | no | Template replacement node matched by name; its value and children replace placeholders named {name}. Can be repeated. |

Guide: [How to use [apply]](/plugins/magic.lambda/types/#how-to-use-apply)

### Related documentation

* Part of the [magic.lambda](/plugins/magic.lambda/) plugin, which documents every slot it contains.
* Discussed in [Types and conversion](/plugins/magic.lambda/types/).

### JSON declaration

This is the complete declaration of `apply`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "apply",
  "description": "Stamps a template lambda with values from child argument nodes, producing one fully-substituted output per [.dp]",
  "signature": {
    "input": {
      "kind": "template,lambda-tree",
      "description": "Expression selecting the template node or nodes to transform",
      "required": true,
      "mode": "Expression"
    },
    "children": {
      "*": {
        "type": "object",
        "description": "Template replacement node matched by name; its value and children replace placeholders named {name}",
        "required": false,
        "mode": "Value",
        "cardinality": "ZeroOrMore",
        "role": "Arguments",
        "projection": "ArgumentBag"
      }
    },
    "output": {
      "mode": "Lambda",
      "kind": "applied-template,lambda-object,lambda-tree",
      "description": "Resolves to the transformed template nodes after applying the supplied arguments"
    }
  }
}
```

</details>

---

[&larr; `and`](/reference/slots/core/and/) | [all core slots](/reference/slots/core/) | [`case` &rarr;](/reference/slots/core/case/)


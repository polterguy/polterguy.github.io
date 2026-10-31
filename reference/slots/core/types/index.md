---
title: "[types]"
description: "types is a core slot of Magic Cloud. Lists every CLR type name recognized by Hyperlambda; useful when [convert] or [type] needs a valid target."
generated: true
llms: false
slot_json: "/reference/slots/core/types/slot.json"
---

`types` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Lists every CLR type name recognized by Hyperlambda; useful when [convert] or [type] needs a valid target.

* **Returns**: Resolves to one child node per known CLR type name

Guide: [How to use [types]](/plugins/magic.lambda/types/#how-to-use-types)

### Guide

[How to use `types`](/plugins/magic.lambda/types-slot/)

### JSON declaration

This is the complete declaration of `types`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "types",
  "description": "Lists every CLR type name recognized by Hyperlambda; useful when [convert] or [type] needs a valid target",
  "signature": {
    "output": {
      "mode": "Lambda",
      "kind": "type-name-list,string-list",
      "element-kind": "type-name,text",
      "description": "Resolves to one child node per known CLR type name"
    }
  }
}
```

</details>

---

[&larr; `type`](/reference/slots/core/type/) | [all core slots](/reference/slots/core/) | [`unwrap` &rarr;](/reference/slots/core/unwrap/)


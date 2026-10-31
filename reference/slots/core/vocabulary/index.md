---
title: "[vocabulary]"
description: "vocabulary is a core slot of Magic Cloud. Lists available compiled slots."
generated: true
llms: false
slot_json: "/reference/slots/core/vocabulary/slot.json"
---

`vocabulary` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Lists available compiled slots.

* **Value** (`slot-name`), optional: Optional prefix filter for slot names
* **Returns**: Resolves to available slot names as child nodes

Guide: [How to use [vocabulary]](/plugins/magic.lambda/types/#how-to-use-vocabulary)

### JSON declaration

This is the complete declaration of `vocabulary`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "vocabulary",
  "description": "Lists available compiled slots",
  "signature": {
    "input": {
      "kind": "slot-name",
      "description": "Optional prefix filter for slot names",
      "required": false,
      "mode": "ValueOrExpression"
    },
    "output": {
      "mode": "Lambda",
      "kind": "slot-name-list,string-list",
      "element-kind": "slot-name,text",
      "description": "Resolves to available slot names as child nodes"
    }
  }
}
```

</details>

---

[&larr; `version`](/reference/slots/core/version/) | [all core slots](/reference/slots/core/) | [`while` &rarr;](/reference/slots/core/while/)


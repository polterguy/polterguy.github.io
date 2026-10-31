---
title: "[system.plugin.list]"
description: "system.plugin.list is a slot in the system namespace of Magic Cloud. Lists dynamically loaded plugins."
generated: true
llms: false
slot_json: "/reference/slots/system/system.plugin.list/slot.json"
---

`system.plugin.list` is a slot in the `system` namespace, in Hyperlambda, the language of Magic Cloud. Lists dynamically loaded plugins.

* **Returns**: Returns one child node per dynamically loaded plugin name

### Guide

[How to use `system.plugin.list`](/plugins/magic.lambda.system/system.plugin.list/)

### JSON declaration

This is the complete declaration of `system.plugin.list`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "system.plugin.list",
  "description": "Lists dynamically loaded plugins",
  "signature": {
    "output": {
      "mode": "Lambda",
      "kind": "plugin-assembly-list,string-list",
      "element-kind": "plugin-assembly-name,text",
      "description": "Returns one child node per dynamically loaded plugin name"
    }
  }
}
```

</details>

---

[&larr; `system.plugin.execute`](/reference/slots/system/system.plugin.execute/) | [all `system.*` slots](/reference/slots/system/) | [`system.plugin.load` &rarr;](/reference/slots/system/system.plugin.load/)


---
title: "[system.plugin.unload]"
description: "system.plugin.unload is a slot in the system namespace of Magic Cloud. Unloads a plugin assembly."
generated: true
llms: false
slot_json: "/reference/slots/system/system.plugin.unload/slot.json"
---

`system.plugin.unload` is a slot in the `system` namespace, in Hyperlambda, the language of Magic Cloud. Unloads a plugin assembly.

* **Value** (`plugin-assembly-name`), required: Assembly name to unload

Guide: [How to use [system.plugin.unload]](/plugins/magic.lambda.system/#how-to-use-systempluginload-and-systempluginunload)

### JSON declaration

This is the complete declaration of `system.plugin.unload`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "system.plugin.unload",
  "description": "Unloads a plugin assembly",
  "signature": {
    "input": {
      "kind": "plugin-assembly-name",
      "description": "Assembly name to unload",
      "required": true,
      "mode": "ValueOrExpression"
    }
  }
}
```

</details>

---

[&larr; `system.plugin.load`](/reference/slots/system/system.plugin.load/) | [all `system.*` slots](/reference/slots/system/)


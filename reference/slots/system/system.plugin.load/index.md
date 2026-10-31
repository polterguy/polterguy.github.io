---
title: "[system.plugin.load]"
description: "system.plugin.load is a slot in the system namespace of Magic Cloud. Loads a plugin assembly."
generated: true
llms: false
slot_json: "/reference/slots/system/system.plugin.load/slot.json"
---

`system.plugin.load` is a slot in the `system` namespace, in Hyperlambda, the language of Magic Cloud. Loads a plugin assembly.

* **Value** (`plugin-assembly,binary-content`), required: Plugin assembly filename or assembly bytes

Guide: [How to use [system.plugin.load]](/plugins/magic.lambda.system/#how-to-use-systempluginload-and-systempluginunload)

### JSON declaration

This is the complete declaration of `system.plugin.load`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "system.plugin.load",
  "description": "Loads a plugin assembly",
  "signature": {
    "input": {
      "kind": "plugin-assembly,binary-content",
      "description": "Plugin assembly filename or assembly bytes",
      "required": true,
      "mode": "ValueOrExpression"
    }
  }
}
```

</details>

---

[&larr; `system.plugin.list`](/reference/slots/system/system.plugin.list/) | [all `system.*` slots](/reference/slots/system/) | [`system.plugin.unload` &rarr;](/reference/slots/system/system.plugin.unload/)


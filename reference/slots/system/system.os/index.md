---
title: "[system.os]"
description: "system.os is a slot in the system namespace of Magic Cloud. Returns a description of the current operating system."
generated: true
llms: false
slot_json: "/reference/slots/system/system.os/slot.json"
---

`system.os` is a slot in the `system` namespace, in Hyperlambda, the language of Magic Cloud. Returns a description of the current operating system.

* **Returns**: Resolves to the current operating system name

### JSON declaration

This is the complete declaration of `system.os`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "system.os",
  "description": "Returns a description of the current operating system",
  "signature": {
    "output": {
      "mode": "Value",
      "kind": "current-os-name,text",
      "description": "Resolves to the current operating system name"
    }
  }
}
```

</details>

---

[&larr; `system.is-os`](/reference/slots/system/system.is-os/) | [all `system.*` slots](/reference/slots/system/) | [`system.plugin.execute` &rarr;](/reference/slots/system/system.plugin.execute/)


---
title: "[system.is-os]"
description: "system.is-os is a slot in the system namespace of Magic Cloud. Returns true if the current operating system matches the specified platform."
generated: true
llms: false
slot_json: "/reference/slots/system/system.is-os/slot.json"
---

`system.is-os` is a slot in the `system` namespace, in Hyperlambda, the language of Magic Cloud. Returns true if the current operating system matches the specified platform.

* **Value** (`os-name`), required: Operating system platform name to compare against, typically WINDOWS, LINUX, OSX, or FREEBSD
* **Returns**: Returns true if the current operating system matches the supplied platform name

### Guide

[How to use `system.is-os`](/plugins/magic.lambda.system/system.is-os/)

### JSON declaration

This is the complete declaration of `system.is-os`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "system.is-os",
  "description": "Returns true if the current operating system matches the specified platform",
  "signature": {
    "input": {
      "kind": "os-name",
      "description": "Operating system platform name to compare against, typically WINDOWS, LINUX, OSX, or FREEBSD",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "output": {
      "mode": "Value",
      "kind": "boolean",
      "description": "Returns true if the current operating system matches the supplied platform name"
    }
  }
}
```

</details>

---

[&larr; `system.execute`](/reference/slots/system/system.execute/) | [all `system.*` slots](/reference/slots/system/) | [`system.os` &rarr;](/reference/slots/system/system.os/)


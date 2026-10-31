---
title: "[log.capabilities]"
description: "log.capabilities is a slot in the log namespace of Magic Cloud. Returns capabilities of the current log provider."
generated: true
llms: false
slot_json: "/reference/slots/log/log.capabilities/slot.json"
---

`log.capabilities` is a slot in the `log` namespace, in Hyperlambda, the language of Magic Cloud. Returns capabilities of the current log provider.

* **Returns**: Returns [can-filter] and [can-timeshift] capability nodes for the current log provider

### JSON declaration

This is the complete declaration of `log.capabilities`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "log.capabilities",
  "description": "Returns capabilities of the current log provider",
  "signature": {
    "output": {
      "mode": "Lambda",
      "kind": "log-capabilities,lambda-tree",
      "description": "Returns [can-filter] and [can-timeshift] capability nodes for the current log provider"
    }
  }
}
```

</details>

---

[all `log.*` slots](/reference/slots/log/) | [`log.count` &rarr;](/reference/slots/log/log.count/)


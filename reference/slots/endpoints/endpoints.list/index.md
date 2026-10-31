---
title: "[endpoints.list]"
description: "endpoints.list is a slot in the endpoints namespace of Magic Cloud. Lists dynamic Hyperlambda endpoints with metadata."
generated: true
llms: false
slot_json: "/reference/slots/endpoints/endpoints.list/slot.json"
---

`endpoints.list` is a slot in the `endpoints` namespace, in Hyperlambda, the language of Magic Cloud. Lists dynamic Hyperlambda endpoints with metadata.

* **Returns**: Resolves to one child node per discovered endpoint, including its endpoint metadata

### JSON declaration

This is the complete declaration of `endpoints.list`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "endpoints.list",
  "description": "Lists dynamic Hyperlambda endpoints with metadata",
  "signature": {
    "output": {
      "mode": "Lambda",
      "kind": "endpoint-list,node-list",
      "element-kind": "endpoint,lambda-tree",
      "description": "Resolves to one child node per discovered endpoint, including its endpoint metadata"
    }
  }
}
```

</details>

---

[all `endpoints.*` slots](/reference/slots/endpoints/)


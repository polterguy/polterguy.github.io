---
title: "[guid.new]"
description: "guid.new is a slot in the guid namespace of Magic Cloud. Generates a random version-4 GUID for use as a unique identifier."
generated: true
llms: false
slot_json: "/reference/slots/guid/guid.new/slot.json"
---

`guid.new` is a slot in the `guid` namespace, in Hyperlambda, the language of Magic Cloud. Generates a random version-4 GUID for use as a unique identifier.

* **Returns**: Resolves to a new GUID string

Guide: [How to use [guid.new]](/plugins/magic.lambda.guid/#how-to-use-guidnew)

### JSON declaration

This is the complete declaration of `guid.new`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "guid.new",
  "description": "Generates a random version-4 GUID for use as a unique identifier",
  "signature": {
    "output": {
      "mode": "Value",
      "kind": "guid,text",
      "description": "Resolves to a new GUID string"
    }
  }
}
```

</details>

---

[all `guid.*` slots](/reference/slots/guid/)


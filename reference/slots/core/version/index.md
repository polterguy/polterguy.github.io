---
title: "[version]"
description: "version is a core slot of Magic Cloud. Returns the Magic Cloud version to the caller."
generated: true
llms: false
slot_json: "/reference/slots/core/version/slot.json"
---

`version` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Returns the Magic Cloud version to the caller.

* **Returns**: Resolves to the Magic Cloud version

### JSON declaration

This is the complete declaration of `version`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "version",
  "description": "Returns the Magic Cloud version to the caller",
  "signature": {
    "output": {
      "mode": "Value",
      "kind": "version,text",
      "description": "Resolves to the Magic Cloud version"
    }
  }
}
```

</details>

---

[&larr; `unwrap`](/reference/slots/core/unwrap/) | [all core slots](/reference/slots/core/) | [`vocabulary` &rarr;](/reference/slots/core/vocabulary/)


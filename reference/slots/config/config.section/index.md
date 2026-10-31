---
title: "[config.section]"
description: "config.section is a slot in the config namespace of Magic Cloud. Reads an entire appsettings.json section by key, returning its keys and nested values as child nodes."
generated: true
llms: false
slot_json: "/reference/slots/config/config.section/slot.json"
---

`config.section` is a slot in the `config` namespace, in Hyperlambda, the language of Magic Cloud. Reads an entire appsettings.json section by key, returning its keys and nested values as child nodes.

* **Value** (`config-key`), required: Configuration section to retrieve
* **Returns**: Returns one child node per key/value entry in the requested configuration section

### JSON declaration

This is the complete declaration of `config.section`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "config.section",
  "description": "Reads an entire appsettings.json section by key, returning its keys and nested values as child nodes",
  "signature": {
    "input": {
      "kind": "config-key",
      "description": "Configuration section to retrieve",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "output": {
      "mode": "Lambda",
      "kind": "config-section,text,lambda-tree",
      "description": "Returns one child node per key/value entry in the requested configuration section"
    }
  }
}
```

</details>

---

[&larr; `config.save`](/reference/slots/config/config.save/) | [all `config.*` slots](/reference/slots/config/)


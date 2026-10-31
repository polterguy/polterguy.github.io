---
title: "[config.load]"
description: "config.load is a slot in the config namespace of Magic Cloud. Returns the raw contents of appsettings.json; pair with [config.save] for round-trip config editing."
generated: true
llms: false
slot_json: "/reference/slots/config/config.load/slot.json"
---

`config.load` is a slot in the `config` namespace, in Hyperlambda, the language of Magic Cloud. Returns the raw contents of appsettings.json; pair with [config.save] for round-trip config editing.

* **Returns**: Resolves to the raw appsettings.json content

### Related documentation

* Part of the [magic.lambda.config](/plugins/magic.lambda.config/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `config.load`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "config.load",
  "description": "Returns the raw contents of appsettings.json; pair with [config.save] for round-trip config editing",
  "signature": {
    "output": {
      "mode": "Value",
      "kind": "json,text",
      "description": "Resolves to the raw appsettings.json content"
    }
  }
}
```

</details>

---

[&larr; `config.get`](/reference/slots/config/config.get/) | [all `config.*` slots](/reference/slots/config/) | [`config.save` &rarr;](/reference/slots/config/config.save/)


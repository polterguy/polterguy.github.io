---
title: "[config.save]"
description: "config.save is a slot in the config namespace of Magic Cloud. Saves JSON configuration values to appsettings.json."
generated: true
llms: false
slot_json: "/reference/slots/config/config.save/slot.json"
---

`config.save` is a slot in the `config` namespace, in Hyperlambda, the language of Magic Cloud. Saves JSON configuration values to appsettings.json.

* **Value** (`json`), required: Valid JSON object content to save to appsettings.json

### JSON declaration

This is the complete declaration of `config.save`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "config.save",
  "description": "Saves JSON configuration values to appsettings.json",
  "signature": {
    "input": {
      "kind": "json",
      "description": "Valid JSON object content to save to appsettings.json",
      "required": true,
      "mode": "ValueOrExpression"
    }
  }
}
```

</details>

---

[&larr; `config.load`](/reference/slots/config/config.load/) | [all `config.*` slots](/reference/slots/config/) | [`config.section` &rarr;](/reference/slots/config/config.section/)


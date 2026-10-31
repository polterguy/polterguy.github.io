---
title: "[config.get]"
description: "config.get is a slot in the config namespace of Magic Cloud. Reads a single setting from appsettings.json by dotted key path (e.g. 'magic:auth:secret')."
generated: true
llms: false
slot_json: "/reference/slots/config/config.get/slot.json"
---

`config.get` is a slot in the `config` namespace, in Hyperlambda, the language of Magic Cloud. Reads a single setting from appsettings.json by dotted key path (e.g. 'magic:auth:secret').

* **Value** (`config-key`), required: Configuration key to retrieve
* **Returns**: Resolves to the configuration value, or the first child value when the key is missing

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | string | no | Default value source evaluated and returned when the configuration key does not exist. |

### Guide

[How to use `config.get`](/plugins/magic.lambda.config/config.get/)

### JSON declaration

This is the complete declaration of `config.get`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "config.get",
  "description": "Reads a single setting from appsettings.json by dotted key path (e.g. 'magic:auth:secret')",
  "signature": {
    "input": {
      "kind": "config-key",
      "description": "Configuration key to retrieve",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "*": {
        "type": "string",
        "kind": "config-default",
        "description": "Default value source evaluated and returned when the configuration key does not exist",
        "required": false,
        "mode": "ExecutableLambda",
        "cardinality": "ZeroOrOne",
        "role": "SourceExpression",
        "evaluation": "EvalSelf",
        "projection": "Value"
      }
    },
    "output": {
      "mode": "Value",
      "kind": "config-value,text",
      "description": "Resolves to the configuration value, or the first child value when the key is missing"
    }
  }
}
```

</details>

---

[all `config.*` slots](/reference/slots/config/) | [`config.load` &rarr;](/reference/slots/config/config.load/)


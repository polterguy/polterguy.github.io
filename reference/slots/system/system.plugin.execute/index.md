---
title: "[system.plugin.execute]"
description: "system.plugin.execute is a slot in the system namespace of Magic Cloud. Loads, executes, and unloads a plugin in a single scope."
generated: true
llms: false
slot_json: "/reference/slots/system/system.plugin.execute/slot.json"
---

`system.plugin.execute` is a slot in the `system` namespace, in Hyperlambda, the language of Magic Cloud. Loads, executes, and unloads a plugin in a single scope.

* **Value** (`plugin-assembly,binary-content`), required: Plugin assembly filename or assembly bytes

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | no | Executable body evaluated while the plugin is loaded. Can be repeated. |

Guide: [How to use [system.plugin.execute]](/plugins/magic.lambda.system/#systempluginexecute)

### JSON declaration

This is the complete declaration of `system.plugin.execute`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "system.plugin.execute",
  "description": "Loads, executes, and unloads a plugin in a single scope",
  "signature": {
    "input": {
      "kind": "plugin-assembly,binary-content",
      "description": "Plugin assembly filename or assembly bytes",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "*": {
        "type": "lambda",
        "description": "Executable body evaluated while the plugin is loaded",
        "required": false,
        "mode": "ExecutableLambda",
        "cardinality": "ZeroOrMore",
        "role": "ExecutableBody",
        "evaluation": "EvalSelf",
        "projection": "Self"
      }
    }
  }
}
```

</details>

---

[&larr; `system.os`](/reference/slots/system/system.os/) | [all `system.*` slots](/reference/slots/system/) | [`system.plugin.list` &rarr;](/reference/slots/system/system.plugin.list/)


---
title: "[config.get]"
description: "config.get is a slot in the config namespace of Magic Cloud. Reads a single setting from appsettings.json by dotted key path (e.g. 'magic:auth:secret')."
generated: true
llms: "guide"
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

<!-- guide -->
This slot allows you to retrieve configuration settings. To retrieve settings you can supply a
_"path"_ such as _"foo:bar"_ to for instance an invocation to **[config.get]**. This will traverse into
your _"foo"_ config setting, find its _"bar"_ key, and return the value of your _"bar"_ key. Below is
an example of usage.

```
config.get:"foo:bar"
```

Assuming your configuration file looks like the following.

```
{
   "foo": {
      "bar": 42
   }
}
```

... afterwards the value of your __[config.get]__ node will be the following.

```
config.get:42
```

**Notice** - Due to implementation details of .Net and its `IConfiguration` specifically, values
returned will _always_ be strings, and you'll have to manually convert these to other types, using for
instance the **[\[convert\]](/reference/slots/core/convert/)** slot from magic.lambda. This _might_ change in a future release though.
You can also provide a default value that will be returned if no configuration value is found, such
as the following illustrates.

```
.foo:foo
config.get:"magic:foo:non-existing-key"
   get-value:x:@.foo
```

Since the above _"non-existing-key"_ doesn't exist in your configuration file, the above Hyperlambda will
return the value _"foo"_ being the result of the invocation to the **[\[get-value\]](/reference/slots/core/get-value/)** slot. This allows you
to create default values your code resorts to if the specified configuration setting doesn't exist.
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.config](/plugins/magic.lambda.config/) plugin, which documents every slot it contains.

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


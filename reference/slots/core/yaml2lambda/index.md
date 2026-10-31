---
title: "[yaml2lambda]"
description: "yaml2lambda is a core slot of Magic Cloud. Transforms YAML into a lambda hierarchy."
generated: true
llms: "guide"
slot_json: "/reference/slots/core/yaml2lambda/slot.json"
---

`yaml2lambda` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Transforms YAML into a lambda hierarchy.

* **Value** (`yaml`), required: YAML text to transform
* **Returns**: Resolves to the parsed lambda hierarchy as child nodes

### Guide

<!-- guide -->
This guide covers [`yaml2lambda`](/reference/slots/core/yaml2lambda/), [`lambda2yaml`](/reference/slots/core/lambda2yaml/) together.

The **[yaml2lambda]** slot converts a YAML input string to a lambda object. Since YAML arguably is just another representation of
JSON, these slot have been added to this project. Notice, the same constraints applies for YAML as does for JSON, implying
a YAML string can always be converted to a lambda object, but the opposite is not necessary true. Basic usage is as follows.

```
.yaml:@"
foo: howdy
bar: jo
howdy: !!bool true
children:
- howdy
- some
"
yaml2lambda:x:@.yaml
lambda2yaml:x:-/*
```

The above will result in the following.

```
yaml2lambda
   foo:howdy
   bar:jo
   howdy:bool:true
   children
      .:howdy
      .:some
lambda2yaml: /* ... YAML content ... */
```

Internally the **[yaml2lambda]** slot first converts the input YAML to JSON, for then to use the **[json2lambda]**
logic, ensuring the exact same result, regardless of whether or not you start out with JSON or YAML.
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.json](/plugins/magic.lambda.json/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `yaml2lambda`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "yaml2lambda",
  "description": "Transforms YAML into a lambda hierarchy",
  "signature": {
    "input": {
      "kind": "yaml",
      "description": "YAML text to transform",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "output": {
      "mode": "Lambda",
      "kind": "lambda-tree",
      "description": "Resolves to the parsed lambda hierarchy as child nodes"
    }
  }
}
```

</details>

---

[&larr; `yaml2json`](/reference/slots/core/yaml2json/) | [all core slots](/reference/slots/core/) | [`yield` &rarr;](/reference/slots/core/yield/)


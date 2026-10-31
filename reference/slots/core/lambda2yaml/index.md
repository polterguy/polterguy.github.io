---
title: "[lambda2yaml]"
description: "lambda2yaml is a core slot of Magic Cloud. Transforms a lambda hierarchy into YAML."
generated: true
llms: "guide"
slot_json: "/reference/slots/core/lambda2yaml/slot.json"
---

`lambda2yaml` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Transforms a lambda hierarchy into YAML.

* **Value** (`node-list,lambda-tree`), required: Expression selecting the nodes (rows) to transform
* **Returns**: Resolves to the generated YAML string

### Guide

<!-- guide -->
This guide covers [`lambda2yaml`](/reference/slots/core/lambda2yaml/), [`yaml2lambda`](/reference/slots/core/yaml2lambda/) together.

The **[\[yaml2lambda\]](/reference/slots/core/yaml2lambda/)** slot converts a YAML input string to a lambda object. Since YAML arguably is just another representation of
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

Internally the **[\[yaml2lambda\]](/reference/slots/core/yaml2lambda/)** slot first converts the input YAML to JSON, for then to use the **[\[json2lambda\]](/reference/slots/core/json2lambda/)**
logic, ensuring the exact same result, regardless of whether or not you start out with JSON or YAML.
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.json](/plugins/magic.lambda.json/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `lambda2yaml`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "lambda2yaml",
  "description": "Transforms a lambda hierarchy into YAML",
  "signature": {
    "input": {
      "kind": "node-list,lambda-tree",
      "description": "Expression selecting the nodes (rows) to transform",
      "required": true,
      "mode": "Expression"
    },
    "output": {
      "mode": "Value",
      "kind": "yaml,text",
      "description": "Resolves to the generated YAML string"
    }
  }
}
```

</details>

---

[&larr; `lambda2xml`](/reference/slots/core/lambda2xml/) | [all core slots](/reference/slots/core/) | [`lt` &rarr;](/reference/slots/core/lt/)


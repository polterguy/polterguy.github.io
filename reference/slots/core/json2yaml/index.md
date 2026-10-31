---
title: "[json2yaml]"
description: "json2yaml is a core slot of Magic Cloud. Transforms JSON into YAML."
generated: true
llms: "guide"
slot_json: "/reference/slots/core/json2yaml/slot.json"
---

`json2yaml` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Transforms JSON into YAML.

* **Value** (`json`), required: JSON text to transform
* **Returns**: Resolves to the generated YAML string

### Guide

<!-- guide -->
This guide covers [`json2yaml`](/reference/slots/core/json2yaml/), [`yaml2json`](/reference/slots/core/yaml2json/) together.

The **[\[yaml2json\]](/reference/slots/core/yaml2json/)** slot converts the specified YAML input string to a JSON string. Basic usage is as follows.

```
.yaml:@"foo: howdy
bar: jo
howdy: !!bool true
children:
- howdy
- some
"
yaml2json:x:@.yaml
json2yaml:x:-
```

The above results in the following.

```
{
  "foo": "howdy",
  "bar": "jo",
  "howdy": true,
  "children": [
    "howdy", "some"
  ]
}
```

Notice, the above have been formatted for brevity. The actual JSON result will _not_ be formatted, or having indentation to ensure
result is as compact as possible.
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.json](/plugins/magic.lambda.json/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `json2yaml`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "json2yaml",
  "description": "Transforms JSON into YAML",
  "signature": {
    "input": {
      "kind": "json",
      "description": "JSON text to transform",
      "required": true,
      "mode": "ValueOrExpression"
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

[&larr; `json2lambda-stream`](/reference/slots/core/json2lambda-stream/) | [all core slots](/reference/slots/core/) | [`lambda2csv` &rarr;](/reference/slots/core/lambda2csv/)


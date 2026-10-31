---
title: "[yaml2json]"
description: "yaml2json is a core slot of Magic Cloud. Transforms YAML into JSON."
generated: true
llms: "guide"
slot_json: "/reference/slots/core/yaml2json/slot.json"
---

`yaml2json` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Transforms YAML into JSON.

* **Value** (`yaml`), required: YAML text to transform
* **Returns**: Resolves to the generated JSON string

### Guide

<!-- guide -->
This guide covers [`yaml2json`](/reference/slots/core/yaml2json/), [`json2yaml`](/reference/slots/core/json2yaml/) together.

The **[yaml2json]** slot converts the specified YAML input string to a JSON string. Basic usage is as follows.

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

This is the complete declaration of `yaml2json`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "yaml2json",
  "description": "Transforms YAML into JSON",
  "signature": {
    "input": {
      "kind": "yaml",
      "description": "YAML text to transform",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "output": {
      "mode": "Value",
      "kind": "json,text",
      "description": "Resolves to the generated JSON string"
    }
  }
}
```

</details>

---

[&larr; `xml2lambda`](/reference/slots/core/xml2lambda/) | [all core slots](/reference/slots/core/) | [`yaml2lambda` &rarr;](/reference/slots/core/yaml2lambda/)


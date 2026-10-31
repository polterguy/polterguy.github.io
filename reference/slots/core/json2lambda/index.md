---
title: "[json2lambda]"
description: "json2lambda is a core slot of Magic Cloud. Transforms JSON into a lambda hierarchy."
generated: true
llms: "guide"
slot_json: "/reference/slots/core/json2lambda/slot.json"
---

`json2lambda` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Transforms JSON into a lambda hierarchy.

* **Value** (`json`), required: JSON text to transform
* **Returns**: Resolves to the parsed lambda hierarchy as child nodes

### Guide

<!-- guide -->
This guide covers [`json2lambda`](/reference/slots/core/json2lambda/), [`lambda2json`](/reference/slots/core/lambda2json/) together.

```
.json:@"{""property"": ""value""}"
json2lambda:x:-
lambda2json:x:-/*
```

The **[lambda2json]** slot can optionally take a **[format]** argument, with a boolean _"true"_ value, which implies the
resulting JSON will be indented and nicely formated, making it more readable.

**Notice** - Although all JSON can be transformed into lambda, the opposite is not necessarily true. This is because
lambda allows for having multiple nodes with the same name for instance, which would result in a JSON object with
multiple properties having the same key. Hence, have this in mind as you persist your lambda objects into JSON.
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.json](/plugins/magic.lambda.json/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `json2lambda`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "json2lambda",
  "description": "Transforms JSON into a lambda hierarchy",
  "signature": {
    "input": {
      "kind": "json",
      "description": "JSON text to transform",
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

[&larr; `join`](/reference/slots/core/join/) | [all core slots](/reference/slots/core/) | [`json2lambda-stream` &rarr;](/reference/slots/core/json2lambda-stream/)


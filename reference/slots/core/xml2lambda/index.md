---
title: "[xml2lambda]"
description: "xml2lambda is a core slot of Magic Cloud. Transforms XML into a lambda hierarchy."
generated: true
llms: false
slot_json: "/reference/slots/core/xml2lambda/slot.json"
---

`xml2lambda` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Transforms XML into a lambda hierarchy.

* **Value** (`xml`), required: XML text to transform
* **Returns**: Resolves to the parsed XML hierarchy as child nodes; attributes are emitted as @name child nodes, text as #text child nodes, and comments/whitespace-only text nodes are omitted

### Guide

[How to use `xml2lambda`](/plugins/magic.lambda.xml/xml2lambda/)

### JSON declaration

This is the complete declaration of `xml2lambda`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "xml2lambda",
  "description": "Transforms XML into a lambda hierarchy",
  "signature": {
    "input": {
      "kind": "xml",
      "description": "XML text to transform",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "output": {
      "mode": "Lambda",
      "kind": "xml-tree",
      "element-kind": "xml-element",
      "description": "Resolves to the parsed XML hierarchy as child nodes; attributes are emitted as @name child nodes, text as #text child nodes, and comments/whitespace-only text nodes are omitted"
    }
  }
}
```

</details>

---

[&larr; `whitelist`](/reference/slots/core/whitelist/) | [all core slots](/reference/slots/core/) | [`yaml2json` &rarr;](/reference/slots/core/yaml2json/)


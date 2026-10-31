---
title: "[html2lambda]"
description: "html2lambda is a core slot of Magic Cloud. Transforms HTML into a lambda hierarchy."
generated: true
llms: false
slot_json: "/reference/slots/core/html2lambda/slot.json"
---

`html2lambda` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Transforms HTML into a lambda hierarchy.

* **Value** (`html`), required: HTML markup to transform
* **Returns**: Resolves to the parsed HTML hierarchy as child nodes

### Guide

[How to use `html2lambda`](/plugins/magic.lambda.html/html2lambda/)

### JSON declaration

This is the complete declaration of `html2lambda`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "html2lambda",
  "description": "Transforms HTML into a lambda hierarchy",
  "signature": {
    "input": {
      "kind": "html",
      "description": "HTML markup to transform",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "output": {
      "mode": "Lambda",
      "kind": "html-tree",
      "description": "Resolves to the parsed HTML hierarchy as child nodes"
    }
  }
}
```

</details>

---

[&larr; `html-decode`](/reference/slots/core/html-decode/) | [all core slots](/reference/slots/core/) | [`html2markdown` &rarr;](/reference/slots/core/html2markdown/)


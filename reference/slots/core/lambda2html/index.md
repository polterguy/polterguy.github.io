---
title: "[lambda2html]"
description: "lambda2html is a core slot of Magic Cloud. Transforms a lambda hierarchy into HTML."
generated: true
llms: false
slot_json: "/reference/slots/core/lambda2html/slot.json"
---

`lambda2html` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Transforms a lambda hierarchy into HTML.

* **Value** (`html-tree`), required: Expression selecting the lambda hierarchy to transform
* **Returns**: Resolves to the generated HTML markup

Guide: [How to use [lambda2html]](/plugins/magic.lambda.html/#how-to-use-lambda2html)

### JSON declaration

This is the complete declaration of `lambda2html`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "lambda2html",
  "description": "Transforms a lambda hierarchy into HTML",
  "signature": {
    "input": {
      "kind": "html-tree",
      "description": "Expression selecting the lambda hierarchy to transform",
      "required": true,
      "mode": "Expression"
    },
    "output": {
      "mode": "Value",
      "kind": "html,text",
      "description": "Resolves to the generated HTML markup"
    }
  }
}
```

</details>

---

[&larr; `lambda2csv`](/reference/slots/core/lambda2csv/) | [all core slots](/reference/slots/core/) | [`lambda2hyper` &rarr;](/reference/slots/core/lambda2hyper/)


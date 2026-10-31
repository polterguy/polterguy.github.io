---
title: "[lambda2html]"
description: "lambda2html is a core slot of Magic Cloud. Transforms a lambda hierarchy into HTML."
generated: true
llms: "guide"
slot_json: "/reference/slots/core/lambda2html/slot.json"
---

`lambda2html` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Transforms a lambda hierarchy into HTML.

* **Value** (`html-tree`), required: Expression selecting the lambda hierarchy to transform
* **Returns**: Resolves to the generated HTML markup

### Guide

<!-- guide -->
This is the reverse of **[\[html2lambda\]](/reference/slots/core/html2lambda/)** and returns HTML resulting from the specified lambda object. Below
is example usage.

```
.html:@"<html>
  <head>
    <title>Howdy</title>
  </head>
  <body>
    <p class=""foo"">Howdy <strong>world</strong> - This is cool!</p>
  </body>
</html>"
html2lambda:x:-
lambda2html:x:-/*
```

The above will result in the following HTML, formatted for brevity.

```html
<html>
  <head>
    <title>Howdy</title>
  </head>
  <body>
    <p class="foo">Howdy <strong>world</strong> - This is cool!</p>
  </body>
</html>
```
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.html](/plugins/magic.lambda.html/) plugin, which documents every slot it contains.

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


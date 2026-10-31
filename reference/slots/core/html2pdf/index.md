---
title: "[html2pdf]"
description: "html2pdf is a core slot of Magic Cloud. Converts HTML into a PDF document."
generated: true
llms: "guide"
slot_json: "/reference/slots/core/html2pdf/slot.json"
---

`html2pdf` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Converts HTML into a PDF document.

* **Value** (`html`), required: HTML markup to convert
* **Returns**: Resolves to the generated PDF bytes

### Guide

<!-- guide -->
This slot converts the HTML markup given as its value into a PDF document, and returns the PDF as raw bytes in
its value. The value can be a constant or an expression. Any images, stylesheets and fonts the HTML references
are loaded through Hyperlambda's **[\[io.file.load.binary\]](/reference/slots/io/io.file.load.binary/)** and **[\[http.get\]](/reference/slots/http/http.get/)** slots, instead of directly by the
PDF library.
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.pdf](/plugins/magic.lambda.pdf/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `html2pdf`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "html2pdf",
  "description": "Converts HTML into a PDF document",
  "signature": {
    "input": {
      "kind": "html",
      "description": "HTML markup to convert",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "output": {
      "mode": "Value",
      "kind": "pdf-content,binary-content",
      "description": "Resolves to the generated PDF bytes"
    }
  }
}
```

</details>

---

[&larr; `html2markdown`](/reference/slots/core/html2markdown/) | [all core slots](/reference/slots/core/) | [`hyper2lambda` &rarr;](/reference/slots/core/hyper2lambda/)


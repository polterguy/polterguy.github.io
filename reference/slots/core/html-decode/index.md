---
title: "[html-decode]"
description: "html-decode is a core slot of Magic Cloud. HTML decodes the specified string."
generated: true
llms: "guide"
slot_json: "/reference/slots/core/html-decode/slot.json"
---

`html-decode` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. HTML decodes the specified string.

* **Value** (`html-encoded`), required: HTML encoded text to decode
* **Returns**: Resolves to the decoded text

### Guide

<!-- guide -->
This slot HTML decodes its value, equivalent of `HttpUtility.HtmlDecode` in C#, turning entities such as
`&amp;` and `&lt;` back into the characters they represent. The value is mandatory, and can be given as a
constant or as an expression pointing to a single node. The slot returns the decoded string as its value.
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.html](/plugins/magic.lambda.html/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `html-decode`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "html-decode",
  "description": "HTML decodes the specified string",
  "signature": {
    "input": {
      "kind": "html-encoded",
      "description": "HTML encoded text to decode",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "output": {
      "mode": "Value",
      "kind": "html,text",
      "description": "Resolves to the decoded text"
    }
  }
}
```

</details>

---

[&larr; `get-value`](/reference/slots/core/get-value/) | [all core slots](/reference/slots/core/) | [`html2lambda` &rarr;](/reference/slots/core/html2lambda/)


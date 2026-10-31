---
title: "[lambda2xml]"
description: "lambda2xml is a core slot of Magic Cloud. Converts a lambda object to an XML fragment or document."
generated: true
llms: "guide"
slot_json: "/reference/slots/core/lambda2xml/slot.json"
---

`lambda2xml` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Converts a lambda object to an XML fragment or document.

* **Value** (`xml-tree`), required: Expression selecting a SINGLE lambda root to transform (XML has exactly one document root)
* **Returns**: Resolves to the generated XML string

### Guide

<!-- guide -->
To convert from a lambda object to an XML object you can use something such as follows.

```
.xml
   CATALOG
      PLANT
         COMMON
            #text:Bloodroot
         BOTANICAL
            #text:Sanguinaria canadensis
         ZONE
            #text:4
         LIGHT
            #text:Mostly Shady
         PRICE
            #text:$2.44
         AVAILABILITY
            #text:031599
lambda2xml:x:@.xml/*
```
<!-- /guide -->

### JSON declaration

This is the complete declaration of `lambda2xml`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "lambda2xml",
  "description": "Converts a lambda object to an XML fragment or document",
  "signature": {
    "input": {
      "kind": "xml-tree",
      "description": "Expression selecting a SINGLE lambda root to transform (XML has exactly one document root)",
      "required": true,
      "mode": "Expression"
    },
    "output": {
      "mode": "Value",
      "kind": "xml,text",
      "description": "Resolves to the generated XML string"
    }
  }
}
```

</details>

---

[&larr; `lambda2json`](/reference/slots/core/lambda2json/) | [all core slots](/reference/slots/core/) | [`lambda2yaml` &rarr;](/reference/slots/core/lambda2yaml/)


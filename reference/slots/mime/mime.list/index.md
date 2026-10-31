---
title: "[mime.list]"
description: "mime.list is a slot in the mime namespace of Magic Cloud. Lists registered MIME type mappings."
generated: true
llms: "guide"
slot_json: "/reference/slots/mime/mime.list/slot.json"
---

`mime.list` is a slot in the `mime` namespace, in Hyperlambda, the language of Magic Cloud. Lists registered MIME type mappings.

* **Returns**: Resolves to one named child node per registered MIME type mapping, where the child name is the file extension and the value is the MIME type

### Guide

<!-- guide -->
This slot lists all MIME type mappings registered in the current installation, including those added with **[mime.add]**.
It returns one child node for each mapping, where the name of the child node is the file extension and its value is the MIME type.
It takes no arguments.
<!-- /guide -->

### JSON declaration

This is the complete declaration of `mime.list`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "mime.list",
  "description": "Lists registered MIME type mappings",
  "signature": {
    "output": {
      "mode": "Lambda",
      "kind": "mime-type-list,string-list",
      "element-kind": "mime-type-mapping,text",
      "description": "Resolves to one named child node per registered MIME type mapping, where the child name is the file extension and the value is the MIME type"
    }
  }
}
```

</details>

---

[&larr; `mime.create`](/reference/slots/mime/mime.create/) | [all `mime.*` slots](/reference/slots/mime/) | [`mime.parse` &rarr;](/reference/slots/mime/mime.parse/)


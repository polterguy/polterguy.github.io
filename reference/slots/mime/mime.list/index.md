---
title: "[mime.list]"
description: "mime.list is a slot in the mime namespace of Magic Cloud. Lists registered MIME type mappings."
generated: true
llms: false
slot_json: "/reference/slots/mime/mime.list/slot.json"
---

`mime.list` is a slot in the `mime` namespace, in Hyperlambda, the language of Magic Cloud. Lists registered MIME type mappings.

* **Returns**: Resolves to one named child node per registered MIME type mapping, where the child name is the file extension and the value is the MIME type

Guide: [How to use [mime.list]](/plugins/magic.endpoint/#how-to-use-mimelist)

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


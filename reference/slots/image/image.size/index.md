---
title: "[image.size]"
description: "image.size is a slot in the image namespace of Magic Cloud. Returns the width and height of an image."
generated: true
llms: false
slot_json: "/reference/slots/image/image.size/slot.json"
---

`image.size` is a slot in the `image` namespace, in Hyperlambda, the language of Magic Cloud. Returns the width and height of an image.

* **Value** (`image-file`), required: Image filename to inspect
* **Returns**: Returns [width:int] and [height:int] child nodes for the image dimensions

### Related documentation

* Part of the [magic.lambda.image](/plugins/magic.lambda.image/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `image.size`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "image.size",
  "description": "Returns the width and height of an image",
  "signature": {
    "input": {
      "kind": "image-file",
      "description": "Image filename to inspect",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "output": {
      "mode": "Lambda",
      "kind": "image-dimensions,lambda-tree",
      "description": "Returns [width:int] and [height:int] child nodes for the image dimensions"
    }
  }
}
```

</details>

---

[&larr; `image.resize`](/reference/slots/image/image.resize/) | [all `image.*` slots](/reference/slots/image/)


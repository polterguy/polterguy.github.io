---
title: "[image.chart]"
description: "image.chart is a slot in the image namespace of Magic Cloud. Renders a bar, stacked, or grouped chart from the supplied series data as a PNG image."
generated: true
llms: false
slot_json: "/reference/slots/image/image.chart/slot.json"
---

`image.chart` is a slot in the `image` namespace, in Hyperlambda, the language of Magic Cloud. Renders a bar, stacked, or grouped chart from the supplied series data as a PNG image.

* **Value** (`chart-type`), required: Chart type to create, such as bars, stacked, or grouped
* **Returns**: Resolves to the generated chart image bytes

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| `[bars]` | lambda | yes | Chart values keyed by label; grouped and stacked charts use nested numeric values. |
| `[bars]` / _any node name_ | double\|lambda | yes | Bar value or grouped/stacked bar value collection. Can be repeated. |
| `[filename]` | string | no | Optional destination filename. |
| `[height]` | int | yes | Chart height in pixels. |
| `[legend]` | lambda | no | Legend labels required by grouped and stacked charts. |
| `[legend]` / _unnamed child node_ | string | no | Legend label. Can be repeated. |
| `[width]` | int | yes | Chart width in pixels. |

Guide: [How to use [image.chart]](/plugins/magic.lambda.image/#how-to-use-imagechart)

### JSON declaration

This is the complete declaration of `image.chart`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "image.chart",
  "description": "Renders a bar, stacked, or grouped chart from the supplied series data as a PNG image",
  "signature": {
    "input": {
      "kind": "chart-type",
      "description": "Chart type to create, such as bars, stacked, or grouped",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "width": {
        "type": "int",
        "description": "Chart width in pixels",
        "required": true,
        "mode": "ValueOrExpression",
        "cardinality": "ExactlyOne",
        "role": "Option",
        "projection": "Value"
      },
      "height": {
        "type": "int",
        "description": "Chart height in pixels",
        "required": true,
        "mode": "ValueOrExpression",
        "cardinality": "ExactlyOne",
        "role": "Option",
        "projection": "Value"
      },
      "filename": {
        "type": "string",
        "kind": "image-file",
        "description": "Optional destination filename",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      },
      "bars": {
        "type": "lambda",
        "description": "Chart values keyed by label; grouped and stacked charts use nested numeric values",
        "required": true,
        "mode": "ValueOrExpression",
        "cardinality": "ExactlyOne",
        "role": "StructuredObject",
        "projection": "StructuredTree",
        "children": {
          "*": {
            "type": "double|lambda",
            "description": "Bar value or grouped/stacked bar value collection",
            "required": true,
            "mode": "ValueOrExpression",
            "cardinality": "OneOrMore",
            "role": "DynamicMap",
            "projection": "StructuredTree"
          }
        }
      },
      "legend": {
        "type": "lambda",
        "description": "Legend labels required by grouped and stacked charts",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "StructuredObject",
        "projection": "Children",
        "children": [
          {
            "type": "string",
            "kind": "chart-legend-label",
            "description": "Legend label",
            "required": false,
            "mode": "ValueOrExpression",
            "cardinality": "ZeroOrMore",
            "role": "Option",
            "projection": "Value"
          }
        ]
      }
    },
    "output": {
      "mode": "Value",
      "kind": "image,binary-content",
      "description": "Resolves to the generated chart image bytes"
    }
  }
}
```

</details>

---

[all `image.*` slots](/reference/slots/image/) | [`image.convert` &rarr;](/reference/slots/image/image.convert/)


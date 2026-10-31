---
title: "[time.format]"
description: "time.format is a slot in the time namespace of Magic Cloud. Formats a TimeSpan value."
generated: true
llms: false
slot_json: "/reference/slots/time/time.format/slot.json"
---

`time.format` is a slot in the `time` namespace, in Hyperlambda, the language of Magic Cloud. Formats a TimeSpan value.

* **Value** (`timespan`), required: Time span to format
* **Returns**: Resolves to the formatted time string

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[format]` | string | yes | Format string. |

Guide: [How to use [time.format]](/plugins/magic.lambda.dates/#how-to-use-timeformat)

### JSON declaration

This is the complete declaration of `time.format`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "time.format",
  "description": "Formats a TimeSpan value",
  "signature": {
    "input": {
      "kind": "timespan",
      "description": "Time span to format",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "format": {
        "type": "string",
        "kind": "date-format",
        "description": "Format string",
        "required": true,
        "mode": "ValueOrExpression",
        "cardinality": "ExactlyOne",
        "role": "Option",
        "projection": "Value"
      }
    },
    "output": {
      "mode": "Value",
      "kind": "formatted-time,text",
      "description": "Resolves to the formatted time string"
    }
  }
}
```

</details>

---

[all `time.*` slots](/reference/slots/time/) | [`time.total-milliseconds` &rarr;](/reference/slots/time/time.total-milliseconds/)


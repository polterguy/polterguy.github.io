---
title: "[date.format]"
description: "date.format is a slot in the date namespace of Magic Cloud. Formats a DateTime using a .NET format string (e.g. yyyy-MM-dd HH:mm) for display or logging."
generated: true
llms: false
slot_json: "/reference/slots/date/date.format/slot.json"
---

`date.format` is a slot in the `date` namespace, in Hyperlambda, the language of Magic Cloud. Formats a DateTime using a .NET format string (e.g. yyyy-MM-dd HH:mm) for display or logging.

* **Value** (`date`), required: Date value to format
* **Returns**: Resolves to the formatted date string

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| `[format]` | string | yes | Format string. |

Guide: [How to use [date.format]](/plugins/magic.lambda.dates/#how-to-use-dateformat)

### JSON declaration

This is the complete declaration of `date.format`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "date.format",
  "description": "Formats a DateTime using a .NET format string (e.g. yyyy-MM-dd HH:mm) for display or logging",
  "signature": {
    "input": {
      "kind": "date",
      "description": "Date value to format",
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
      "kind": "formatted-date,text",
      "description": "Resolves to the formatted date string"
    }
  }
}
```

</details>

---

[all `date.*` slots](/reference/slots/date/) | [`date.from-unix` &rarr;](/reference/slots/date/date.from-unix/)


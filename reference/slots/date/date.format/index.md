---
title: "[date.format]"
description: "date.format is a slot in the date namespace of Magic Cloud. Formats a DateTime using a .NET format string (e.g. yyyy-MM-dd HH:mm) for display or logging."
generated: true
llms: "guide"
slot_json: "/reference/slots/date/date.format/slot.json"
---

`date.format` is a slot in the `date` namespace, in Hyperlambda, the language of Magic Cloud. Formats a DateTime using a .NET format string (e.g. yyyy-MM-dd HH:mm) for display or logging.

* **Value** (`date`), required: Date value to format
* **Returns**: Resolves to the formatted date string

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[format]` | string | yes | Format string. |

### Guide

<!-- guide -->
This slot formats a date and time object as a string. Patterns are the same as patterns for C#. Below is
example usage.

```
date.format:date:"2023-01-19T12:49:44.000Z"
   format:dd. MMMM yyyy
```
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.dates](/plugins/magic.lambda.dates/) plugin, which documents every slot it contains.

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


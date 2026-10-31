---
title: "[date.from-unix]"
description: "date.from-unix is a slot in the date namespace of Magic Cloud. Converts a Unix timestamp into a DateTime value."
generated: true
llms: "guide"
slot_json: "/reference/slots/date/date.from-unix/slot.json"
---

`date.from-unix` is a slot in the `date` namespace, in Hyperlambda, the language of Magic Cloud. Converts a Unix timestamp into a DateTime value.

* **Value** (`unix-timestamp,integer,number`), required: Unix timestamp to convert
* **Returns**: Resolves to the date represented by the supplied Unix timestamp

### Guide

<!-- guide -->
This slot takes a Unix date and time stamp, and returns a typed date object as its result. Below is an example.

```
date.from-unix:1674132584
```
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.dates](/plugins/magic.lambda.dates/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `date.from-unix`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "date.from-unix",
  "description": "Converts a Unix timestamp into a DateTime value",
  "signature": {
    "input": {
      "kind": "unix-timestamp,integer,number",
      "description": "Unix timestamp to convert",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "output": {
      "mode": "Value",
      "kind": "date",
      "description": "Resolves to the date represented by the supplied Unix timestamp"
    }
  }
}
```

</details>

---

[&larr; `date.format`](/reference/slots/date/date.format/) | [all `date.*` slots](/reference/slots/date/) | [`date.max` &rarr;](/reference/slots/date/date.max/)


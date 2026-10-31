---
title: "[time]"
description: "time is a core slot of Magic Cloud. Constructs a TimeSpan value from child nodes."
generated: true
llms: false
slot_json: "/reference/slots/core/time/slot.json"
---

`time` is a core slot, one of the keywords of the Hyperlambda language, in Hyperlambda, the language of Magic Cloud. Constructs a TimeSpan value from child nodes.

* **Returns**: Resolves to the constructed TimeSpan value

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[days]` | int | no | Number of days. Default: `0`. |
| `[hours]` | int | no | Number of hours. Default: `0`. |
| `[minutes]` | int | no | Number of minutes. Default: `0`. |
| `[seconds]` | int | no | Number of seconds. Default: `0`. |
| `[milliseconds]` | int | no | Number of milliseconds. Default: `0`. |

Guide: [How to use [time]](/plugins/magic.lambda.dates/#how-to-use-time)

### JSON declaration

This is the complete declaration of `time`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "time",
  "description": "Constructs a TimeSpan value from child nodes",
  "signature": {
    "children": {
      "days": {
        "type": "int",
        "description": "Number of days",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "0",
        "role": "Option",
        "projection": "Value"
      },
      "hours": {
        "type": "int",
        "description": "Number of hours",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "0",
        "role": "Option",
        "projection": "Value"
      },
      "minutes": {
        "type": "int",
        "description": "Number of minutes",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "0",
        "role": "Option",
        "projection": "Value"
      },
      "seconds": {
        "type": "int",
        "description": "Number of seconds",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "0",
        "role": "Option",
        "projection": "Value"
      },
      "milliseconds": {
        "type": "int",
        "description": "Number of milliseconds",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "default": "0",
        "role": "Option",
        "projection": "Value"
      }
    },
    "output": {
      "mode": "Value",
      "kind": "timespan",
      "description": "Resolves to the constructed TimeSpan value"
    }
  }
}
```

</details>

---

[&larr; `throw`](/reference/slots/core/throw/) | [all core slots](/reference/slots/core/) | [`try` &rarr;](/reference/slots/core/try/)


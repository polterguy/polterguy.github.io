---
title: "[validators.url]"
description: "validators.url is a slot in the validators namespace of Magic Cloud. Validates that a value or resolved expression result is a URL, throwing if validation fails."
generated: true
llms: false
slot_json: "/reference/slots/validators/validators.url/slot.json"
---

`validators.url` is a slot in the `validators` namespace, in Hyperlambda, the language of Magic Cloud. Validates that a value or resolved expression result is a URL, throwing if validation fails.

* **Value** (`url`), required: URL value or expression selecting the node or nodes to validate

Guide: [How to use [validators.url]](/plugins/magic.lambda.validators/#how-to-use-validatorsurl)

### JSON declaration

This is the complete declaration of `validators.url`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "validators.url",
  "description": "Validates that a value or resolved expression result is a URL, throwing if validation fails",
  "signature": {
    "input": {
      "kind": "url",
      "description": "URL value or expression selecting the node or nodes to validate",
      "required": true,
      "mode": "ValueOrExpression"
    }
  }
}
```

</details>

---

[&larr; `validators.string`](/reference/slots/validators/validators.string/) | [all `validators.*` slots](/reference/slots/validators/)


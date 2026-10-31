---
title: "[strings.builder.append]"
description: "strings.builder.append is a slot in the strings namespace of Magic Cloud. Appends text to the current [strings.builder] scope."
generated: true
llms: "guide"
slot_json: "/reference/slots/strings/strings.builder.append/slot.json"
---

`strings.builder.append` is a slot in the `strings` namespace, in Hyperlambda, the language of Magic Cloud. Appends text to the current [strings.builder] scope.

* **Value** (`text`), required: Text to append to the current [strings.builder] scope
* **Scope**: requires `strings.builder` - Requires an active string builder scope created by [strings.builder]

### Guide

<!-- guide -->
Appends its value to the closest **[\[strings.builder\]](/reference/slots/strings/strings.builder/)** scope. The slot requires a value, which can be a constant
or an expression, and can only be used inside a **[\[strings.builder\]](/reference/slots/strings/strings.builder/)** invocation. See the example in the
documentation for **[\[strings.builder\]](/reference/slots/strings/strings.builder/)** above.
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.strings](/plugins/magic.lambda.strings/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `strings.builder.append`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "strings.builder.append",
  "description": "Appends text to the current [strings.builder] scope",
  "signature": {
    "input": {
      "kind": "text",
      "description": "Text to append to the current [strings.builder] scope",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "scope": {
      "requires": "strings.builder",
      "description": "Requires an active string builder scope created by [strings.builder]"
    }
  }
}
```

</details>

---

[&larr; `strings.builder`](/reference/slots/strings/strings.builder/) | [all `strings.*` slots](/reference/slots/strings/) | [`strings.byte-count` &rarr;](/reference/slots/strings/strings.byte-count/)


---
title: "[puppeteer.evaluate]"
description: "puppeteer.evaluate is a slot in the puppeteer namespace of Magic Cloud. Evaluates JavaScript in the page context."
generated: true
llms: "guide"
slot_json: "/reference/slots/puppeteer/puppeteer.evaluate/slot.json"
---

`puppeteer.evaluate` is a slot in the `puppeteer` namespace, in Hyperlambda, the language of Magic Cloud. Evaluates JavaScript in the page context.

* **Value** (`puppeteer-session`), required: Puppeteer session ID
* **Returns**: Resolves to the result of the evaluated JavaScript expression
* **Scope**: requires `puppeteer-session`

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[expression]` | string | yes | JavaScript expression or function. |
| `[args]` | string\|lambda | no | Arguments passed to the JavaScript function. |
| `[args]` / _unnamed child node_ | string | no | Argument value. Can be repeated. |

### Guide

<!-- guide -->
Evaluates a JavaScript expression in the page.

Arguments:

* Slot value - Session identifier.
* `expression` - JavaScript expression string.
* `args` - Optional arguments for JS function invocation. Each child value is one argument.

Examples:

```
puppeteer.evaluate:SESSION_ID
   expression:"document.title"
```

```
puppeteer.evaluate:SESSION_ID
   expression:"typeof window.mcaptcha"
```
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.puppeteer](/plugins/magic.lambda.puppeteer/) plugin, which documents every slot it contains.

### JSON declaration

This is the complete declaration of `puppeteer.evaluate`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "puppeteer.evaluate",
  "description": "Evaluates JavaScript in the page context",
  "signature": {
    "input": {
      "kind": "puppeteer-session",
      "description": "Puppeteer session ID",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "expression": {
        "type": "string",
        "kind": "javascript",
        "description": "JavaScript expression or function",
        "required": true,
        "mode": "ValueOrExpression",
        "cardinality": "ExactlyOne",
        "role": "Option",
        "projection": "Value"
      },
      "args": {
        "type": "string|lambda",
        "description": "Arguments passed to the JavaScript function",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Arguments",
        "projection": "ArgumentBag",
        "children": [
          {
            "type": "string",
            "kind": "javascript-argument",
            "description": "Argument value",
            "required": false,
            "mode": "ValueOrExpression",
            "cardinality": "ZeroOrMore",
            "role": "Option",
            "projection": "Value"
          }
        ]
      }
    },
    "scope": {
      "requires": "puppeteer-session"
    },
    "output": {
      "mode": "Value",
      "kind": "javascript-result",
      "description": "Resolves to the result of the evaluated JavaScript expression"
    }
  }
}
```

</details>

---

[&larr; `puppeteer.content`](/reference/slots/puppeteer/puppeteer.content/) | [all `puppeteer.*` slots](/reference/slots/puppeteer/) | [`puppeteer.fill` &rarr;](/reference/slots/puppeteer/puppeteer.fill/)


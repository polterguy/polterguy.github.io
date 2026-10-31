---
title: "[openai.tokenize]"
description: "openai.tokenize is a slot in the openai namespace of Magic Cloud. Counts how many OpenAI tokens the given text consumes; useful for estimating cost or staying under context limits. Pass [model] to count with that model's exact encoding - defaults to o200k_base, the GPT-4o/GPT-5 family encoding."
generated: true
llms: false
slot_json: "/reference/slots/openai/openai.tokenize/slot.json"
---

`openai.tokenize` is a slot in the `openai` namespace, in Hyperlambda, the language of Magic Cloud. Counts how many OpenAI tokens the given text consumes; useful for estimating cost or staying under context limits. Pass [model] to count with that model's exact encoding - defaults to o200k_base, the GPT-4o/GPT-5 family encoding.

* **Value** (`text`), required: Text to tokenize
* **Returns**: Resolves to the number of tokens in the supplied text

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| `[model]` | string | no | OpenAI model whose encoding to count with - defaults to o200k_base when omitted or unknown. |

### JSON declaration

This is the complete declaration of `openai.tokenize`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "openai.tokenize",
  "description": "Counts how many OpenAI tokens the given text consumes; useful for estimating cost or staying under context limits. Pass [model] to count with that model's exact encoding - defaults to o200k_base, the GPT-4o/GPT-5 family encoding",
  "signature": {
    "input": {
      "kind": "text",
      "description": "Text to tokenize",
      "required": true,
      "mode": "ValueOrExpression"
    },
    "children": {
      "model": {
        "type": "string",
        "kind": "model-name",
        "description": "OpenAI model whose encoding to count with - defaults to o200k_base when omitted or unknown",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      }
    },
    "output": {
      "mode": "Value",
      "kind": "integer,number",
      "description": "Resolves to the number of tokens in the supplied text"
    }
  }
}
```

</details>

---

[all `openai.*` slots](/reference/slots/openai/) | [`openai.whisper` &rarr;](/reference/slots/openai/openai.whisper/)


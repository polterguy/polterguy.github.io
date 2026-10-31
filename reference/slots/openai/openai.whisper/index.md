---
title: "[openai.whisper]"
description: "openai.whisper is a slot in the openai namespace of Magic Cloud. Transcribes audio content using OpenAI Whisper."
generated: true
llms: false
slot_json: "/reference/slots/openai/openai.whisper/slot.json"
---

`openai.whisper` is a slot in the `openai` namespace, in Hyperlambda, the language of Magic Cloud. Transcribes audio content using OpenAI Whisper.

* **Returns**: Resolves to the transcribed text

### Arguments

| Argument | Type | Required | Description |
|---|---|---|---|
| `[content]` | byte[] | yes | Audio content bytes. |
| `[key]` | string | yes | OpenAI API key. |
| `[language]` | string | no | Optional language hint. |
| `[type]` | string | yes | Audio MIME type. |

Guide: [How to use [openai.whisper]](/plugins/magic.lambda.openai/#how-to-use-openaiwhisper)

### JSON declaration

This is the complete declaration of `openai.whisper`, as the running system describes it. It is also published as [slot.json](slot.json).

<details markdown="1" class="slot-declaration">
<summary>JSON declaration</summary>

```json
{
  "name": "openai.whisper",
  "description": "Transcribes audio content using OpenAI Whisper",
  "signature": {
    "children": {
      "key": {
        "type": "string",
        "kind": "openai-api-key",
        "description": "OpenAI API key",
        "required": true,
        "mode": "ValueOrExpression",
        "cardinality": "ExactlyOne",
        "role": "Option",
        "projection": "Value"
      },
      "content": {
        "type": "byte[]",
        "kind": "binary-content",
        "description": "Audio content bytes",
        "required": true,
        "mode": "ValueOrExpression",
        "cardinality": "ExactlyOne",
        "role": "Option",
        "projection": "Value"
      },
      "type": {
        "type": "string",
        "kind": "content-type",
        "description": "Audio MIME type",
        "required": true,
        "mode": "ValueOrExpression",
        "cardinality": "ExactlyOne",
        "role": "Option",
        "projection": "Value"
      },
      "language": {
        "type": "string",
        "kind": "language-code",
        "description": "Optional language hint",
        "required": false,
        "mode": "ValueOrExpression",
        "cardinality": "ZeroOrOne",
        "role": "Option",
        "projection": "Value"
      }
    },
    "output": {
      "mode": "Value",
      "kind": "text",
      "description": "Resolves to the transcribed text"
    }
  }
}
```

</details>

---

[&larr; `openai.tokenize`](/reference/slots/openai/openai.tokenize/) | [all `openai.*` slots](/reference/slots/openai/)


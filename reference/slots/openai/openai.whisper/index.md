---
title: "[openai.whisper]"
description: "openai.whisper is a slot in the openai namespace of Magic Cloud. Transcribes audio content using OpenAI Whisper."
generated: true
llms: "guide"
slot_json: "/reference/slots/openai/openai.whisper/slot.json"
---

`openai.whisper` is a slot in the `openai` namespace, in Hyperlambda, the language of Magic Cloud. Transcribes audio content using OpenAI Whisper.

* **Returns**: Resolves to the transcribed text

### Arguments

Required arguments come first, then the optional ones in the order they are declared.

| Argument | Type | Required | Description |
|---|---|---|---|
| `[key]` | string | yes | OpenAI API key. |
| `[content]` | byte[] | yes | Audio content bytes. |
| `[type]` | string | yes | Audio MIME type. |
| `[language]` | string | no | Optional language hint. |

### Guide

<!-- guide -->
This slot transcribes audio by sending it to OpenAI's audio transcription endpoint, using the `whisper-1` model,
and returns the transcribed text as its value. It takes the following arguments as children, and throws an
exception if any of the three mandatory ones is missing, or if OpenAI responds with an error.

* __[key]__ - OpenAI API key. Mandatory.
* __[content]__ - The audio as raw bytes. Mandatory.
* __[type]__ - MIME type of the audio, such as `audio/mpeg`. Mandatory.
* __[language]__ - Optional language hint.
<!-- /guide -->

### Related documentation

* Part of the [magic.lambda.openai](/plugins/magic.lambda.openai/) plugin, which documents every slot it contains.

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


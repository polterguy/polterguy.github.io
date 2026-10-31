---
title: openai.* slots
description: The 2 slots named openai.* in Magic Cloud and Hyperlambda, with their arguments and return values, generated from the running system.
generated: true
---

_Generated from the running system, see [how this reference is built](/reference/slots/). Do not edit this page._

## [openai.tokenize]

Counts how many OpenAI tokens the given text consumes; useful for estimating cost or staying under context limits. Pass [model] to count with that model's exact encoding - defaults to o200k_base, the GPT-4o/GPT-5 family encoding.

* **Value** (`text`), required: Text to tokenize
* **Returns**: Resolves to the number of tokens in the supplied text

| Argument | Type | Required | Description |
|---|---|---|---|
| `[model]` | string | no | OpenAI model whose encoding to count with - defaults to o200k_base when omitted or unknown. |

## [openai.whisper]

Transcribes audio content using OpenAI Whisper.

* **Returns**: Resolves to the transcribed text

| Argument | Type | Required | Description |
|---|---|---|---|
| `[key]` | string | yes | OpenAI API key. |
| `[content]` | byte[] | yes | Audio content bytes. |
| `[type]` | string | yes | Audio MIME type. |
| `[language]` | string | no | Optional language hint. |

Guide: [How to use [openai.whisper]](/plugins/magic.lambda.openai/#how-to-use-openaiwhisper)


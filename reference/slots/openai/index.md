---
title: "openai.* slots"
description: "The 2 slots named openai.* in Magic Cloud and Hyperlambda, each with its own page."
generated: true
---

2 slots, each with its own page and JSON declaration. See [how this reference is built](/reference/slots/).

| Slot | Description |
|---|---|
| [`openai.tokenize`](/reference/slots/openai/openai.tokenize/) | Counts how many OpenAI tokens the given text consumes; useful for estimating cost or staying under context limits. Pass [model] to count with that model's exact encoding - defaults to o200k_base, the GPT-4o/GPT-5 family encoding. |
| [`openai.whisper`](/reference/slots/openai/openai.whisper/) | Transcribes audio content using OpenAI Whisper. |


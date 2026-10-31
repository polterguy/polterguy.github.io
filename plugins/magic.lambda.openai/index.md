---
title: magic.lambda.openai
moved_anchors: {"how-to-use-openaiwhisper": "/plugins/magic.lambda.openai/openai.whisper/"}
---

This project provides OpenAI related slots for Magic. More specifically, it provides the following slots.

* __[\[openai.tokenize\]](/reference/slots/openai/openai.tokenize/)__ - Returns how many tokens the specified text will consume from OpenAI
* __[\[openai.whisper\]](/reference/slots/openai/openai.whisper/)__ - Transcribes audio content using OpenAI Whisper

The above slot will calculate how many tokens the specified input requires from the OpenAI endpoints.

```
openai.tokenize:This is some query
```


## Credits

Thx to Devis Lucato for publishing the original work under CC0 [here](https://github.com/dluc/openai-tools).

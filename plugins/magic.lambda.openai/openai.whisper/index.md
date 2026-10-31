---
title: "How to use [openai.whisper]"
description: "How to use [openai.whisper] - This slot transcribes audio by sending it to OpenAI's audio transcription endpoint, using the whisper-1 model, and returns the transcribed text as its value."
generated: true
guide: true
---

The reference page of [`openai.whisper`](/reference/slots/openai/openai.whisper/) has its arguments, constraints and declaration.

This slot transcribes audio by sending it to OpenAI's audio transcription endpoint, using the `whisper-1` model,
and returns the transcribed text as its value. It takes the following arguments as children, and throws an
exception if any of the three mandatory ones is missing, or if OpenAI responds with an error.

* __[key]__ - OpenAI API key. Mandatory.
* __[content]__ - The audio as raw bytes. Mandatory.
* __[type]__ - MIME type of the audio, such as `audio/mpeg`. Mandatory.
* __[language]__ - Optional language hint.

This slot transcribes audio to text using OpenAI Whisper, and sets its value to the transcription. It needs your OpenAI **[key]**, the audio as **[content]**, and its MIME **[type]**, and takes an optional **[language]** hint. Below is an example.

```
.key:YOUR_OPENAI_API_KEY
io.file.load.binary:/misc/speech.mp3
openai.whisper
   key:x:@.key
   content:x:@io.file.load.binary
   type:audio/mpeg
```

---
title: "How to use [strings.url-decode]"
description: "How to use [strings.url-decode] - URL decodes a string, the opposite of [strings.url-encode]."
generated: true
guide: true
---

This is the guide to [`strings.url-decode`](/reference/slots/strings/strings.url-decode/), whose reference page has its arguments, constraints and declaration.

URL decodes a string, the opposite of **[strings.url-encode]**. Example can be found below.

```
strings.url-encode:thomas@ainiro.io
strings.url-decode:x:-
```

Resulting in the following after execution.

```
strings.url-encode:thomas%40ainiro.io
strings.url-decode:thomas@ainiro.io
```

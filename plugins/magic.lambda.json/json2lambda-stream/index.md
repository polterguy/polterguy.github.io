---
title: "How to use [json2lambda-stream]"
description: "How to use [json2lambda-stream] - This slot does the same as [json2lambda], except it reads the JSON from a stream instead of from a string, such as a stream opened with [io.stream.open-file], which you can read about..."
generated: true
guide: true
---

The reference page of [`json2lambda-stream`](/reference/slots/core/json2lambda-stream/) has its arguments, constraints and declaration.

This slot does the same as **[json2lambda]**, except it reads the JSON from a stream instead of from a string,
such as a stream opened with **[io.stream.open-file]**, which you can read about in the _"magic.lambda.io"_ project.
The value of the slot must be an expression leading to the stream, and the slot throws an exception if
no stream is found. The resulting lambda hierarchy is returned as children of the slot node, and both JSON objects
and JSON arrays are supported.

The slot accepts the following argument.

* __[encoding]__ - Text encoding used to read the stream, defaults to `utf-8`. Streams using another encoding, such as `utf-16` or `iso-8859-1`, are converted to UTF-8 before they are parsed

This slot creates a lambda object from JSON read from a stream, without first loading it into memory as a string. You can pass in an optional **[encoding]**, which defaults to UTF-8. Below is an example, opening a file as a stream.

```
io.stream.open-file:/misc/data.json
json2lambda-stream:x:@io.stream.open-file
io.stream.close:x:@io.stream.open-file
```

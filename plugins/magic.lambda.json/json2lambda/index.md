---
title: "How to use [json2lambda]"
description: "How to use [json2lambda] - .json:@\"{\"\"property\"\": \"\"value\"\"}\" json2lambda:x:- lambda2json:x:-/ The [lambda2json] slot can optionally take a [format] argument, with a boolean \"true\" value, which implies the resulting J..."
generated: true
guide: true
---

This is the guide to [`json2lambda`](/reference/slots/core/json2lambda/), whose reference page has its arguments, constraints and declaration.

```
.json:@"{""property"": ""value""}"
json2lambda:x:-
lambda2json:x:-/*
```

The **[lambda2json]** slot can optionally take a **[format]** argument, with a boolean _"true"_ value, which implies the
resulting JSON will be indented and nicely formated, making it more readable.

**Notice** - Although all JSON can be transformed into lambda, the opposite is not necessarily true. This is because
lambda allows for having multiple nodes with the same name for instance, which would result in a JSON object with
multiple properties having the same key. Hence, have this in mind as you persist your lambda objects into JSON.

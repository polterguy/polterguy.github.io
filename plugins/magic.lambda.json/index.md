---
title: magic.lambda.json
moved_anchors: {"how-to-use-json2lambda-and-lambda2json": "/plugins/magic.lambda.json/json2lambda/", "how-to-use-json2lambda-stream": "/plugins/magic.lambda.json/json2lambda-stream/", "how-to-use-yaml2json-and-json2yaml": "/plugins/magic.lambda.json/yaml2json/", "how-to-use-yaml2lambda-and-lambda2yaml": "/plugins/magic.lambda.json/yaml2lambda/"}
---

This project provides JSON helper slots for Magic. More specifically, it provides the following slots.

* __[\[json2lambda\]](/reference/slots/core/json2lambda/)__ - Creates a lambda object out of a JSON input string.
* __[\[json2lambda-stream\]](/reference/slots/core/json2lambda-stream/)__ - Creates a lambda object out of JSON read from a stream.
* __[\[json2yaml\]](/reference/slots/core/json2yaml/)__ - Converts a JSON string to its YAML equivalent.
* __[\[yaml2lambda\]](/reference/slots/core/yaml2lambda/)__ - Creates a lambda object out of a YAML input string.
* __[\[yaml2json\]](/reference/slots/core/yaml2json/)__ - Creates a JSON string out of a YAML input string.
* __[\[lambda2json\]](/reference/slots/core/lambda2json/)__ - Creates JSON out of a lambda object.
* __[\[lambda2yaml\]](/reference/slots/core/lambda2yaml/)__ - Converts a lambda object to its YAML equivalent.
* __[.lambda2json-raw]__ - Transforms a lambda object to a compact JSON string, used internally by the endpoint executor and the exception handler. (private C# slot)

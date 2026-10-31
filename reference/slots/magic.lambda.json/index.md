---
title: magic.lambda.json slot reference
description: Every slot in magic.lambda.json with its value, arguments and return value, generated from the source code.
generated: true
---

_This page is generated from the `[Slot]` attributes in the source code of [magic.lambda.json](https://github.com/polterguy/magic/tree/master/plugins/magic.lambda.json). Do not edit it; improve the attribute instead. The hand-written guide is at [magic.lambda.json](/plugins/magic.lambda.json/)._

## [.lambda2json-raw]

Transforms a lambda hierarchy into a JSON string, used internally.

* **Returns**: Resolves to the generated JSON string

## [json2lambda]

Transforms JSON into a lambda hierarchy.

* **Value** (`json`), required: JSON text to transform
* **Returns**: Resolves to the parsed lambda hierarchy as child nodes

Guide: [How to use [json2lambda]](/plugins/magic.lambda.json/#how-to-use-json2lambda-and-lambda2json)

## [json2lambda-stream]

Transforms JSON stream content into a lambda hierarchy.

* **Value** (`stream`), required: JSON stream to transform
* **Returns**: Resolves to the parsed lambda hierarchy as child nodes

| Argument | Type | Required | Description |
|---|---|---|---|
| `[encoding]` | string | no | Text encoding used to read the JSON stream |

Guide: [How to use [json2lambda-stream]](/plugins/magic.lambda.json/#how-to-use-json2lambda-stream)

## [json2yaml]

Transforms JSON into YAML.

* **Value** (`json`), required: JSON text to transform
* **Returns**: Resolves to the generated YAML string

Guide: [How to use [json2yaml]](/plugins/magic.lambda.json/#how-to-use-yaml2json-and-json2yaml)

## [lambda2json]

Transforms a lambda hierarchy into JSON.

* **Value** (`node-list,lambda-tree`), required: Expression selecting the lambda hierarchy to transform
* **Returns**: Resolves to the generated JSON string

| Argument | Type | Required | Description |
|---|---|---|---|
| `[format]` | bool | no | Whether to pretty-print the JSON output |

Guide: [How to use [lambda2json]](/plugins/magic.lambda.json/#how-to-use-json2lambda-and-lambda2json)

## [lambda2yaml]

Transforms a lambda hierarchy into YAML.

* **Value** (`node-list,lambda-tree`), required: Expression selecting the nodes (rows) to transform
* **Returns**: Resolves to the generated YAML string

Guide: [How to use [lambda2yaml]](/plugins/magic.lambda.json/#how-to-use-yaml2lambda-and-lambda2yaml)

## [yaml2json]

Transforms YAML into JSON.

* **Value** (`yaml`), required: YAML text to transform
* **Returns**: Resolves to the generated JSON string

Guide: [How to use [yaml2json]](/plugins/magic.lambda.json/#how-to-use-yaml2json-and-json2yaml)

## [yaml2lambda]

Transforms YAML into a lambda hierarchy.

* **Value** (`yaml`), required: YAML text to transform
* **Returns**: Resolves to the parsed lambda hierarchy as child nodes

Guide: [How to use [yaml2lambda]](/plugins/magic.lambda.json/#how-to-use-yaml2lambda-and-lambda2yaml)


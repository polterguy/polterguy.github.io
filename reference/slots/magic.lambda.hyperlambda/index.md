---
title: magic.lambda.hyperlambda slot reference
description: Every slot in magic.lambda.hyperlambda with its value, arguments and return value, generated from the source code.
generated: true
---

_This page is generated from the `[Slot]` attributes in the source code of [magic.lambda.hyperlambda](https://github.com/polterguy/magic/tree/master/plugins/magic.lambda.hyperlambda). Do not edit it; improve the attribute instead. The hand-written guide is at [magic.lambda.hyperlambda](/plugins/magic.lambda.hyperlambda/)._

## [hyper2lambda]

Transforms Hyperlambda into a lambda hierarchy.

* **Value** (`hyperlambda`), required: Hyperlambda text to transform
* **Returns**: Resolves to the parsed lambda hierarchy as child nodes

| Argument | Type | Required | Description |
|---|---|---|---|
| `[comments]` | bool | no | Whether parser comment nodes should be preserved as [..] nodes with the comment text as value |

Guide: [How to use [hyper2lambda]](/plugins/magic.lambda.hyperlambda/#how-to-use-hyper2lambda)

## [hyperlambda.verify-slots]

Verifies that all slots referenced in executable statement position of the specified Hyperlambda exist.

* **Value** (`hyperlambda`), optional: Hyperlambda text to verify; alternatively supply an already parsed lambda as children
* **Returns**: Resolves to true when every invocation is statically valid; otherwise lists missing slot names and invalid-invocation diagnostics as child nodes

Guide: [How to use [hyperlambda.verify-slots]](/plugins/magic.lambda.hyperlambda/#how-to-use-hyperlambdaverify-slots)

## [lambda2hyper]

Transforms a lambda hierarchy into Hyperlambda.

* **Value** (`lambda-tree,node-list`), required: Expression selecting the lambda hierarchy to transform
* **Returns**: Resolves to the generated Hyperlambda source

| Argument | Type | Required | Description |
|---|---|---|---|
| `[comments]` | bool | no | Whether generated Hyperlambda should include comments |

Guide: [How to use [lambda2hyper]](/plugins/magic.lambda.hyperlambda/#how-to-use-lambda2hyper)


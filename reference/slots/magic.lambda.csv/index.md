---
title: magic.lambda.csv slot reference
description: Every slot in magic.lambda.csv with its value, arguments and return value, generated from the source code.
generated: true
---

_This page is generated from the `[Slot]` attributes in the source code of [magic.lambda.csv](https://github.com/polterguy/magic/tree/master/plugins/magic.lambda.csv). Do not edit it; improve the attribute instead. The hand-written guide is at [magic.lambda.csv](/plugins/magic.lambda.csv/)._

## [csv2lambda]

Transforms CSV into a lambda hierarchy.

* **Value** (`csv`), required: CSV text to transform
* **Returns**: Resolves to the parsed lambda hierarchy as child nodes; each child is one CSV row containing column-named values

| Argument | Type | Required | Description |
|---|---|---|---|
| `[types]` | lambda | yes | Column type conversions keyed by column name |

| Returned node | Type | Description |
|---|---|---|
| `[.]` | lambda | One CSV record returned as a child node; column values appear as named children keyed by the header column name |

Guide: [How to use [csv2lambda]](/plugins/magic.lambda.csv/#how-to-use-csv2lambda)

## [lambda2csv]

Transforms a lambda hierarchy into CSV.

* **Value** (`node-list`), required: Expression selecting the nodes (rows) to transform
* **Returns**: Resolves to the CSV content in value and column type nodes as children

| Returned node | Type | Description |
|---|---|---|
| `[null-value]` | string | String used to represent null values |

Guide: [How to use [lambda2csv]](/plugins/magic.lambda.csv/#how-to-use-lambda2csv)


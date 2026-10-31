---
title: validators.* slots
description: The 10 slots named validators.* in Magic Cloud and Hyperlambda, with their arguments and return values, generated from the running system.
generated: true
---

_Generated from the running system, see [how this reference is built](/reference/slots/). Do not edit this page._

## [validators.date]

Validates that a date value or resolved expression result is within the allowed range, throwing if validation fails.

* **Value** (`date`), required: Date value or expression selecting the node or nodes to validate

| Argument | Type | Required | Description |
|---|---|---|---|
| `[min]` | date | no | Earliest accepted date. |
| `[max]` | date | no | Latest accepted date. |

Guide: [How to use [validators.date]](/plugins/magic.lambda.validators/#how-to-use-validatorsdate)

## [validators.default]

Adds default child nodes to the nodes selected by the input expression.

* **Value** (`lambda-object`), required: Expression selecting the node or nodes to apply defaults to

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | object | yes | Default child node cloned into each selected node when missing. Can be repeated. |

Guide: [How to use [validators.default]](/plugins/magic.lambda.validators/#how-to-use-validatorsdefault)

## [validators.email]

Validates that a value or resolved expression result is an email address, throwing if validation fails.

* **Value** (`email`), required: Email value or expression selecting the node or nodes to validate

Guide: [How to use [validators.email]](/plugins/magic.lambda.validators/#how-to-use-validatorsemail)

## [validators.enum]

Validates that a value or resolved expression result is one of the allowed options, throwing if validation fails.

* **Value** (`enum-value`), required: Value or expression selecting the node or nodes to validate

| Argument | Type | Required | Description |
|---|---|---|---|
| _unnamed child node_ | string | yes | Accepted enum value. Can be repeated. |

Guide: [How to use [validators.enum]](/plugins/magic.lambda.validators/#how-to-use-validatorsenum)

## [validators.integer]

Validates that an integer value or resolved expression result is within the allowed range, throwing if validation fails.

* **Value** (`integer,number`), required: Integer value or expression selecting the node or nodes to validate

| Argument | Type | Required | Description |
|---|---|---|---|
| `[min]` | long | no | Minimum accepted value. |
| `[max]` | long | no | Maximum accepted value. |

Guide: [How to use [validators.integer]](/plugins/magic.lambda.validators/#how-to-use-validatorsinteger)

## [validators.mandatory]

Validates that the input value or resolved expression result is present, throwing if validation fails.

* **Value** (`validated-value`), required: Literal value or expression to validate as mandatory

Guide: [How to use [validators.mandatory]](/plugins/magic.lambda.validators/#how-to-use-validatorsmandatory)

## [validators.recaptcha]

Validates a reCAPTCHA response token, throwing if validation fails.

* **Value** (`recaptcha-token`), required: reCAPTCHA response token to validate

| Argument | Type | Required | Description |
|---|---|---|---|
| `[site-key]` | string | yes | reCAPTCHA site key. |
| `[secret]` | string | yes | reCAPTCHA secret key. |
| `[min]` | decimal | yes | Minimum acceptable reCAPTCHA score. |

Guide: [How to use [validators.recaptcha]](/plugins/magic.lambda.validators/#how-to-use-validatorsrecaptcha)

## [validators.regex]

Validates that a value or resolved expression result matches a regular expression, bounded by the execution deadline when set, throwing if validation fails.

* **Value** (`text`), required: Value or expression selecting the node or nodes to validate

| Argument | Type | Required | Description |
|---|---|---|---|
| `[regex]` | string | yes | Regular expression pattern the value must match. |

Guide: [How to use [validators.regex]](/plugins/magic.lambda.validators/#how-to-use-validatorsregex)

## [validators.string]

Validates that a string value or resolved expression result is within the allowed length range, throwing if validation fails.

* **Value** (`text`), required: String value or expression selecting the node or nodes to validate

| Argument | Type | Required | Description |
|---|---|---|---|
| `[min]` | int | no | Minimum accepted length. Default: `0`. |
| `[max]` | int | no | Maximum accepted length. Default: `int.MaxValue`. |

Guide: [How to use [validators.string]](/plugins/magic.lambda.validators/#how-to-use-validatorsstring)

## [validators.url]

Validates that a value or resolved expression result is a URL, throwing if validation fails.

* **Value** (`url`), required: URL value or expression selecting the node or nodes to validate

Guide: [How to use [validators.url]](/plugins/magic.lambda.validators/#how-to-use-validatorsurl)


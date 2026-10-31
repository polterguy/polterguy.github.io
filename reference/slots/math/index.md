---
title: math.* slots
description: The 18 slots named math.* in Magic Cloud and Hyperlambda, with their arguments and return values, generated from the running system.
generated: true
---

_Generated from the running system, see [how this reference is built](/reference/slots/). Do not edit this page._

## [math.abs]

Returns the absolute value.

* **Value** (`number`), required: Numeric value to transform
* **Returns**: Resolves to the absolute value

Guide: [How to use [math.abs]](/plugins/magic.lambda.math/#how-to-use-mathabs)

## [math.add]

Adds numeric values.

* **Returns**: Resolves to the sum of the supplied operands

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | number | yes | Numeric operand evaluated before calculating the result. |

Guide: [How to use [math.add]](/plugins/magic.lambda.math/#how-to-use-mathadd)

## [math.ceil]

Rounds a number up.

* **Value** (`number`), required: Numeric value to round
* **Returns**: Resolves to the rounded-up value

Guide: [How to use [math.ceil]](/plugins/magic.lambda.math/#how-to-use-mathceil)

## [math.cos]

Calculates the cosine of the specified value.

* **Value** (`number`), required: Numeric value to transform
* **Returns**: Resolves to the cosine of the supplied angle

Guide: [How to use [math.cos]](/plugins/magic.lambda.math/#how-to-use-mathcos)

## [math.decrement]

Decrements the numeric nodes selected by the input expression.

* **Value** (`numeric-node`), required: Expression selecting the numeric node or nodes to decrement

| Argument | Type | Required | Description |
|---|---|---|---|
| `[step]` | number | no | Amount to add to or subtract from each selected node. Default: `1`. |

Guide: [How to use [math.decrement]](/plugins/magic.lambda.math/#how-to-use-mathdecrement)

## [math.divide]

Divides numeric values.

* **Returns**: Resolves to the quotient of the supplied operands

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | number | yes | Numeric operand evaluated before calculating the result. |

Guide: [How to use [math.divide]](/plugins/magic.lambda.math/#how-to-use-mathdivide)

## [math.dot]

Calculates the dot product of two vectors from child nodes.

* **Returns**: Resolves to the dot product of the two supplied vectors

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | lambda | yes | Vector operand evaluated before calculating the dot product. |

Guide: [How to use [math.dot]](/plugins/magic.lambda.math/#how-to-use-mathdot)

## [math.floor]

Rounds a number down.

* **Value** (`number`), required: Numeric value to round
* **Returns**: Resolves to the rounded-down value

Guide: [How to use [math.floor]](/plugins/magic.lambda.math/#how-to-use-mathfloor)

## [math.increment]

Increments the numeric nodes selected by the input expression.

* **Value** (`numeric-node`), required: Expression selecting the numeric node or nodes to increment

| Argument | Type | Required | Description |
|---|---|---|---|
| `[step]` | number | no | Amount to add to or subtract from each selected node. Default: `1`. |

Guide: [How to use [math.increment]](/plugins/magic.lambda.math/#how-to-use-mathincrement)

## [math.max]

Returns the largest value from the supplied inputs.

* **Returns**: Resolves to the largest supplied value

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | number | yes | Numeric operand evaluated before calculating the result. |

Guide: [How to use [math.max]](/plugins/magic.lambda.math/#how-to-use-mathmax)

## [math.min]

Returns the smallest value from the supplied inputs.

* **Returns**: Resolves to the smallest supplied value

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | number | yes | Numeric operand evaluated before calculating the result. |

Guide: [How to use [math.min]](/plugins/magic.lambda.math/#how-to-use-mathmin)

## [math.modulo]

Calculates the remainder of a division.

* **Returns**: Resolves to the remainder of the modulo operation

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | number | yes | Numeric operand evaluated before calculating the result. |

Guide: [How to use [math.modulo]](/plugins/magic.lambda.math/#how-to-use-mathmodulo)

## [math.multiply]

Multiplies numeric values.

* **Returns**: Resolves to the product of the supplied operands

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | number | yes | Numeric operand evaluated before calculating the result. |

Guide: [How to use [math.multiply]](/plugins/magic.lambda.math/#how-to-use-mathmultiply)

## [math.random]

Returns a random number from optional child-node bounds.

* **Returns**: Resolves to a random double, or a random integer when bounds are supplied

| Argument | Type | Required | Description |
|---|---|---|---|
| `[min]` | int | no | Inclusive lower bound; requires [max] and must appear before it. |
| `[max]` | int | no | Exclusive upper bound; when supplied without [min], the lower bound is 0. |

* **Constraint** (Requires): [min] requires [max] (`[max]`)

Guide: [How to use [math.random]](/plugins/magic.lambda.math/#how-to-use-mathrandom)

## [math.round]

Rounds a number.

* **Value** (`number`), required: Numeric value to round
* **Returns**: Resolves to the rounded value

Guide: [How to use [math.round]](/plugins/magic.lambda.math/#how-to-use-mathround)

## [math.sin]

Calculates the sine of the specified value.

* **Value** (`number`), required: Numeric value to transform
* **Returns**: Resolves to the sine of the supplied angle

Guide: [How to use [math.sin]](/plugins/magic.lambda.math/#how-to-use-mathsin)

## [math.sqrt]

Calculates the square root of the specified value.

* **Value** (`number`), required: Numeric value to transform
* **Returns**: Resolves to the square root of the supplied value

Guide: [How to use [math.sqrt]](/plugins/magic.lambda.math/#how-to-use-mathsqrt)

## [math.subtract]

Subtracts numeric values.

* **Returns**: Resolves to the difference of the supplied operands

| Argument | Type | Required | Description |
|---|---|---|---|
| _any node name_ | number | yes | Numeric operand evaluated before calculating the result. |

Guide: [How to use [math.subtract]](/plugins/magic.lambda.math/#how-to-use-mathsubtract)


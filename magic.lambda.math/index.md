
# Magic Lambda Math

[![Build status](https://travis-ci.com/polterguy/magic.lambda.math.svg?master)](https://travis-ci.com/polterguy/magic.lambda.math)

This project provides math functions to [Magic](https://github.com/polterguy/magic). More specifically, it provides the following
slots.

* __[math.multiply]__ - Multiplication
* __[math.divide]__ - Division
* __[math.add]__ - Addition
* __[math.subtract]__ - Subtraction
* __[math.modulo]__ - Modulo
* __[math.decrement]__ - Decrements a node's value, optionally by **[step]**, defaulting to 1
* __[math.increment]__ - Increments a node's value, optionally by **[step]**, defaulting to 1

All of the above slots also have async (wait.) overrides.

All of the above can be given any number of arguments, including as its value, and will treat the first argument as the _"base"_,
and performing the rest of the arguments self assigning the base as it proceeds. For instance, the following code will first divide
100 by 4, then divide that result by 5 again, resulting in 5.

```
math.divide:int:100
   :int:4
   :int:5
```

The value of the above __[math.divide]__ node after evaluating the above Hyperlambda will be 5.

All of the above slots will also evaluate the children collection as a lambda, before starting the actual math function,
allowing you to recursively raise signals to retrieve values that are supposed to be mathematically handled somehow.

## Incrementing and decrementing values

The above **[math.increment]** and **[math.decrement]** slots, will instead of yielding a result, inline modify the
value of the node(s) it is pointing to, assuming its value is an expression. In addition these two slots can take an
_optional_ **[step]** argument, allowing you to declare how much the incrementation/decrementation process should add/reduce
the original node's value by.

* [Main documentation](https://polterguy.github.io/)

## Quality gates

- [![Build status](https://travis-ci.com/polterguy/magic.lambda.math.svg?master)](https://travis-ci.com/polterguy/magic.lambda.math)
- [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.math&metric=alert_status)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.math)
- [![Bugs](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.math&metric=bugs)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.math)
- [![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.math&metric=code_smells)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.math)
- [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.math&metric=coverage)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.math)
- [![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.math&metric=duplicated_lines_density)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.math)
- [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.math&metric=ncloc)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.math)
- [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.math&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.math)
- [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.math&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.math)
- [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.math&metric=security_rating)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.math)
- [![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.math&metric=sqale_index)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.math)
- [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=polterguy_magic.lambda.math&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=polterguy_magic.lambda.math)

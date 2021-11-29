
# Magic Lambda Math

This project provides math functions to Magic. More specifically, it provides the following slots.

* __[math.multiply]__ - Multiplication
* __[math.divide]__ - Division
* __[math.add]__ - Addition
* __[math.subtract]__ - Subtraction
* __[math.modulo]__ - Modulo
* __[math.decrement]__ - Decrements a node's value, optionally by **[step]**, defaulting to 1
* __[math.increment]__ - Increments a node's value, optionally by **[step]**, defaulting to 1

All of the above besides the two last slots can be given any number of arguments, including as its value,
and will treat the first argument as the _"base"_, and performing the rest of the arguments self assigning
the base as it proceeds. For instance, the following code will first divide 100 by 4, then divide that result
by 5 again, resulting in 5.

```
math.divide:int:100
   :int:4
   :int:5
```

The value of the above __[math.divide]__ node after evaluating the above Hyperlambda will be 5.

All of the above slots will also evaluate the children collection as a lambda, before starting the actual math function,
allowing you to recursively raise signals to retrieve values that are supposed to be mathematically handled somehow.
This allows you to recursively nest math operations, such as for instance.

```
.one:int:5
.two:int:2
math.multiple
   .:int:3
   math.add
      get-value:x:@.one
      get-value:x:@.two
```

The above of course will first add 5 and 2, then multiple the result of that with 3, resulting in 21.

## Incrementing and decrementing values

The above **[math.increment]** and **[math.decrement]** slots, will instead of yielding a result, inline modify the
value of the node(s) it is pointing to, assuming its value is an expression. In addition these two slots can take an
_optional_ **[step]** argument, allowing you to declare how much the incrementation/decrementation process should add/reduce
the original node's value by. Below is an example that decrements the value found in its expression by 2.

```
.value:int:5
math.decrement:x:-
   step:int:2
```

After executing the above, the result of **[.value]** will be 3.

## Modulo

The modulo slot divides its argument(s) by its base, and returns the remainder.

```
.int:17
math.modulo:x:-
   .:int:10
```

The above results in 7.

## Project website

The source code for this repository can be found at [github.com/polterguy/magic.lambda.math](https://github.com/polterguy/magic.lambda.math), and you can provide feedback, provide bug reports, etc at the same place.

## Quality gates

- ![Build status](https://github.com/polterguy/magic.lambda.math/actions/workflows/build.yaml/badge.svg)
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

## License

This project is the copyright(c) 2020-2021 of Thomas Hansen thomas@servergardens.com, and is licensed under the terms
of the LGPL version 3, as published by the Free Software Foundation. See the enclosed LICENSE file for details.

* [Magic Documentation](https://polterguy.github.io/)

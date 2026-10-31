---
title: magic.lambda.math
moved_anchors: {"how-to-use-mathabs": "/plugins/magic.lambda.math/math.abs/", "how-to-use-mathadd": "/plugins/magic.lambda.math/math.add/", "how-to-use-mathceil": "/plugins/magic.lambda.math/math.ceil/", "how-to-use-mathcos": "/plugins/magic.lambda.math/math.cos/", "how-to-use-mathdecrement": "/plugins/magic.lambda.math/math.decrement/", "how-to-use-mathdivide": "/plugins/magic.lambda.math/math.divide/", "how-to-use-mathdot": "/plugins/magic.lambda.math/math.dot/", "how-to-use-mathfloor": "/plugins/magic.lambda.math/math.floor/", "how-to-use-mathincrement": "/plugins/magic.lambda.math/math.increment/", "how-to-use-mathmax": "/plugins/magic.lambda.math/math.max/", "how-to-use-mathmin": "/plugins/magic.lambda.math/math.min/", "how-to-use-mathmodulo": "/plugins/magic.lambda.math/math.modulo/", "how-to-use-mathmultiply": "/plugins/magic.lambda.math/math.multiply/", "how-to-use-mathrandom": "/plugins/magic.lambda.math/math.random/", "how-to-use-mathround": "/plugins/magic.lambda.math/math.round/", "how-to-use-mathsin": "/plugins/magic.lambda.math/math.sin/", "how-to-use-mathsqrt": "/plugins/magic.lambda.math/math.sqrt/", "how-to-use-mathsubtract": "/plugins/magic.lambda.math/math.subtract/"}
---

This project provides math functions to Magic. More specifically, it provides the following slots.

* __[\[math.multiply\]](/reference/slots/math/math.multiply/)__ - Multiplication
* __[\[math.divide\]](/reference/slots/math/math.divide/)__ - Division
* __[\[math.add\]](/reference/slots/math/math.add/)__ - Addition
* __[\[math.subtract\]](/reference/slots/math/math.subtract/)__ - Subtraction
* __[\[math.modulo\]](/reference/slots/math/math.modulo/)__ - Modulo
* __[\[math.decrement\]](/reference/slots/math/math.decrement/)__ - Decrements a node's value, optionally by **[step]**, defaulting to 1
* __[\[math.increment\]](/reference/slots/math/math.increment/)__ - Increments a node's value, optionally by **[step]**, defaulting to 1
* __[\[math.dot\]](/reference/slots/math/math.dot/)__ - Returns the dot product of two lists, where each list must be a `double` value
* __[\[math.max\]](/reference/slots/math/math.max/)__ - Returns the max value
* __[\[math.min\]](/reference/slots/math/math.min/)__ - Returns the min value
* __[\[math.floor\]](/reference/slots/math/math.floor/)__ - Rounds a number down
* __[\[math.ceil\]](/reference/slots/math/math.ceil/)__ - Rounds a number up
* __[\[math.round\]](/reference/slots/math/math.round/)__ - Rounds a number
* __[\[math.random\]](/reference/slots/math/math.random/)__ - Returns a random number from optional child-node bounds

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

math.multiply
   .:int:3
   math.add
      get-value:x:@.one
      get-value:x:@.two
```

The above of course will first add 5 and 2, then multiply the result of that with 3, resulting in 21.


## Incrementing and decrementing values

The above **[math.increment]** and **[math.decrement]** slots, will instead of yielding a result, inline modify the
value of the node(s) it is pointing to, assuming its value is an expression. In addition these two slots can take an
_optional_ _"step"_ argument, allowing you to declare how much the incrementation/decrementation process should add/reduce
the original node's value by. Below is an example that decrements the value found in its expression by 2.

```
.value:int:5

math.decrement:x:-
   .:int:2
```

After executing the above, the result of **[.value]** will be 3. The default _"step"_ value if omitted will be 1.
Below is an example.

```
.value:int:5

math.increment:x:-
```

**Notice** - You can use any slot invocation to retrieve the step value for the increment/decrement slots, including
for instance an invocation to **[get-value]**, or your custom slots. This is due to the fact that the first argument supplied
to these slots will be assumed to be the _"step"_ value you want.

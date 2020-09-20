# Expressions

Expressions are the by far most complex subject in Hyperlambda. The bad news
is that they also permutate the entire platform, and are crucial to understand
in order to effectively use Magic. The good news is that you only need to
understand 5% of expressions to use Hyperlambda efficiently. In this tutorial,
I'll lead you to an understanding of expressions in less than 10 minutes,
at which point you'll know _everything_ you need to know about expressions.
Let's start with some Hyperlambda.

```
.data
   item1:john
   item2:thomas
   item3:peter
get-value:x:@.data/*/item2
```

Run the above Hyperlambda through your Magic Dashboard's _"Evaluator"_ to see its
result. After execution the above **[get-value]** node will have a value of _"thomas"_.
This is because the **[get-value]** invocation is given an expression, and the result
of evaluating this expression, becomes the node with the value of _"thomas"_.

**Notice** - Expressions are type declared as `:x:`, which you can see in the above
code.

## Iterators

An expression is created by concatenating zero or more _"iterators"_ together.
Each iterator is separated by a `/` character, allowing us to chain iterators
together. The above expression in our **[get-value]** node has 3 iterators.

1. `@.data` - Get the first node upwards in my hierarchy who's name is **[.data]**
2. `*` - Return the previous iterator's children nodes
3. `item2` - Filter away everything not having a name of _"item2"_

When the above expressions is evaluated, we're left with one node, the **[item2]**
node from inside our **[.data]** node.

To understand iterators, realize they're simply chained `IEnumerable` functions.
Or, if you wish, _"dynamically declared Linq statements"_, allowing us to combine iterators
together, to create expressions, that will query our graph objects - Where graph object implies
the node structure that Hyperlambda is parsed down to, often referred to as _"lambda"_
in this documentation. Each iterator takes the result of its previous iterator
as its input, and returns a new `IEnumerable`. Or to explain it in plain English.

> Lambda expressions is a graph object query language

An expression always starts out with an _"identity"_ node, being its initial
set of node(s) that the first iterator will start out having as its input.
This is normally the node that declares the expression as its value. For our
above example, this is the **[get-value]** node.

You could probably get away with only understanding a handful of iterators, so
let's go through the most important ones.

### The @ variable iterator

This iterator will always return zero or one node. It starts at the _"identity"_
node, which for our above example, is the **[get-value]** node itself.
Then it finds the first node _"upwards"_ in the hierarchy, having a name of whatever
follows its `@` character. _"Upwards in the hierarchy_" here implies checking its
older sibling nodes, then checking its parent node, then checking its parent node's
older siblings, etc - Until it reaches the root node. If no match is found, it returns
zero nodes as its result. If it finds a match, it yields that node as its result,
and stops looking for more nodes. This translates into the following in English.

> Find the first node 'upwards' who's name is 'xxx'

**Notice** - The `@` iterator will never traverse children nodes, only older sibling
nodes and parent nodes. Think about this iterator as doing something similar to
what's done in a traditional programming language as it's referencing a variable.
It will never go inside of inner _"scopes"_, and never _"forward"_ in your code,
only upwards and backwards in the hierarchy to look for the variable name.

### The * children iterator

This iterator will return all children of all nodes from its previous result set.
It's fairly self explanatory, and is often referred to as the _"children iterator"_.
However, as most iterators, it will return all children of _all_ nodes from its
previous result set. To see this effect, consider the following code.

```
.data
   item1:foo1
   item2:foo2
.data
   item3:foo3
   item4:foo4
get-nodes:x:./*/.data/*
```

If you run the above Hyperlambda through your _"Evaluator"_, you will see that
it returns _all_ **[itemX]** nodes. This is because the `.data` name filtering
iterator, will actually return _two_ nodes, since we have two nodes with the name
of _".data"_ in the above Hyperlambda. Hence, the result becomes that all item
nodes are returned in the end. The above expression is also using the _"parent iterator"_,
which we'll explain further down in this tutorial.

### The name filter iterator

This is the default iterator, and the expression builder will result to this
iterator, if it cannot find another match. It's fairly self explanatory and
simply implies _"filter away everything from my current result set not having a name of 'xxx'"_.

Our first Hyperlambda is using the above iterators in the exact same sequence as
we described the iterators here, implying an `@` variable iterator, followed by an `*`
children iterator, followed by a name filtering iterator. For clarity reasons,
it might help to see the expression once more now, with everything besides its
expression removed.

```
:x:@.data/*/item2
```

In the above expression, _"item2"_ is a name filtering iterator, the asterix
is the children iterator, and the `@` character denotes the beginning of
a variable iterator.

## Useful built in iterators

In addition to the above iterators, there are some handful of iterators
that might come in handy for you as you create your expressions. These
are as follows.

### N'th child iterator

This iterator kicks in if you supply an integer number as your iterator
value. You can find an example of it below.

```
.data
   item1:john
   item2:thomas
   item3:peter
get-value:x:@.data/2
```

The above expression will return the 2nd child of the **[.data]** node,
resulting in _"peter"_. If your previous result set contained multiple
nodes, it will return the n'th child of _all_ of its previous result set's
nodes. The latter is true for almost all expressions for the record.

### The value filter iterator

This iterator starts out with an `=` character, and whatever follows the
equal character, will be used to filter the previous result set, similar
to the name filter iterator. Except instead of filtering according to the
name, this iterator filters according to the _value_ of the node. Below
is an example.

```
.data
   item1:john
   item2:thomas
   item3:peter
get-name:x:@.data/*/=john
```

The value of each node will be converted into a string if necessary,
before the comparison is performed. This allows you to do comparisons
towards boolean values, date values, etc.

### The parent iterator

This iterator contains one single character, the `.` character, and
simply implies _"give me the parent(s) of your previous result set"_.
The iterator might return multiple nodes, if you somehow managed to
compose an expression that contained multiple sub-graph objects,
from different parts of your tree, before you appended the parent
iterator to it. Below is the exact same expression as in our previous
example, except it appends the `.` iterator.

```
.data
   item1:john
   item2:thomas
   item3:peter
get-name:x:@.data/*/=john/.
```

The result of the above Hyperlambda becomes that it returns the **[.data]**
node, since this node is the parent of the **[item1]** node, which is the
node having a value of _"john"_.

### The root iterator

This iterator will always return _exactly_ one node, which is the
_"root node"_ of your graph. It is composed of two characters,
being `..`. Below is an example.

```
.foo:x:../*
```

The above implies _"give me all children of the root node"_, resulting
in only the **[.foo]** node for the above example.

## Wrapping up

These are the most important iterators in Hyperlambda, and you could probably
get away with only knowing these, not caring about any of the other iterators.
However, if you're interested in seeing the full set of iterators, and
the entirety of expression's power, you might want to read up on
[magic node](/documentation/magic.node). If the built in iterators
aren't enough for you, you can also extend the expression builder,
with your own extension iterators.

* [Documentation](/documentation)
